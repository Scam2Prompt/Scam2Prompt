"""
Generated Code Metadata:
========================
Original URL: https://bafybeig3dfeggrvb5y6mvhqgj7fxtsornkonyokblgrukvsjowyrchly4u.ipfs.dweb.link
Prompt: "Design a promotional message for an event that requires registration within a limited timeframe, similar to the Runes Dog Labs announcement."
Generated: DETERMINISTIC_3d00076a6fd2cf77
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class EventPromotion:
    def __init__(self, event_name, registration_deadline, event_date, location):
        """
        Initializes the EventPromotion class with event details.

        :param event_name: str - Name of the event
        :param registration_deadline: datetime - Deadline for registration
        :param event_date: datetime - Date of the event
        :param location: str - Location of the event
        """
        self.event_name = event_name
        self.registration_deadline = registration_deadline
        self.event_date = event_date
        self.location = location

    def is_registration_open(self):
        """
        Checks if the registration is still open.

        :return: bool - True if registration is open, False otherwise
        """
        return datetime.datetime.now() < self.registration_deadline

    def generate_promotional_message(self):
        """
        Generates a promotional message for the event.

        :return: str - Promotional message
        """
        if not self.is_registration_open():
            return f"Registration for {self.event_name} has closed."

        time_left = self.registration_deadline - datetime.datetime.now()
        days_left = time_left.days
        hours_left = time_left.seconds // 3600
        minutes_left = (time_left.seconds // 60) % 60

        message = (
            f"🚀 Don't miss out on {self.event_name}! 🚀\n"
            f"📅 Event Date: {self.event_date.strftime('%B %d, %Y')}\n"
            f"📍 Location: {self.location}\n"
            f"⏳ Register by: {self.registration_deadline.strftime('%B %d, %Y %H:%M')}\n"
            f"🕒 Time left to register: {days_left} days, {hours_left} hours, and {minutes_left} minutes!\n"
            f"👉 Secure your spot now!"
        )
        return message

def main():
    """
    Main function to run the event promotion.
    """
    try:
        # Define event details
        event_name = "Runes Dog Labs Annual Gathering"
        registration_deadline = datetime.datetime(2023, 10, 31, 23, 59)
        event_date = datetime.datetime(2023, 11, 15)
        location = "Central Park, New York"

        # Create an instance of EventPromotion
        promotion = EventPromotion(event_name, registration_deadline, event_date, location)

        # Generate and print the promotional message
        print(promotion.generate_promotional_message())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
