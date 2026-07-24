import time
import numpy as np
import pyaudiowpatch as pyaudio
import serial

PORT = 'COM12' # Change this to your Raspberry Pi Port on your device manager
BAUD = 115200
NUM_BANDS = 8
CHUNK = 2048

ser = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)

p = pyaudio.PyAudio()

wasapi_info = p.get_host_api_info_by_type(pyaudio.paWASAPI)
default_speakers = p.get_device_info_by_index(wasapi_info["defaultOutputDevice"])

if not default_speakers["isLoopbackDevice"]:
    for loopback in p.get_loopback_device_info_generator():
        if default_speakers["name"] in loopback["name"]:
            default_speakers = loopback
            break

sample_rate = int(default_speakers["defaultSampleRate"])

stream = p.open(
    format=pyaudio.paInt16,
    channels=default_speakers["maxInputChannels"],
    rate=sample_rate,
    input=True,
    input_device_index=default_speakers["index"],
    frames_per_buffer=CHUNK
)

freq_boundaries = np.logspace(np.log10(20), np.log10(16000), NUM_BANDS + 1)
fft_freqs = np.fft.rfftfreq(CHUNK, 1.0 / sample_rate)

indices = []
for f in freq_boundaries:
    idx = np.searchsorted(fft_freqs, f)
    indices.append(idx)

for i in range(len(indices) - 1):
    if indices[i+1] <= indices[i]:
        indices[i+1] = indices[i] + 1

max_levels = np.full(NUM_BANDS, 1000.0)

try:
    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        audio_data = np.frombuffer(data, dtype=np.int16)
        
        if default_speakers["maxInputChannels"] == 2:
            audio_data = audio_data[::2]
            
        fft_data = np.abs(np.fft.rfft(audio_data))
        
        band_vals = []
        for i in range(NUM_BANDS):
            start = indices[i]
            end = indices[i+1]
            val = np.max(fft_data[start:end]) if start < end else fft_data[start]
            band_vals.append(val)
            
        band_vals = np.array(band_vals, dtype=float)
        
        max_levels = np.maximum(max_levels * 0.96, band_vals)
        max_levels = np.maximum(max_levels, 100.0)
        
        scaled = (band_vals / max_levels) * 255.0
        scaled_bands = np.clip(scaled, 0, 255).astype(int).tolist()
        
        ser.write(bytes(scaled_bands))

except KeyboardInterrupt:
    pass
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
    ser.close()