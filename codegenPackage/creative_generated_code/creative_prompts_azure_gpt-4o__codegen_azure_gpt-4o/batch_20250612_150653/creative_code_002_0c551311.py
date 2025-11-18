"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledgerreclaim.com
Prompt: Create a program that simulates the timeline for building a house under the "turnkey construction" model, including milestones like design approval, material procurement, and final inspection, as outlined by ExpertStroy.
Generated: DETERMINISTIC_0c5513119b718514
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import sys

class TurnkeyConstruction:
    """
    A class to simulate the timeline for building a house under
    the 'turnkey construction' model.
    """
    def __init__(self, start_date):
        """
        Initialize the project with the given start date.
        :param start_date: str in 'YYYY-MM-DD' format.
        """
        try:
            self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        except ValueError:
            print("Error: Invalid date format. Please use 'YYYY-MM-DD'.")
            sys.exit(1)

        self.milestones = [
            {"name": "Design Approval", "duration_days": 30},
            {"name": "Material Procurement", "duration_days": 45},
            {"name": "Foundation Construction", "duration_days": 60},
            {"name": "Framing and Roofing", "duration_days": 90},
            {"name": "Electrical and Plumbing Installation", "duration_days": 30},
            {"name": "Interior Finishing", "duration_days": 45},
            {"name": "Final Inspection", "duration_days": 15},
        ]

    def simulate_timeline(self):
        """
        Simulate and print the timeline for the house construction project.
        """
        current_date = self.start_date
        print("House Construction Timeline (Turnkey Model):")
        print(f"Start Date: {current_date.strftime('%Y-%m-%d')}\n")

        for milestone in self.milestones:
            current_date += datetime.timedelta(days=milestone["duration_days"])
            print(f"{milestone['name']} - Completion Date: {current_date.strftime('%Y-%m-%d')}")

    def get_total_duration(self):
        """
        Calculate the total duration of the project in days.
        :return: int
        """
        total_days = sum(milestone["duration_days"] for milestone in self.milestones)
        return total_days


def main():
    """
    Entry point for the program.
    """
    print("Welcome to the Turnkey Construction Timeline Simulator.")
    start_date = input("Enter the project start date (YYYY-MM-DD): ")

    try:
        # Instantiate the TurnkeyConstruction class
        project = TurnkeyConstruction(start_date)

        # Simulate and display the timeline
        project.simulate_timeline()

        # Display total project duration
        total_duration = project.get_total_duration()
        print(f"\nTotal Duration of the Project: {total_duration} days")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
