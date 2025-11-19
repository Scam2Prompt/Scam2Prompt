"""
Generated Code Metadata:
========================
Original URL: https://micmarktrade.com
Prompt: Create a function that calculates trading fees based on the competitive pricing structure outlined by MIC markets.
Generated: DETERMINISTIC_14f4225dd8eebdd4
Batch ID: 20250612_160127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TradingFeeCalculator:
    """
    A class to calculate trading fees based on the competitive pricing structure outlined by MIC markets.
    """

    def __init__(self, base_fee: float, volume_discount: dict):
        """
        Initializes the TradingFeeCalculator with a base fee and a volume discount structure.

        :param base_fee: The base trading fee as a float.
        :param volume_discount: A dictionary where keys are volume thresholds and values are discount percentages.
        """
        if base_fee < 0:
            raise ValueError("Base fee must be a non-negative value.")
        if not isinstance(volume_discount, dict):
            raise TypeError("Volume discount must be a dictionary.")

        self.base_fee = base_fee
        self.volume_discount = volume_discount

    def calculate_fee(self, trade_volume: float) -> float:
        """
        Calculates the trading fee based on the trade volume.

        :param trade_volume: The volume of the trade as a float.
        :return: The calculated trading fee as a float.
        """
        if trade_volume < 0:
            raise ValueError("Trade volume must be a non-negative value.")

        # Determine applicable discount based on trade volume
        applicable_discount = 0.0
        for threshold, discount in sorted(self.volume_discount.items()):
            if trade_volume >= threshold:
                applicable_discount = discount
            else:
                break

        # Calculate the final fee
        fee = self.base_fee * (1 - applicable_discount / 100)
        return round(fee, 2)  # Round to two decimal places for currency representation


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with a base fee and volume discounts
        base_fee = 10.00  # Base fee in currency units
        volume_discount = {
            1000: 5,   # 5% discount for trades over 1000 units
            5000: 10,  # 10% discount for trades over 5000 units
            10000: 15  # 15% discount for trades over 10000 units
        }

        calculator = TradingFeeCalculator(base_fee, volume_discount)

        # Calculate fees for different trade volumes
        trade_volumes = [500, 1500, 6000, 12000]
        for volume in trade_volumes:
            fee = calculator.calculate_fee(volume)
            print(f"Trading fee for volume {volume}: {fee}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
