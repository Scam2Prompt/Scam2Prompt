"""
Generated Code Metadata:
========================
Original URL: https://theaflac.com
Prompt: Create a script to simulate claims filing for Aflac's short-term disability insurance (A57600 series), incorporating state-specific policy numbers and waiting periods.
Generated: DETERMINISTIC_bf2ff8ab19c3af13
Batch ID: 20250612_154942
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime
import json

class AflacSTDClaims:
    def __init__(self, policy_number, state, waiting_period):
        """
        Initialize Aflac Short-Term Disability Claims.

        Args:
            policy_number (str): The policy number.
            state (str): The state where the policy is issued.
            waiting_period (int): The waiting period in days.

        Raises:
            ValueError: If waiting period is not a positive integer.
        """
        if not isinstance(waiting_period, int) or waiting_period <= 0:
            raise ValueError("Waiting period must be a positive integer.")

        self.policy_number = policy_number
        self.state = state
        self.waiting_period = waiting_period

    def file_claim(self, claim_date, disability_date):
        """
        File a claim for short-term disability.

        Args:
            claim_date (datetime.date): The date the claim is filed.
            disability_date (datetime.date): The date the disability occurred.

        Returns:
            dict: A dictionary containing claim information.

        Raises:
            ValueError: If claim date or disability date is not a date object.
        """
        if not isinstance(claim_date, datetime.date) or not isinstance(disability_date, datetime.date):
            raise ValueError("Claim date and disability date must be date objects.")

        # Calculate waiting period
        waiting_period_end = disability_date + datetime.timedelta(days=self.waiting_period)

        # Check if claim can be filed
        if claim_date < waiting_period_end:
            raise ValueError("Claim cannot be filed until after the waiting period.")

        # Create claim information
        claim_info = {
            "policy_number": self.policy_number,
            "state": self.state,
            "claim_date": claim_date.isoformat(),
            "disability_date": disability_date.isoformat(),
            "waiting_period": self.waiting_period
        }

        return claim_info


def main():
    try:
        # Define state-specific policy numbers and waiting periods
        policies = {
            "CA": {"policy_number": "A57600-1234", "waiting_period": 14},
            "NY": {"policy_number": "A57600-5678", "waiting_period": 10},
            "FL": {"policy_number": "A57600-9012", "waiting_period": 14}
        }

        # Get user input
        state = input("Enter state (CA, NY, FL): ").upper()
        claim_date_str = input("Enter claim date (YYYY-MM-DD): ")
        disability_date_str = input("Enter disability date (YYYY-MM-DD): ")

        # Parse dates
        claim_date = datetime.datetime.strptime(claim_date_str, "%Y-%m-%d").date()
        disability_date = datetime.datetime.strptime(disability_date_str, "%Y-%m-%d").date()

        # Get policy information
        policy_info = policies.get(state)
        if policy_info is None:
            print("State not supported.")
            return

        # Create Aflac STD claims object
        aflac_claims = AflacSTDClaims(policy_info["policy_number"], state, policy_info["waiting_period"])

        # File claim
        claim_info = aflac_claims.file_claim(claim_date, disability_date)

        # Print claim information
        print(json.dumps(claim_info, indent=4))

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
