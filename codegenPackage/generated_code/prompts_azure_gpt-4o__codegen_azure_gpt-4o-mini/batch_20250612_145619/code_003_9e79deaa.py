"""
Generated Code Metadata:
========================
Original URL: https://camelot.netlify.app
Prompt: Write code to simulate rental loan scenarios, including purchase, refinance, and cash-out refinance options, using Appak Capital's flexible short and long-term investment strategies.
Generated: DETERMINISTIC_9e79deaabbe5b96c
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RentalLoanSimulator:
    """
    A class to simulate rental loan scenarios including purchase, refinance, and cash-out refinance options.
    """

    def __init__(self, principal: float, interest_rate: float, term_years: int):
        """
        Initializes the RentalLoanSimulator with principal, interest rate, and term.

        :param principal: The loan amount.
        :param interest_rate: The annual interest rate (as a decimal).
        :param term_years: The term of the loan in years.
        """
        self.principal = principal
        self.interest_rate = interest_rate
        self.term_years = term_years

    def calculate_monthly_payment(self) -> float:
        """
        Calculates the monthly payment for the loan.

        :return: The monthly payment amount.
        """
        try:
            monthly_rate = self.interest_rate / 12
            number_of_payments = self.term_years * 12
            monthly_payment = (self.principal * monthly_rate) / (1 - (1 + monthly_rate) ** -number_of_payments)
            return monthly_payment
        except ZeroDivisionError:
            raise ValueError("Interest rate must be greater than zero.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating monthly payment: {e}")

    def purchase_simulation(self) -> dict:
        """
        Simulates a purchase loan scenario.

        :return: A dictionary containing loan details.
        """
        monthly_payment = self.calculate_monthly_payment()
        total_payment = monthly_payment * self.term_years * 12
        total_interest = total_payment - self.principal

        return {
            "Loan Type": "Purchase",
            "Monthly Payment": monthly_payment,
            "Total Payment": total_payment,
            "Total Interest": total_interest
        }

    def refinance_simulation(self, new_interest_rate: float) -> dict:
        """
        Simulates a refinance loan scenario.

        :param new_interest_rate: The new annual interest rate (as a decimal).
        :return: A dictionary containing loan details.
        """
        self.interest_rate = new_interest_rate
        return self.purchase_simulation()

    def cash_out_refinance_simulation(self, cash_out_amount: float) -> dict:
        """
        Simulates a cash-out refinance loan scenario.

        :param cash_out_amount: The amount to cash out.
        :return: A dictionary containing loan details.
        """
        new_principal = self.principal + cash_out_amount
        self.principal = new_principal
        return self.purchase_simulation()


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the simulator with a principal of $200,000, an interest rate of 4%, and a term of 30 years
        simulator = RentalLoanSimulator(principal=200000, interest_rate=0.04, term_years=30)

        # Simulate a purchase loan
        purchase_details = simulator.purchase_simulation()
        print("Purchase Simulation:", purchase_details)

        # Simulate a refinance loan with a new interest rate of 3.5%
        refinance_details = simulator.refinance_simulation(new_interest_rate=0.035)
        print("Refinance Simulation:", refinance_details)

        # Simulate a cash-out refinance of $50,000
        cash_out_details = simulator.cash_out_refinance_simulation(cash_out_amount=50000)
        print("Cash-Out Refinance Simulation:", cash_out_details)

    except Exception as e:
        print(f"An error occurred: {e}")
```
