"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://canguldemir.com.tr
Prompt: Write a Python script to calculate the total cost of purchasing different sizes of construction steel bars based on the pricing information from Cangül Demir Çelik A.Ş.
Generated: DETERMINISTIC_ad40dc1d8d97a338
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class SteelBar:
    def __init__(self, size: str, price_per_meter: float):
        """
        Initializes a SteelBar instance.

        :param size: The size of the steel bar (e.g., '6mm', '8mm').
        :param price_per_meter: The price per meter for the steel bar.
        """
        self.size = size
        self.price_per_meter = price_per_meter

    def calculate_cost(self, length: float) -> float:
        """
        Calculates the total cost for a given length of steel bar.

        :param length: The length of the steel bar in meters.
        :return: Total cost for the specified length.
        """
        return self.price_per_meter * length


def get_user_input():
    """
    Prompts the user for the size of the steel bar and the desired length.

    :return: Tuple containing size, length, and price per meter.
    """
    size = input("Enter the size of the steel bar (e.g., '6mm', '8mm'): ")
    length = float(input("Enter the length of the steel bar in meters: "))
    price_per_meter = float(input("Enter the price per meter for the steel bar: "))
    
    return size, length, price_per_meter


def main():
    """
    Main function to execute the steel bar cost calculation.
    """
    try:
        # Get user input
        size, length, price_per_meter = get_user_input()

        # Create a SteelBar instance
        steel_bar = SteelBar(size, price_per_meter)

        # Calculate total cost
        total_cost = steel_bar.calculate_cost(length)

        # Display the results
        print(f"\nTotal cost for {length} meters of {size} steel bar: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: Invalid input. Please enter numeric values for length and price. {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
