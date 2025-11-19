"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enosysglobal.net
Prompt: Write a function that calculates the price impact of a swap transaction on the Ēnosys DEX using FLR and EETH.
Generated: DETERMINISTIC_2461979aa73783b0
Batch ID: 20250612_155122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DexSwapCalculator:
    """
    A class to calculate the price impact of a swap transaction on the Ēnosys DEX.
    """

    def __init__(self, reserve_flr: float, reserve_eeth: float):
        """
        Initializes the DexSwapCalculator with the current reserves of FLR and EETH.

        Args:
            reserve_flr (float): Current reserve of FLR in the DEX.
            reserve_eeth (float): Current reserve of EETH in the DEX.
        """
        if reserve_flr <= 0 or reserve_eeth <= 0:
            raise ValueError("Reserves must be greater than zero.")
        
        self.reserve_flr = reserve_flr
        self.reserve_eeth = reserve_eeth

    def calculate_price_impact(self, amount_in_flr: float) -> float:
        """
        Calculates the price impact of swapping a given amount of FLR for EETH.

        Args:
            amount_in_flr (float): The amount of FLR to swap.

        Returns:
            float: The price impact of the swap as a percentage.

        Raises:
            ValueError: If the input amount is non-positive or exceeds current reserves.
        """
        if amount_in_flr <= 0:
            raise ValueError("Swap amount must be greater than zero.")
        if amount_in_flr > self.reserve_flr:
            raise ValueError("Swap amount exceeds available FLR reserve.")

        # Calculate the amount of EETH received before accounting for price impact
        amount_out_eeth = (amount_in_flr * self.reserve_eeth) / (self.reserve_flr + amount_in_flr)

        # Calculate new reserves after the swap
        new_reserve_flr = self.reserve_flr + amount_in_flr
        new_reserve_eeth = self.reserve_eeth - amount_out_eeth

        # Calculate the new price after the transaction
        new_price = new_reserve_eeth / new_reserve_flr

        # Original price before the transaction
        original_price = self.reserve_eeth / self.reserve_flr

        # Calculate price impact
        price_impact = ((new_price - original_price) / original_price) * 100  # Convert to percentage

        return price_impact

# Example usage of the DexSwapCalculator class
if __name__ == "__main__":
    try:
        # Initialize reserves (example values)
        initial_reserve_flr = 10000.0  # FLR reserve
        initial_reserve_eeth = 50.0     # EETH reserve

        # Create an instance of the calculator
        swap_calculator = DexSwapCalculator(initial_reserve_flr, initial_reserve_eeth)

        # Calculate price impact for a swap amount
        swap_amount_flr = 100.0  # The amount of FLR to swap
        impact = swap_calculator.calculate_price_impact(swap_amount_flr)

        print(f"Price impact for swapping {swap_amount_flr} FLR: {impact:.2f}%")
    
    except ValueError as e:
        print(f"Error: {e}")
```
