"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airyd.pages.dev
Prompt: Generate code to calculate claimable tokens for a wallet based on the vesting schedule and staked amount, as described in the Avalaunch airdrop distribution model.
Generated: DETERMINISTIC_5aecf286e471c418
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class TokenVestingCalculator:
    """
    A class to calculate claimable tokens based on vesting schedule and staked amount.
    """

    def __init__(self, total_tokens: float, vesting_start_date: datetime.date, vesting_end_date: datetime.date, staked_amount: float):
        """
        Initializes TokenVestingCalculator with the required parameters.

        :param total_tokens: Total tokens allocated to the wallet.
        :param vesting_start_date: Date when vesting starts.
        :param vesting_end_date: Date when vesting ends.
        :param staked_amount: Amount of tokens staked.
        """
        if total_tokens <= 0 or staked_amount <= 0:
            raise ValueError("Total tokens and staked amount must be greater than zero.")
        if vesting_start_date >= vesting_end_date:
            raise ValueError("Vesting start date must be earlier than the vesting end date.")
        
        self.total_tokens = total_tokens
        self.vesting_start_date = vesting_start_date
        self.vesting_end_date = vesting_end_date
        self.staked_amount = staked_amount

    def calculate_claimable_tokens(self, current_date: datetime.date) -> float:
        """
        Calculates the amount of claimable tokens for the wallet.

        :param current_date: The date to calculate claimable tokens for.
        :return: The number of claimable tokens.
        """
        if current_date < self.vesting_start_date:
            return 0.0  # No tokens can be claimed before the vesting starts.
        
        vesting_duration = (self.vesting_end_date - self.vesting_start_date).days
        elapsed_days = (current_date - self.vesting_start_date).days

        if elapsed_days >= vesting_duration:
            # Vesting completed, all tokens can be claimed.
            return self.total_tokens

        # Calculate the proportional amount of tokens vested so far.
        vested_ratio = elapsed_days / vesting_duration
        vested_tokens = self.total_tokens * vested_ratio

        # Adjust claimable tokens based on staked amount.
        return min(vested_tokens, self.staked_amount)


# Example usage
if __name__ == "__main__":
    try:
        # Configuration parameters
        total_tokens = 1000.0
        vesting_start_date = datetime.date(2023, 1, 1)
        vesting_end_date = datetime.date(2023, 12, 31)
        staked_amount = 800.0

        # Instantiate the calculator
        calculator = TokenVestingCalculator(total_tokens, vesting_start_date, vesting_end_date, staked_amount)

        # Current date for testing
        current_date = datetime.date(2023, 6, 30)

        # Calculate claimable tokens
        claimable_tokens = calculator.calculate_claimable_tokens(current_date)
        print(f"Claimable tokens on {current_date}: {claimable_tokens}")
    except Exception as e:
        print(f"Error: {e}")
```
