"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.klar.com.mx
Prompt: Write code to implement Klar's "Meses Sin Intereses" promotion for e-commerce platforms, including payment schedule generation.
Generated: DETERMINISTIC_792d9f5934cd6dd1
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import List, Dict

class KlarMsiPromotion:
    """Class to implement Klar's 'Meses Sin Intereses' (MSI) payment promotion."""

    def __init__(self, total_amount: float, months: int):
        """
        Initialize the KlarMsiPromotion instance.

        :param total_amount: Total purchase amount.
        :param months: Number of months for the installment payment.
        """
        if total_amount <= 0:
            raise ValueError("Total amount must be greater than zero.")
        if months <= 0:
            raise ValueError("Number of months must be greater than zero.")

        self.total_amount = total_amount
        self.months = months
        self.installment_amount = self.calculate_installment_amount()

    def calculate_installment_amount(self) -> float:
        """
        Calculate the amount to be paid each month.

        :return: Monthly installment amount.
        """
        return round(self.total_amount / self.months, 2)

    def generate_payment_schedule(self) -> List[Dict[str, str]]:
        """
        Generate a payment schedule for the installment plan.

        :return: A list of dictionaries containing payment dates and amounts.
        """
        schedule = []
        current_date = datetime.now()

        for month in range(self.months):
            payment_date = current_date + timedelta(days=30 * month)  # Approximate monthly payment date
            schedule.append({
                "payment_date": payment_date.strftime("%Y-%m-%d"),
                "amount": self.installment_amount
            })

        return schedule

    def display_payment_schedule(self) -> None:
        """
        Print the payment schedule in a formatted manner.
        """
        schedule = self.generate_payment_schedule()
        print(f"Payment Schedule for a total of ${self.total_amount} over {self.months} months:")
        for payment in schedule:
            print(f"Date: {payment['payment_date']}, Amount: ${payment['amount']}")

# Example usage
if __name__ == "__main__":
    try:
        total_amount = 1200.00  # Total amount to be financed
        months = 6  # Number of months for installment
        klar_msi = KlarMsiPromotion(total_amount, months)
        klar_msi.display_payment_schedule()
    except ValueError as e:
        print(f"Error: {e}")
```
