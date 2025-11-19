"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: Write a Python script that calculates the estimated cost of roofing services based on user input for roof type (tile, shingle, metal, flat) and square footage, similar to a roofing calculator.
Generated: DETERMINISTIC_fc12d2725ca3695a
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# roofing_calculator.py

class RoofingCalculator:
    """
    Calculates the estimated cost of roofing services based on roof type and square footage.
    """

    def __init__(self):
        # Define the cost per square foot for each roof type
        self.roof_costs = {
            "tile": 10.00,
            "shingle": 5.00,
            "metal": 7.00,
            "flat": 3.00
        }

    def calculate_cost(self, roof_type, square_footage):
        """
        Calculates the estimated cost of roofing services.

        Args:
            roof_type (str): The type of roof (tile, shingle, metal, flat)
            square_footage (float): The square footage of the roof

        Returns:
            float: The estimated cost of roofing services
        """
        try:
            # Validate roof type
            if roof_type not in self.roof_costs:
                raise ValueError("Invalid roof type")

            # Validate square footage
            if square_footage <= 0:
                raise ValueError("Square footage must be greater than zero")

            # Calculate cost
            cost = self.roof_costs[roof_type] * square_footage
            return cost

        except ValueError as e:
            print(f"Error: {e}")
            return None

    def get_roof_types(self):
        """
        Returns a list of supported roof types.

        Returns:
            list: A list of supported roof types
        """
        return list(self.roof_costs.keys())


def main():
    calculator = RoofingCalculator()

    print("Roofing Calculator")
    print("------------------")

    # Get roof type from user
    print("Supported roof types:")
    for i, roof_type in enumerate(calculator.get_roof_types()):
        print(f"{i+1}. {roof_type.capitalize()}")
    roof_type_choice = input("Enter the number of your roof type: ")
    roof_type = calculator.get_roof_types()[int(roof_type_choice) - 1]

    # Get square footage from user
    while True:
        try:
            square_footage = float(input("Enter the square footage of your roof: "))
            if square_footage <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number greater than zero.")

    # Calculate and display cost
    cost = calculator.calculate_cost(roof_type, square_footage)
    if cost is not None:
        print(f"Estimated cost: ${cost:.2f}")


if __name__ == "__main__":
    main()
```
