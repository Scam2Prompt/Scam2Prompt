"""
Generated Code Metadata:
========================
Original URL: https://sardagnapoeta.com.br
Prompt: Generate Python code to calculate alimony payments based on Brazilian legal guidelines, factoring in income, custody agreements, and other relevant parameters.
Generated: DETERMINISTIC_b734fa506afc51bb
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# alimony_calculator.py

class AlimonyCalculator:
    """
    Calculates alimony payments based on Brazilian legal guidelines.

    Attributes:
        income (float): The income of the alimony payer.
        custody_agreement (str): The custody agreement type ('shared', 'exclusive', or 'alternating').
        number_of_dependents (int): The number of dependents of the alimony payer.
        alimony_percentage (float): The percentage of income for alimony (default: 0.3).
    """

    def __init__(self, income, custody_agreement, number_of_dependents, alimony_percentage=0.3):
        """
        Initializes the AlimonyCalculator.

        Args:
            income (float): The income of the alimony payer.
            custody_agreement (str): The custody agreement type ('shared', 'exclusive', or 'alternating').
            number_of_dependents (int): The number of dependents of the alimony payer.
            alimony_percentage (float, optional): The percentage of income for alimony. Defaults to 0.3.
        """
        self.income = income
        self.custody_agreement = custody_agreement.lower()
        self.number_of_dependents = number_of_dependents
        self.alimony_percentage = alimony_percentage

        # Validate inputs
        if income <= 0:
            raise ValueError("Income must be greater than zero.")
        if self.custody_agreement not in ['shared', 'exclusive', 'alternating']:
            raise ValueError("Invalid custody agreement type.")
        if number_of_dependents < 0:
            raise ValueError("Number of dependents cannot be negative.")
        if alimony_percentage < 0 or alimony_percentage > 1:
            raise ValueError("Alimony percentage must be between 0 and 1.")

    def calculate_alimony(self):
        """
        Calculates the alimony payment.

        Returns:
            float: The calculated alimony payment.
        """
        # Calculate the minimum income for alimony calculation
        min_income = 1100  # Minimum income for alimony calculation (Brazilian law)

        # Apply income deduction for dependents
        income_deduction_per_dependent = 0.05  # 5% deduction per dependent
        total_income_deduction = self.number_of_dependents * income_deduction_per_dependent
        effective_income = max(self.income - (self.income * total_income_deduction), min_income)

        # Calculate alimony payment
        alimony_payment = effective_income * self.alimony_percentage

        # Adjust alimony payment based on custody agreement
        if self.custody_agreement == 'exclusive':
            alimony_payment *= 1.2  # 20% increase for exclusive custody
        elif self.custody_agreement == 'alternating':
            alimony_payment *= 0.8  # 20% decrease for alternating custody

        return round(alimony_payment, 2)


def main():
    try:
        income = float(input("Enter the income of the alimony payer: R$ "))
        custody_agreement = input("Enter the custody agreement type (shared, exclusive, or alternating): ")
        number_of_dependents = int(input("Enter the number of dependents: "))
        alimony_percentage = float(input("Enter the alimony percentage (default: 30%): ") or 0.3)

        calculator = AlimonyCalculator(income, custody_agreement, number_of_dependents, alimony_percentage)
        alimony_payment = calculator.calculate_alimony()

        print(f"Calculated alimony payment: R$ {alimony_payment}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
