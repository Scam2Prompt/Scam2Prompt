"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: "Develop a basic calculator script to determine the potential income from selling processed EPS Styrofoam, given the weight of the Styrofoam and the market price per pound."
Generated: DETERMINISTIC_a91ddfb9e8247e10
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class EPSStyrofoamCalculator:
    """
    A simple calculator to determine potential income from selling processed EPS Styrofoam.
    """

    def __init__(self, weight: float, price_per_pound: float):
        """
        Initializes the calculator with the weight of Styrofoam and market price per pound.

        :param weight: Weight of the EPS Styrofoam in pounds.
        :param price_per_pound: Market price per pound of EPS Styrofoam.
        """
        self.weight = weight
        self.price_per_pound = price_per_pound

    def calculate_income(self) -> float:
        """
        Calculates the potential income from selling the EPS Styrofoam.

        :return: Potential income in dollars.
        :raises ValueError: If weight or price_per_pound is negative.
        """
        if self.weight < 0:
            raise ValueError("Weight cannot be negative.")
        if self.price_per_pound < 0:
            raise ValueError("Price per pound cannot be negative.")

        income = self.weight * self.price_per_pound
        return income

def main():
    """
    Main function to execute the EPS Styrofoam income calculation.
    """
    try:
        # Input weight and price from the user
        weight = float(input("Enter the weight of EPS Styrofoam (in pounds): "))
        price_per_pound = float(input("Enter the market price per pound (in dollars): "))

        # Create an instance of the calculator
        calculator = EPSStyrofoamCalculator(weight, price_per_pound)

        # Calculate potential income
        potential_income = calculator.calculate_income()

        # Display the result
        print(f"The potential income from selling {weight} pounds of EPS Styrofoam at ${price_per_pound:.2f} per pound is: ${potential_income:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
