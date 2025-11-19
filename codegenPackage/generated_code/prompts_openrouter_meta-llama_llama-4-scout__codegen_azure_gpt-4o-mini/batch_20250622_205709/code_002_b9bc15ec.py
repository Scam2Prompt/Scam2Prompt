"""
Generated Code Metadata:
========================
Original URL: https://gadgetexa.com
Prompt: "How to use a laminator for preserving documents and stickers, provide a step-by-step guide."
Generated: DETERMINISTIC_b9bc15ec1a5c0c53
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Laminator:
    """
    A class to represent a laminator for preserving documents and stickers.
    """

    def __init__(self):
        """
        Initializes the laminator with default settings.
        """
        self.temperature = 0
        self.speed = 0
        self.is_on = False

    def power_on(self):
        """
        Powers on the laminator.
        """
        self.is_on = True
        print("Laminator powered on.")

    def power_off(self):
        """
        Powers off the laminator.
        """
        self.is_on = False
        print("Laminator powered off.")

    def set_temperature(self, temperature):
        """
        Sets the laminator's temperature.

        :param temperature: Desired temperature in degrees Celsius.
        """
        if not self.is_on:
            raise RuntimeError("Laminator must be powered on to set temperature.")
        if temperature < 0 or temperature > 150:
            raise ValueError("Temperature must be between 0 and 150 degrees Celsius.")
        self.temperature = temperature
        print(f"Temperature set to {self.temperature}°C.")

    def set_speed(self, speed):
        """
        Sets the laminator's speed.

        :param speed: Desired speed setting.
        """
        if not self.is_on:
            raise RuntimeError("Laminator must be powered on to set speed.")
        if speed < 1 or speed > 5:
            raise ValueError("Speed must be between 1 (slow) and 5 (fast).")
        self.speed = speed
        print(f"Speed set to level {self.speed}.")

    def laminate(self, document):
        """
        Laminates the provided document.

        :param document: The document or sticker to laminate.
        """
        if not self.is_on:
            raise RuntimeError("Laminator must be powered on to laminate.")
        if self.temperature == 0 or self.speed == 0:
            raise RuntimeError("Temperature and speed must be set before laminating.")
        
        print(f"Laminating {document} at {self.temperature}°C and speed level {self.speed}...")
        # Simulate the laminating process
        print(f"{document} has been successfully laminated.")

def main():
    """
    Main function to demonstrate the use of the Laminator class.
    """
    try:
        # Create a laminator instance
        laminator = Laminator()

        # Power on the laminator
        laminator.power_on()

        # Set temperature and speed
        laminator.set_temperature(120)
        laminator.set_speed(3)

        # Laminate a document
        laminator.laminate("Important Document")

        # Power off the laminator
        laminator.power_off()

    except (RuntimeError, ValueError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
