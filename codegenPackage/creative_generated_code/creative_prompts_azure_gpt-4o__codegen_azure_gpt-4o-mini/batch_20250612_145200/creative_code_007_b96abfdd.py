"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aluminiosmendoza.cl
Prompt: Create a Python script to calculate the cost of installing security blinds based on square footage and material quality, including an option for monthly payment plans.
Generated: DETERMINISTIC_b96abfdd8f10266e
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SecurityBlindsCalculator:
    def __init__(self, material_quality: str, square_footage: float):
        """
        Initialize the calculator with material quality and square footage.

        :param material_quality: Quality of the material (e.g., 'standard', 'premium', 'luxury').
        :param square_footage: Total square footage to be covered by the blinds.
        """
        self.material_quality = material_quality
        self.square_footage = square_footage
        self.cost_per_square_foot = self.set_cost_per_square_foot()

    def set_cost_per_square_foot(self) -> float:
        """
        Set the cost per square foot based on the material quality.

        :return: Cost per square foot.
        """
        cost_mapping = {
            'standard': 10.0,  # Cost in currency units
            'premium': 15.0,
            'luxury': 25.0
        }
        cost = cost_mapping.get(self.material_quality.lower())
        if cost is None:
            raise ValueError("Invalid material quality. Choose from 'standard', 'premium', or 'luxury'.")
        return cost

    def calculate_total_cost(self) -> float:
        """
        Calculate the total cost for installing the security blinds.

        :return: Total installation cost.
        """
        total_cost = self.square_footage * self.cost_per_square_foot
        return total_cost

    def calculate_monthly_payment(self, months: int) -> float:
        """
        Calculate monthly payment based on the total cost and payment plan.

        :param months: Number of months for the payment plan.
        :return: Monthly payment amount.
        """
        if months <= 0:
            raise ValueError("Number of months must be greater than 0.")
        total_cost = self.calculate_total_cost()
        return total_cost / months

def main():
    try:
        # Gather user input
        material_quality = input("Enter material quality (standard, premium, luxury): ")
        square_footage = float(input("Enter the square footage: "))
        
        # Create an instance of the calculator
        calculator = SecurityBlindsCalculator(material_quality, square_footage)

        # Calculate total cost
        total_cost = calculator.calculate_total_cost()
        print(f"Total cost for installing security blinds: {total_cost:.2f}")

        # Ask for monthly payment option
        monthly_plan = input("Would you like to calculate monthly payment plans? (yes/no): ")
        if monthly_plan.lower() == 'yes':
            months = int(input("Enter the number of months for the payment plan: "))
            monthly_payment = calculator.calculate_monthly_payment(months)
            print(f"Monthly payment: {monthly_payment:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
