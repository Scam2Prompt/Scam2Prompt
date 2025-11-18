"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daisuo.cn
Prompt: Write code to calculate transaction fees for spot and futures trading on the 欧易交易所 (OKX) platform, using the fee structure provided (e.g., 0.08% for maker orders).
Generated: DETERMINISTIC_d2b430547a1f9199
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class OKXTransactionFeeCalculator:
    """
    A class to calculate transaction fees for spot and futures trading
    on the OKX platform based on the provided fee structure.
    """

    def __init__(self, maker_fee_rate=0.0008, taker_fee_rate=0.0008):
        """
        Initializes the fee calculator with default maker and taker fee rates.

        Parameters:
        maker_fee_rate (float): The maker order fee rate, default is 0.08%
        taker_fee_rate (float): The taker order fee rate, default is 0.08%
        """
        self.maker_fee_rate = maker_fee_rate
        self.taker_fee_rate = taker_fee_rate

    def calculate_fee(self, order_type, amount):
        """
        Calculates the transaction fee based on the order type and amount.

        Parameters:
        order_type (str): The type of order ('maker' or 'taker').
        amount (float): The amount of the transaction.

        Returns:
        float: The calculated transaction fee.

        Raises:
        ValueError: If the order_type is not 'maker' or 'taker'.
        Exception: If the amount is less than or equal to zero.
        """
        if amount <= 0:
            raise Exception("Transaction amount must be greater than zero.")

        if order_type.lower() == 'maker':
            fee = amount * self.maker_fee_rate
            return fee
        elif order_type.lower() == 'taker':
            fee = amount * self.taker_fee_rate
            return fee
        else:
            raise ValueError("Invalid order type. Must be 'maker' or 'taker'.")

# Example usage:
if __name__ == "__main__":
    fee_calculator = OKXTransactionFeeCalculator()

    try:
        # Calculate fees for a maker order of $1000
        maker_fee = fee_calculator.calculate_fee('maker', 1000)
        print(f"Maker Fee: ${maker_fee:.2f}")

        # Calculate fees for a taker order of $1000
        taker_fee = fee_calculator.calculate_fee('taker', 1000)
        print(f"Taker Fee: ${taker_fee:.2f}")

    except Exception as e:
        print(f"Error: {e}")
```
