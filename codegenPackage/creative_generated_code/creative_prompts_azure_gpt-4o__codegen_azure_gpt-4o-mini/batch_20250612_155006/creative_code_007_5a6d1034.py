"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bromptonsciences.com
Prompt: Create a program to track trading fees and calculate referral commissions earned through Arkham Exchange's affiliate program.
Generated: DETERMINISTIC_5a6d1034668249de
Batch ID: 20250612_155006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradingFeeTracker:
    """
    A class to track trading fees and calculate referral commissions
    earned through the Arkham Exchange's affiliate program.
    """

    def __init__(self):
        """
        Initializes the TradingFeeTracker with empty records.
        """
        self.trades = []  # List to store trade records
        self.referral_commission_rate = 0.1  # 10% referral commission rate

    def add_trade(self, trade_amount: float, trading_fee: float):
        """
        Add a trade record.

        Args:
            trade_amount (float): The amount of the trade.
            trading_fee (float): The fee incurred for the trade.

        Raises:
            ValueError: If trade_amount or trading_fee is negative.
        """
        if trade_amount < 0 or trading_fee < 0:
            raise ValueError("Trade amount and trading fee must be non-negative.")

        self.trades.append({
            'trade_amount': trade_amount,
            'trading_fee': trading_fee
        })

    def total_trading_fees(self) -> float:
        """
        Calculates the total trading fees incurred.

        Returns:
            float: The total trading fees.
        """
        return sum(trade['trading_fee'] for trade in self.trades)

    def calculate_referral_commission(self) -> float:
        """
        Calculates the total referral commissions earned.

        Returns:
            float: The total referral commissions.
        """
        total_fees = self.total_trading_fees()
        return total_fees * self.referral_commission_rate

    def __str__(self):
        """
        Returns a string representation of the trading fees and commissions.

        Returns:
            str: Summary of trading fees and referral commission.
        """
        total_fees = self.total_trading_fees()
        referral_commission = self.calculate_referral_commission()
        return (f"Total Trading Fees: ${total_fees:.2f}\n"
                f"Referral Commission Earned: ${referral_commission:.2f}")

if __name__ == "__main__":
    # Example usage of TradingFeeTracker
    tracker = TradingFeeTracker()

    # Adding trades with amounts and fees
    try:
        tracker.add_trade(1000, 15)
        tracker.add_trade(2500, 40)
        tracker.add_trade(500, 10)

        # Display the summary of trading fees and referral commissions
        print(tracker)

    except ValueError as e:
        print(f"Error: {e}")
```
