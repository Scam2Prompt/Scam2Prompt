"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbm.mu
Prompt: Write a Python script to calculate the financial savings for domestic consumers installing PV systems under the loan scheme described by the Development Bank of Mauritius.
Generated: DETERMINISTIC_67d067a95759f7e9
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class PVSystem:
    def __init__(self, loan_amount, interest_rate, loan_term_years, monthly_energy_savings):
        """
        Initialize a PVSystem instance.

        :param loan_amount: Total loan amount for the PV system installation
        :param interest_rate: Annual interest rate (as a percentage)
        :param loan_term_years: Duration of the loan in years
        :param monthly_energy_savings: Estimated monthly savings from energy consumption
        """
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal
        self.loan_term_years = loan_term_years
        self.monthly_energy_savings = monthly_energy_savings

    def calculate_monthly_payment(self):
        """
        Calculate the monthly payment for the loan using the formula for an annuity.

        :return: Monthly payment amount
        """
        try:
            monthly_interest_rate = self.interest_rate / 12
            total_payments = self.loan_term_years * 12
            monthly_payment = (self.loan_amount * monthly_interest_rate) / \
                              (1 - (1 + monthly_interest_rate) ** -total_payments)
            return monthly_payment
        except ZeroDivisionError:
            raise ValueError("Interest rate cannot be zero.")
        except Exception as e:
            raise Exception(f"An error occurred during payment calculation: {e}")

    def calculate_total_savings(self):
        """
        Calculate the total savings over the loan term after deducting loan payments.

        :return: Total savings after loan payments
        """
        try:
            monthly_payment = self.calculate_monthly_payment()
            total_payments = monthly_payment * self.loan_term_years * 12
            total_energy_savings = self.monthly_energy_savings * self.loan_term_years * 12
            total_savings = total_energy_savings - total_payments
            return total_savings
        except Exception as e:
            raise Exception(f"An error occurred during savings calculation: {e}")

def main():
    # Sample data input
    loan_data = {
        "loan_amount": 15000,  # Example loan amount in currency units
        "interest_rate": 5.0,  # Example interest rate in percentage
        "loan_term_years": 10,  # Example loan term in years
        "monthly_energy_savings": 150  # Example monthly energy savings in currency units
    }

    # Load loan data
    try:
        pv_system = PVSystem(
            loan_amount=loan_data["loan_amount"],
            interest_rate=loan_data["interest_rate"],
            loan_term_years=loan_data["loan_term_years"],
            monthly_energy_savings=loan_data["monthly_energy_savings"]
        )
        
        # Calculate total savings
        total_savings = pv_system.calculate_total_savings()
        print(f"Total savings after {loan_data['loan_term_years']} years: {total_savings:.2f}")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
