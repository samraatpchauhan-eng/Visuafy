#include <Adafruit_NeoPixel.h>

#define DATA_PIN    15
#define NUM_LEDS    64
#define NUM_COLS    8
#define MAX_HEIGHT  8
Adafruit_NeoPixel matrix(NUM_LEDS, DATA_PIN, NEO_GRB + NEO_KHZ800);
byte columnHeights[NUM_COLS];

int getPixelIndex(int x, int y) {
  return (y * NUM_COLS) + x;
}

void setup() {
  Serial.begin(115200);
  matrix.begin();
  matrix.setBrightness(10);
  matrix.show();
}

void loop() {
  if (Serial.available() >= NUM_COLS) {
    for (int i = 0; i < NUM_COLS; i++) {
      columnHeights[i] = Serial.read();
    }
    updateDisplay();
  }
}

void updateDisplay() {
  matrix.clear();
  for (int col = 0; col < NUM_COLS; col++) {
    int height = map(columnHeights[col], 0, 255, 0, MAX_HEIGHT);

    for (int row = 0; row < height; row++) {
      int y = row;
      int x = (NUM_COLS - 1) - col;
      int pixelIdx = getPixelIndex(x, y);

      uint32_t color;
      if (row < 4) {
        color = matrix.Color(0, 255, 0);
      } else if (row < 6) {
        color = matrix.Color(255, 255, 0);
      } else {
        color = matrix.Color(255, 0, 0);
      }

      matrix.setPixelColor(pixelIdx, color);
    }
  }

  matrix.show();
}