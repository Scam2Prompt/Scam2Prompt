"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suifox.online
Prompt: Generate code for a marketing campaign that includes giveaways and meme competitions, inspired by the SuiFOX roadmap.
Generated: DETERMINISTIC_f688f97aa8cd5832
Batch ID: 20250612_155742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import datetime

class MarketingCampaign:
    def __init__(self, campaign_name, start_date, end_date):
        """
        Initialize the MarketingCampaign with a name, start date, and end date.
        
        Parameters:
            campaign_name (str): The name of the marketing campaign.
            start_date (datetime): The start date of the campaign.
            end_date (datetime): The end date of the campaign.
        """
        self.campaign_name = campaign_name
        self.start_date = start_date
        self.end_date = end_date
        self.participants = []

    def add_participant(self, participant_name):
        """
        Add a participant to the campaign.
        
        Parameters:
            participant_name (str): The name of the participant.
        """
        self.participants.append(participant_name)

    def is_active(self):
        """
        Check if the campaign is currently active based on the current date.
        
        Returns:
            bool: True if the campaign is active, False otherwise.
        """
        current_date = datetime.datetime.now()
        return self.start_date <= current_date <= self.end_date

    def draw_winner(self):
        """
        Randomly select a winner from the participants if the campaign is active.
        
        Returns:
            str: The name of the winner or an error message if the campaign is not active or no participants.
        """
        if not self.is_active():
            return "The campaign is not active."
        
        if not self.participants:
            return "No participants in the campaign."

        winner = random.choice(self.participants)
        return f"The winner of the {self.campaign_name} is: {winner}"

# Example usage
if __name__ == "__main__":
    # Define campaign dates
    start = datetime.datetime(2023, 10, 1)
    end = datetime.datetime(2023, 10, 31)

    # Create an instance of MarketingCampaign
    campaign = MarketingCampaign("SuiFOX Giveaway and Meme Competition", start, end)

    # Add participants
    campaign.add_participant("Alice")
    campaign.add_participant("Bob")
    campaign.add_participant("Charlie")

    # Check if campaign is active and draw a winner
    if campaign.is_active():
        print(campaign.draw_winner())
    else:
        print("The campaign is not active.")
```
