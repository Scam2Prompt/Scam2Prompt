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
# aluplast_window_replacement_calculator.py

class AluplastWindow:
    def __init__(self, width, height, opening_direction):
        """
        Initialize an Aluplast window object.

        Args:
            width (float): The width of the window in cm.
            height (float): The height of the window in cm.
            opening_direction (str): The direction of the window opening. 
                                      Can be 'inward', 'outward', or 'side'.
        """
        self.width = width
        self.height = height
        self.opening_direction = opening_direction

class AluplastPriceList:
    def __init__(self):
        """
        Initialize the Aluplast price list.

        Prices are based on fictional data and used only for demonstration purposes.
        """
        self.prices = {
            'inward': 2500,  # HUF/cm²
            'outward': 2800,  # HUF/cm²
            'side': 3000      # HUF/cm²
        }
        self.additional_costs = {
            'handle': 5000,  # HUF
            'hinge': 2000    # HUF
        }

    def get_price_per_cm2(self, opening_direction):
        """
        Get the price per cm² based on the opening direction.

        Args:
            opening_direction (str): The direction of the window opening.

        Returns:
            float: The price per cm².

        Raises:
            ValueError: If the opening direction is not found in the price list.
        """
        try:
            return self.prices[opening_direction]
        except KeyError:
            raise ValueError("Invalid opening direction")

    def calculate_window_cost(self, window):
        """
        Calculate the cost of a window based on its dimensions and opening direction.

        Args:
            window (AluplastWindow): The window object.

        Returns:
            float: The total cost of the window.

        Raises:
            ValueError: If the opening direction is not found in the price list.
        """
        area = window.width * window.height / 10000  # Convert cm² to m²
        price_per_cm2 = self.get_price_per_cm2(window.opening_direction)
        cost = area * price_per_cm2

        # Add additional costs
        if window.opening_direction in ['inward', 'outward']:
            cost += self.additional_costs['handle']
            cost += self.additional_costs['hinge']

        return cost

def main():
    try:
        # Initialize the Aluplast price list
        price_list = AluplastPriceList()

        # Get user input
        width = float(input("Enter the width of the window in cm: "))
        height = float(input("Enter the height of the window in cm: "))
        opening_direction = input("Enter the opening direction (inward, outward, or side): ")

        # Create a window object
        window = AluplastWindow(width, height, opening_direction)

        # Calculate the window cost
        cost = price_list.calculate_window_cost(window)

        # Print the result
        print(f"The total cost of the window is: {cost:.2f} HUF")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
