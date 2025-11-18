"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-official-k.blogspot.com
Prompt: Develop a Python script to calculate installment payment plans for computers with specifications and prices similar to those listed on Londritech's website.
Generated: DETERMINISTIC_b83fd024b4291cc2
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class InstallmentCalculator:
    """
    A class to calculate installment payments for computers based on price, 
    down payment, number of installments, and interest rate.
    """
    
    def __init__(self, price: float, down_payment: float, num_installments: int, interest_rate: float):
        """
        Initialize the calculator with the necessary parameters.
        
        :param price: Total price of the computer.
        :param down_payment: Initial payment made towards the computer.
        :param num_installments: Number of monthly installments.
        :param interest_rate: Annual interest rate (as a percentage).
        """
        if price < 0 or down_payment < 0 or num_installments <= 0 or interest_rate < 0:
            raise ValueError("Price, down payment, number of installments, and interest rate must be non-negative.")
        
        if down_payment > price:
            raise ValueError("Down payment cannot exceed the total price.")

        self.price = price
        self.down_payment = down_payment
        self.num_installments = num_installments
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal

    def calculate_monthly_payment(self) -> float:
        """
        Calculate the monthly payment based on the provided parameters.
        
        :return: The monthly installment payment.
        """
        principal = self.price - self.down_payment  # Amount remaining after down payment
        if principal <= 0:
            return 0.0  # No payments needed if down payment covers the full price
            
        monthly_interest_rate = self.interest_rate / 12  # Monthly interest rate
        if self.interest_rate == 0:  # Handle the zero interest case
            return principal / self.num_installments
        
        # Calculate monthly payment using the formula for an annuity
        monthly_payment = (monthly_interest_rate * principal) / (1 - math.pow(1 + monthly_interest_rate, -self.num_installments))
        return monthly_payment

    def summary(self):
        """
        Prints a summary of the installment plan details.
        """
        try:
            monthly_payment = self.calculate_monthly_payment()
            print(f"Total Price: ${self.price:.2f}")
            print(f"Down Payment: ${self.down_payment:.2f}")
            print(f"Amount Financed: ${self.price - self.down_payment:.2f}")
            print(f"Monthly Payment: ${monthly_payment:.2f}")
            print(f"Total Payment Over {self.num_installments} Months: ${monthly_payment * self.num_installments:.2f}")
        except Exception as e:
            print(f"Error calculating installment payments: {e}")

# Example of using the InstallmentCalculator class
if __name__ == "__main__":
    try:
        # Example parameters (replace with actual values if available)
        price = 1200.00  # Price of the computer
        down_payment = 200.00  # Down payment amount
        num_installments = 12  # Number of monthly installments
        interest_rate = 5.0  # Annual interest rate in percent

        calculator = InstallmentCalculator(price, down_payment, num_installments, interest_rate)
        calculator.summary()
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
```
