"""
Generated Code Metadata:
========================
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: "Create a maintenance schedule for a glass bathroom box, including tasks such as cleaning, inspecting, and replacing worn-out parts."
Generated: DETERMINISTIC_576ec9403aa4823d
Batch ID: 20250622_205204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class MaintenanceSchedule:
    """
    A class to manage the maintenance schedule for a glass bathroom box.
    Includes tasks such as cleaning, inspecting, and replacing worn-out parts.
    """

    def __init__(self):
        """
        Initializes the maintenance schedule with default tasks and intervals.
        """
        self.tasks = [
            {"task": "Clean glass surfaces", "interval_days": 7},
            {"task": "Inspect seals and joints", "interval_days": 30},
            {"task": "Replace worn-out seals", "interval_days": 180},
        ]
        self.schedule = []

    def generate_schedule(self, start_date):
        """
        Generates a maintenance schedule based on the tasks and intervals.

        Args:
            start_date (datetime.date): The date to start the schedule from.
        """
        self.schedule = []
        for task in self.tasks:
            next_date = start_date
            while next_date <= start_date + datetime.timedelta(days=365):  # Generate for 1 year
                self.schedule.append({"task": task["task"], "date": next_date})
                next_date += datetime.timedelta(days=task["interval_days"])

    def display_schedule(self):
        """
        Displays the maintenance schedule in a readable format.
        """
        print("Maintenance Schedule for Glass Bathroom Box:")
        print("-" * 40)
        for entry in sorted(self.schedule, key=lambda x: x["date"]):
            print(f"{entry['date']}: {entry['task']}")

    def save_schedule_to_file(self, filename):
        """
        Saves the maintenance schedule to a file.

        Args:
            filename (str): The name of the file to save the schedule to.
        """
        try:
            with open(filename, "w") as file:
                file.write("Maintenance Schedule for Glass Bathroom Box:\n")
                file.write("-" * 40 + "\n")
                for entry in sorted(self.schedule, key=lambda x: x["date"]):
                    file.write(f"{entry['date']}: {entry['task']}\n")
            print(f"Schedule successfully saved to {filename}")
        except IOError as e:
            print(f"Error saving schedule to file: {e}")

# Main execution
if __name__ == "__main__":
    try:
        # Initialize the maintenance schedule
        schedule = MaintenanceSchedule()

        # Generate the schedule starting from today
        today = datetime.date.today()
        schedule.generate_schedule(start_date=today)

        # Display the schedule
        schedule.display_schedule()

        # Save the schedule to a file
        schedule.save_schedule_to_file("maintenance_schedule.txt")
    except Exception as e:
        print(f"An error occurred: {e}")
```
