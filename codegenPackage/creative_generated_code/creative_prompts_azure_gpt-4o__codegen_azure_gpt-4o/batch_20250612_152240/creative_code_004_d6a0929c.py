"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bevm-airdrop.vercel.app
Prompt: Write a program to display the monthly unlock schedule for the GEB airdrop allocation, including the percentages specified (0.33% for the first 12 months and 0.125% for the next 48 months).
Generated: DETERMINISTIC_d6a0929cd4401811
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class GEBUnlockSchedule:
    def __init__(self, start_date):
        """
        Initialize the GEB Unlock Schedule with a start date.

        :param start_date: The start date of the unlock schedule (datetime object)
        """
        self.start_date = start_date
        self.schedule = []  # Will hold the unlock schedule

    def generate_schedule(self):
        """
        Generate the unlock schedule for GEB allocation based on the following criteria:
        - 0.33% unlock monthly for the first 12 months
        - 0.125% unlock monthly for the next 48 months
        """
        months_phase1 = 12  # First 12 months
        rate_phase1 = 0.33  # Unlock rate for phase 1 (percentage)

        months_phase2 = 48  # Next 48 months
        rate_phase2 = 0.125  # Unlock rate for phase 2 (percentage)

        # Generate phase 1 schedule
        for month in range(1, months_phase1 + 1):
            unlock_date = self.start_date + timedelta(days=month * 30)  # Approximate 1 month as 30 days
            self.schedule.append({
                "month": month,
                "unlock_date": unlock_date.strftime("%Y-%m-%d"),
                "unlock_rate": rate_phase1
            })

        # Generate phase 2 schedule
        for month in range(1, months_phase2 + 1):
            unlock_date = self.start_date + timedelta(days=(months_phase1 + month) * 30)
            self.schedule.append({
                "month": months_phase1 + month,
                "unlock_date": unlock_date.strftime("%Y-%m-%d"),
                "unlock_rate": rate_phase2
            })

    def display_schedule(self):
        """
        Display the generated unlock schedule in a readable format.
        """
        if not self.schedule:
            print("No schedule generated. Please run generate_schedule() first.")
            return

        print(f"{'Month':<6}{'Unlock Date':<15}{'Unlock Rate (%)':<15}")
        print("-" * 36)
        for entry in self.schedule:
            print(f"{entry['month']:<6}{entry['unlock_date']:<15}{entry['unlock_rate']:<15.3f}")


# Main Execution
if __name__ == "__main__":
    try:
        # Define the start date for the airdrop schedule
        start_date = datetime(2023, 1, 1)  # Example start date (January 1, 2023)

        # Initialize and generate the unlock schedule
        schedule = GEBUnlockSchedule(start_date)
        schedule.generate_schedule()

        # Display the generated schedule
        schedule.display_schedule()

    except Exception as e:
        print(f"An error occurred: {e}")
```
