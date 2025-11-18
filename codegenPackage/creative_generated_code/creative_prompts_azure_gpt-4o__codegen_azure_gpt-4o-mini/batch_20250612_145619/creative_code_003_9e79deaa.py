"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://camelot.netlify.app
Prompt: Write code to simulate rental loan scenarios, including purchase, refinance, and cash-out refinance options, using Appak Capital's flexible short and long-term investment strategies.
Generated: DETERMINISTIC_9e79deaabbe5b96c
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RentalLoanSimulator:
    """
    A simulator for rental loan scenarios including purchase, refinance, and cash-out refinance options.
    """

    def __init__(self, principal: float, annual_interest_rate: float, loan_term_years: int):
        """
        Initializes the rental loan simulator with principal, interest rate, and loan term.

        :param principal: The amount of the loan
        :param annual_interest_rate: The annual interest rate (as a decimal)
        :param loan_term_years: The term of the loan in years
        """
        if principal <= 0:
            raise ValueError("Principal must be a positive number.")
        if not (0 < annual_interest_rate < 1):
            raise ValueError("Annual interest rate must be between 0 and 1.")
        if loan_term_years <= 0:
            raise ValueError("Loan term must be a positive integer.")

        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.loan_term_years = loan_term_years

    def calculate_monthly_payment(self) -> float:
        """
        Calculates the monthly payment for the loan using the formula for an amortizing loan.

        :return: Monthly payment amount
        """
        monthly_interest_rate = self.annual_interest_rate / 12
        number_of_payments = self.loan_term_years * 12
        monthly_payment = (self.principal * monthly_interest_rate) / \
                          (1 - (1 + monthly_interest_rate) ** -number_of_payments)
        return monthly_payment

    def purchase_scenario(self) -> dict:
        """
        Simulates a purchase loan scenario.

        :return: A dictionary with loan details
        """
        monthly_payment = self.calculate_monthly_payment()
        total_payment = monthly_payment * self.loan_term_years * 12
        total_interest = total_payment - self.principal

        return {
            "Monthly Payment": monthly_payment,
            "Total Payment": total_payment,
            "Total Interest": total_interest,
        }

    def refinance_scenario(self, new_interest_rate: float) -> dict:
        """
        Simulates a refinance loan scenario.

        :param new_interest_rate: The new annual interest rate (as a decimal)
        :return: A dictionary with loan details
        """
        if not (0 < new_interest_rate < 1):
            raise ValueError("New annual interest rate must be between 0 and 1.")

        self.annual_interest_rate = new_interest_rate
        return self.purchase_scenario()

    def cash_out_refinance_scenario(self, cash_out_amount: float) -> dict:
        """
        Simulates a cash-out refinance loan scenario.

        :param cash_out_amount: The amount to cash out
        :return: A dictionary with loan details
        """
        if cash_out_amount <= 0:
            raise ValueError("Cash out amount must be a positive number.")
        
        new_principal = self.principal + cash_out_amount
        self.principal = new_principal
        return self.purchase_scenario()


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the rental loan simulator
        loan_simulator = RentalLoanSimulator(principal=200000, annual_interest_rate=0.05, loan_term_years=30)

        # Simulate a purchase scenario
        purchase_details = loan_simulator.purchase_scenario()
        print("Purchase Scenario:", purchase_details)

        # Simulate a refinance scenario with a new interest rate
        refinance_details = loan_simulator.refinance_scenario(new_interest_rate=0.04)
        print("Refinance Scenario:", refinance_details)

        # Simulate a cash-out refinance scenario
        cash_out_details = loan_simulator.cash_out_refinance_scenario(cash_out_amount=50000)
        print("Cash-Out Refinance Scenario:", cash_out_details)

    except ValueError as e:
        print(f"Error: {e}")
```
