"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mitofi-launchpad.pages.dev
Prompt: Generate a script to calculate the overflow subscription allocation for BLACK tokens based on the Mito Launchpad's subscription style and staked INJ contributions.
Generated: DETERMINISTIC_6e3d770789a16afa
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MitoLaunchpad:
    def __init__(self, total_black_tokens: float, total_inj_staked: float):
        """
        Initializes the Mito Launchpad with total BLACK tokens and total INJ staked.

        Parameters:
            total_black_tokens (float): Total amount of BLACK tokens available for distribution.
            total_inj_staked (float): Total amount of INJ staked by all participants.
        """
        if total_black_tokens <= 0:
            raise ValueError("Total BLACK tokens must be greater than zero.")
        if total_inj_staked <= 0:
            raise ValueError("Total INJ staked must be greater than zero.")

        self.total_black_tokens = total_black_tokens
        self.total_inj_staked = total_inj_staked

    def calculate_allocation(self, user_inj_staked: float) -> float:
        """
        Calculates the overflow subscription allocation for BLACK tokens based on user INJ contribution.

        Parameters:
            user_inj_staked (float): The amount of INJ staked by the user.

        Returns:
            float: The allocation of BLACK tokens for the user.
        """
        if user_inj_staked < 0:
            raise ValueError("User INJ staked must be non-negative.")

        # Calculate the allocation based on the proportion of user INJ staked to total INJ staked
        allocation = (user_inj_staked / self.total_inj_staked) * self.total_black_tokens
        
        # Ensure the allocation does not exceed total available BLACK tokens
        allocation = min(allocation, self.total_black_tokens)

        logging.info(f"User INJ staked: {user_inj_staked}, Allocation of BLACK tokens: {allocation}")
        return allocation


if __name__ == "__main__":
    try:
        # Example values for initialization
        total_black_tokens = 10000.0  # Total BLACK tokens available for allocation
        total_inj_staked = 50000.0     # Total INJ staked by all participants

        # Create an instance of the Mito Launchpad
        launchpad = MitoLaunchpad(total_black_tokens, total_inj_staked)

        # Example user contribution
        user_inj_staked = 2500.0        # User's INJ staked amount

        # Calculate and print the allocation of BLACK tokens for the user
        allocation = launchpad.calculate_allocation(user_inj_staked)
        print(f"Allocated BLACK tokens for the user: {allocation:.2f}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
