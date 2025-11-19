"""
Generated Code Metadata:
========================
Original URL: https://xanade.com
Prompt: Write a code example in Python for interfacing with the 2.4-inch TFT LCD touch screen shield (240x320 ILI9341 controller) and the Raspberry Pi 5 single-board computer (8GB) to create a simple user interface.
Generated: DETERMINISTIC_73674f8ef7770517
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import RPi.GPIO as GPIO
import spidev
import time
from datetime import datetime

# Define constants for the TFT LCD screen
TFT_WIDTH = 240
TFT_HEIGHT = 320
ILI9341_VSWRST = 0x01
ILI9341_SWRESET = 0x02
ILI9341_RDDID = 0x04
ILI9341_RDDST = 0x09

# Define constants for SPI communication
SPI_PORT = 0
SPI_DEVICE = 0

def init_spi():
    """Initialize SPI communication"""
    spi = spidev.SpiDev()
    spi.open(SPI_PORT, SPI_DEVICE)
    spi.max_speed_hz = 10000000
    return spi

def send_command(spi, command):
    """Send a command to the TFT LCD screen"""
    spi.xfer([command])

def send_data(spi, data):
    """Send data to the TFT LCD screen"""
    spi.xfer([data])

def reset(spi):
    """Reset the TFT LCD screen"""
    send_command(spi, ILI9341_SWRESET)
    time.sleep(0.1)

def init_tft(spi):
    """Initialize the TFT LCD screen"""
    reset(spi)

    # Initialize the ILI9341 controller
    send_command(spi, ILI9341_VSWRST)
    time.sleep(0.1)

    send_command(spi, ILI9341_SWRESET)
    time.sleep(0.1)

    send_command(spi, ILI9341_RDDID)
    time.sleep(0.1)

    send_command(spi, ILI9341_RDDST)

def draw_pixel(spi, x, y, color):
    """Draw a pixel on the TFT LCD screen"""
    send_command(spi, 0x2C)  # Set pixel format
    spi.xfer([0x00, 0x00, 0x00, 0x00, 0x00])  # Dummy data
    spi.xfer([x >> 8, x & 0xFF, y >> 8, y & 0xFF, color >> 16, (color >> 8) & 0xFF, color & 0xFF])

def draw_rectangle(spi, x, y, w, h, color):
    """Draw a rectangle on the TFT LCD screen"""
    for i in range(h):
        for j in range(w):
            draw_pixel(spi, x + j, y + i, color)

def main():
    try:
        # Initialize SPI communication
        spi = init_spi()

        # Initialize the TFT LCD screen
        init_tft(spi)

        # Draw a red rectangle
        draw_rectangle(spi, 100, 100, 40, 40, 0xFF0000)

        # Keep the program running
        while True:
            pass

    except KeyboardInterrupt:
        GPIO.cleanup()
        spi.close()

if __name__ == "__main__":
    main()
```
