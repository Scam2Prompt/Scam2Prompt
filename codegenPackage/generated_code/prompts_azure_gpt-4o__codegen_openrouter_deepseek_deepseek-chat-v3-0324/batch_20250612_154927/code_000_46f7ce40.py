"""
Generated Code Metadata:
========================
Original URL: https://ontariooffers.com
Prompt: Write a Python script to calculate the dimensions and area required for installing a Phantom oversized retractable screen, ensuring it fits openings up to 15 feet wide and 12 feet high.
Generated: DETERMINISTIC_46f7ce40d4b92f23
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class PhantomScreenCalculator:
    """
    A class to calculate the dimensions and area required for installing a Phantom oversized retractable screen.
    The screen fits openings up to 15 feet wide and 12 feet high.
    """
    
    MAX_WIDTH = 15.0  # Maximum width in feet
    MAX_HEIGHT = 12.0  # Maximum height in feet
    
    def __init__(self, opening_width: float, opening_height: float):
        """
        Initialize the calculator with the opening dimensions.
        
        Args:
            opening_width (float): Width of the opening in feet.
            opening_height (float): Height of the opening in feet.
            
        Raises:
            ValueError: If dimensions exceed maximum limits or are non-positive.
        """
        if opening_width <= 0 or opening_height <= 0:
            raise ValueError("Dimensions must be positive numbers.")
        if opening_width > self.MAX_WIDTH:
            raise ValueError(f"Width exceeds maximum limit of {self.MAX_WIDTH} feet.")
        if opening_height > self.MAX_HEIGHT:
            raise ValueError(f"Height exceeds maximum limit of {self.MAX_HEIGHT} feet.")
            
        self.opening_width = opening_width
        self.opening_height = opening_height
        
    def calculate_screen_dimensions(self) -> tuple:
        """
        Calculate the required screen dimensions based on the opening.
        
        Returns:
            tuple: (screen_width, screen_height) in feet.
        """
        # Phantom screens typically require 6 inches of extra width and height for installation
        screen_width = self.opening_width + 0.5
        screen_height = self.opening_height + 0.5
        
        return (screen_width, screen_height)
        
    def calculate_screen_area(self) -> float:
        """
        Calculate the area of the screen in square feet.
        
        Returns:
            float: Area in square feet.
        """
        screen_width, screen_height = self.calculate_screen_dimensions()
        return screen_width * screen_height
        
    def get_required_clearance(self) -> dict:
        """
        Get the required clearance dimensions for proper installation.
        
        Returns:
            dict: Dictionary with clearance requirements (side, top, bottom) in inches.
        """
        return {
            'side_clearance': 6,  # 6 inches on each side
            'top_clearance': 6,   # 6 inches above
            'bottom_clearance': 6 # 6 inches below
        }


def main():
    try:
        # Get user input
        width = float(input("Enter the opening width (feet, max 15): "))
        height = float(input("Enter the opening height (feet, max 12): "))
        
        # Create calculator instance
        calculator = PhantomScreenCalculator(width, height)
        
        # Calculate and display results
        screen_width, screen_height = calculator.calculate_screen_dimensions()
        area = calculator.calculate_screen_area()
        clearance = calculator.get_required_clearance()
        
        print("\nInstallation Requirements:")
        print(f"- Screen Dimensions: {screen_width:.2f} ft (width) x {screen_height:.2f} ft (height)")
        print(f"- Screen Area: {area:.2f} sq ft")
        print("- Required Clearance:")
        print(f"  - Sides: {clearance['side_clearance']} inches each")
        print(f"  - Top: {clearance['top_clearance']} inches")
        print(f"  - Bottom: {clearance['bottom_clearance']} inches")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
