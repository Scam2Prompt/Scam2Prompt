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
# Import necessary modules
from typing import Optional

class OKXTradingFeeCalculator:
    """
    A class to calculate transaction fees for spot and futures trading
    based on OKX's fee structure.

    Attributes:
        maker_fee_rate (float): Percentage fee rate for maker orders.
        taker_fee_rate (float): Percentage fee rate for taker orders.
    """

    def __init__(self, maker_fee_rate: float = 0.0008, taker_fee_rate: float = 0.001):
        """
        Initializes the OKXTradingFeeCalculator with fee rates.

        Args:
            maker_fee_rate (float): Fee rate for maker orders (default: 0.08%).
            taker_fee_rate (float): Fee rate for taker orders (default: 0.1%).
        """
        self.maker_fee_rate = maker_fee_rate
        self.taker_fee_rate = taker_fee_rate

    def calculate_fee(self, order_type: str, trade_amount: float) -> Optional[float]:
        """
        Calculates the transaction fee based on order type and trade amount.

        Args:
            order_type (str): Type of the order ('maker' or 'taker').
            trade_amount (float): The trade amount in USD.

        Returns:
            float: The transaction fee in USD, or None if the order type is invalid.

        Raises:
            ValueError: If trade_amount is negative or zero.
        """
        if trade_amount <= 0:
            raise ValueError("Trade amount must be greater than zero.")

        if order_type.lower() == 'maker':
            return trade_amount * self.maker_fee_rate
        elif order_type.lower() == 'taker':
            return trade_amount * self.taker_fee_rate
        else:
            # Invalid order type
            print("Error: Invalid order type. Must be 'maker' or 'taker'.")
            return None

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with default fee rates
        calculator = OKXTradingFeeCalculator()

        # Calculate fees for spot trading
        spot_trade_amount = 1000  # Example trade amount in USD
        spot_fee_maker = calculator.calculate_fee('maker', spot_trade_amount)
        spot_fee_taker = calculator.calculate_fee('taker', spot_trade_amount)

        print(f"Maker fee for spot trading: ${spot_fee_maker:.2f}")
        print(f"Taker fee for spot trading: ${spot_fee_taker:.2f}")

        # Calculate fees for futures trading
        futures_trade_amount = 5000  # Example trade amount in USD
        futures_fee_maker = calculator.calculate_fee('maker', futures_trade_amount)
        futures_fee_taker = calculator.calculate_fee('taker', futures_trade_amount)

        print(f"Maker fee for futures trading: ${futures_fee_maker:.2f}")
        print(f"Taker fee for futures trading: ${futures_fee_taker:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
