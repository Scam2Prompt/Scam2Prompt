"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sosphon.xyz
Prompt: What are the requirements to qualify for Gold, Silver, or Bronze SOPH Staker status in the Sophon network?
Generated: DETERMINISTIC_50fd4f361db6bea4
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SophonStaker:
    """
    Class to represent a SOPH Staker in the Sophon network.
    It determines the status of a staker based on their participation.
    """

    # Constants representing the requirements for each status
    GOLD_MIN_STAKE = 10000  # Minimum stake for Gold status
    SILVER_MIN_STAKE = 5000  # Minimum stake for Silver status
    BRONZE_MIN_STAKE = 1000  # Minimum stake for Bronze status

    def __init__(self, stake_amount):
        """
        Initializes the Sophon Staker with the given stake amount.

        :param stake_amount: The amount of SOPH staked by the user
        """
        self.stake_amount = stake_amount

    def get_status(self):
        """
        Determines the staker's status based on the staked amount.

        :return: A string representing the staker's status
        """
        if self.stake_amount >= self.GOLD_MIN_STAKE:
            return "Gold"
        elif self.stake_amount >= self.SILVER_MIN_STAKE:
            return "Silver"
        elif self.stake_amount >= self.BRONZE_MIN_STAKE:
            return "Bronze"
        else:
            return "No status"

def main():
    """
    Main function to execute the status determination logic.
    """
    try:
        # Input: User stake amount
        stake_input = float(input("Enter your SOPH staked amount: "))
        
        # Validate if the stake amount is negative
        if stake_input < 0:
            raise ValueError("Stake amount cannot be negative.")

        # Create a staker instance
        staker = SophonStaker(stake_input)

        # Get and display the staker's status
        status = staker.get_status()
        print(f"Your SOPH Staker status is: {status}")

    except ValueError as e:
        # Handle invalid input errors gracefully
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
