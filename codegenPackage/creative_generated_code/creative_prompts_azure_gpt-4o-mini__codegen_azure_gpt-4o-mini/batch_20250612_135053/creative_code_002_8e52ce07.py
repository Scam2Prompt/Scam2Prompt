"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixbtc.online
Prompt: Create a function that calculates the mixing fee based on a user-defined percentage (1% to 5%) and includes the miner fee for a Bitcoin mixer application.
Generated: DETERMINISTIC_8e52ce07a34c22d3
Batch ID: 20250612_135053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BitcoinMixer:
    def __init__(self):
        """
        Initializes the BitcoinMixer class.
        """
        self.min_percentage = 1
        self.max_percentage = 5

    def calculate_mixing_fee(self, amount: float, percentage: float) -> float:
        """
        Calculates the mixing fee based on the specified percentage.

        Args:
            amount (float): The amount of Bitcoin to mix.
            percentage (float): The percentage fee for mixing (between 1% and 5%).

        Returns:
            float: The calculated mixing fee.

        Raises:
            ValueError: If the percentage is outside the allowed range (1% - 5%).
            ValueError: If the amount is negative or zero.
        """
        # Validate the input percentage
        if not (self.min_percentage <= percentage <= self.max_percentage):
            raise ValueError(f"Percentage must be between {self.min_percentage}% and {self.max_percentage}%.")
        
        # Validate the input amount
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        # Calculate the mixing fee
        mixing_fee = (percentage / 100) * amount
        return mixing_fee

    def calculate_total_with_miner_fee(self, amount: float, percentage: float, miner_fee: float = 0.0001) -> float:
        """
        Calculates the total amount after mixing fee and miner fee.

        Args:
            amount (float): The amount of Bitcoin to mix.
            percentage (float): The percentage fee for mixing (between 1% and 5%).
            miner_fee (float): The fixed miner fee (default is 0.0001 BTC).

        Returns:
            float: The total amount after applying the mixing fee and miner fee.

        Raises:
            ValueError: If the percentage is outside the allowed range (1% - 5%).
            ValueError: If the amount is negative or zero.
        """
        mixing_fee = self.calculate_mixing_fee(amount, percentage)
        total_after_fees = amount - mixing_fee - miner_fee
        return total_after_fees

# Example usage:
if __name__ == "__main__":
    mixer = BitcoinMixer()
    try:
        amount_to_mix = 1.0  # Amount in BTC
        fee_percentage = 3.0  # Fee percentage
        
        mixing_fee = mixer.calculate_mixing_fee(amount_to_mix, fee_percentage)
        total_amount_after_fees = mixer.calculate_total_with_miner_fee(amount_to_mix, fee_percentage)
        
        print(f"Mixing fee for {amount_to_mix} BTC at {fee_percentage}%: {mixing_fee} BTC")
        print(f"Total amount after fees: {total_amount_after_fees} BTC")
    except ValueError as e:
        print(f"Error: {e}")
```
