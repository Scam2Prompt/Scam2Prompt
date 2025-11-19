"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://collaborativesolutions.com
Prompt: Describe the process for participating in Workday industry summits and networking events.
Generated: DETERMINISTIC_1b52780ed3d90224
Batch ID: 20250612_135617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WorkdayEvent:
    """
    A class to represent a Workday industry summit or networking event.
    """

    def __init__(self, event_name, date, location):
        """
        Initializes the WorkdayEvent object with event details.

        :param event_name: Name of the event
        :param date: Date of the event in 'YYYY-MM-DD' format
        :param location: Location of the event
        """
        self.event_name = event_name
        self.date = date
        self.location = location

    def register_participant(self, participant_name, email):
        """
        Registers a participant for the event.

        :param participant_name: Name of the participant
        :param email: Email of the participant
        :raises ValueError: If the email format is invalid
        """
        if not self._is_valid_email(email):
            raise ValueError("Invalid email format.")

        # Simulating participant registration
        print(f"Participant '{participant_name}' registered for '{self.event_name}' on {self.date} at {self.location}.")

    @staticmethod
    def _is_valid_email(email):
        """
        Validates the email format.

        :param email: Email to validate
        :return: True if the email format is valid, otherwise False
        """
        import re
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None


def main():
    """
    Main function to demonstrate the registration process for Workday events.
    """
    try:
        # Example of creating an event
        workday_summit = WorkdayEvent("Workday Industry Summit", "2023-11-15", "San Francisco, CA")

        # Registering participants
        workday_summit.register_participant("John Doe", "john.doe@example.com")
        workday_summit.register_participant("Jane Smith", "jane.smith@example.com")

        # Example of error handling with an invalid email
        workday_summit.register_participant("Invalid User", "invalid-email")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
