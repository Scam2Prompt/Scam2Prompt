"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earthmeta-aijko.pages.dev
Prompt: Create a script for automating the distribution of $EMT tokens during the vesting schedule, releasing 20% of tokens every two weeks after the initial claim date.
Generated: DETERMINISTIC_e6f7995765e64bcf
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from datetime import datetime, timedelta


class TokenVesting:
    def __init__(self, total_tokens, claim_date):
        """
        Initializes the TokenVesting contract.

        :param total_tokens: Total number of tokens to be distributed.
        :param claim_date: Initial claim date (format: 'YYYY-MM-DD').
        """
        self.total_tokens = total_tokens
        self.claim_date = datetime.strptime(claim_date, '%Y-%m-%d')
        self.remaining_tokens = total_tokens
        self.vesting_schedule = self.generate_vesting_schedule()
        self.claimed_tokens = 0

    def generate_vesting_schedule(self):
        """
        Generates the token vesting schedule.

        :return: A list of distribution dates and amounts.
        """
        vesting_schedule = []
        release_percentage = 0.2  # 20%
        release_amount = int(self.total_tokens * release_percentage)
        release_interval = timedelta(days=14)  # Every two weeks

        current_release_date = self.claim_date
        while self.remaining_tokens > 0:
            tokens_to_release = min(self.remaining_tokens, release_amount)
            vesting_schedule.append({'date': current_release_date, 'amount': tokens_to_release})
            self.remaining_tokens -= tokens_to_release
            current_release_date += release_interval

        return vesting_schedule

    def claim_tokens(self):
        """
        Allows the user to claim tokens based on the vesting schedule and current date.
        """
        current_date = datetime.now()
        available_to_claim = 0

        for release in self.vesting_schedule:
            if release['date'] <= current_date and release['amount'] > 0:
                available_to_claim += release['amount']
                release['amount'] = 0  # Mark tokens as claimed

        if available_to_claim == 0:
            print("No tokens available for claim at this time.")
            return

        self.claimed_tokens += available_to_claim
        print(f"{available_to_claim} EMT tokens successfully claimed!")
        print(f"Total claimed tokens: {self.claimed_tokens}")
        print(f"Remaining tokens in vesting schedule: {self.total_tokens - self.claimed_tokens}")

    def show_vesting_schedule(self):
        """
        Displays the vesting schedule.
        """
        print("Vesting Schedule:")
        for release in self.vesting_schedule:
            release_status = "Claimed" if release['amount'] == 0 else "Available"
            print(f"Date: {release['date'].strftime('%Y-%m-%d')}, Amount: {release['amount']}, Status: {release_status}")


# Example Usage
if __name__ == "__main__":
    try:
        # Instantiate the vesting contract
        total_tokens = 10000
        initial_claim_date = '2023-10-01'
        vesting_contract = TokenVesting(total_tokens, initial_claim_date)

        # Display vesting schedule
        vesting_contract.show_vesting_schedule()

        # Simulate claiming tokens (run periodically or manually when needed)
        print("\nAttempting to claim tokens...")
        vesting_contract.claim_tokens()

        print("\nUpdated Vesting Schedule:")
        vesting_contract.show_vesting_schedule()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
```
