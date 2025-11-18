"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demoovortex.vercel.app
Prompt: Create a function to calculate rewards in USDT based on trading activity, adhering to Tether's marketing campaign rules.
Generated: DETERMINISTIC_27fab8cd3d73e085
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradingActivity:
    """
    A class to represent trading activity and calculate rewards in USDT.
    """

    def __init__(self, trades):
        """
        Initializes the TradingActivity with a list of trades.

        :param trades: List of trade amounts in USDT.
        """
        if not isinstance(trades, list):
            raise ValueError("Trades should be a list of trade amounts.")

        self.trades = trades

    def calculate_rewards(self):
        """
        Calculates rewards based on trading activity according to marketing campaign rules.

        Returns:
            float: Total rewards in USDT.
        """
        total_rewards = 0.0
        
        for trade in self.trades:
            if trade < 0:
                raise ValueError("Trade amounts cannot be negative.")
            # Example reward structure based on trade amount
            if trade < 100:
                total_rewards += trade * 0.01  # 1% reward for trades under $100
            elif trade < 1000:
                total_rewards += trade * 0.02  # 2% reward for trades between $100 and $1000
            else:
                total_rewards += trade * 0.03  # 3% reward for trades over $1000
        
        return round(total_rewards, 2)

# Example usage
if __name__ == "__main__":
    try:
        trades = [50, 200, 1500, 300, -10]  # Sample trade amounts
        activity = TradingActivity(trades)
        rewards = activity.calculate_rewards()
        print(f"Total Rewards in USDT: {rewards}")
    except ValueError as e:
        print(f"Error: {e}")
```
