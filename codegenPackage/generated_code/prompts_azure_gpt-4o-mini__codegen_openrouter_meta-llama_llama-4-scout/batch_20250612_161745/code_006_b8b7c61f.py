"""
Generated Code Metadata:
========================
Original URL: https://lethmixedslowpitch.com
Prompt: What features does Slo-Pitch Central offer for organizing and managing slo-pitch events effectively?
Generated: DETERMINISTIC_b8b7c61f6722b89c
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# slo_pitch_central.py

class SloPitchCentral:
    """
    A class representing Slo-Pitch Central, an event management system.
    """

    def __init__(self):
        """
        Initializes the SloPitchCentral object.
        """
        self.events = {}

    def create_event(self, event_name, date, time, location):
        """
        Creates a new slo-pitch event.

        Args:
            event_name (str): The name of the event.
            date (str): The date of the event in YYYY-MM-DD format.
            time (str): The time of the event in HH:MM format.
            location (str): The location of the event.

        Returns:
            bool: True if the event was created successfully, False otherwise.
        """
        if event_name in self.events:
            print(f"Event '{event_name}' already exists.")
            return False

        self.events[event_name] = {
            "date": date,
            "time": time,
            "location": location,
            "teams": [],
            "players": []
        }

        print(f"Event '{event_name}' created successfully.")
        return True

    def add_team(self, event_name, team_name):
        """
        Adds a team to an existing slo-pitch event.

        Args:
            event_name (str): The name of the event.
            team_name (str): The name of the team.

        Returns:
            bool: True if the team was added successfully, False otherwise.
        """
        if event_name not in self.events:
            print(f"Event '{event_name}' does not exist.")
            return False

        if team_name in self.events[event_name]["teams"]:
            print(f"Team '{team_name}' already exists in event '{event_name}'.")
            return False

        self.events[event_name]["teams"].append(team_name)
        print(f"Team '{team_name}' added to event '{event_name}' successfully.")
        return True

    def add_player(self, event_name, player_name, team_name):
        """
        Adds a player to a team in an existing slo-pitch event.

        Args:
            event_name (str): The name of the event.
            player_name (str): The name of the player.
            team_name (str): The name of the team.

        Returns:
            bool: True if the player was added successfully, False otherwise.
        """
        if event_name not in self.events:
            print(f"Event '{event_name}' does not exist.")
            return False

        if team_name not in self.events[event_name]["teams"]:
            print(f"Team '{team_name}' does not exist in event '{event_name}'.")
            return False

        if player_name in self.events[event_name]["players"]:
            print(f"Player '{player_name}' already exists in event '{event_name}'.")
            return False

        self.events[event_name]["players"].append({"name": player_name, "team": team_name})
        print(f"Player '{player_name}' added to team '{team_name}' in event '{event_name}' successfully.")
        return True

    def view_event_details(self, event_name):
        """
        Displays the details of an existing slo-pitch event.

        Args:
            event_name (str): The name of the event.

        Returns:
            bool: True if the event details were displayed successfully, False otherwise.
        """
        if event_name not in self.events:
            print(f"Event '{event_name}' does not exist.")
            return False

        event = self.events[event_name]
        print(f"Event Name: {event_name}")
        print(f"Date: {event['date']}")
        print(f"Time: {event['time']}")
        print(f"Location: {event['location']}")
        print(f"Teams: {', '.join(event['teams'])}")
        print("Players:")
        for player in event["players"]:
            print(f"- {player['name']} ({player['team']})")

        return True


def main():
    slo_pitch_central = SloPitchCentral()

    while True:
        print("\nSlo-Pitch Central Menu:")
        print("1. Create Event")
        print("2. Add Team")
        print("3. Add Player")
        print("4. View Event Details")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            event_name = input("Enter event name: ")
            date = input("Enter event date (YYYY-MM-DD): ")
            time = input("Enter event time (HH:MM): ")
            location = input("Enter event location: ")
            slo_pitch_central.create_event(event_name, date, time, location)
        elif choice == "2":
            event_name = input("Enter event name: ")
            team_name = input("Enter team name: ")
            slo_pitch_central.add_team(event_name, team_name)
        elif choice == "3":
            event_name = input("Enter event name: ")
            player_name = input("Enter player name: ")
            team_name = input("Enter team name: ")
            slo_pitch_central.add_player(event_name, player_name, team_name)
        elif choice == "4":
            event_name = input("Enter event name: ")
            slo_pitch_central.view_event_details(event_name)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
