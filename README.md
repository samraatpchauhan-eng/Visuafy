# Visuafy 

Visuafy is a small desktop audio visualizer specifically designed for windows, and works with all kinds of media programs, and even works with a bluetooth speaker connected externally! It features an 8x8 led matrix, powered by a Raspberry Pi Pico rp2040 microcontroller, and will elevate your desk workspace, or even turn it into a rave!

## Features:
* **Sharp 8x8 LED matrix display:**  Visuafy features a bright LED matrix display, making it bright, aswell as power efficient .
* **Lightweight Python Script:** For Visuafy to run fully, there is an external, but very lightweight python script that runs in the background, to ensure all forms of audio being outputted by your windows machine gets caputured on Visuafy.
* **Small Footprint:** The case is engineered to be nice and compact to fit in many spots on your desk, without taking up loads of space.

---

### Case Assembly & Fitment
*A 3D CAD visualization highlighting how the LED matrix, and microcontroller interface together seamlessly.*

<img width="2560" height="2048" alt="12cd770d-0592-4ff2-b6a9-bc2bf382ee7a" src="https://github.com/user-attachments/assets/7c3234d2-44c9-48d8-9ace-28277985cbc1" />

<img width="1305" height="1114" alt="Screenshot 2026-07-24 111021" src="https://github.com/user-attachments/assets/1b71afdd-2950-4ec0-a936-c1b2d21a9c85" />

---

### Schematic Design
*The circuit schematic mapping the switch routing, and quad encoder connections to the microcontroller.*

<img width="931" height="888" alt="Screenshot 2026-07-24 190716" src="https://github.com/user-attachments/assets/59b283b3-8880-4682-949e-5433f481179d" />

---

## How to Flash
1. Press and hold the physical **BOOT** button on the RP2040 controller board.
2. Reconnect the USB cable while holding the button, then release it.
3. A virtual drive named will mount to your operating system.
4. Drag and drop the `VisuafyFirmware.ino.uf2` binary file directly onto the root of the drive.
5. The device will automatically flash, reboot, and initialize as an operational HID keyboard device.
6. Download the provided `Visuafy.py` file, and save it on your "Desktop"
7. Run the python script on Windows PowerShell (But first make sure you have python installed on your machine), and enjoy!

---

## AI Attribution Note
**Please Note that AI was utilized for some basic project planning and debugging of the Firmware and Python Script files in Arduino IDE and VS.Code**
