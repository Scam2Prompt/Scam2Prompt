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
# environmental_campaign_tracker.py

import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

class EnvironmentalCampaign:
    def __init__(self, name):
        """
        Initialize an environmental campaign.

        Args:
            name (str): The name of the campaign.
        """
        self.name = name
        self.participants = []
        self.events = []

    def add_participant(self, name, contact_info):
        """
        Add a participant to the campaign.

        Args:
            name (str): The name of the participant.
            contact_info (str): The contact information of the participant.
        """
        self.participants.append({"name": name, "contact_info": contact_info})

    def add_event(self, date, location, description):
        """
        Add an event to the campaign.

        Args:
            date (str): The date of the event in YYYY-MM-DD format.
            location (str): The location of the event.
            description (str): A brief description of the event.
        """
        self.events.append({"date": datetime.strptime(date, "%Y-%m-%d"), "location": location, "description": description})

    def get_participant_count(self):
        """
        Get the number of participants in the campaign.

        Returns:
            int: The number of participants.
        """
        return len(self.participants)

    def get_event_count(self):
        """
        Get the number of events in the campaign.

        Returns:
            int: The number of events.
        """
        return len(self.events)

    def visualize_participation(self):
        """
        Visualize the participation in the campaign over time.
        """
        event_dates = [event["date"] for event in self.events]
        participant_counts = [self.get_participant_count() for _ in event_dates]

        plt.figure(figsize=(10, 6))
        plt.plot(event_dates, participant_counts, marker="o")
        plt.xlabel("Date")
        plt.ylabel("Participant Count")
        plt.title(f"Participation in {self.name} Campaign")
        plt.grid(True)
        plt.show()


class CampaignTracker:
    def __init__(self):
        """
        Initialize a campaign tracker.
        """
        self.campaigns = {}

    def add_campaign(self, name):
        """
        Add a campaign to the tracker.

        Args:
            name (str): The name of the campaign.
        """
        self.campaigns[name] = EnvironmentalCampaign(name)

    def get_campaign(self, name):
        """
        Get a campaign from the tracker.

        Args:
            name (str): The name of the campaign.

        Returns:
            EnvironmentalCampaign: The campaign object.
        """
        return self.campaigns.get(name)

    def save_to_csv(self, filename):
        """
        Save the campaign data to a CSV file.

        Args:
            filename (str): The name of the CSV file.
        """
        data = []
        for campaign_name, campaign in self.campaigns.items():
            for event in campaign.events:
                data.append({
                    "campaign_name": campaign_name,
                    "date": event["date"].strftime("%Y-%m-%d"),
                    "location": event["location"],
                    "description": event["description"],
                    "participant_count": campaign.get_participant_count()
                })

        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)


def main():
    try:
        tracker = CampaignTracker()

        while True:
            print("1. Add campaign")
            print("2. Add participant")
            print("3. Add event")
            print("4. Visualize participation")
            print("5. Save to CSV")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter campaign name: ")
                tracker.add_campaign(name)
            elif choice == "2":
                campaign_name = input("Enter campaign name: ")
                campaign = tracker.get_campaign(campaign_name)
                if campaign:
                    name = input("Enter participant name: ")
                    contact_info = input("Enter participant contact info: ")
                    campaign.add_participant(name, contact_info)
                else:
                    print("Campaign not found.")
            elif choice == "3":
                campaign_name = input("Enter campaign name: ")
                campaign = tracker.get_campaign(campaign_name)
                if campaign:
                    date = input("Enter event date (YYYY-MM-DD): ")
                    location = input("Enter event location: ")
                    description = input("Enter event description: ")
                    campaign.add_event(date, location, description)
                else:
                    print("Campaign not found.")
            elif choice == "4":
                campaign_name = input("Enter campaign name: ")
                campaign = tracker.get_campaign(campaign_name)
                if campaign:
                    campaign.visualize_participation()
                else:
                    print("Campaign not found.")
            elif choice == "5":
                filename = input("Enter CSV filename: ")
                tracker.save_to_csv(filename)
            elif choice == "6":
                break
            else:
                print("Invalid option. Please choose again.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
