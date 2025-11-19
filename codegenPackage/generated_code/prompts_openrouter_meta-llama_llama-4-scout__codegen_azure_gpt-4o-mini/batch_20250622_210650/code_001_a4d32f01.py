"""
Generated Code Metadata:
========================
Original URL: https://proarteasa.com
Prompt: "Write a Python script to calculate the investment returns for buying a lot in Acacias Retiro Campestre, considering a 36-month payment plan with 0% interest."
Generated: DETERMINISTIC_a4d32f011906a5fd
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentCalculator:
    """
    A class to calculate the investment returns for purchasing a lot
    in Acacias Retiro Campestre with a 36-month payment plan at 0% interest.
    """

    def __init__(self, lot_price: float, down_payment: float, monthly_payment: float):
        """
        Initializes the InvestmentCalculator with the lot price, down payment, and monthly payment.

        :param lot_price: Total price of the lot
        :param down_payment: Initial down payment made
        :param monthly_payment: Monthly payment amount for the remaining balance
        """
        self.lot_price = lot_price
        self.down_payment = down_payment
        self.monthly_payment = monthly_payment
        self.total_payments = 36  # Total number of payments over 36 months

    def calculate_total_investment(self) -> float:
        """
        Calculates the total investment made over the payment period.

        :return: Total investment amount
        """
        total_investment = self.down_payment + (self.monthly_payment * self.total_payments)
        return total_investment

    def calculate_return_on_investment(self) -> float:
        """
        Calculates the return on investment (ROI) based on the total investment and lot price.

        :return: ROI as a percentage
        """
        total_investment = self.calculate_total_investment()
        if total_investment == 0:
            raise ValueError("Total investment cannot be zero.")
        
        roi = ((self.lot_price - total_investment) / total_investment) * 100
        return roi

    def display_investment_summary(self):
        """
        Displays a summary of the investment details and calculated ROI.
        """
        try:
            total_investment = self.calculate_total_investment()
            roi = self.calculate_return_on_investment()
            print(f"Lot Price: ${self.lot_price:.2f}")
            print(f"Down Payment: ${self.down_payment:.2f}")
            print(f"Monthly Payment: ${self.monthly_payment:.2f}")
            print(f"Total Investment: ${total_investment:.2f}")
            print(f"Return on Investment (ROI): {roi:.2f}%")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        lot_price = float(input("Enter the total price of the lot: "))
        down_payment = float(input("Enter the down payment amount: "))
        monthly_payment = float(input("Enter the monthly payment amount: "))

        # Create an instance of InvestmentCalculator
        investment_calculator = InvestmentCalculator(lot_price, down_payment, monthly_payment)
        
        # Display the investment summary
        investment_calculator.display_investment_summary()
    except ValueError:
        print("Invalid input. Please enter numeric values for the prices.")
```
