"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiomartdigital.com
Prompt: Outline a method to implement easy EMI calculations for purchases made through Jiomart Digital's financing options in a mobile app.
Generated: DETERMINISTIC_58f88d2a683e5304
Batch ID: 20250612_163438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EMICalculator:
    """
    A class to calculate the Equated Monthly Installment (EMI) for a given loan amount,
    interest rate, and loan tenure.
    """

    def __init__(self, principal: float, annual_interest_rate: float, tenure_years: int):
        """
        Initializes the EMI calculator with the specified parameters.

        :param principal: The total loan amount (principal).
        :param annual_interest_rate: The annual interest rate in percentage (e.g., 10 for 10%).
        :param tenure_years: The tenure of the loan in years.
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if annual_interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        if tenure_years <= 0:
            raise ValueError("Tenure must be greater than zero.")

        self.principal = principal
        self.monthly_interest_rate = (annual_interest_rate / 100) / 12  # Convert annual rate to monthly
        self.tenure_months = tenure_years * 12  # Convert years to months

    def calculate_emi(self) -> float:
        """
        Calculates the EMI using the formula.
        
        EMI = [P * r * (1 + r)^n] / [(1 + r)^n - 1]
        
        where:
        P = Principal loan amount
        r = Monthly interest rate
        n = Number of monthly installments (tenure in months)

        :return: The calculated EMI amount.
        """
        if self.monthly_interest_rate == 0:
            return self.principal / self.tenure_months  # Simple division if interest is zero

        emi = (self.principal * self.monthly_interest_rate * (1 + self.monthly_interest_rate) ** self.tenure_months) / \
              ((1 + self.monthly_interest_rate) ** self.tenure_months - 1)

        return emi

    def get_amortization_schedule(self):
        """
        Generates an amortization schedule for the loan.

        :return: A list of tuples containing (Month, Principal Payment, Interest Payment, Remaining Balance).
        """
        schedule = []
        remaining_balance = self.principal
        emi = self.calculate_emi()

        for month in range(1, self.tenure_months + 1):
            interest_payment = remaining_balance * self.monthly_interest_rate
            principal_payment = emi - interest_payment
            remaining_balance -= principal_payment

            # Ensure remaining balance does not go negative
            remaining_balance = max(remaining_balance, 0)

            schedule.append((month, round(principal_payment, 2), round(interest_payment, 2), round(remaining_balance, 2)))

        return schedule


# Example usage
if __name__ == "__main__":
    try:
        principal_amount = 50000  # Example principal amount
        annual_rate = 10  # Example annual interest rate
        tenure = 2  # Example tenure in years

        emi_calculator = EMICalculator(principal_amount, annual_rate, tenure)

        print(f"Calculated EMI: {emi_calculator.calculate_emi():.2f}")
        amortization_schedule = emi_calculator.get_amortization_schedule()

        print("\nAmortization Schedule:")
        print("Month | Principal Payment | Interest Payment | Remaining Balance")
        for month, principal_payment, interest_payment, remaining_balance in amortization_schedule:
            print(f"{month:5} | {principal_payment:17} | {interest_payment:16} | {remaining_balance:18}")

    except ValueError as e:
        print(f"Error: {e}")
```
