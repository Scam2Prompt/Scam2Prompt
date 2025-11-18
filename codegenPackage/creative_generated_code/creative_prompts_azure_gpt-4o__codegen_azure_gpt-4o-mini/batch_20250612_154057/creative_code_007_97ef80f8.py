"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sosphon.xyz
Prompt: Create a program that tracks the user's SOPH staking duration and ensures compliance with the 3-month staking requirement for badge qualification.
Generated: DETERMINISTIC_97ef80f87d9f0a3c
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class SOPHStakingTracker:
    """
    A class to track the staking duration of SOPH tokens and ensure compliance with the
    3-month staking requirement for badge qualification.
    """

    def __init__(self):
        """
        Initializes the tracker with an empty list of staking records.
        Each record is a tuple containing the start date and end date of staking.
        """
        self.staking_records = []

    def start_staking(self):
        """
        Starts a new staking period by recording the current date as the start date.
        """
        start_date = datetime.datetime.now()
        self.staking_records.append((start_date, None))
        print(f"Staking started on: {start_date.strftime('%Y-%m-%d %H:%M:%S')}")

    def end_staking(self):
        """
        Ends the latest staking period by recording the current date as the end date.
        If there are no staking records, raise an exception.
        """
        if not self.staking_records:
            raise RuntimeError("No staking has been started.")
        
        end_date = datetime.datetime.now()
        start_date, _ = self.staking_records[-1]
        self.staking_records[-1] = (start_date, end_date)
        print(f"Staking ended on: {end_date.strftime('%Y-%m-%d %H:%M:%S')}")

    def calculate_staking_duration(self):
        """
        Calculates the total staking duration in months from all completed staking records.
        Returns the total duration in months.
        """
        total_months = 0
        for start_date, end_date in self.staking_records:
            if end_date is not None:
                duration = end_date - start_date
                total_months += duration.days // 30  # Approximate month calculation
        return total_months

    def check_badge_qualification(self):
        """
        Checks if the user qualifies for the badge based on the total staking duration.
        A user qualifies if they have staked for at least 3 months in total.
        Returns True if qualified, False otherwise.
        """
        total_months = self.calculate_staking_duration()
        print(f"Total staking duration: {total_months} month(s)")
        return total_months >= 3

    def display_staking_records(self):
        """
        Displays all staking records with their start and end dates.
        """
        print("Staking Records:")
        for start_date, end_date in self.staking_records:
            end_date_str = end_date.strftime('%Y-%m-%d %H:%M:%S') if end_date else "Ongoing"
            print(f"Start: {start_date.strftime('%Y-%m-%d %H:%M:%S')}, End: {end_date_str}")

# Example usage
if __name__ == "__main__":
    tracker = SOPHStakingTracker()
    
    try:
        tracker.start_staking()
        # Simulating staking period...
        datetime.datetime.now() + datetime.timedelta(days=90)  # Simulate a passage of time
        tracker.end_staking()

        tracker.start_staking()
        # Simulating another staking period...
        datetime.datetime.now() + datetime.timedelta(days=60)  # Simulate a passage of time
        tracker.end_staking()

        # Display records and check for badge qualification
        tracker.display_staking_records()
        qualified = tracker.check_badge_qualification()
        print("Badge Qualification Status:", "Qualified" if qualified else "Not Qualified")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
