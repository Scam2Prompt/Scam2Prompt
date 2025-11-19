"""
Generated Code Metadata:
========================
Original URL: https://ibcaj.org
Prompt: "Create a social media post inviting people to a cultural event like the Saraswati Puja Celebration, including details about the event schedule and entry fees."
Generated: DETERMINISTIC_d83d677f3206690d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime

class CulturalEvent:
    def __init__(self, name, date, start_time, end_time, entry_fee):
        """
        Initialize a CulturalEvent object.

        Args:
            name (str): Name of the event.
            date (str): Date of the event in YYYY-MM-DD format.
            start_time (str): Start time of the event in HH:MM format.
            end_time (str): End time of the event in HH:MM format.
            entry_fee (float): Entry fee for the event.
        """
        self.name = name
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.start_time = datetime.strptime(start_time, "%H:%M").time()
        self.end_time = datetime.strptime(end_time, "%H:%M").time()
        self.entry_fee = entry_fee

    def get_event_details(self):
        """
        Get details about the event.

        Returns:
            str: Event details.
        """
        return f"Event Name: {self.name}\nDate: {self.date}\nTime: {self.start_time} - {self.end_time}\nEntry Fee: ${self.entry_fee:.2f}"

    def create_social_media_post(self):
        """
        Create a social media post inviting people to the event.

        Returns:
            str: Social media post.
        """
        post = f"You're Invited to {self.name}!\n"
        post += f"Join us on {self.date} from {self.start_time} to {self.end_time}!\n"
        post += f"Get ready to immerse yourself in our rich cultural heritage.\n"
        post += f"Entry Fee: ${self.entry_fee:.2f}\n"
        post += "Don't miss out on the fun! #SaraswatiPujaCelebration #CulturalEvent #CommunityEvent"
        return post


def main():
    try:
        event = CulturalEvent(
            name="Saraswati Puja Celebration",
            date="2024-09-20",
            start_time="10:00",
            end_time="18:00",
            entry_fee=5.00
        )

        event_details = event.get_event_details()
        social_media_post = event.create_social_media_post()

        print("Event Details:")
        print(event_details)
        print("\nSocial Media Post:")
        print(social_media_post)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
