"""
Generated Code Metadata:
========================
Original URL: https://emarlado.com
Prompt: Explain the concept of CFD expiries and swap fees in the context of Emarlado's trading services, and provide a code example for calculating these fees.
Generated: DETERMINISTIC_d8ba7dd6b148a964
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TradingService:
    """
    A class to represent a trading service that handles Contracts for Difference (CFD) expiries and swap fees.
    """

    def __init__(self, cfd_expiry_days: int, swap_fee_rate: float):
        """
        Initializes the TradingService with CFD expiry days and swap fee rate.

        :param cfd_expiry_days: Number of days until the CFD expires.
        :param swap_fee_rate: Daily swap fee rate as a percentage.
        """
        if cfd_expiry_days < 0:
            raise ValueError("CFD expiry days must be non-negative.")
        if swap_fee_rate < 0:
            raise ValueError("Swap fee rate must be non-negative.")

        self.cfd_expiry_days = cfd_expiry_days
        self.swap_fee_rate = swap_fee_rate

    def calculate_swap_fee(self, position_value: float) -> float:
        """
        Calculates the total swap fee for a given position value over the CFD expiry period.

        :param position_value: The monetary value of the CFD position.
        :return: Total swap fee for the position.
        """
        if position_value < 0:
            raise ValueError("Position value must be non-negative.")

        # Calculate the total swap fee
        total_swap_fee = (self.swap_fee_rate / 100) * position_value * self.cfd_expiry_days
        return total_swap_fee

    def get_cfd_expiry_info(self) -> str:
        """
        Provides information about the CFD expiry.

        :return: A string describing the CFD expiry.
        """
        return f"CFD expires in {self.cfd_expiry_days} days."

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the trading service with 5 days until expiry and a swap fee rate of 0.1%
        trading_service = TradingService(cfd_expiry_days=5, swap_fee_rate=0.1)

        # Calculate the swap fee for a position value of $10,000
        position_value = 10000.0
        swap_fee = trading_service.calculate_swap_fee(position_value)

        # Output the results
        print(trading_service.get_cfd_expiry_info())
        print(f"Total swap fee for a position value of ${position_value}: ${swap_fee:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
