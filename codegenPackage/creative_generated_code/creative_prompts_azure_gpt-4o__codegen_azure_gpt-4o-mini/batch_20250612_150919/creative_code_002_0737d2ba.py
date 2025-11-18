"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mauvworld.pages.dev
Prompt: Create a function in Python to calculate the remaining unlocked tokens for MAUW's 1st, 2nd, and 3rd viral airdrops based on their respective locking periods.
Generated: DETERMINISTIC_0737d2ba7a286c66
Batch ID: 20250612_150919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class TokenAirdrop:
    """
    Class to calculate remaining unlocked tokens for MAUW's viral airdrops.
    """

    def __init__(self, airdrop_dates):
        """
        Initializes the TokenAirdrop class with airdrop dates.

        :param airdrop_dates: A dictionary with airdrop period details.
                              Example: {
                                  'first': {'date': '2022-01-01', 'lock_period': 90},
                                  'second': {'date': '2022-04-01', 'lock_period': 60},
                                  'third': {'date': '2022-06-01', 'lock_period': 30}
                              }
        """
        self.airdrop_dates = airdrop_dates

    def calculate_remaining_tokens(self, airdrop_name):
        """
        Calculate the remaining unlocked tokens for a given airdrop.

        :param airdrop_name: The name of the airdrop ('first', 'second', 'third').
        :return: Remaining unlocked tokens or an error message if invalid input.
        """
        try:
            # Retrieve the airdrop details
            airdrop_info = self.airdrop_dates[airdrop_name]
            airdrop_date = datetime.strptime(airdrop_info['date'], '%Y-%m-%d')
            lock_period_days = airdrop_info['lock_period']

            # Calculate unlock date
            unlock_date = airdrop_date + timedelta(days=lock_period_days)
            current_date = datetime.now()

            # Determine remaining unlocked tokens
            if current_date >= unlock_date:
                return 0  # No remaining tokens locked
            else:
                remaining_days = (unlock_date - current_date).days
                return remaining_days  # Remaining days until unlock
            
        except KeyError:
            return f"Error: Airdrop '{airdrop_name}' does not exist."
        except ValueError as e:
            return f"Error: {str(e)}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"


# Example usage:
if __name__ == "__main__":
    airdrop_data = {
        'first': {'date': '2022-01-01', 'lock_period': 90},
        'second': {'date': '2022-04-01', 'lock_period': 60},
        'third': {'date': '2022-06-01', 'lock_period': 30}
    }

    token_airdrop = TokenAirdrop(airdrop_data)

    # Calculate remaining unlocked tokens for each airdrop
    for airdrop in airdrop_data.keys():
        remaining_tokens = token_airdrop.calculate_remaining_tokens(airdrop)
        print(f"Remaining unlocked tokens for {airdrop} airdrop: {remaining_tokens}")
```
