"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mommymilestones.com
Prompt: How can I create a celebration event for a milestone in motherhood using the concepts from Mommy Milestones?
Generated: DETERMINISTIC_fd395d69189460c7
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class CelebrationEvent:
    """
    A class to represent a celebration event for a milestone in motherhood.
    """

    def __init__(self, milestone: str, date: datetime.date, location: str, guests: list):
        """
        Initializes a CelebrationEvent instance.

        :param milestone: Description of the motherhood milestone.
        :param date: Date of the celebration.
        :param location: Location where the celebration will take place.
        :param guests: List of guests invited to the celebration.
        """
        self.milestone = milestone
        self.date = date
        self.location = location
        self.guests = guests

    def add_guest(self, guest: str):
        """
        Adds a guest to the celebration.

        :param guest: The name of the guest to add.
        """
        if guest:
            self.guests.append(guest)
        else:
            raise ValueError("Guest name cannot be empty.")

    def remove_guest(self, guest: str):
        """
        Removes a guest from the celebration.

        :param guest: The name of the guest to remove.
        :raises ValueError: If the guest is not found in the guest list.
        """
        try:
            self.guests.remove(guest)
        except ValueError as e:
            raise ValueError(f"Guest '{guest}' not found in the guest list.") from e

    def update_location(self, new_location: str):
        """
        Updates the location of the celebration.

        :param new_location: The new location for the celebration.
        """
        if new_location:
            self.location = new_location
        else:
            raise ValueError("Location cannot be empty.")

    def display_event_details(self):
        """
        Displays the details of the celebration event.
        """
        event_details = (
            f"Milestone: {self.milestone}\n"
            f"Date: {self.date.strftime('%Y-%m-%d')}\n"
            f"Location: {self.location}\n"
            f"Guests: {', '.join(self.guests)}"
        )
        print(event_details)


# Example usage
if __name__ == "__main__":
    try:
        # Create a celebration event for a milestone
        milestone_event = CelebrationEvent(
            milestone="First Birthday Celebration",
            date=datetime.date(2023, 10, 10),
            location="Central Park",
            guests=["Alice", "Bob", "Charlie"]
        )

        # Display event details
        milestone_event.display_event_details()

        # Adding a guest
        milestone_event.add_guest("Diana")

        # Removing a guest
        milestone_event.remove_guest("Charlie")

        # Updating the location
        milestone_event.update_location("Community Center")

        # Display updated event details
        milestone_event.display_event_details()

    except Exception as e:
        print(f"An error occurred: {e}")
```
