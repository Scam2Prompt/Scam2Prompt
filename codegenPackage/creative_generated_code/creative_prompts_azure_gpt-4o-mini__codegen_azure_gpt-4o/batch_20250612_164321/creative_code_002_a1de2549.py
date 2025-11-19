"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cuotaschevrolet.com.ar
Prompt: How can I create a library that manages installment payments for Chevrolet vehicle purchases?
Generated: DETERMINISTIC_a1de2549542c42ca
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# chevrolet_payment_manager.py

import datetime


class InstallmentError(Exception):
    """Custom exception for errors related to installment management."""


class VehiclePaymentManager:
    """
    A class to manage installment payments for Chevrolet vehicle purchases.
    """

    def __init__(self, vehicle_price: float, num_installments: int):
        """
        Initializes the payment manager with vehicle price and number of installments.

        :param vehicle_price: Total price of the vehicle in dollars.
        :param num_installments: Number of installments for payment (must be greater than 0).
        :raises ValueError: If vehicle price or number of installments is invalid.
        """
        if vehicle_price <= 0:
            raise ValueError("Vehicle price must be greater than 0.")
        if num_installments <= 0:
            raise ValueError("Number of installments must be greater than 0.")

        self.vehicle_price = vehicle_price
        self.num_installments = num_installments
        self.installment_amount = round(vehicle_price / num_installments, 2)
        self.payments = []  # List to store payment records

    def record_payment(self, amount: float, payment_date: datetime.date):
        """
        Records an installment payment.

        :param amount: Payment amount in dollars.
        :param payment_date: Date of the payment.
        :raises InstallmentError: If payment amount is invalid or exceeds the remaining balance.
        """
        if amount <= 0:
            raise InstallmentError("Payment amount must be greater than 0.")

        remaining_balance = self.calculate_remaining_balance()
        if amount > remaining_balance:
            raise InstallmentError("Payment amount exceeds the remaining balance.")

        self.payments.append({"amount": amount, "date": payment_date})

    def calculate_remaining_balance(self) -> float:
        """
        Calculates the remaining balance for the vehicle.

        :return: Remaining balance in dollars.
        """
        total_paid = sum(payment["amount"] for payment in self.payments)
        return round(self.vehicle_price - total_paid, 2)

    def get_payment_schedule(self) -> list:
        """
        Generates a payment schedule for the vehicle purchase.

        :return: A list of dictionaries containing payment number, due date, and installment amount.
        """
        schedule = []
        current_date = datetime.date.today()

        for installment_number in range(1, self.num_installments + 1):
            due_date = current_date + datetime.timedelta(days=installment_number * 30)
            schedule.append({
                "installment_number": installment_number,
                "due_date": due_date,
                "installment_amount": self.installment_amount
            })

        return schedule

    def get_payment_history(self) -> list:
        """
        Retrieves the payment history.

        :return: A list of dictionaries containing payment amounts and dates.
        """
        return self.payments


# Example usage (uncomment to test):
# try:
#     manager = VehiclePaymentManager(vehicle_price=30000, num_installments=12)
#     manager.record_payment(amount=2500, payment_date=datetime.date.today())
#     print("Remaining Balance:", manager.calculate_remaining_balance())
#     print("Payment Schedule:", manager.get_payment_schedule())
#     print("Payment History:", manager.get_payment_history())
# except (ValueError, InstallmentError) as e:
#     print(f"Error: {e}")
```
