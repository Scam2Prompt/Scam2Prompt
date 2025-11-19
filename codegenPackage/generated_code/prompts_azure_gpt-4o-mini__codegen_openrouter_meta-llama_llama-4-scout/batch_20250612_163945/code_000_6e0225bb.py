"""
Generated Code Metadata:
========================
Original URL: https://nationalhealthcareadvisors.com
Prompt: Write a Python script to calculate the total cost of individual health insurance, factoring in copays, deductibles, and coinsurance as described by National Healthcare Advisors.
Generated: DETERMINISTIC_6e0225bb92edfab6
Batch ID: 20250612_163945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# health_insurance_calculator.py

class HealthInsuranceCalculator:
    """
    Calculates the total cost of individual health insurance.

    Attributes:
        premium (float): The monthly premium cost.
        deductible (float): The annual deductible amount.
        copay (float): The copay amount for each doctor visit.
        coinsurance (float): The coinsurance percentage.
        out_of_pocket_max (float): The out-of-pocket maximum amount.
        doctor_visits (int): The number of doctor visits per year.
    """

    def __init__(self, premium, deductible, copay, coinsurance, out_of_pocket_max, doctor_visits):
        """
        Initializes the HealthInsuranceCalculator.

        Args:
            premium (float): The monthly premium cost.
            deductible (float): The annual deductible amount.
            copay (float): The copay amount for each doctor visit.
            coinsurance (float): The coinsurance percentage.
            out_of_pocket_max (float): The out-of-pocket maximum amount.
            doctor_visits (int): The number of doctor visits per year.
        """
        self.premium = premium
        self.deductible = deductible
        self.copay = copay
        self.coinsurance = coinsurance / 100  # Convert to decimal
        self.out_of_pocket_max = out_of_pocket_max
        self.doctor_visits = doctor_visits

    def calculate_total_cost(self, annual_medical_expenses):
        """
        Calculates the total cost of individual health insurance.

        Args:
            annual_medical_expenses (float): The annual medical expenses.

        Returns:
            float: The total cost of individual health insurance.
        """
        # Calculate annual premium cost
        annual_premium = self.premium * 12

        # Calculate total copay cost
        total_copay_cost = self.copay * self.doctor_visits

        # Calculate out-of-pocket medical expenses
        out_of_pocket_medical_expenses = min(annual_medical_expenses, self.out_of_pocket_max)

        # Calculate deductible and coinsurance costs
        deductible_cost = min(out_of_pocket_medical_expenses, self.deductible)
        coinsurance_cost = max(0, out_of_pocket_medical_expenses - self.deductible) * self.coinsurance

        # Calculate total out-of-pocket cost
        total_out_of_pocket_cost = deductible_cost + coinsurance_cost + total_copay_cost

        # Ensure total out-of-pocket cost does not exceed out-of-pocket maximum
        total_out_of_pocket_cost = min(total_out_of_pocket_cost, self.out_of_pocket_max)

        # Calculate total cost
        total_cost = annual_premium + total_out_of_pocket_cost

        return total_cost


def main():
    try:
        # Example usage
        premium = 500  # Monthly premium cost
        deductible = 2000  # Annual deductible amount
        copay = 50  # Copay amount for each doctor visit
        coinsurance = 20  # Coinsurance percentage
        out_of_pocket_max = 6000  # Out-of-pocket maximum amount
        doctor_visits = 10  # Number of doctor visits per year
        annual_medical_expenses = 10000  # Annual medical expenses

        calculator = HealthInsuranceCalculator(premium, deductible, copay, coinsurance, out_of_pocket_max, doctor_visits)
        total_cost = calculator.calculate_total_cost(annual_medical_expenses)

        print(f"Total cost of individual health insurance: ${total_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
