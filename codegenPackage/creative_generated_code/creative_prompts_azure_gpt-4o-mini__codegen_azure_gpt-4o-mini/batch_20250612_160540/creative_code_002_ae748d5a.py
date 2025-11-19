"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gannibalcrypto.ru
Prompt: Can you explain the multi-tiered commission system on Binance and how it impacts active traders?
Generated: DETERMINISTIC_ae748d5a15794833
Batch ID: 20250612_160540
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BinanceCommission:
    """
    This class represents a multi-tiered commission system for active traders on Binance.
    It calculates the commission based on the trading volume and the user's tier level.
    """

    def __init__(self):
        # Define the tiers and their corresponding commission rates
        self.tiers = {
            'Tier 1': {'volume': 0, 'maker_fee': 0.001, 'taker_fee': 0.001},
            'Tier 2': {'volume': 100000, 'maker_fee': 0.0009, 'taker_fee': 0.0009},
            'Tier 3': {'volume': 500000, 'maker_fee': 0.0008, 'taker_fee': 0.0008},
            'Tier 4': {'volume': 1000000, 'maker_fee': 0.0007, 'taker_fee': 0.0007},
            'Tier 5': {'volume': 5000000, 'maker_fee': 0.0006, 'taker_fee': 0.0006},
        }

    def get_tier(self, trading_volume):
        """
        Determines the user's tier based on their trading volume.

        Args:
            trading_volume (float): The total trading volume of the user.

        Returns:
            str: The tier level of the user.
        """
        for tier, data in reversed(self.tiers.items()):
            if trading_volume >= data['volume']:
                return tier
        return 'No Tier'

    def calculate_commission(self, trading_volume, order_type='maker'):
        """
        Calculates the commission based on trading volume and order type.

        Args:
            trading_volume (float): The total trading volume of the user.
            order_type (str): The type of order ('maker' or 'taker').

        Returns:
            float: The total commission fee.
        """
        # Validate input
        if trading_volume < 0:
            raise ValueError("Trading volume cannot be negative.")
        if order_type not in ['maker', 'taker']:
            raise ValueError("Order type must be 'maker' or 'taker'.")

        tier = self.get_tier(trading_volume)
        commission_rate = self.tiers[tier]['maker_fee'] if order_type == 'maker' else self.tiers[tier]['taker_fee']
        
        commission = trading_volume * commission_rate
        return commission

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of BinanceCommission
        binance_commission = BinanceCommission()

        # Define trading volume for the example
        trading_volume = 1500000  # Example trading volume
        order_type = 'taker'  # Example order type

        # Calculate commission
        commission = binance_commission.calculate_commission(trading_volume, order_type)
        print(f"Commission for {trading_volume} at '{order_type}' order type: {commission:.6f} BTC")

    except ValueError as e:
        print(f"Error: {e}")
```
