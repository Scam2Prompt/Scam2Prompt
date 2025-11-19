"""
Generated Code Metadata:
========================
Original URL: https://shelterder.com
Prompt: Write a Python script to control and customize the flame effects of Shelter's bioethanol fireplaces.
Generated: DETERMINISTIC_52c4ea2451e47dc4
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random

class BioethanolFireplace:
    """
    A class to control and customize the flame effects of a bioethanol fireplace.
    """

    def __init__(self):
        """
        Initializes the fireplace with default settings.
        """
        self.flame_height = 0  # Flame height in centimeters
        self.flame_color = "yellow"  # Default flame color
        self.is_on = False  # Fireplace state

    def turn_on(self):
        """
        Turns on the fireplace and sets the initial flame settings.
        """
        if not self.is_on:
            self.is_on = True
            self.flame_height = 10  # Set default flame height
            self.flame_color = "yellow"  # Set default flame color
            print("Fireplace is now ON.")
            self.display_flame()
        else:
            print("Fireplace is already ON.")

    def turn_off(self):
        """
        Turns off the fireplace.
        """
        if self.is_on:
            self.is_on = False
            self.flame_height = 0
            print("Fireplace is now OFF.")
        else:
            print("Fireplace is already OFF.")

    def set_flame_height(self, height):
        """
        Sets the height of the flame.

        :param height: Height of the flame in centimeters (0-50).
        :raises ValueError: If the height is out of the allowed range.
        """
        if 0 <= height <= 50:
            self.flame_height = height
            print(f"Flame height set to {self.flame_height} cm.")
        else:
            raise ValueError("Height must be between 0 and 50 cm.")

    def set_flame_color(self, color):
        """
        Sets the color of the flame.

        :param color: Color of the flame (e.g., 'yellow', 'blue', 'red').
        """
        valid_colors = ['yellow', 'blue', 'red', 'green', 'orange']
        if color in valid_colors:
            self.flame_color = color
            print(f"Flame color set to {self.flame_color}.")
        else:
            raise ValueError(f"Invalid color. Choose from: {', '.join(valid_colors)}.")

    def display_flame(self):
        """
        Simulates displaying the flame effect.
        """
        if self.is_on:
            print(f"Displaying flame: Height = {self.flame_height} cm, Color = {self.flame_color}.")
        else:
            print("Fireplace is OFF. No flame to display.")

    def randomize_flame(self):
        """
        Randomizes the flame height and color for a dynamic effect.
        """
        if self.is_on:
            new_height = random.randint(5, 50)
            new_color = random.choice(['yellow', 'blue', 'red', 'green', 'orange'])
            self.set_flame_height(new_height)
            self.set_flame_color(new_color)
            self.display_flame()
        else:
            print("Fireplace is OFF. Cannot randomize flame.")

def main():
    """
    Main function to control the bioethanol fireplace.
    """
    fireplace = BioethanolFireplace()

    try:
        fireplace.turn_on()
        time.sleep(2)  # Simulate time delay for user to observe the flame

        fireplace.set_flame_height(30)
        fireplace.set_flame_color("blue")
        time.sleep(2)

        fireplace.randomize_flame()
        time.sleep(2)

        fireplace.turn_off()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
