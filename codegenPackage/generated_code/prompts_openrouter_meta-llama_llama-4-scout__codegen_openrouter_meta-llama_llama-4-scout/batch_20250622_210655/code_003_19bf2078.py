"""
Generated Code Metadata:
========================
Original URL: https://jusoor.ch
Prompt: "Design a program to track and report human rights abuses, inspired by Jusoor International's investigative journalism and media advocacy efforts."
Generated: DETERMINISTIC_19bf2078c483c148
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# human_rights_abuse_tracker.py

import datetime
import json

class HumanRightsAbuse:
    def __init__(self, date, location, description, victims=None, perpetrators=None):
        """
        Initialize a HumanRightsAbuse object.

        Args:
            date (str): Date of the abuse in YYYY-MM-DD format.
            location (str): Location of the abuse.
            description (str): Description of the abuse.
            victims (list, optional): List of victim names. Defaults to None.
            perpetrators (list, optional): List of perpetrator names. Defaults to None.
        """
        self.date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        self.location = location
        self.description = description
        self.victims = victims if victims else []
        self.perpetrators = perpetrators if perpetrators else []

    def to_dict(self):
        """
        Convert the HumanRightsAbuse object to a dictionary.

        Returns:
            dict: Dictionary representation of the HumanRightsAbuse object.
        """
        return {
            "date": self.date.isoformat(),
            "location": self.location,
            "description": self.description,
            "victims": self.victims,
            "perpetrators": self.perpetrators,
        }

class HumanRightsAbuseTracker:
    def __init__(self):
        """
        Initialize a HumanRightsAbuseTracker object.
        """
        self.abuses = []

    def add_abuse(self, abuse):
        """
        Add a human rights abuse to the tracker.

        Args:
            abuse (HumanRightsAbuse): HumanRightsAbuse object to add.
        """
        self.abuses.append(abuse)

    def get_abuses(self):
        """
        Get all human rights abuses in the tracker.

        Returns:
            list: List of HumanRightsAbuse objects.
        """
        return self.abuses

    def save_to_json(self, filename):
        """
        Save the human rights abuses to a JSON file.

        Args:
            filename (str): Name of the JSON file.

        Raises:
            Exception: If an error occurs while saving to the JSON file.
        """
        try:
            with open(filename, "w") as file:
                json.dump([abuse.to_dict() for abuse in self.abuses], file, indent=4)
        except Exception as e:
            print(f"Error saving to JSON file: {e}")

    def load_from_json(self, filename):
        """
        Load human rights abuses from a JSON file.

        Args:
            filename (str): Name of the JSON file.

        Raises:
            Exception: If an error occurs while loading from the JSON file.
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.abuses = [HumanRightsAbuse(**abuse) for abuse in data]
        except Exception as e:
            print(f"Error loading from JSON file: {e}")

def main():
    tracker = HumanRightsAbuseTracker()

    while True:
        print("\nHuman Rights Abuse Tracker")
        print("1. Add abuse")
        print("2. View abuses")
        print("3. Save to JSON")
        print("4. Load from JSON")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            location = input("Enter location: ")
            description = input("Enter description: ")
            victims = input("Enter victims (comma-separated): ").split(",")
            victims = [victim.strip() for victim in victims]
            perpetrators = input("Enter perpetrators (comma-separated): ").split(",")
            perpetrators = [perpetrator.strip() for perpetrator in perpetrators]

            abuse = HumanRightsAbuse(date, location, description, victims, perpetrators)
            tracker.add_abuse(abuse)
        elif choice == "2":
            for i, abuse in enumerate(tracker.get_abuses()):
                print(f"\nAbuse {i+1}:")
                print(f"Date: {abuse.date}")
                print(f"Location: {abuse.location}")
                print(f"Description: {abuse.description}")
                print(f"Victims: {', '.join(abuse.victims)}")
                print(f"Perpetrators: {', '.join(abuse.perpetrators)}")
        elif choice == "3":
            filename = input("Enter JSON filename: ")
            tracker.save_to_json(filename)
        elif choice == "4":
            filename = input("Enter JSON filename: ")
            tracker.load_from_json(filename)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
