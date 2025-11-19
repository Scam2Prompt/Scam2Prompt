"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://micmarktrade.com
Prompt: Create a function that calculates trading fees based on the competitive pricing structure outlined by MIC markets.
Generated: DETERMINISTIC_14f4225dd8eebdd4
Batch ID: 20250612_160127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradingFeeCalculator:
    """
    A class to calculate trading fees based on MIC (Market Identifier Code)
    competitive pricing structures.
    """

    def __init__(self):
        """
        Initializes the fee structures for supported MIC markets.
        Fee structures can be updated based on the latest pricing policies.
        """
        self.fee_structures = {
            "NASDAQ": {"maker_fee": 0.002, "taker_fee": 0.003},  # Example fees
            "NYSE": {"maker_fee": 0.0015, "taker_fee": 0.0025},  # Example fees
            "LSE": {"maker_fee": 0.001, "taker_fee": 0.002},     # Example fees
        }

    def calculate_fee(self, mic: str, trade_type: str, trade_volume: float) -> float:
        """
        Calculates the trading fee based on the MIC market, trade type, and trade volume.
        
        :param mic: str - Market Identifier Code (e.g., 'NASDAQ', 'NYSE', 'LSE')
        :param trade_type: str - Type of trade ('maker' or 'taker')
        :param trade_volume: float - Trade volume in USD or equivalent currency
        
        :return: float - Calculated trading fee
        
        :raises ValueError: If the MIC or trade type is unsupported, or if trade_volume is negative
        """
        # Validate inputs
        if mic not in self.fee_structures:
            raise ValueError(f"Unsupported MIC: {mic}. Supported MICs are: {list(self.fee_structures.keys())}")
        if trade_type not in ["maker", "taker"]:
            raise ValueError("Trade type must be 'maker' or 'taker'.")
        if trade_volume < 0:
            raise ValueError("Trade volume must be non-negative.")

        # Retrieve the fee rates
        fee_rate = self.fee_structures[mic].get(f"{trade_type}_fee")
        
        # Calculate the fee
        trading_fee = trade_volume * fee_rate
        
        return trading_fee


# Example usage:
if __name__ == "__main__":
    try:
        calculator = TradingFeeCalculator()
        mic = "NASDAQ"
        trade_type = "maker"
        trade_volume = 100000  # Example trade volume

        fee = calculator.calculate_fee(mic=mic, trade_type=trade_type, trade_volume=trade_volume)
        print(f"Trading fee for {mic} ({trade_type}): ${fee:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
