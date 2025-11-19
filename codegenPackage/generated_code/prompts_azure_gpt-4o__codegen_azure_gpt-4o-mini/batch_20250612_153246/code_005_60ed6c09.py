"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Develop a program that calculates the cost of ablakcsere (window replacement) based on the Aluplast árlista (price list) and user input for dimensions and opening directions.
Generated: DETERMINISTIC_60ed6c096a120c3e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class WindowReplacementCalculator:
    """
    A class to calculate the cost of window replacement based on user input dimensions
    and opening directions, using a predefined price list.
    """

    # Price list for different window types (in HUF)
    PRICE_LIST = {
        'fixed': 20000,  # Fixed window
        'casement': 25000,  # Casement window
        'sliding': 30000,  # Sliding window
        'awning': 28000,  # Awning window
    }

    def __init__(self, width: float, height: float, window_type: str):
        """
        Initializes the calculator with window dimensions and type.

        :param width: Width of the window in meters
        :param height: Height of the window in meters
        :param window_type: Type of the window (fixed, casement, sliding, awning)
        """
        self.width = width
        self.height = height
        self.window_type = window_type.lower()

    def validate_input(self):
        """
        Validates the input dimensions and window type.

        :raises ValueError: If dimensions are non-positive or window type is invalid
        """
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be positive values.")
        if self.window_type not in self.PRICE_LIST:
            raise ValueError(f"Invalid window type. Choose from: {', '.join(self.PRICE_LIST.keys())}")

    def calculate_area(self) -> float:
        """
        Calculates the area of the window.

        :return: Area of the window in square meters
        """
        return self.width * self.height

    def calculate_cost(self) -> float:
        """
        Calculates the total cost of the window replacement.

        :return: Total cost in HUF
        """
        area = self.calculate_area()
        base_cost = self.PRICE_LIST[self.window_type]
        total_cost = base_cost * area
        return total_cost

    def get_cost(self) -> float:
        """
        Public method to get the total cost after validating input.

        :return: Total cost in HUF
        """
        self.validate_input()
        return self.calculate_cost()


def main():
    """
    Main function to execute the window replacement cost calculation.
    """
    try:
        # User input for window dimensions and type
        width = float(input("Enter the width of the window in meters: "))
        height = float(input("Enter the height of the window in meters: "))
        window_type = input("Enter the type of window (fixed, casement, sliding, awning): ")

        # Create an instance of the calculator
        calculator = WindowReplacementCalculator(width, height, window_type)

        # Calculate and display the cost
        cost = calculator.get_cost()
        print(f"The total cost of the window replacement is: {cost:.2f} HUF")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
