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
class EthenaRewardsCampaign:
    def __init__(self, participant_id, eth_balance):
        """
        Initialize the EthenaRewardsCampaign with participant details.

        :param participant_id: Unique identifier for the participant
        :param eth_balance: Current ETH balance of the participant
        """
        self.participant_id = participant_id
        self.eth_balance = eth_balance
        self.rewards_earned = 0.0
        self.vesting_period = 30  # Vesting period in days
        self.vesting_start = None

    def participate(self):
        """
        Method to allow a participant to join the Ethena rewards campaign.
        Checks if the participant meets the eligibility criteria.
        """
        if self.eth_balance < 0.1:
            raise ValueError("Insufficient ETH balance to participate. Minimum required is 0.1 ETH.")
        
        # Simulate the start of the vesting period
        self.vesting_start = self.current_date()
        print(f"Participant {self.participant_id} has successfully joined the Ethena rewards campaign.")

    def current_date(self):
        """
        Get the current date.

        :return: Current date as a string in the format YYYY-MM-DD
        """
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d")

    def earn_rewards(self, amount):
        """
        Method to simulate earning rewards.

        :param amount: Amount of rewards earned
        :raises ValueError: If the amount is negative
        """
        if amount < 0:
            raise ValueError("Rewards amount cannot be negative.")
        
        self.rewards_earned += amount
        print(f"Participant {self.participant_id} earned {amount} rewards. Total rewards: {self.rewards_earned}")

    def check_vesting_status(self):
        """
        Check if the participant's rewards are vested.

        :return: Vesting status as a string
        """
        if self.vesting_start is None:
            return "Participant has not joined the campaign yet."

        days_passed = self.calculate_days_passed()
        if days_passed >= self.vesting_period:
            return f"Rewards are vested. Total rewards: {self.rewards_earned}"
        else:
            remaining_days = self.vesting_period - days_passed
            return f"Rewards are in vesting period. {remaining_days} days remaining."

    def calculate_days_passed(self):
        """
        Calculate the number of days passed since the vesting started.

        :return: Number of days passed
        """
        from datetime import datetime
        start_date = datetime.strptime(self.vesting_start, "%Y-%m-%d")
        current_date = datetime.now()
        return (current_date - start_date).days

# Example usage:
if __name__ == "__main__":
    try:
        participant = EthenaRewardsCampaign(participant_id="user123", eth_balance=0.2)
        participant.participate()
        participant.earn_rewards(50)
        print(participant.check_vesting_status())
    except ValueError as e:
        print(f"Error: {e}")
```
