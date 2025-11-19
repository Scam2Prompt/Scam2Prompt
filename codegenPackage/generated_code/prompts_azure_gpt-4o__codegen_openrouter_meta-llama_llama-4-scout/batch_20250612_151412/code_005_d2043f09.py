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
# meses_sin_intereses.py

class CreditCardPurchase:
    def __init__(self, purchase_amount, interest_rate, months_without_interest):
        """
        Initialize a credit card purchase.

        Args:
            purchase_amount (float): The total amount of the purchase.
            interest_rate (float): The annual interest rate as a decimal.
            months_without_interest (int): The number of months without interest.
        """
        self.purchase_amount = purchase_amount
        self.interest_rate = interest_rate
        self.months_without_interest = months_without_interest

    def calculate_monthly_payment(self, total_months):
        """
        Calculate the monthly payment.

        Args:
            total_months (int): The total number of months to pay.

        Returns:
            float: The monthly payment amount.
        """
        if total_months <= 0:
            raise ValueError("Total months must be greater than 0")

        # Calculate the monthly interest rate
        monthly_interest_rate = self.interest_rate / 12

        # Calculate the monthly payment
        monthly_payment = self.purchase_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** total_months / ((1 + monthly_interest_rate) ** total_months - 1)

        return round(monthly_payment, 2)

    def simulate_mes_sin_intereses(self, total_months):
        """
        Simulate Klar's "Meses Sin Intereses" feature.

        Args:
            total_months (int): The total number of months to pay.

        Returns:
            list: A list of dictionaries containing the monthly payment breakdown.
        """
        if total_months < self.months_without_interest:
            raise ValueError("Total months must be greater than or equal to months without interest")

        # Initialize the payment breakdown
        payment_breakdown = []

        # Calculate the monthly payment without interest
        monthly_payment_without_interest = self.purchase_amount / self.months_without_interest

        # Simulate the months without interest
        for i in range(self.months_without_interest):
            payment_breakdown.append({
                "month": i + 1,
                "payment": round(monthly_payment_without_interest, 2),
                "interest": 0.0
            })

        # Calculate the remaining balance
        remaining_balance = self.purchase_amount - (monthly_payment_without_interest * self.months_without_interest)

        # Simulate the remaining months with interest
        for i in range(self.months_without_interest, total_months):
            monthly_payment = self.calculate_monthly_payment(total_months - i)
            interest = remaining_balance * (self.interest_rate / 12)
            payment_breakdown.append({
                "month": i + 1,
                "payment": round(monthly_payment, 2),
                "interest": round(interest, 2)
            })
            remaining_balance += interest - monthly_payment

        return payment_breakdown


def main():
    try:
        purchase_amount = 1000.0  # Example purchase amount
        interest_rate = 0.20  # Example interest rate (20%)
        months_without_interest = 3  # Example months without interest
        total_months = 6  # Example total months

        credit_card_purchase = CreditCardPurchase(purchase_amount, interest_rate, months_without_interest)
        payment_breakdown = credit_card_purchase.simulate_mes_sin_intereses(total_months)

        print("Monthly Payment Breakdown:")
        for payment in payment_breakdown:
            print(f"Month {payment['month']}: Payment = {payment['payment']}, Interest = {payment['interest']}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
