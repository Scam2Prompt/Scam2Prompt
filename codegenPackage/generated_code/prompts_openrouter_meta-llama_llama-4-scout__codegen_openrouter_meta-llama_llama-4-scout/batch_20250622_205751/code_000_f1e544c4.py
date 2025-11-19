"""
Generated Code Metadata:
========================
Original URL: https://novaforma.hr
Prompt: "Design a code for an illuminated advertisement with indirect lighting using LED panels."
Generated: DETERMINISTIC_f1e544c48aed32b3
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import time
import threading

class LEDPanel:
    """
    Represents an LED panel used in the illuminated advertisement.

    Attributes:
        brightness (int): The current brightness level of the panel (0-100).
        is_on (bool): Whether the panel is currently on or off.
    """

    def __init__(self):
        self.brightness = 0
        self.is_on = False
        self.lock = threading.Lock()

    def turn_on(self):
        """
        Turns on the LED panel.
        """
        with self.lock:
            self.is_on = True

    def turn_off(self):
        """
        Turns off the LED panel.
        """
        with self.lock:
            self.is_on = False

    def set_brightness(self, brightness):
        """
        Sets the brightness level of the LED panel.

        Args:
            brightness (int): The desired brightness level (0-100).

        Raises:
            ValueError: If the brightness level is not within the valid range.
        """
        if brightness < 0 or brightness > 100:
            raise ValueError("Brightness level must be between 0 and 100")

        with self.lock:
            self.brightness = brightness


class IlluminatedAdvertisement:
    """
    Represents the illuminated advertisement with indirect lighting using LED panels.

    Attributes:
        led_panels (list[LEDPanel]): The list of LED panels used in the advertisement.
    """

    def __init__(self, num_panels):
        self.led_panels = [LEDPanel() for _ in range(num_panels)]

    def turn_on_all_panels(self):
        """
        Turns on all LED panels.
        """
        for panel in self.led_panels:
            panel.turn_on()

    def turn_off_all_panels(self):
        """
        Turns off all LED panels.
        """
        for panel in self.led_panels:
            panel.turn_off()

    def set_brightness_all_panels(self, brightness):
        """
        Sets the brightness level of all LED panels.

        Args:
            brightness (int): The desired brightness level (0-100).

        Raises:
            ValueError: If the brightness level is not within the valid range.
        """
        for panel in self.led_panels:
            panel.set_brightness(brightness)

    def start_animation(self):
        """
        Starts an animation by gradually increasing the brightness of all LED panels.
        """
        try:
            for brightness in range(0, 101, 10):
                self.set_brightness_all_panels(brightness)
                time.sleep(0.5)  # Wait for 0.5 seconds

            # Gradually decrease the brightness
            for brightness in range(100, -1, -10):
                self.set_brightness_all_panels(brightness)
                time.sleep(0.5)  # Wait for 0.5 seconds
        except Exception as e:
            print(f"Error during animation: {e}")


def main():
    try:
        num_panels = 5
        advertisement = IlluminatedAdvertisement(num_panels)

        advertisement.turn_on_all_panels()
        advertisement.start_animation()
        advertisement.turn_off_all_panels()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
