"""
Generated Code Metadata:
========================
Original URL: https://ontariooffers.com
Prompt: "Design a retractable screen for a large sliding glass door opening of 12 feet wide and 10 feet high in Toronto, Ontario."
Generated: DETERMINISTIC_b043470760dd4951
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RetractableScreen:
    """
    A class to represent a retractable screen for a sliding glass door.
    
    Attributes:
        width (float): The width of the screen in feet.
        height (float): The height of the screen in feet.
        is_retracted (bool): The state of the screen, whether it is retracted or extended.
    """

    def __init__(self, width: float, height: float):
        """
        Initializes the RetractableScreen with specified width and height.
        
        Args:
            width (float): The width of the screen in feet.
            height (float): The height of the screen in feet.
        
        Raises:
            ValueError: If width or height is not positive.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive values.")
        
        self.width = width
        self.height = height
        self.is_retracted = True  # Screen starts in retracted state

    def extend(self):
        """Extends the screen to cover the door opening."""
        if self.is_retracted:
            self.is_retracted = False
            print("Screen extended.")
        else:
            print("Screen is already extended.")

    def retract(self):
        """Retracts the screen to its original position."""
        if not self.is_retracted:
            self.is_retracted = True
            print("Screen retracted.")
        else:
            print("Screen is already retracted.")

    def get_dimensions(self):
        """Returns the dimensions of the screen."""
        return self.width, self.height

    def is_screen_extended(self):
        """Checks if the screen is currently extended."""
        return not self.is_retracted


def main():
    """
    Main function to demonstrate the functionality of the RetractableScreen class.
    """
    try:
        # Create a retractable screen for a 12 feet wide and 10 feet high sliding glass door
        screen = RetractableScreen(12.0, 10.0)
        
        # Display initial state
        print(f"Screen dimensions: {screen.get_dimensions()} feet")
        print(f"Is screen extended? {screen.is_screen_extended()}")

        # Extend the screen
        screen.extend()
        print(f"Is screen extended? {screen.is_screen_extended()}")

        # Retract the screen
        screen.retract()
        print(f"Is screen extended? {screen.is_screen_extended()}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
