"""
Generated Code Metadata:
========================
Original URL: https://strk.site
Prompt: Write a Python script to calculate the cost of apartment renovation based on the rates provided on the webpage (e.g., 9,990 rub/m² for standard renovation). Include options for cosmetic, capital, and designer renovations.
Generated: DETERMINISTIC_86d0862dfc429808
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# renovation_cost_calculator.py

class RenovationCostCalculator:
    """
    Calculates the cost of apartment renovation based on the provided rates.
    """

    def __init__(self):
        # Renovation rates per square meter in rubles
        self.renovation_rates = {
            "cosmetic": 9990,
            "capital": 14990,
            "designer": 24990
        }

    def calculate_cost(self, area, renovation_type):
        """
        Calculates the renovation cost based on the area and renovation type.

        Args:
            area (float): Apartment area in square meters.
            renovation_type (str): Type of renovation (cosmetic, capital, designer).

        Returns:
            float: Renovation cost in rubles.

        Raises:
            ValueError: If renovation type is not supported.
            TypeError: If area is not a positive number.
        """
        if not isinstance(area, (int, float)) or area <= 0:
            raise TypeError("Area must be a positive number.")

        if renovation_type not in self.renovation_rates:
            raise ValueError(f"Unsupported renovation type: {renovation_type}. "
                             f"Supported types: {list(self.renovation_rates.keys())}")

        rate = self.renovation_rates[renovation_type]
        cost = area * rate
        return cost


def main():
    calculator = RenovationCostCalculator()

    print("Renovation Cost Calculator")
    print("---------------------------")

    area = float(input("Enter apartment area in square meters: "))

    print("Renovation types:")
    for i, renovation_type in enumerate(calculator.renovation_rates.keys()):
        print(f"{i+1}. {renovation_type.capitalize()}")

    renovation_type_choice = int(input("Enter renovation type number: "))
    renovation_type = list(calculator.renovation_rates.keys())[renovation_type_choice - 1]

    try:
        cost = calculator.calculate_cost(area, renovation_type)
        print(f"Renovation cost: {cost:,.2f} rubles")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
