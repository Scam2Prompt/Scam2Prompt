"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webactivitychains.network
Prompt: Create a script to handle staking and unstaking operations for digital assets, incorporating the "STAKING / UNSTAKING" functionality described on ChainDispute.com.
Generated: DETERMINISTIC_accc6602018d147d
Batch ID: 20250612_145150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class StakingManager:
    """
    A class to handle staking and unstaking operations for digital assets.
    """

    def __init__(self):
        """Initialize the StakingManager with empty staking records."""
        # Dictionary to hold user staking info: {user_id: {'staked_amount': float, 'stake_time': datetime}}
        self.staking_records = {}

    def stake(self, user_id, amount):
        """
        Stake a digital asset for a specific user.

        Args:
            user_id (str): Unique identifier for the user.
            amount (float): Amount to be staked.

        Returns:
            dict: Confirmation of staking.
        """
        try:
            if amount <= 0:
                raise ValueError("Amount to stake must be greater than zero.")

            current_time = datetime.datetime.now()

            # If user already staked assets, add to the existing amount
            if user_id in self.staking_records:
                self.staking_records[user_id]['staked_amount'] += amount
                self.staking_records[user_id]['stake_time'] = current_time
            else:
                # Create a new staking record
                self.staking_records[user_id] = {
                    'staked_amount': amount,
                    'stake_time': current_time
                }

            return {
                'status': 'success',
                'message': f"{amount} assets staked successfully.",
                'staked_amount': self.staking_records[user_id]['staked_amount']
            }

        except ValueError as ve:
            return {'status': 'error', 'message': str(ve)}

        except Exception as e:
            return {'status': 'error', 'message': "An unexpected error occurred."}

    def unstake(self, user_id, amount):
        """
        Unstake a digital asset for a specific user.

        Args:
            user_id (str): Unique identifier for the user.
            amount (float): Amount to be unstaked.

        Returns:
            dict: Confirmation of unstaking or error message.
        """
        try:
            if amount <= 0:
                raise ValueError("Amount to unstake must be greater than zero.")

            if user_id not in self.staking_records:
                raise ValueError("No staking record found for the user.")

            user_record = self.staking_records[user_id]

            if amount > user_record['staked_amount']:
                raise ValueError("Unstaking amount exceeds staked assets.")

            # Reduce the staked amount
            user_record['staked_amount'] -= amount

            # Remove user record if all assets are unstaked
            if user_record['staked_amount'] == 0:
                del self.staking_records[user_id]

            return {
                'status': 'success',
                'message': f"{amount} assets unstaked successfully.",
                'remaining_staked_amount': user_record['staked_amount'] if user_id in self.staking_records else 0
            }

        except ValueError as ve:
            return {'status': 'error', 'message': str(ve)}

        except Exception as e:
            return {'status': 'error', 'message': "An unexpected error occurred."}

    def get_staking_info(self, user_id):
        """
        Retrieve staking information for a specific user.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            dict: Staking information or error message if no record exists.
        """
        try:
            if user_id not in self.staking_records:
                raise ValueError("No staking record found for the user.")

            return {
                'status': 'success',
                'staking_info': self.staking_records[user_id]
            }

        except ValueError as ve:
            return {'status': 'error', 'message': str(ve)}

        except Exception as e:
            return {'status': 'error', 'message': "An unexpected error occurred."}


# Example usage
if __name__ == "__main__":
    staking_manager = StakingManager()

    # Test staking
    print(staking_manager.stake("user123", 100))
    print(staking_manager.stake("user123", 50))

    # Test unstaking
    print(staking_manager.unstake("user123", 30))
    print(staking_manager.unstake("user123", 150))

    # Get staking info
    print(staking_manager.get_staking_info("user123"))

    # Test unstaking all
    print(staking_manager.unstake("user123", 120))
    print(staking_manager.get_staking_info("user123"))
```
