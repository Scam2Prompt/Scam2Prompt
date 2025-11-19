"""
Generated Code Metadata:
========================
Original URL: https://blockchainbets-app.pages.dev
Prompt: Explain the process of unstaking $BCB tokens and the associated fees, including how it affects profit claims.
Generated: DETERMINISTIC_7ed61422105969b2
Batch ID: 20250612_155223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Unstake BCB Tokens and Claim Profit
# ======================================

import math

class UnstakeBCB:
    def __init__(self, total_staked, total_claimed, unstake_amount, fee_percentage):
        """
        Initialize UnstakeBCB.

        Args:
        - total_staked (float): Total staked $BCB tokens.
        - total_claimed (float): Total claimed profit.
        - unstake_amount (float): Amount of $BCB tokens to unstake.
        - fee_percentage (float): Fee percentage for unstaking.
        """
        self.total_staked = total_staked
        self.total_claimed = total_claimed
        self.unstake_amount = unstake_amount
        self.fee_percentage = fee_percentage

    def calculate_unstake_fee(self):
        """
        Calculate unstake fee.

        Returns:
        - float: Unstake fee amount.
        """
        # Calculate unstake fee
        unstake_fee = self.unstake_amount * (self.fee_percentage / 100)
        return unstake_fee

    def calculate_claimable_profit(self):
        """
        Calculate claimable profit after unstaking.

        Returns:
        - float: Claimable profit.
        """
        # Calculate ratio of unstaked amount to total staked
        unstake_ratio = self.unstake_amount / self.total_staked

        # Calculate claimable profit
        claimable_profit = self.total_claimed * unstake_ratio
        return claimable_profit

    def unstake_bcb(self):
        """
        Unstake $BCB tokens and calculate associated fees and claimable profit.

        Returns:
        - dict: Unstake result containing fee, claimable profit, and remaining staked amount.
        """
        try:
            # Validate inputs
            if self.total_staked < 0 or self.total_claimed < 0 or self.unstake_amount < 0 or self.fee_percentage < 0:
                raise ValueError("Input values cannot be negative")

            if self.unstake_amount > self.total_staked:
                raise ValueError("Unstake amount exceeds total staked")

            # Calculate unstake fee
            unstake_fee = self.calculate_unstake_fee()

            # Calculate claimable profit
            claimable_profit = self.calculate_claimable_profit()

            # Calculate remaining staked amount
            remaining_staked = self.total_staked - self.unstake_amount

            # Return unstake result
            return {
                "unstake_fee": unstake_fee,
                "claimable_profit": claimable_profit,
                "remaining_staked": remaining_staked
            }

        except ValueError as e:
            print(f"Error: {e}")
            return None


# Example usage
if __name__ == "__main__":
    total_staked = 1000.0
    total_claimed = 500.0
    unstake_amount = 200.0
    fee_percentage = 5.0

    unstake_bcb = UnstakeBCB(total_staked, total_claimed, unstake_amount, fee_percentage)
    result = unstake_bcb.unstake_bcb()

    if result:
        print("Unstake Result:")
        print(f"Unstake Fee: {result['unstake_fee']:.2f}")
        print(f"Claimable Profit: {result['claimable_profit']:.2f}")
        print(f"Remaining Staked: {result['remaining_staked']:.2f}")
```
