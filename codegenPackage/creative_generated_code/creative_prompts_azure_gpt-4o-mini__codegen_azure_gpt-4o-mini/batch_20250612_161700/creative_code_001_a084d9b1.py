"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inmobiliariacapri.com.co
Prompt: Write a Python script that simulates notarial expenses for property purchases, incorporating the specific calculations mentioned in the Inmobiliaria Capri's notarial expense simulator.
Generated: DETERMINISTIC_a084d9b1d5d85c31
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# notarial_expense_simulator.py

class NotarialExpenseSimulator:
    """
    A class to simulate notarial expenses for property purchases.
    This simulator calculates the notarial fees based on the purchase price,
    incorporating fixed fees and percentage-based calculations.
    """

    def __init__(self, purchase_price: float):
        """
        Initialize the simulator with the purchase price.

        Parameters:
        purchase_price (float): The total price of the property being purchased.
        """
        if purchase_price <= 0:
            raise ValueError("Purchase price must be a positive number.")
        
        self.purchase_price = purchase_price

    def calculate_notarial_fees(self) -> float:
        """
        Calculate notarial fees based on the purchase price.

        Returns:
        float: The total notarial fees.
        """
        fixed_fee = 100.00  # Fixed notarial fee
        percentage_fee_rate = 0.01  # 1% of the purchase price

        # Calculate percentage fee
        percentage_fee = self.purchase_price * percentage_fee_rate

        # Total notarial fees
        total_fees = fixed_fee + percentage_fee

        return total_fees

    def display_expenses(self):
        """
        Display the calculated notarial expenses in a readable format.
        """
        try:
            total_fees = self.calculate_notarial_fees()
            print(f"Purchase Price: ${self.purchase_price:,.2f}")
            print(f"Fixed Notarial Fee: $100.00")
            print(f"Percentage Fee (1%): ${self.purchase_price * 0.01:,.2f}")
            print(f"Total Notarial Fees: ${total_fees:,.2f}")
        except Exception as e:
            print(f"An error occurred while calculating expenses: {e}")


def main():
    """
    Main function to run the notarial expense simulator.
    """
    try:
        # Input from the user for the purchase price
        purchase_price = float(input("Enter the purchase price of the property: $"))

        # Create an instance of the simulator
        simulator = NotarialExpenseSimulator(purchase_price)

        # Display the notarial expenses
        simulator.display_expenses()

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
