"""
Generated Code Metadata:
========================
Original URL: https://aluminiosmendoza.cl
Prompt: Create a Python script to calculate the cost of installing security blinds based on square footage and material quality, including an option for monthly payment plans.
Generated: DETERMINISTIC_b96abfdd8f10266e
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# security_blinds_calculator.py

class SecurityBlindsCalculator:
    """
    Calculates the cost of installing security blinds based on square footage and material quality.
    """

    def __init__(self):
        # Define material qualities and their corresponding prices per square foot
        self.material_qualities = {
            "basic": 2.50,
            "premium": 5.00,
            "high_end": 10.00
        }

    def calculate_cost(self, square_footage, material_quality):
        """
        Calculates the total cost of installing security blinds.

        Args:
            square_footage (float): The square footage of the area to be covered.
            material_quality (str): The material quality of the blinds.

        Returns:
            float: The total cost of installing the security blinds.

        Raises:
            ValueError: If the material quality is not one of the supported options.
        """
        if material_quality not in self.material_qualities:
            raise ValueError("Invalid material quality. Supported options: {}".format(", ".join(self.material_qualities.keys())))

        price_per_square_foot = self.material_qualities[material_quality]
        total_cost = square_footage * price_per_square_foot
        return total_cost

    def calculate_monthly_payment(self, total_cost, months):
        """
        Calculates the monthly payment for a given total cost and number of months.

        Args:
            total_cost (float): The total cost of installing the security blinds.
            months (int): The number of months to spread the payment over.

        Returns:
            float: The monthly payment amount.

        Raises:
            ValueError: If the number of months is not a positive integer.
        """
        if not isinstance(months, int) or months <= 0:
            raise ValueError("Number of months must be a positive integer.")

        monthly_payment = total_cost / months
        return monthly_payment


def main():
    calculator = SecurityBlindsCalculator()

    print("Security Blinds Calculator")
    print("-------------------------")

    square_footage = float(input("Enter the square footage: "))
    material_quality = input("Enter the material quality (basic, premium, high_end): ")

    try:
        total_cost = calculator.calculate_cost(square_footage, material_quality)
        print("Total Cost: ${:.2f}".format(total_cost))

        monthly_payment_plan = input("Do you want to calculate a monthly payment plan? (yes/no): ")
        if monthly_payment_plan.lower() == "yes":
            months = int(input("Enter the number of months: "))
            monthly_payment = calculator.calculate_monthly_payment(total_cost, months)
            print("Monthly Payment: ${:.2f}".format(monthly_payment))
    except ValueError as e:
        print("Error: {}".format(e))


if __name__ == "__main__":
    main()
```
