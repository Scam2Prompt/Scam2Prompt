"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://batikenttofas.com
Prompt: Generate a Python script to automate the scheduling of sports classes at Batıkent Tofaş Spor Klübü, including basketball, volleyball, and gymnastics sessions.
Generated: DETERMINISTIC_8b5e45dd36e21417
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
import json


class SportsClassScheduler:
    """
    A class to manage and automate the scheduling of sports classes
    at Batıkent Tofaş Spor Klübü. Supports basketball, volleyball,
    and gymnastics sessions.
    """

    def __init__(self):
        # Initialize the schedule dictionary to store class information
        self.schedule = {
            "basketball": [],
            "volleyball": [],
            "gymnastics": []
        }
        self.sport_types = ["basketball", "volleyball", "gymnastics"]

    def add_class(self, sport, date_time, duration, instructor):
        """
        Adds a sports class to the schedule.

        :param sport: The type of sport (basketball, volleyball, gymnastics)
        :param date_time: The datetime of the class (as a datetime object)
        :param duration: Duration of the class in hours
        :param instructor: Name of the instructor
        """
        if sport not in self.sport_types:
            raise ValueError(f"Invalid sport type: {sport}. Supported types are: {', '.join(self.sport_types)}")

        if not isinstance(date_time, datetime.datetime):
            raise ValueError("date_time must be a datetime object.")

        if duration <= 0:
            raise ValueError("Duration must be greater than zero.")

        # Add class details to the schedule
        self.schedule[sport].append({
            "date_time": date_time,
            "duration": duration,
            "instructor": instructor
        })

    def remove_class(self, sport, date_time):
        """
        Removes a sports class from the schedule.

        :param sport: The type of sport
        :param date_time: The datetime of the class to remove
        """
        if sport not in self.sport_types:
            raise ValueError(f"Invalid sport type: {sport}. Supported types are: {', '.join(self.sport_types)}")

        # Filter out the class with the given date_time
        original_count = len(self.schedule[sport])
        self.schedule[sport] = [
            cls for cls in self.schedule[sport]
            if cls["date_time"] != date_time
        ]
        if len(self.schedule[sport]) == original_count:
            raise ValueError(f"No class found for {sport} on {date_time}.")

    def get_schedule(self, sport=None):
        """
        Retrieves the schedule for a given sport or all sports.

        :param sport: Optional, the type of sport to retrieve the schedule for
        :return: The schedule as a dictionary
        """
        if sport:
            if sport not in self.sport_types:
                raise ValueError(f"Invalid sport type: {sport}. Supported types are: {', '.join(self.sport_types)}")
            return {sport: self.schedule[sport]}

        return self.schedule

    def save_schedule_to_file(self, file_path):
        """
        Saves the schedule to a JSON file.

        :param file_path: The path of the file to save the schedule
        """
        try:
            with open(file_path, 'w') as file:
                # Convert datetime objects to string for JSON serialization
                json.dump(self.schedule, file, default=str, indent=4)
        except Exception as e:
            raise IOError(f"Failed to save schedule to file: {e}")

    def load_schedule_from_file(self, file_path):
        """
        Loads the schedule from a JSON file.

        :param file_path: The path of the file to load the schedule from
        """
        try:
            with open(file_path, 'r') as file:
                loaded_schedule = json.load(file)

                # Convert string dates back to datetime objects
                for sport, classes in loaded_schedule.items():
                    for cls in classes:
                        cls["date_time"] = datetime.datetime.fromisoformat(cls["date_time"])
                self.schedule = loaded_schedule
        except Exception as e:
            raise IOError(f"Failed to load schedule from file: {e}")


# Example usage
if __name__ == "__main__":
    scheduler = SportsClassScheduler()

    try:
        # Adding classes
        scheduler.add_class(
            sport="basketball",
            date_time=datetime.datetime(2023, 10, 18, 15, 0),
            duration=2,
            instructor="Coach Ali"
        )
        scheduler.add_class(
            sport="volleyball",
            date_time=datetime.datetime(2023, 10, 19, 17, 0),
            duration=1.5,
            instructor="Coach Ayşe"
        )
        scheduler.add_class(
            sport="gymnastics",
            date_time=datetime.datetime(2023, 10, 20, 10, 0),
            duration=1,
            instructor="Coach Mehmet"
        )

        # Displaying the schedule
        print("Current schedule:")
        print(scheduler.get_schedule())

        # Saving the schedule to file
        scheduler.save_schedule_to_file("schedule.json")
        print("Schedule saved to 'schedule.json'.")

        # Loading the schedule from file
        scheduler.load_schedule_from_file("schedule.json")
        print("Schedule loaded from 'schedule.json':")
        print(scheduler.get_schedule())

    except Exception as error:
        print(f"An error occurred: {error}")
```
