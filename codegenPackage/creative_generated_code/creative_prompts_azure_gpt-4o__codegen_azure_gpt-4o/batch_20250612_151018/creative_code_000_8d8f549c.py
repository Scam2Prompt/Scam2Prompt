"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-200--nervous-kare-6f3c45.netlify.app
Prompt: Write a Python script to create a scheduling system for refuse and recycling collection, including features for tracking collection dates and locations specific to the City of York.
Generated: DETERMINISTIC_8d8f549c7a76ef3b
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta


class RefuseAndRecyclingScheduler:
    """
    A scheduling system for refuse and recycling collection in the City of York.
    Tracks collection dates and locations.
    """

    def __init__(self):
        # Initialize data storage for schedules
        self.schedules = {}  # Dictionary to store schedules by location
        self.collection_types = ["Refuse", "Recycling"]  # Types of collections

    def add_location(self, location: str):
        """
        Add a new location to the scheduler if it doesn't already exist.
        :param location: Name of the location (e.g., street or neighborhood).
        """
        if location not in self.schedules:
            self.schedules[location] = []
            print(f"[INFO] Location '{location}' added.")
        else:
            print(f"[WARNING] Location '{location}' already exists.")

    def schedule_collection(self, location: str, collection_date: str, collection_type: str):
        """
        Schedule a collection for a specific location and date.
        :param location: Name of the location.
        :param collection_date: Collection date in 'YYYY-MM-DD' format.
        :param collection_type: Type of collection ('Refuse' or 'Recycling').
        """
        if collection_type not in self.collection_types:
            print(f"[ERROR] Invalid collection type: '{collection_type}'.")
            return

        try:
            # Validate and parse the date
            collection_date_obj = datetime.strptime(collection_date, "%Y-%m-%d")
        except ValueError:
            print(f"[ERROR] Invalid date format: '{collection_date}'. Use 'YYYY-MM-DD'.")
            return

        if location not in self.schedules:
            print(f"[ERROR] Location '{location}' not found. Please add it first.")
            return

        # Add the collection to the schedule
        self.schedules[location].append({
            "date": collection_date_obj,
            "type": collection_type
        })
        print(f"[INFO] Scheduled {collection_type} collection for {location} on {collection_date}.")

    def get_schedule(self, location: str):
        """
        Retrieve the collection schedule for a specific location.
        :param location: Name of the location.
        :return: List of collection events or a message if the location does not exist.
        """
        if location not in self.schedules:
            print(f"[ERROR] No schedule found for location '{location}'.")
            return []

        # Sort schedule by date
        schedule = sorted(self.schedules[location], key=lambda x: x["date"])
        return schedule

    def save_schedule_to_file(self, filename: str):
        """
        Save the current schedule to a JSON file.
        :param filename: Path to the file.
        """
        try:
            # Convert datetime objects to strings for serialization
            serializable_schedule = {
                location: [{"date": entry["date"].strftime("%Y-%m-%d"), "type": entry["type"]}
                           for entry in events]
                for location, events in self.schedules.items()
            }

            with open(filename, "w") as file:
                json.dump(serializable_schedule, file, indent=4)
            print(f"[INFO] Schedule saved to '{filename}'.")
        except IOError as e:
            print(f"[ERROR] Could not save schedule to file: {e}")

    def load_schedule_from_file(self, filename: str):
        """
        Load the schedule from a JSON file.
        :param filename: Path to the file.
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)

            # Convert date strings back to datetime objects
            self.schedules = {
                location: [{"date": datetime.strptime(entry["date"], "%Y-%m-%d"), "type": entry["type"]}
                           for entry in events]
                for location, events in data.items()
            }
            print(f"[INFO] Schedule loaded from '{filename}'.")
        except FileNotFoundError:
            print(f"[ERROR] File '{filename}' not found.")
        except json.JSONDecodeError:
            print(f"[ERROR] Failed to parse JSON file '{filename}'.")
        except Exception as e:
            print(f"[ERROR] An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    scheduler = RefuseAndRecyclingScheduler()

    # Add locations
    scheduler.add_location("Downtown")
    scheduler.add_location("North Side")

    # Schedule collections
    scheduler.schedule_collection("Downtown", "2023-12-01", "Refuse")
    scheduler.schedule_collection("Downtown", "2023-12-08", "Recycling")
    scheduler.schedule_collection("North Side", "2023-12-02", "Refuse")

    # Get and print schedules
    print("\nDowntown Schedule:")
    for event in scheduler.get_schedule("Downtown"):
        print(f" - {event['date'].strftime('%Y-%m-%d')} ({event['type']})")

    # Save to and load from file
    scheduler.save_schedule_to_file("schedule.json")
    scheduler.load_schedule_from_file("schedule.json")
```
