"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tecnicos-whirlpool.com
Prompt: Write Python code for scheduling a Whirlpool appliance repair service, including user input for appliance type, issue description, and preferred date, referencing the agendamiento process described on https://tecnicos-whirlpool.com.
Generated: DETERMINISTIC_27b2c61a6965144b
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class ApplianceRepairScheduler:
    def __init__(self):
        """Initialize the scheduler with an empty list of scheduled repairs."""
        self.scheduled_repairs = []

    def get_appliance_type(self):
        """Prompt the user for the type of appliance and validate the input."""
        appliance_types = ['Refrigerator', 'Washer', 'Dryer', 'Dishwasher', 'Oven']
        print("Available appliance types:")
        for i, appliance in enumerate(appliance_types, start=1):
            print(f"{i}. {appliance}")

        while True:
            try:
                choice = int(input("Select the appliance type by number: "))
                if 1 <= choice <= len(appliance_types):
                    return appliance_types[choice - 1]
                else:
                    print("Invalid choice. Please select a valid appliance type.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_issue_description(self):
        """Prompt the user for the issue description."""
        return input("Please describe the issue with your appliance: ")

    def get_preferred_date(self):
        """Prompt the user for a preferred date and validate the input."""
        while True:
            try:
                date_input = input("Enter your preferred date for the repair (YYYY-MM-DD): ")
                preferred_date = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
                if preferred_date < datetime.date.today():
                    print("The preferred date cannot be in the past. Please try again.")
                else:
                    return preferred_date
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

    def schedule_repair(self, appliance_type, issue_description, preferred_date):
        """Schedule a repair service and add it to the list of scheduled repairs."""
        repair_info = {
            'appliance_type': appliance_type,
            'issue_description': issue_description,
            'preferred_date': preferred_date
        }
        self.scheduled_repairs.append(repair_info)
        print(f"Repair scheduled successfully: {repair_info}")

    def run(self):
        """Run the main scheduling process."""
        print("Welcome to the Whirlpool Appliance Repair Scheduler!")
        appliance_type = self.get_appliance_type()
        issue_description = self.get_issue_description()
        preferred_date = self.get_preferred_date()
        self.schedule_repair(appliance_type, issue_description, preferred_date)

if __name__ == "__main__":
    scheduler = ApplianceRepairScheduler()
    scheduler.run()
```
