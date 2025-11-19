"""
Generated Code Metadata:
========================
Original URL: https://sharawatch.org
Prompt: Create a program to track and visualize public participation in environmental campaigns, inspired by the collaborative approach of "Čuvari Šare."
Generated: DETERMINISTIC_86af4a47514cf038
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class EnvironmentalCampaignTracker:
    """
    A class to track and visualize public participation in environmental campaigns.
    """

    def __init__(self):
        """
        Initializes the tracker with an empty DataFrame to store campaign data.
        """
        self.data = pd.DataFrame(columns=['Campaign', 'Participants', 'Date'])

    def add_campaign(self, campaign_name: str, participants: int, date: str):
        """
        Adds a new campaign to the tracker.

        :param campaign_name: Name of the environmental campaign
        :param participants: Number of participants in the campaign
        :param date: Date of the campaign in 'YYYY-MM-DD' format
        """
        try:
            new_campaign = {'Campaign': campaign_name, 'Participants': participants, 'Date': pd.to_datetime(date)}
            self.data = self.data.append(new_campaign, ignore_index=True)
        except Exception as e:
            print(f"Error adding campaign: {e}")

    def visualize_participation(self):
        """
        Visualizes the participation in campaigns using a bar plot.
        """
        if self.data.empty:
            print("No data available to visualize.")
            return

        plt.figure(figsize=(10, 6))
        sns.barplot(data=self.data, x='Campaign', y='Participants', palette='viridis')
        plt.title('Public Participation in Environmental Campaigns')
        plt.xlabel('Campaign')
        plt.ylabel('Number of Participants')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def save_data(self, file_path: str):
        """
        Saves the campaign data to a CSV file.

        :param file_path: Path to the CSV file where data will be saved
        """
        try:
            self.data.to_csv(file_path, index=False)
            print(f"Data saved to {file_path}")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self, file_path: str):
        """
        Loads campaign data from a CSV file.

        :param file_path: Path to the CSV file to load data from
        """
        try:
            self.data = pd.read_csv(file_path)
            self.data['Date'] = pd.to_datetime(self.data['Date'])
            print(f"Data loaded from {file_path}")
        except Exception as e:
            print(f"Error loading data: {e}")

# Example usage
if __name__ == "__main__":
    tracker = EnvironmentalCampaignTracker()
    tracker.add_campaign("Clean the River", 150, "2023-05-20")
    tracker.add_campaign("Plant a Tree", 200, "2023-06-15")
    tracker.visualize_participation()
    tracker.save_data("campaign_data.csv")
    tracker.load_data("campaign_data.csv")
```
