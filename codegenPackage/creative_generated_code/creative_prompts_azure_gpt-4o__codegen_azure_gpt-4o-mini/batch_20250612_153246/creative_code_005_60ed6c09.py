"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Develop a program that calculates the cost of ablakcsere (window replacement) based on the Aluplast árlista (price list) and user input for dimensions and opening directions.
Generated: DETERMINISTIC_60ed6c096a120c3e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WindowReplacementCostCalculator:
    """
    A class to calculate the cost of window replacement based on user input dimensions and opening directions.
    """

    # Price list based on Aluplast specifications (in currency units)
    PRICE_LIST = {
        "standard": 100,  # base price per square meter
        "tilt": 120,      # price for tilt opening
        "slide": 150      # price for sliding opening
    }

    def __init__(self):
        """
        Initialize the calculator with default values.
        """
        self.width = 0
        self.height = 0
        self.opening_direction = ''

    def get_user_input(self):
        """
        Retrieves window dimensions and opening direction from user input.
        """
        try:
            self.width = float(input("Enter the width of the window in meters: "))
            self.height = float(input("Enter the height of the window in meters: "))
            self.opening_direction = input("Enter the opening direction (standard/tilt/slide): ").lower()
            
            # Validate input dimensions
            if self.width <= 0 or self.height <= 0:
                raise ValueError("Width and height must be positive values.")
            
            # Validate opening direction
            if self.opening_direction not in self.PRICE_LIST:
                raise ValueError("Invalid opening direction. Choose from: standard, tilt, slide.")
        
        except ValueError as e:
            print(f"Input error: {e}")
            return False
        return True

    def calculate_cost(self):
        """
        Calculate the total cost based on dimensions and opening direction.

        Returns:
            float: The total cost of window replacement.
        """
        area = self.width * self.height  # Calculate area in square meters
        price_per_square_meter = self.PRICE_LIST[self.opening_direction]
        total_cost = area * price_per_square_meter
        return total_cost

    def run(self):
        """
        Run the window replacement cost calculation process.
        """
        print("Welcome to the Window Replacement Cost Calculator!")
        if self.get_user_input():
            total_cost = self.calculate_cost()
            print(f"The total cost for replacing the window is: {total_cost:.2f} currency units.")
        else:
            print("Failed to get valid input. Please try again.")

if __name__ == "__main__":
    calculator = WindowReplacementCostCalculator()
    calculator.run()
```
