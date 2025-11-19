"""
Generated Code Metadata:
========================
Original URL: https://zivoe.pages.dev
Prompt: Generate code to simulate the deposit and vesting process for pZVE tokens on Zivoe, considering the 3X and 1X launch bonuses for Senior and Junior Tranches.
Generated: DETERMINISTIC_21fe2905ac6cd2e1
Batch ID: 20250622_204635
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenVesting:
    def __init__(self, total_tokens, tranche):
        """
        Initialize the TokenVesting class.

        :param total_tokens: Total number of tokens to be vested.
        :param tranche: The tranche type ('Senior' or 'Junior').
        """
        self.total_tokens = total_tokens
        self.tranche = tranche
        self.vested_tokens = 0
        self.bonus_multiplier = self.get_bonus_multiplier()

    def get_bonus_multiplier(self):
        """
        Determine the bonus multiplier based on the tranche type.

        :return: Bonus multiplier (3 for Senior, 1 for Junior).
        """
        if self.tranche == 'Senior':
            return 3
        elif self.tranche == 'Junior':
            return 1
        else:
            raise ValueError("Invalid tranche type. Must be 'Senior' or 'Junior'.")

    def deposit_tokens(self, amount):
        """
        Deposit tokens into the vesting contract.

        :param amount: Amount of tokens to deposit.
        :raises ValueError: If the amount is negative or exceeds available tokens.
        """
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        if amount > self.total_tokens:
            raise ValueError("Deposit amount exceeds total tokens.")
        
        self.total_tokens -= amount
        self.vested_tokens += amount * self.bonus_multiplier
        print(f"Deposited {amount} tokens. Total vested tokens: {self.vested_tokens}")

    def release_tokens(self, amount):
        """
        Release vested tokens.

        :param amount: Amount of tokens to release.
        :raises ValueError: If the amount is negative or exceeds vested tokens.
        """
        if amount < 0:
            raise ValueError("Release amount cannot be negative.")
        if amount > self.vested_tokens:
            raise ValueError("Release amount exceeds vested tokens.")
        
        self.vested_tokens -= amount
        print(f"Released {amount} tokens. Remaining vested tokens: {self.vested_tokens}")

    def get_vested_balance(self):
        """
        Get the current balance of vested tokens.

        :return: The number of vested tokens.
        """
        return self.vested_tokens

# Example usage
if __name__ == "__main__":
    try:
        # Create a TokenVesting instance for Senior tranche
        senior_vesting = TokenVesting(total_tokens=1000, tranche='Senior')
        senior_vesting.deposit_tokens(200)
        print(f"Vested balance: {senior_vesting.get_vested_balance()}")

        # Release some tokens
        senior_vesting.release_tokens(300)  # This should raise an error
    except ValueError as e:
        print(f"Error: {e}")
```
