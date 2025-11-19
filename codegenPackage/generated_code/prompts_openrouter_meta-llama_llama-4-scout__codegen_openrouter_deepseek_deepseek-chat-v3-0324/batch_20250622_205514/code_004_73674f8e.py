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
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TFT LCD Touch Screen Interface for Raspberry Pi 5
2.4-inch ILI9341 Controller (240x320 resolution)
"""

import time
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont
import spidev
import ST7789 as ST7789

# Display configuration
DISPLAY_WIDTH = 240
DISPLAY_HEIGHT = 320
SPI_SPEED_MHZ = 80

# Pin configuration (BCM numbering)
RST_PIN = 25
DC_PIN = 24
BL_PIN = 18
SPI_PORT = 0
SPI_DEVICE = 0

# Touch screen configuration (XPT2046)
TOUCH_CS_PIN = 8
TOUCH_IRQ_PIN = 7

class TouchScreenUI:
    def __init__(self):
        """Initialize the TFT display and touch interface."""
        try:
            # Configure GPIO
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            
            # Initialize display
            self._init_display()
            
            # Initialize touch screen
            self._init_touch()
            
            # Create blank image and draw object
            self.image = Image.new("RGB", (DISPLAY_WIDTH, DISPLAY_HEIGHT), color=(0, 0, 0))
            self.draw = ImageDraw.Draw(self.image)
            
            # Load default font
            try:
                self.font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
            except:
                self.font = ImageFont.load_default()
            
            # Backlight on
            GPIO.setup(BL_PIN, GPIO.OUT)
            GPIO.output(BL_PIN, GPIO.HIGH)
            
        except Exception as e:
            self.cleanup()
            raise RuntimeError(f"Initialization failed: {str(e)}")

    def _init_display(self):
        """Initialize the ST7789 display controller."""
        self.disp = ST7789.ST7789(
            port=SPI_PORT,
            cs=SPI_DEVICE,
            dc=DC_PIN,
            rst=RST_PIN,
            backlight=BL_PIN,
            width=DISPLAY_WIDTH,
            height=DISPLAY_HEIGHT,
            rotation=90,
            spi_speed_hz=SPI_SPEED_MHZ * 1000 * 1000
        )
        self.disp.begin()

    def _init_touch(self):
        """Initialize the XPT2046 touch controller."""
        GPIO.setup(TOUCH_CS_PIN, GPIO.OUT)
        GPIO.setup(TOUCH_IRQ_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        self.spi = spidev.SpiDev()
        self.spi.open(SPI_PORT, SPI_DEVICE)
        self.spi.max_speed_hz = 1000000
        self.spi.mode = 0b00

    def read_touch(self):
        """Read touch position.
        Returns: (x, y) coordinates or None if not touched.
        """
        if GPIO.input(TOUCH_IRQ_PIN) == GPIO.LOW:
            # Read X and Y coordinates
            x = self._read_touch_coord(0xD0)
            y = self._read_touch_coord(0x90)
            
            # Convert to display coordinates
            x = max(0, min(x, 4095)) * DISPLAY_WIDTH // 4095
            y = max(0, min(y, 4095)) * DISPLAY_HEIGHT // 4095
            
            return (x, DISPLAY_HEIGHT - y)  # Flip Y axis
        return None

    def _read_touch_coord(self, command):
        """Read a single coordinate from the touch controller."""
        data = self.spi.xfer2([command, 0x00, 0x00])
        return ((data[1] << 8) | data[2]) >> 3

    def draw_button(self, x, y, width, height, text, color, text_color=(255, 255, 255)):
        """Draw a button on the display."""
        self.draw.rectangle((x, y, x + width, y + height), fill=color, outline=(255, 255, 255))
        text_width, text_height = self.draw.textsize(text, font=self.font)
        self.draw.text(
            (x + (width - text_width) // 2, y + (height - text_height) // 2),
            text,
            font=self.font,
            fill=text_color
        )

    def update_display(self):
        """Update the display with the current image."""
        self.disp.display(self.image)

    def clear_screen(self, color=(0, 0, 0)):
        """Clear the screen with specified color."""
        self.draw.rectangle((0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT), fill=color)
        self.update_display()

    def cleanup(self):
        """Clean up resources."""
        try:
            GPIO.output(BL_PIN, GPIO.LOW)
            self.spi.close()
            self.disp.reset()
            GPIO.cleanup()
        except:
            pass

def main():
    """Main demo function."""
    try:
        ui = TouchScreenUI()
        ui.clear_screen()
        
        # Draw UI elements
        ui.draw_button(20, 20, 200, 60, "Button 1", (0, 0, 255))
        ui.draw_button(20, 100, 200, 60, "Button 2", (0, 255, 0))
        ui.draw.text((20, 180), "Touch the screen to test", font=ui.font, fill=(255, 255, 255))
        ui.update_display()
        
        print("Touch screen demo running. Press Ctrl+C to exit.")
        
        while True:
            touch_pos = ui.read_touch()
            if touch_pos:
                print(f"Touched at: {touch_pos}")
                # Simple button detection
                if 20 <= touch_pos[0] <= 220 and 20 <= touch_pos[1] <= 80:
                    print("Button 1 pressed")
                elif 20 <= touch_pos[0] <= 220 and 100 <= touch_pos[1] <= 160:
                    print("Button 2 pressed")
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        ui.cleanup()

if __name__ == "__main__":
    main()
```
