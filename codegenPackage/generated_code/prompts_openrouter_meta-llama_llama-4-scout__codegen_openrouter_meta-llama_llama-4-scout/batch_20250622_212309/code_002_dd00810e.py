"""
Generated Code Metadata:
========================
Original URL: https://paradigmgroup.co.ug
Prompt: "Generate a Python script for media selection and management in event planning for brand activations in South Africa."
Generated: DETERMINISTIC_dd00810efff255d2
Batch ID: 20250622_212309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# media_selector.py

"""
Media Selection and Management Script for Event Planning in South Africa.

This script provides a basic framework for selecting and managing media for brand activations.
It allows users to add, remove, and list media channels, as well as assign channels to events.

Author: [Your Name]
Date: [Today's Date]
"""

import datetime

class MediaChannel:
    """Represents a media channel."""

    def __init__(self, name, channel_type, cost):
        """
        Initializes a MediaChannel object.

        Args:
            name (str): The name of the media channel.
            channel_type (str): The type of media channel (e.g., TV, Radio, Social Media).
            cost (float): The cost of advertising on this channel.
        """
        self.name = name
        self.channel_type = channel_type
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.channel_type}) - R {self.cost}"


class Event:
    """Represents an event."""

    def __init__(self, name, date, budget):
        """
        Initializes an Event object.

        Args:
            name (str): The name of the event.
            date (datetime.date): The date of the event.
            budget (float): The budget for the event.
        """
        self.name = name
        self.date = date
        self.budget = budget
        self.media_channels = []

    def add_media_channel(self, media_channel):
        """
        Adds a media channel to the event.

        Args:
            media_channel (MediaChannel): The media channel to add.

        Raises:
            ValueError: If the media channel's cost exceeds the event's remaining budget.
        """
        if media_channel.cost > self.budget:
            raise ValueError("Media channel's cost exceeds the event's remaining budget.")
        self.media_channels.append(media_channel)
        self.budget -= media_channel.cost

    def __str__(self):
        event_info = f"{self.name} on {self.date}\n"
        event_info += f"Budget: R {self.budget}\n"
        event_info += "Media Channels:\n"
        for channel in self.media_channels:
            event_info += f"- {channel}\n"
        return event_info


class MediaManager:
    """Manages media channels and events."""

    def __init__(self):
        self.media_channels = []
        self.events = []

    def add_media_channel(self, name, channel_type, cost):
        """
        Adds a media channel.

        Args:
            name (str): The name of the media channel.
            channel_type (str): The type of media channel.
            cost (float): The cost of advertising on this channel.
        """
        media_channel = MediaChannel(name, channel_type, cost)
        self.media_channels.append(media_channel)

    def remove_media_channel(self, name):
        """
        Removes a media channel.

        Args:
            name (str): The name of the media channel to remove.

        Raises:
            ValueError: If the media channel does not exist.
        """
        for channel in self.media_channels:
            if channel.name == name:
                self.media_channels.remove(channel)
                return
        raise ValueError("Media channel does not exist.")

    def add_event(self, name, date, budget):
        """
        Adds an event.

        Args:
            name (str): The name of the event.
            date (datetime.date): The date of the event.
            budget (float): The budget for the event.
        """
        event = Event(name, date, budget)
        self.events.append(event)

    def assign_media_channel_to_event(self, event_name, channel_name):
        """
        Assigns a media channel to an event.

        Args:
            event_name (str): The name of the event.
            channel_name (str): The name of the media channel.

        Raises:
            ValueError: If the event or media channel does not exist.
        """
        event = next((event for event in self.events if event.name == event_name), None)
        media_channel = next((channel for channel in self.media_channels if channel.name == channel_name), None)
        if event is None:
            raise ValueError("Event does not exist.")
        if media_channel is None:
            raise ValueError("Media channel does not exist.")
        event.add_media_channel(media_channel)

    def list_media_channels(self):
        """Lists all media channels."""
        for channel in self.media_channels:
            print(channel)

    def list_events(self):
        """Lists all events."""
        for event in self.events:
            print(event)
            print("------------------------")


def main():
    media_manager = MediaManager()

    while True:
        print("Media Selection and Management Script")
        print("-------------------------------------")
        print("1. Add media channel")
        print("2. Remove media channel")
        print("3. Add event")
        print("4. Assign media channel to event")
        print("5. List media channels")
        print("6. List events")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter media channel name: ")
            channel_type = input("Enter media channel type: ")
            cost = float(input("Enter media channel cost: R "))
            media_manager.add_media_channel(name, channel_type, cost)
        elif choice == "2":
            name = input("Enter media channel name: ")
            try:
                media_manager.remove_media_channel(name)
            except ValueError as e:
                print(e)
        elif choice == "3":
            name = input("Enter event name: ")
            date_input = input("Enter event date (YYYY-MM-DD): ")
            date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
            budget = float(input("Enter event budget: R "))
            media_manager.add_event(name, date, budget)
        elif choice == "4":
            event_name = input("Enter event name: ")
            channel_name = input("Enter media channel name: ")
            try:
                media_manager.assign_media_channel_to_event(event_name, channel_name)
            except ValueError as e:
                print(e)
        elif choice == "5":
            media_manager.list_media_channels()
        elif choice == "6":
            media_manager.list_events()
        elif choice == "7":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
