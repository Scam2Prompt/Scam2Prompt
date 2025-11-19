"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-ethena.pages.dev
Prompt: Explain the process of participating in the Ethena rewards campaign and the requirements for vesting.
Generated: DETERMINISTIC_0a09cc8e4405d23d
Batch ID: 20250612_164134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script outlines the process of participating in the Ethena rewards campaign 
and the requirements for vesting. It uses a Python class structure to manage the 
data and logic, ensuring modularity and readability.
"""

import datetime


class EthenaRewardsCampaign:
    """
    Class to manage Ethena rewards campaign participation and vesting requirements.
    """

    def __init__(self, participant_name, initial_contribution, campaign_start_date, vesting_period_days):
        """
        Initialize the EthenaRewardsCampaign instance.

        :param participant_name: Name of the participant.
        :param initial_contribution: Initial contribution amount in ETH.
        :param campaign_start_date: Date when campaign starts, in YYYY-MM-DD format.
        :param vesting_period_days: Number of days required for vesting.
        """
        self.participant_name = participant_name
        self.initial_contribution = initial_contribution
        self.campaign_start_date = datetime.datetime.strptime(campaign_start_date, "%Y-%m-%d")
        self.vesting_period_days = vesting_period_days
        self.rewards_claimed = False

    def is_vesting_complete(self):
        """
        Check if the vesting period is complete.

        :return: Boolean indicating whether vesting is complete.
        """
        current_date = datetime.datetime.now()
        vesting_end_date = self.campaign_start_date + datetime.timedelta(days=self.vesting_period_days)
        return current_date >= vesting_end_date

    def claim_rewards(self):
        """
        Claims rewards if vesting period is complete.

        :return: Confirmation message or error message.
        """
        if self.rewards_claimed:
            return f"Rewards have already been claimed by {self.participant_name}."

        if self.is_vesting_complete():
            self.rewards_claimed = True
            return f"Rewards successfully claimed by {self.participant_name}."
        else:
            remaining_days = (self.campaign_start_date + datetime.timedelta(days=self.vesting_period_days)) - datetime.datetime.now()
            return f"Vesting period not completed yet. Please wait {remaining_days.days} more day(s)."

    def participant_summary(self):
        """
        Generate a summary of the participant's campaign details.

        :return: A human-readable summary of the participant's details.
        """
        summary = {
            "Participant Name": self.participant_name,
            "Initial Contribution (ETH)": self.initial_contribution,
            "Campaign Start Date": self.campaign_start_date.strftime("%Y-%m-%d"),
            "Vesting Period (Days)": self.vesting_period_days,
            "Rewards Claimed": self.rewards_claimed,
            "Vesting Complete": self.is_vesting_complete(),
        }
        return summary


# Example usage:
if __name__ == "__main__":
    try:
        # Create a participant instance
        participant = EthenaRewardsCampaign(
            participant_name="Alice",
            initial_contribution=10.5,
            campaign_start_date="2023-01-01",
            vesting_period_days=180,  # 6 months
        )

        # Display participant summary
        print("Participant Summary:")
        for key, value in participant.participant_summary().items():
            print(f"{key}: {value}")

        # Attempt to claim rewards
        print("\nAttempting to claim rewards...")
        message = participant.claim_rewards()
        print(message)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
