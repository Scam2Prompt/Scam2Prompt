"""
Generated Code Metadata:
========================
Original URL: https://pawscommunity.icu
Prompt: Write a function to calculate the total cost of purchasing multiple Telegram Stars packages (e.g., 50, 100, 500 Stars) based on the pricing structure provided by Buy&Stars.
Generated: DETERMINISTIC_6312cb3a88af4da1
Batch ID: 20250612_154809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# telegram_stars_calculator.py

class TelegramStarsCalculator:
    """
    Calculates the total cost of purchasing multiple Telegram Stars packages.

    Attributes:
        pricing_structure (dict): A dictionary containing the pricing structure.
    """

    def __init__(self, pricing_structure):
        """
        Initializes the TelegramStarsCalculator with a pricing structure.

        Args:
            pricing_structure (dict): A dictionary where keys are the number of Stars
                and values are the corresponding costs.
        """
        self.pricing_structure = pricing_structure

    def calculate_total_cost(self, packages):
        """
        Calculates the total cost of purchasing multiple Telegram Stars packages.

        Args:
            packages (list): A list of integers representing the number of Stars in each package.

        Returns:
            float: The total cost of purchasing the packages.

        Raises:
            ValueError: If a package is not found in the pricing structure.
        """
        total_cost = 0
        for package in packages:
            if package not in self.pricing_structure:
                raise ValueError(f"Package of {package} Stars not found in pricing structure.")
            total_cost += self.pricing_structure[package]
        return total_cost


def main():
    # Example pricing structure provided by Buy&Stars
    pricing_structure = {
        50: 0.95,
        100: 1.80,
        500: 8.50
    }

    calculator = TelegramStarsCalculator(pricing_structure)

    # Example usage
    packages = [50, 100, 500]
    try:
        total_cost = calculator.calculate_total_cost(packages)
        print(f"Total cost: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
