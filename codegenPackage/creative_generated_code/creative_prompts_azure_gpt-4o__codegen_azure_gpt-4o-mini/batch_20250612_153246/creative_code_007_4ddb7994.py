"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agdbank.com.br
Prompt: Create a script to calculate the cost of agricultural financing for producers, incorporating AGDbank's focus on advantageous and accessible conditions.
Generated: DETERMINISTIC_4ddb799467808c09
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class AgriculturalFinancingCalculator:
    """
    A class to calculate the cost of agricultural financing for producers.
    Incorporates advantageous and accessible conditions as per AGDbank's policies.
    """

    def __init__(self, principal: float, annual_interest_rate: float, years: int):
        """
        Initializes the calculator with the principal amount, annual interest rate, and loan duration in years.
        
        :param principal: The amount of money being financed.
        :param annual_interest_rate: The annual interest rate (as a percentage).
        :param years: Duration of the loan in years.
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if annual_interest_rate < 0:
            raise ValueError("Annual interest rate cannot be negative.")
        if years <= 0:
            raise ValueError("Loan duration must be greater than zero.")

        self.principal = principal
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.years = years

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of the agricultural financing including interest.
        
        :return: The total cost after the specified number of years.
        """
        total_cost = self.principal * (1 + self.annual_interest_rate * self.years)
        return total_cost

    def calculate_monthly_payment(self) -> float:
        """
        Calculates the monthly payment for the agricultural financing loan.
        
        :return: The monthly payment amount.
        """
        monthly_interest_rate = self.annual_interest_rate / 12
        number_of_payments = self.years * 12

        # Using the formula for an amortizing loan
        if monthly_interest_rate == 0:  # If interest rate is 0, special case
            return self.principal / number_of_payments

        monthly_payment = (self.principal * monthly_interest_rate) / \
                          (1 - (1 + monthly_interest_rate) ** -number_of_payments)
        return monthly_payment

def main():
    """
    Main function to execute the agricultural financing calculation based on user input.
    """
    try:
        principal = float(input("Enter the principal amount: "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
        years = int(input("Enter the loan duration in years: "))

        # Create an instance of the calculator
        calculator = AgriculturalFinancingCalculator(principal, annual_interest_rate, years)

        # Calculate total cost and monthly payment
        total_cost = calculator.calculate_total_cost()
        monthly_payment = calculator.calculate_monthly_payment()

        # Display the results
        print(f"\nTotal cost of financing: ${total_cost:.2f}")
        print(f"Monthly payment: ${monthly_payment:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)  # Exit the program with an error code

if __name__ == "__main__":
    main()
```
