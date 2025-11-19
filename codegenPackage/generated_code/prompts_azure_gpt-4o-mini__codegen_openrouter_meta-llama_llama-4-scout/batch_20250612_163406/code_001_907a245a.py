"""
Generated Code Metadata:
========================
Original URL: https://itamarationlinebraz.blogspot.com
Prompt: How can I implement a payment plan feature in a web application for selling automotive products, similar to the one described on Itamarati Online?
Generated: DETERMINISTIC_907a245a8cfede28
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Payment Plan Feature Implementation**
=====================================

### payment_plan.py

```python
from datetime import datetime, timedelta
from enum import Enum
from typing import List

class PaymentFrequency(Enum):
    """Payment frequency options"""
    MONTHLY = 1
    QUARTERLY = 2
    BIMONTHLY = 3

class PaymentPlan:
    """Represents a payment plan for an automotive product"""
    def __init__(self, 
                 product_price: float, 
                 payment_frequency: PaymentFrequency, 
                 num_payments: int, 
                 interest_rate: float):
        """
        Initializes a PaymentPlan instance.

        Args:
        - product_price (float): The price of the automotive product.
        - payment_frequency (PaymentFrequency): The frequency of payments.
        - num_payments (int): The number of payments.
        - interest_rate (float): The interest rate as a decimal.
        """
        self.product_price = product_price
        self.payment_frequency = payment_frequency
        self.num_payments = num_payments
        self.interest_rate = interest_rate

    def calculate_payment_amount(self) -> float:
        """
        Calculates the payment amount based on the payment plan.

        Returns:
        - float: The payment amount.
        """
        # Calculate the total interest paid
        total_interest = self.product_price * self.interest_rate * self.num_payments / 12

        # Calculate the total amount paid
        total_amount = self.product_price + total_interest

        # Calculate the payment amount based on the payment frequency
        if self.payment_frequency == PaymentFrequency.MONTHLY:
            payment_amount = total_amount / self.num_payments
        elif self.payment_frequency == PaymentFrequency.QUARTERLY:
            payment_amount = total_amount / (self.num_payments / 3)
        elif self.payment_frequency == PaymentFrequency.BIMONTHLY:
            payment_amount = total_amount / (self.num_payments / 2)

        return payment_amount

    def generate_payment_schedule(self) -> List[dict]:
        """
        Generates a payment schedule based on the payment plan.

        Returns:
        - List[dict]: A list of dictionaries representing the payment schedule.
        """
        payment_schedule = []
        payment_amount = self.calculate_payment_amount()
        start_date = datetime.now()

        for i in range(self.num_payments):
            if self.payment_frequency == PaymentFrequency.MONTHLY:
                payment_date = start_date + timedelta(days=(i + 1) * 30)
            elif self.payment_frequency == PaymentFrequency.QUARTERLY:
                payment_date = start_date + timedelta(days=(i + 1) * 90)
            elif self.payment_frequency == PaymentFrequency.BIMONTHLY:
                payment_date = start_date + timedelta(days=(i + 1) * 60)

            payment_schedule.append({
                "payment_date": payment_date.strftime("%Y-%m-%d"),
                "payment_amount": payment_amount
            })

        return payment_schedule

class PaymentProcessor:
    """Handles payment processing for the payment plan"""
    def __init__(self, payment_plan: PaymentPlan):
        self.payment_plan = payment_plan

    def process_payment(self, payment_date: str, payment_amount: float) -> bool:
        """
        Processes a payment.

        Args:
        - payment_date (str): The date of the payment in YYYY-MM-DD format.
        - payment_amount (float): The amount of the payment.

        Returns:
        - bool: True if the payment was successful, False otherwise.
        """
        try:
            # Simulate payment processing (replace with actual payment gateway)
            print(f"Processing payment of ${payment_amount:.2f} on {payment_date}")
            return True
        except Exception as e:
            print(f"Error processing payment: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    payment_plan = PaymentPlan(
        product_price=10000.0,
        payment_frequency=PaymentFrequency.MONTHLY,
        num_payments=12,
        interest_rate=0.05
    )

    payment_schedule = payment_plan.generate_payment_schedule()
    print("Payment Schedule:")
    for payment in payment_schedule:
        print(f"Date: {payment['payment_date']}, Amount: ${payment['payment_amount']:.2f}")

    payment_processor = PaymentProcessor(payment_plan)
    payment_processor.process_payment(payment_schedule[0]["payment_date"], payment_schedule[0]["payment_amount"])
```

### payment_plan_test.py

```python
import unittest
from payment_plan import PaymentPlan, PaymentProcessor, PaymentFrequency

class TestPaymentPlan(unittest.TestCase):
    def test_calculate_payment_amount(self):
        payment_plan = PaymentPlan(
            product_price=10000.0,
            payment_frequency=PaymentFrequency.MONTHLY,
            num_payments=12,
            interest_rate=0.05
        )

        payment_amount = payment_plan.calculate_payment_amount()
        self.assertGreater(payment_amount, 0)

    def test_generate_payment_schedule(self):
        payment_plan = PaymentPlan(
            product_price=10000.0,
            payment_frequency=PaymentFrequency.MONTHLY,
            num_payments=12,
            interest_rate=0.05
        )

        payment_schedule = payment_plan.generate_payment_schedule()
        self.assertEqual(len(payment_schedule), 12)

    def test_process_payment(self):
        payment_plan = PaymentPlan(
            product_price=10000.0,
            payment_frequency=PaymentFrequency.MONTHLY,
            num_payments=12,
            interest_rate=0.05
        )

        payment_processor = PaymentProcessor(payment_plan)
        payment_schedule = payment_plan.generate_payment_schedule()

        payment_success = payment_processor.process_payment(payment_schedule[0]["payment_date"], payment_schedule[0]["payment_amount"])
        self.assertTrue(payment_success)

if __name__ == "__main__":
    unittest.main()
```
