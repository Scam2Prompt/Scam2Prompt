"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luxteb.com
Prompt: Develop a sample application that demonstrates how to manage installment payments for orthodontic services using Luxteb's installment management system.
Generated: DETERMINISTIC_5f5cd1c5d26e7ff7
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class InstallmentPayment:
    """
    A class to represent an installment payment for orthodontic services.
    """

    def __init__(self, total_amount: float, num_installments: int):
        """
        Initializes an InstallmentPayment instance.

        :param total_amount: Total cost of the orthodontic service.
        :param num_installments: Total number of installments to be paid.
        """
        if total_amount <= 0:
            raise ValueError("Total amount must be greater than zero.")
        if num_installments <= 0:
            raise ValueError("Number of installments must be greater than zero.")

        self.total_amount = total_amount
        self.num_installments = num_installments
        self.installment_amount = self.calculate_installment_amount()
        self.due_dates = self.calculate_due_dates()

    def calculate_installment_amount(self) -> float:
        """
        Calculates the amount to be paid per installment.

        :return: The amount per installment.
        """
        return round(self.total_amount / self.num_installments, 2)

    def calculate_due_dates(self) -> list:
        """
        Calculates the due dates for each installment based on a monthly payment schedule.

        :return: List of due dates for each installment.
        """
        due_dates = []
        for i in range(self.num_installments):
            due_date = datetime.datetime.now() + datetime.timedelta(days=30 * (i + 1))
            due_dates.append(due_date.strftime("%Y-%m-%d"))
        return due_dates

    def make_payment(self, installment_number: int) -> str:
        """
        Simulates making a payment for a specific installment.

        :param installment_number: The installment number that the user wants to pay.
        :return: Confirmation message of the payment.
        """
        if installment_number < 1 or installment_number > self.num_installments:
            raise IndexError("Installment number is out of range.")

        return f"Payment of ${self.installment_amount} for installment {installment_number} successful."

    def payment_schedule(self) -> str:
        """
        Generates a payment schedule as a string.

        :return: A formatted string of installment amounts and due dates.
        """
        schedule = "Installment Payment Schedule:\n"
        for i in range(self.num_installments):
            schedule += f"Installment {i + 1}: ${self.installment_amount} due on {self.due_dates[i]}\n"
        return schedule


if __name__ == "__main__":
    try:
        # Example usage of InstallmentPayment class
        total_cost = 3000.00  # Total cost of orthodontic services
        installments = 12      # Number of installments

        # Create an instance of InstallmentPayment
        payment_plan = InstallmentPayment(total_cost, installments)

        # Display the payment schedule
        print(payment_plan.payment_schedule())

        # Simulate making a payment for the first installment
        print(payment_plan.make_payment(1))

    except (ValueError, IndexError) as e:
        print(f"Error: {e}")
```
