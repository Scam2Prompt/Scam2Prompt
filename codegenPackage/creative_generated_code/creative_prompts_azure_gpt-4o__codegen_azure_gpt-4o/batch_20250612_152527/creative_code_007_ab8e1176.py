"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vote-jup.pages.dev
Prompt: Write a function to calculate the diminishing voting power for a wallet unlocking JUP tokens over the 30-day countdown, as described on the Jupiter voting platform.
Generated: DETERMINISTIC_ab8e117683d78002
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_voting_power(unlock_day: int, total_tokens: float) -> float:
    """
    Calculate the diminishing voting power based on the day a wallet unlocks JUP tokens.

    :param unlock_day: The day the wallet unlocks tokens (0-30, where 0 means now and 30 means full countdown).
    :param total_tokens: The total number of JUP tokens in the wallet.
    :return: The voting power as a float.
    
    Voting power diminishes linearly starting from 100% (day 0) to 0% (day 30).
    """
    try:
        # Validate inputs
        if not (0 <= unlock_day <= 30):
            raise ValueError("unlock_day must be between 0 and 30, inclusive.")
        if total_tokens < 0:
            raise ValueError("total_tokens must be a non-negative number.")

        # Calculate diminishing voting power
        diminishing_factor = (30 - unlock_day) / 30  # Linear decrease from 1 to 0
        voting_power = total_tokens * diminishing_factor

        return round(voting_power, 2)  # Return rounded value for cleaner output

    except ValueError as ve:
        # Handle invalid input values
        print(f"Input Error: {ve}")
        return 0.0  # Return neutral voting power in case of error

    except Exception as e:
        # Catch unexpected errors
        print(f"Unexpected Error: {e}")
        return 0.0  # Return neutral voting power in case of error


# Example Usage
if __name__ == '__main__':
    wallet_unlock_day = 15  # Day when the wallet unlocks
    wallet_tokens = 1000.0  # Total JUP tokens in the wallet

    voting_power = calculate_voting_power(wallet_unlock_day, wallet_tokens)
    print(f"Voting Power: {voting_power}")
```
