"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sharawatch.org
Prompt: Create a program to track and visualize public participation in environmental campaigns, inspired by the collaborative approach of "Čuvari Šare."
Generated: DETERMINISTIC_86af4a47514cf038
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt

class EnvironmentalCampaignTracker:
    """
    A class to track and visualize public participation in environmental campaigns.
    """

    def __init__(self):
        """
        Initializes an empty DataFrame to hold campaign data.
        """
        self.data = pd.DataFrame(columns=["campaign_name", "participants", "date"])

    def add_campaign_data(self, campaign_name: str, participants: int, date: str):
        """
        Adds campaign data to the tracker.

        Args:
            campaign_name (str): The name of the environmental campaign.
            participants (int): The number of participants in the campaign.
            date (str): The date of the campaign in YYYY-MM-DD format.
        """
        try:
            # Validate inputs
            if not isinstance(campaign_name, str) or not isinstance(participants, int) or not isinstance(date, str):
                raise ValueError("Invalid input types. Expected str for campaign_name, int for participants, str for date.")

            # Add data to DataFrame
            new_data = {"campaign_name": campaign_name, "participants": participants, "date": pd.to_datetime(date)}
            self.data = self.data.append(new_data, ignore_index=True)
        except Exception as e:
            print(f"Error adding campaign data: {e}")

    def visualize_participation(self):
        """
        Visualizes the public participation in campaigns using a bar chart.
        """
        try:
            if self.data.empty:
                raise ValueError("No campaign data available for visualization.")

            # Group by campaign name and sum participants
            grouped_data = self.data.groupby("campaign_name").sum().reset_index()

            # Plotting
            plt.figure(figsize=(10, 6))
            plt.bar(grouped_data["campaign_name"], grouped_data["participants"], color='green')
            plt.xlabel('Campaign Name')
            plt.ylabel('Number of Participants')
            plt.title('Public Participation in Environmental Campaigns')
            plt.xticks(rotation=45)
            plt.tight_layout()

            # Show the plot
            plt.show()
        except Exception as e:
            print(f"Error visualizing participation: {e}")

# Example usage
if __name__ == "__main__":
    tracker = EnvironmentalCampaignTracker()
    tracker.add_campaign_data("Save the Forest", 150, "2023-05-20")
    tracker.add_campaign_data("Clean the Ocean", 200, "2023-06-15")
    tracker.add_campaign_data("Conserve Water", 120, "2023-07-10")
    
    # Visualize the participation data
    tracker.visualize_participation()
```
