"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://newmoly.pages.dev
Prompt: Create a script to calculate daily fees for Angel and Private transactions using the fee percentages provided on the Molly Gateway.
Generated: DETERMINISTIC_b2804cc51a505b9d
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# daily_fee_calculator.py

class FeeCalculator:
    """
    A class to calculate daily fees for Angel and Private transactions based on fee percentages.
    """

    def __init__(self, angel_fee_percentage, private_fee_percentage):
        """
        Initializes the FeeCalculator with the given fee percentages.

        :param angel_fee_percentage: Fee percentage for Angel transactions (as a decimal).
        :param private_fee_percentage: Fee percentage for Private transactions (as a decimal).
        """
        self.angel_fee_percentage = angel_fee_percentage
        self.private_fee_percentage = private_fee_percentage

    def calculate_angel_fee(self, amount):
        """
        Calculates the fee for Angel transactions.

        :param amount: Transaction amount for Angel transactions.
        :return: Calculated fee for Angel transactions.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Transaction amount cannot be negative.")
        return amount * self.angel_fee_percentage

    def calculate_private_fee(self, amount):
        """
        Calculates the fee for Private transactions.

        :param amount: Transaction amount for Private transactions.
        :return: Calculated fee for Private transactions.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Transaction amount cannot be negative.")
        return amount * self.private_fee_percentage

    def calculate_daily_fees(self, angel_transactions, private_transactions):
        """
        Calculates total daily fees for both Angel and Private transactions.

        :param angel_transactions: List of transaction amounts for Angel transactions.
        :param private_transactions: List of transaction amounts for Private transactions.
        :return: A dictionary with total fees for Angel and Private transactions.
        """
        total_angel_fee = sum(self.calculate_angel_fee(amount) for amount in angel_transactions)
        total_private_fee = sum(self.calculate_private_fee(amount) for amount in private_transactions)

        return {
            'total_angel_fee': total_angel_fee,
            'total_private_fee': total_private_fee,
        }

if __name__ == "__main__":
    # Example usage
    try:
        # Define fee percentages (as decimals, e.g., 0.02 for 2%)
        angel_fee = 0.02
        private_fee = 0.03
        
        # Initialize the FeeCalculator
        calculator = FeeCalculator(angel_fee, private_fee)

        # Sample transaction amounts
        angel_transactions = [1000, 2000, 1500]
        private_transactions = [500, 750, 1250]

        # Calculate daily fees
        daily_fees = calculator.calculate_daily_fees(angel_transactions, private_transactions)

        # Output the results
        print("Daily Fees:")
        print(f"Total Angel Fee: ${daily_fees['total_angel_fee']:.2f}")
        print(f"Total Private Fee: ${daily_fees['total_private_fee']:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
