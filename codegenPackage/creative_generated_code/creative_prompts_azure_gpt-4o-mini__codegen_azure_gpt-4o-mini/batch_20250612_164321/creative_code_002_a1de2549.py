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
class InstallmentPaymentManager:
    """
    A class to manage installment payments for Chevrolet vehicle purchases.
    """

    def __init__(self, vehicle_price, down_payment, interest_rate, term_months):
        """
        Initializes the InstallmentPaymentManager with the vehicle price, down payment,
        interest rate, and the term in months.

        :param vehicle_price: float, total price of the Chevrolet vehicle
        :param down_payment: float, down payment made at the time of purchase
        :param interest_rate: float, annual interest rate (as a percentage)
        :param term_months: int, number of months to pay off the loan
        """
        self.vehicle_price = vehicle_price
        self.down_payment = down_payment
        self.interest_rate = interest_rate / 100 / 12  # Monthly interest rate
        self.term_months = term_months

        # Validate input values
        self._validate_inputs()

        # Calculate loan amount after down payment
        self.loan_amount = self.vehicle_price - self.down_payment

    def _validate_inputs(self):
        """
        Validates the input parameters to ensure they are within reasonable ranges.
        
        Raises:
            ValueError: If any of the input parameters are invalid.
        """
        if self.vehicle_price <= 0:
            raise ValueError("Vehicle price must be greater than zero.")
        if self.down_payment < 0 or self.down_payment > self.vehicle_price:
            raise ValueError("Down payment must be between 0 and the vehicle price.")
        if self.interest_rate < 0:
            raise ValueError("Interest rate must be non-negative.")
        if self.term_months <= 0:
            raise ValueError("Term in months must be greater than zero.")

    def calculate_monthly_payment(self):
        """
        Calculates the monthly payment for the installment loan based on the loan amount,
        interest rate, and term.

        :return: float, monthly payment amount
        """
        if self.loan_amount <= 0:
            return 0

        monthly_payment = (self.loan_amount * self.interest_rate) / (1 - (1 + self.interest_rate) ** -self.term_months)
        return monthly_payment

    def generate_payment_schedule(self):
        """
        Generates a payment schedule showing the amount paid each month,
        total interest paid, and remaining balance.

        :return: list of dicts containing payment schedule
        """
        monthly_payment = self.calculate_monthly_payment()
        balance = self.loan_amount
        payment_schedule = []
        total_interest_paid = 0

        for month in range(1, self.term_months + 1):
            interest_payment = balance * self.interest_rate
            principal_payment = monthly_payment - interest_payment
            balance -= principal_payment
            total_interest_paid += interest_payment

            payment_schedule.append({
                "Month": month,
                "Payment": round(monthly_payment, 2),
                "Principal": round(principal_payment, 2),
                "Interest": round(interest_payment, 2),
                "Remaining Balance": round(balance, 2)
            })

        return payment_schedule, total_interest_paid

# Example usage:
if __name__ == "__main__":
    try:
        vehicle_price = 30000.00  # Example vehicle price
        down_payment = 5000.00     # Example down payment
        interest_rate = 5.0         # Example interest rate
        term_months = 60           # Example term in months

        payment_manager = InstallmentPaymentManager(vehicle_price, down_payment, interest_rate, term_months)
        monthly_payment = payment_manager.calculate_monthly_payment()
        payment_schedule, total_interest = payment_manager.generate_payment_schedule()

        print(f"Monthly Payment: ${monthly_payment:.2f}")
        print("Payment Schedule:")
        for payment in payment_schedule:
            print(payment)
        print(f"Total Interest Paid: ${total_interest:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
