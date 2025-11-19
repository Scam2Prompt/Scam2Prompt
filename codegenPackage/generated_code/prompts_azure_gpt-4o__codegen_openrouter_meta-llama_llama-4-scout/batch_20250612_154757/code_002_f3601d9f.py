"""
Generated Code Metadata:
========================
Original URL: https://m.cjjzqkc.cn
Prompt: Create a script to calculate trading fees on the OKX platform for spot and derivative transactions, considering the fee reduction for holding OKB tokens.
Generated: DETERMINISTIC_f3601d9f4c45f3f9
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# trading_fee_calculator.py

import math

class OKXTradingFeeCalculator:
    """
    Calculates trading fees on the OKX platform for spot and derivative transactions.
    """

    def __init__(self, okb_balance: float, fee_tier: str = "Basic"):
        """
        Initializes the calculator with OKB balance and fee tier.

        Args:
        - okb_balance (float): The user's OKB balance.
        - fee_tier (str): The user's fee tier (Basic, Intermediate, Advanced). Defaults to "Basic".
        """
        self.okb_balance = okb_balance
        self.fee_tier = fee_tier

        # OKX fee tiers and corresponding maker/taker fees
        self.fee_tiers = {
            "Basic": {"maker": 0.0015, "taker": 0.0015},
            "Intermediate": {"maker": 0.001, "taker": 0.001},
            "Advanced": {"maker": 0.0005, "taker": 0.0005}
        }

        # OKB holding-based fee discounts
        self.okb_discounts = {
            0: 0,
            500: 0.1,
            1000: 0.2,
            5000: 0.3,
            10000: 0.4,
            50000: 0.5
        }

    def get_fee_tier(self) -> dict:
        """
        Returns the fee tier details.

        Returns:
        - dict: The fee tier details with maker and taker fees.
        """
        return self.fee_tiers.get(self.fee_tier)

    def calculate_okb_discount(self) -> float:
        """
        Calculates the OKB holding-based fee discount.

        Returns:
        - float: The fee discount percentage.
        """
        discount = 0
        for balance, discount_percentage in self.okb_discounts.items():
            if self.okb_balance >= balance:
                discount = discount_percentage
        return discount

    def calculate_trading_fee(self, transaction_type: str, trade_amount: float, trade_price: float) -> float:
        """
        Calculates the trading fee for a given transaction.

        Args:
        - transaction_type (str): The type of transaction (spot or derivative).
        - trade_amount (float): The trade amount.
        - trade_price (float): The trade price.

        Returns:
        - float: The trading fee.

        Raises:
        - ValueError: If the transaction type is not supported.
        """
        if transaction_type not in ["spot", "derivative"]:
            raise ValueError("Unsupported transaction type")

        fee_tier = self.get_fee_tier()
        if not fee_tier:
            raise ValueError("Invalid fee tier")

        # Calculate trading fee
        trading_fee = trade_amount * trade_price * fee_tier["taker"]

        # Apply OKB holding-based fee discount
        okb_discount = self.calculate_okb_discount()
        trading_fee *= (1 - okb_discount)

        return trading_fee

def main():
    # Example usage
    calculator = OKXTradingFeeCalculator(okb_balance=10000)
    print("Fee Tier:", calculator.get_fee_tier())

    trade_amount = 1.0
    trade_price = 20000.0

    spot_fee = calculator.calculate_trading_fee("spot", trade_amount, trade_price)
    derivative_fee = calculator.calculate_trading_fee("derivative", trade_amount, trade_price)

    print(f"Spot Trading Fee: ${spot_fee:.8f}")
    print(f"Derivative Trading Fee: ${derivative_fee:.8f}")

if __name__ == "__main__":
    main()
```
