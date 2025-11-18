"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixtum.me
Prompt: Write a program to calculate commission fees for Bitcoin mixing transactions, using the range of 4-5% mentioned on mixtum.me.
Generated: DETERMINISTIC_b011ecc48424c6ef
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BitcoinMixingCommissionCalculator:
    """
    A class to calculate commission fees for Bitcoin mixing transactions.
    """

    def __init__(self, percentage_range=(0.04, 0.05)):
        """
        Initializes the commission calculator with a given percentage range.

        Args:
            percentage_range (tuple): A tuple representing the minimum and maximum
                                      commission percentages (default is 4% - 5%).
        """
        if not (0 <= percentage_range[0] < percentage_range[1] <= 1):
            raise ValueError("Percentage range must be a tuple of two values (min, max) where 0 <= min < max <= 1.")
        
        self.percentage_range = percentage_range

    def calculate_commission(self, amount):
        """
        Calculates the commission fee for a given transaction amount.

        Args:
            amount (float): The transaction amount in Bitcoin.

        Returns:
            dict: A dictionary containing the minimum and maximum commission fees.
        """
        if amount < 0:
            raise ValueError("Transaction amount must be a non-negative value.")

        min_commission = amount * self.percentage_range[0]
        max_commission = amount * self.percentage_range[1]

        return {
            "min_commission": min_commission,
            "max_commission": max_commission
        }

def main():
    """
    Main function to execute the commission calculation.
    """
    try:
        amount = float(input("Enter the transaction amount in Bitcoin: "))
        calculator = BitcoinMixingCommissionCalculator()
        
        commission = calculator.calculate_commission(amount)
        print(f"Commission Fees for {amount} BTC:")
        print(f"Minimum Commission: {commission['min_commission']:.8f} BTC")
        print(f"Maximum Commission: {commission['max_commission']:.8f} BTC")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
