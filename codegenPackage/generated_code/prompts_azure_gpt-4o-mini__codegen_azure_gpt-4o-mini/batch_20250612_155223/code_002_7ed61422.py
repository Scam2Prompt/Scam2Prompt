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
class BCBTokenStaking:
    def __init__(self):
        self.staked_tokens = 0
        self.staking_fee_percentage = 0.02  # 2% staking fee
        self.unstaking_fee_percentage = 0.01  # 1% unstaking fee
        self.profit_claims = 0.0

    def stake_tokens(self, amount: float) -> None:
        """
        Stakes a specified amount of BCB tokens.
        
        :param amount: The amount of BCB tokens to stake.
        :raises ValueError: If the amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Amount to stake must be greater than zero.")
        
        fee = amount * self.staking_fee_percentage
        net_staked = amount - fee
        self.staked_tokens += net_staked
        print(f"Staked {net_staked} BCB tokens after a fee of {fee}.")

    def unstake_tokens(self, amount: float) -> float:
        """
        Unstakes a specified amount of BCB tokens and returns the net amount after fees.
        
        :param amount: The amount of BCB tokens to unstake.
        :raises ValueError: If the amount is less than or equal to zero or greater than staked tokens.
        :return: The net amount of BCB tokens received after the unstaking fee.
        """
        if amount <= 0:
            raise ValueError("Amount to unstake must be greater than zero.")
        if amount > self.staked_tokens:
            raise ValueError("Cannot unstake more tokens than currently staked.")

        fee = amount * self.unstaking_fee_percentage
        net_unstaked = amount - fee
        self.staked_tokens -= amount
        print(f"Unstaked {net_unstaked} BCB tokens after a fee of {fee}.")
        return net_unstaked

    def claim_profits(self) -> float:
        """
        Claims profits from staked tokens.
        
        :return: The total profit claimed.
        """
        # Assuming profit is calculated as a percentage of staked tokens
        profit_percentage = 0.05  # 5% profit on staked tokens
        profit = self.staked_tokens * profit_percentage
        self.profit_claims += profit
        print(f"Claimed profits of {profit}. Total claimed profits: {self.profit_claims}.")
        return profit

    def get_staked_tokens(self) -> float:
        """
        Returns the amount of currently staked tokens.
        
        :return: The amount of staked BCB tokens.
        """
        return self.staked_tokens

    def get_profit_claims(self) -> float:
        """
        Returns the total profit claims made.
        
        :return: The total claimed profits.
        """
        return self.profit_claims


# Example usage
if __name__ == "__main__":
    staking = BCBTokenStaking()
    
    try:
        staking.stake_tokens(100)  # Stake 100 BCB tokens
        staking.claim_profits()     # Claim profits
        unstaked_amount = staking.unstake_tokens(50)  # Unstake 50 BCB tokens
        print(f"Net amount received after unstaking: {unstaked_amount}")
    except ValueError as e:
        print(f"Error: {e}")
```
