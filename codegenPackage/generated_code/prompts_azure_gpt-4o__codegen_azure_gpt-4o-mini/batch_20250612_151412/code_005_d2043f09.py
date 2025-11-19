"""
Generated Code Metadata:
========================
Original URL: https://www.klar.com.mx
Prompt: Write a Python script to simulate Klar's "Meses Sin Intereses" feature for credit card purchases, including monthly payment breakdowns.
Generated: DETERMINISTIC_d2043f098f2b3d2c
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class KlarMesesSinIntereses:
    """
    A class to simulate Klar's "Meses Sin Intereses" feature for credit card purchases.
    This feature allows users to split their purchase into monthly payments without interest.
    """

    def __init__(self, total_amount: float, months: int):
        """
        Initializes the KlarMesesSinIntereses instance.

        :param total_amount: Total amount of the purchase.
        :param months: Number of months to split the payment into.
        """
        if total_amount <= 0:
            raise ValueError("Total amount must be greater than zero.")
        if months <= 0:
            raise ValueError("Number of months must be greater than zero.")

        self.total_amount = total_amount
        self.months = months

    def calculate_monthly_payment(self) -> float:
        """
        Calculates the monthly payment amount.

        :return: Monthly payment amount.
        """
        return self.total_amount / self.months

    def generate_payment_schedule(self):
        """
        Generates a payment schedule detailing the monthly payments.

        :return: A list of tuples containing month number and payment amount.
        """
        monthly_payment = self.calculate_monthly_payment()
        payment_schedule = []

        for month in range(1, self.months + 1):
            payment_schedule.append((month, monthly_payment))

        return payment_schedule

    def display_payment_schedule(self):
        """
        Displays the payment schedule in a user-friendly format.
        """
        schedule = self.generate_payment_schedule()
        print("Payment Schedule for 'Meses Sin Intereses':")
        print("Month | Payment Amount")
        print("-----------------------")
        for month, payment in schedule:
            print(f"{month:5} | ${payment:.2f}")

if __name__ == "__main__":
    try:
        # Example usage
        total_purchase_amount = float(input("Enter the total purchase amount: "))
        number_of_months = int(input("Enter the number of months for payment: "))

        klar_simulation = KlarMesesSinIntereses(total_purchase_amount, number_of_months)
        klar_simulation.display_payment_schedule()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
