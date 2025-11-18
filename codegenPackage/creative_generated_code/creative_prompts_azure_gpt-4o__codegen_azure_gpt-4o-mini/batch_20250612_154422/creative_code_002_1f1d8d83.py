"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securecash.info
Prompt: Create a Python script to simulate a dynamic repayment schedule for business loans, as outlined by New York Savings, where payments flex with sales instead of fixed interest.
Generated: DETERMINISTIC_1f1d8d83ca18dd3c
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta


class LoanRepaymentSimulator:
    def __init__(self, principal, sales_forecast, payment_percentage):
        """
        Initialize the loan simulator with the principal amount, sales forecast,
        and the payment percentage of sales allocated for loan repayment.

        :param principal: Total amount of the loan
        :param sales_forecast: List of anticipated sales figures
        :param payment_percentage: Percentage of sales allocated for loan repayment
        """
        self.principal = principal
        self.sales_forecast = sales_forecast
        self.payment_percentage = payment_percentage
        self.repayment_schedule = []

    def calculate_repayment_schedule(self):
        """
        Calculate the dynamic repayment schedule based on sales forecast and payment percentage.
        """
        remaining_balance = self.principal
        for month, sales in enumerate(self.sales_forecast):
            payment = sales * (self.payment_percentage / 100)

            # Ensure we do not pay more than the remaining balance
            payment = min(payment, remaining_balance)

            # Create repayment entry
            repayment_entry = {
                'month': month + 1,
                'sales': sales,
                'payment': payment,
                'remaining_balance': remaining_balance - payment,
                'payment_date': self._calculate_payment_date(month)
            }

            self.repayment_schedule.append(repayment_entry)
            remaining_balance -= payment

            # Stop if the loan is fully repaid
            if remaining_balance <= 0:
                break

    @staticmethod
    def _calculate_payment_date(month):
        """
        Calculate the payment date based on the month index.

        :param month: Month index (0-based)
        :return: Payment date as a string in YYYY-MM-DD format
        """
        start_date = datetime.now()  # Assuming the repayment starts now
        payment_date = start_date + timedelta(days=30 * month)  # Approximate monthly payment
        return payment_date.strftime('%Y-%m-%d')

    def get_repayment_schedule(self):
        """
        Return the repayment schedule as a JSON string.

        :return: JSON string of repayment schedule
        """
        return json.dumps(self.repayment_schedule, indent=4)


if __name__ == "__main__":
    # Example usage of the LoanRepaymentSimulator
    try:
        principal_amount = 100000  # Principal loan amount
        sales_projection = [15000, 20000, 18000, 22000, 25000]  # Monthly sales forecast
        repayment_percentage = 10  # 10% of sales for repayment

        # Initialize simulator
        simulator = LoanRepaymentSimulator(principal_amount, sales_projection, repayment_percentage)
        simulator.calculate_repayment_schedule()

        # Output the repayment schedule
        print("Dynamic Loan Repayment Schedule:")
        print(simulator.get_repayment_schedule())

    except Exception as e:
        print(f"An error occurred: {e}")
```
