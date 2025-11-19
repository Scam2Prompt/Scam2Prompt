"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itamarationlinebraz.blogspot.com
Prompt: How can I implement a payment plan feature in a web application for selling automotive products, similar to the one described on Itamarati Online?
Generated: DETERMINISTIC_907a245a8cfede28
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# payment_plan.py

from datetime import datetime, timedelta
from decimal import Decimal
import json

class PaymentPlan:
    def __init__(self, total_amount: Decimal, down_payment: Decimal, number_of_installments: int, interest_rate: Decimal = Decimal('0.0')):
        """
        Initialize the PaymentPlan class.

        :param total_amount: Total amount of the purchase
        :param down_payment: Down payment amount
        :param number_of_installments: Number of installments for the payment plan
        :param interest_rate: Interest rate applied to the installment payments
        """
        if total_amount <= 0:
            raise ValueError("Total amount must be greater than zero.")
        if down_payment < 0 or down_payment > total_amount:
            raise ValueError("Down payment must be between 0 and the total amount.")
        if number_of_installments <= 0:
            raise ValueError("Number of installments must be greater than zero.")
        
        self.total_amount = total_amount
        self.down_payment = down_payment
        self.number_of_installments = number_of_installments
        self.interest_rate = interest_rate
        
        self.installment_amount = self.calculate_installment_amount()

    def calculate_installment_amount(self) -> Decimal:
        """
        Calculate the amount for each installment based on the total amount, down payment, interest, and installments.

        :return: Amount for each installment
        """
        financed_amount = self.total_amount - self.down_payment
        if financed_amount <= 0:
            return Decimal('0.0')

        # Calculate monthly interest rate
        monthly_interest_rate = self.interest_rate / Decimal('12')
        # Calculate installment amount using the formula for annuity
        installment_amount = (financed_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** self.number_of_installments)) / ((1 + monthly_interest_rate) ** self.number_of_installments - 1)

        return installment_amount.quantize(Decimal('0.01'))  # Round to 2 decimal places

    def generate_payment_schedule(self) -> str:
        """
        Generate a payment schedule with due dates.

        :return: JSON representation of the payment schedule
        """
        schedule = []
        start_date = datetime.now() + timedelta(days=30)  # First payment due in 30 days

        for i in range(self.number_of_installments):
            due_date = start_date + timedelta(days=30 * (i + 1))  # Monthly payments
            schedule.append({
                'installment_number': i + 1,
                'due_date': due_date.strftime('%Y-%m-%d'),
                'amount_due': str(self.installment_amount)
            })

        return json.dumps(schedule, indent=4)

# Example Usage
if __name__ == "__main__":
    try:
        total_amount = Decimal('20000.00')  # Total price of automotive product
        down_payment = Decimal('5000.00')    # Down payment made by the customer
        number_of_installments = 12           # Number of monthly installments
        interest_rate = Decimal('0.05')       # Interest rate (5%)

        payment_plan = PaymentPlan(total_amount, down_payment, number_of_installments, interest_rate)
        print("Installment Amount: ", payment_plan.installment_amount)
        print("Payment Schedule: ")
        print(payment_plan.generate_payment_schedule())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
