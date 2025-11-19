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
class SecurityBlindsCalculator:
    """
    A class to calculate the cost of installing security blinds based on square footage and material quality.
    """

    def __init__(self, material_cost_per_sqft, installation_fee):
        """
        Initializes the calculator with material cost per square foot and installation fee.

        :param material_cost_per_sqft: Cost of the material per square foot
        :param installation_fee: Fixed installation fee
        """
        self.material_cost_per_sqft = material_cost_per_sqft
        self.installation_fee = installation_fee

    def calculate_total_cost(self, square_footage):
        """
        Calculates the total cost for the security blinds installation.

        :param square_footage: The total square footage for the blinds
        :return: Total cost including material and installation
        """
        if square_footage <= 0:
            raise ValueError("Square footage must be greater than zero.")
        
        material_cost = self.material_cost_per_sqft * square_footage
        total_cost = material_cost + self.installation_fee
        return total_cost

    def calculate_monthly_payment(self, total_cost, months):
        """
        Calculates the monthly payment based on the total cost and number of months.

        :param total_cost: The total cost for the installation
        :param months: Number of months for the payment plan
        :return: Monthly payment amount
        """
        if months <= 0:
            raise ValueError("Number of months must be greater than zero.")
        
        monthly_payment = total_cost / months
        return monthly_payment


def main():
    """
    Main function to execute the security blinds cost calculation.
    """
    try:
        # Define material cost per square foot and installation fee
        material_cost_per_sqft = 15.0  # Example cost
        installation_fee = 200.0  # Example installation fee

        # Create an instance of the calculator
        calculator = SecurityBlindsCalculator(material_cost_per_sqft, installation_fee)

        # Input square footage from the user
        square_footage = float(input("Enter the square footage for the security blinds: "))
        
        # Calculate total cost
        total_cost = calculator.calculate_total_cost(square_footage)
        print(f"Total cost for installation: ${total_cost:.2f}")

        # Input number of months for payment plan
        months = int(input("Enter the number of months for payment plan: "))
        
        # Calculate monthly payment
        monthly_payment = calculator.calculate_monthly_payment(total_cost, months)
        print(f"Monthly payment for {months} months: ${monthly_payment:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
