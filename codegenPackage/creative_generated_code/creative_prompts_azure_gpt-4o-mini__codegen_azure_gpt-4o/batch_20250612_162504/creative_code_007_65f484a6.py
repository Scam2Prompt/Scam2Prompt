"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solmeme-io.pages.dev
Prompt: Create a tutorial for setting up a Solana Hacker House event to foster community building among developers.
Generated: DETERMINISTIC_65f484a63c9466f9
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to set up a Solana Hacker House event.
This script includes functionality to add attendees, schedule sessions, and manage event details.
Usage:
- Run the script to initialize the event data.
- Follow prompts to manage attendees, sessions, and event details.
"""

import datetime
import json
import os


class SolanaHackerHouse:
    """
    A class to manage a Solana Hacker House event.
    Includes functionality for managing attendees, sessions, and event details.
    """

    def __init__(self, event_name, location, start_date, end_date):
        """
        Initialize the Hacker House event with essential details.

        :param event_name: Name of the event
        :param location: Location of the event
        :param start_date: Event start date (YYYY-MM-DD)
        :param end_date: Event end date (YYYY-MM-DD)
        """
        self.event_name = event_name
        self.location = location
        self.start_date = self.validate_date(start_date)
        self.end_date = self.validate_date(end_date)
        self.attendees = []
        self.sessions = []

    @staticmethod
    def validate_date(date_str):
        """
        Validates and converts a date string to a datetime object.

        :param date_str: Date string in YYYY-MM-DD format
        :return: Parsed datetime object
        :raises ValueError: If the date format is invalid
        """
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError as e:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.") from e

    def add_attendee(self, name, email):
        """
        Adds an attendee to the event.

        :param name: Full name of the attendee
        :param email: Email address of the attendee
        """
        if any(attendee["email"] == email for attendee in self.attendees):
            print(f"An attendee with email {email} is already registered.")
            return

        self.attendees.append({"name": name, "email": email})
        print(f"Attendee {name} added successfully.")

    def schedule_session(self, title, description, session_date, duration_minutes):
        """
        Schedules a session for the event.

        :param title: Title of the session
        :param description: Description of the session
        :param session_date: Date of the session (YYYY-MM-DD)
        :param duration_minutes: Duration of the session in minutes
        """
        session_date_obj = self.validate_date(session_date)
        if session_date_obj < self.start_date or session_date_obj > self.end_date:
            print("Session date must fall within the event dates.")
            return

        self.sessions.append({
            "title": title,
            "description": description,
            "date": session_date_obj,
            "duration_minutes": duration_minutes
        })
        print(f"Session '{title}' scheduled successfully.")

    def save_event_details(self, file_path="event_details.json"):
        """
        Saves the event details (attendees and sessions) to a JSON file.

        :param file_path: Path to the JSON file
        """
        event_data = {
            "event_name": self.event_name,
            "location": self.location,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "attendees": self.attendees,
            "sessions": self.sessions
        }

        try:
            with open(file_path, "w") as file:
                json.dump(event_data, file, indent=4)
            print(f"Event details saved to {file_path}.")
        except (OSError, IOError) as e:
            print(f"Failed to save event details: {e}")

    def load_event_details(self, file_path="event_details.json"):
        """
        Loads event details (attendees and sessions) from a JSON file.

        :param file_path: Path to the JSON file
        """
        if not os.path.exists(file_path):
            print(f"File {file_path} does not exist.")
            return

        try:
            with open(file_path, "r") as file:
                event_data = json.load(file)
            self.event_name = event_data["event_name"]
            self.location = event_data["location"]
            self.start_date = datetime.datetime.strptime(event_data["start_date"], "%Y-%m-%d").date()
            self.end_date = datetime.datetime.strptime(event_data["end_date"], "%Y-%m-%d").date()
            self.attendees = event_data["attendees"]
            self.sessions = event_data["sessions"]
            print(f"Event details loaded from {file_path}.")
        except (OSError, IOError, json.JSONDecodeError) as e:
            print(f"Failed to load event details: {e}")


if __name__ == "__main__":
    # Initialize the Solana Hacker House event
    event = SolanaHackerHouse(
        event_name="Solana Hacker House NYC",
        location="New York City",
        start_date="2023-11-01",
        end_date="2023-11-05"
    )

    # Example usage
    event.add_attendee(name="Alice Doe", email="alice@example.com")
    event.add_attendee(name="Bob Smith", email="bob@example.com")
    event.schedule_session(
        title="Intro to Solana",
        description="Learn the basics of building on Solana.",
        session_date="2023-11-02",
        duration_minutes=120
    )
    event.save_event_details()
    event.load_event_details()
```
