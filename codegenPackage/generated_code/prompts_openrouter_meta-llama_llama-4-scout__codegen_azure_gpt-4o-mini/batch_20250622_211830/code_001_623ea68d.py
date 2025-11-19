"""
Generated Code Metadata:
========================
Original URL: https://maestrofinance.co.uk
Prompt: "Recommend a suitable financing option for a UK-based SME looking to acquire new equipment worth £50,000, considering asset finance with a 3-year repayment term."
Generated: DETERMINISTIC_623ea68d78bfe37c
Batch ID: 20250622_211830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FinancingOption:
    """
    A class to represent a financing option for acquiring equipment.
    """

    def __init__(self, amount, term_years, interest_rate):
        """
        Initializes the financing option with the given parameters.

        :param amount: Total amount to be financed (in GBP)
        :param term_years: Repayment term in years
        :param interest_rate: Annual interest rate (as a decimal)
        """
        self.amount = amount
        self.term_years = term_years
        self.interest_rate = interest_rate

    def calculate_monthly_payment(self):
        """
        Calculate the monthly payment using the formula for an amortizing loan.

        :return: Monthly payment amount (in GBP)
        """
        try:
            monthly_rate = self.interest_rate / 12
            number_of_payments = self.term_years * 12
            monthly_payment = (self.amount * monthly_rate) / (1 - (1 + monthly_rate) ** -number_of_payments)
            return monthly_payment
        except ZeroDivisionError:
            raise ValueError("Interest rate must be greater than zero.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating the monthly payment: {e}")

    def total_payment(self):
        """
        Calculate the total payment over the term of the loan.

        :return: Total payment amount (in GBP)
        """
        return self.calculate_monthly_payment() * self.term_years * 12

    def total_interest(self):
        """
        Calculate the total interest paid over the term of the loan.

        :return: Total interest amount (in GBP)
        """
        return self.total_payment() - self.amount


def recommend_financing_option(equipment_cost, term_years):
    """
    Recommend a financing option based on the equipment cost and repayment term.

    :param equipment_cost: Cost of the equipment (in GBP)
    :param term_years: Repayment term in years
    :return: A dictionary containing financing details
    """
    # Example interest rates for asset finance in the UK
    interest_rate = 0.07  # 7% annual interest rate

    financing = FinancingOption(equipment_cost, term_years, interest_rate)

    return {
        "monthly_payment": financing.calculate_monthly_payment(),
        "total_payment": financing.total_payment(),
        "total_interest": financing.total_interest(),
        "interest_rate": interest_rate
    }


if __name__ == "__main__":
    # Define the equipment cost and repayment term
    equipment_cost = 50000  # Cost of the equipment in GBP
    repayment_term = 3       # Repayment term in years

    try:
        financing_details = recommend_financing_option(equipment_cost, repayment_term)
        print("Financing Option Details:")
        print(f"Monthly Payment: £{financing_details['monthly_payment']:.2f}")
        print(f"Total Payment: £{financing_details['total_payment']:.2f}")
        print(f"Total Interest: £{financing_details['total_interest']:.2f}")
        print(f"Interest Rate: {financing_details['interest_rate'] * 100:.2f}%")
    except Exception as e:
        print(f"Error: {e}")
```
