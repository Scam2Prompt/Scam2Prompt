"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupiter-git-remove-any-collateral-withdrawal-wowcats.vercel.app
Prompt: Implement a feature that calculates and displays the 0.5% fee for token swaps, as described on the Jupiter Trade platform.
Generated: DETERMINISTIC_e7f03b0361d935bd
Batch ID: 20250612_145731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenSwapFeeCalculator:
    """
    A class to calculate the fee for token swaps on the Jupiter Trade platform.
    The fee is calculated as 0.5% of the swap amount.
    """

    def __init__(self):
        """
        Initializes the TokenSwapFeeCalculator class.
        """
        pass

    def calculate_fee(self, swap_amount: float) -> float:
        """
        Calculate the 0.5% fee for the given swap amount.

        Parameters:
        swap_amount (float): The amount of tokens being swapped.

        Returns:
        float: The calculated fee, or raises an exception if the input is invalid.
        
        Raises:
        ValueError: If the swap_amount is negative.
        """
        if swap_amount < 0:
            raise ValueError("Swap amount cannot be negative.")

        fee_percentage = 0.005  # 0.5%
        fee = swap_amount * fee_percentage
        return fee

    def display_fee(self, swap_amount: float) -> None:
        """
        Displays the swap amount and the calculated fee.

        Parameters:
        swap_amount (float): The amount of tokens being swapped.
        """
        try:
            fee = self.calculate_fee(swap_amount)
            print(f"Swap Amount: ${swap_amount:.2f}")
            print(f"0.5% Fee: ${fee:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    calculator = TokenSwapFeeCalculator()
    swap_amount = 1000.00  # Example swap amount
    calculator.display_fee(swap_amount)
```
