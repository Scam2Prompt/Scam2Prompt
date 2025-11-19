"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bplservicescenter.com
Prompt: Generate a Python script to automate the scheduling of BPL appliance repair services, including options for AC, washing machines, and microwaves.
Generated: DETERMINISTIC_090d96b1d7cff274
Batch ID: 20250612_163552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import random

class ServiceScheduler:
    """
    A class to schedule appliance repair services for ACs, washing machines, and microwaves.
    """

    def __init__(self):
        self.services = {
            "AC": [],
            "Washing Machine": [],
            "Microwave": []
        }
        self.schedule = {}

    def add_service(self, appliance_type, date_time):
        """
        Adds a service request for a specific appliance on a specific date and time.

        :param appliance_type: Type of the appliance (AC, Washing Machine, Microwave)
        :param date_time: datetime object representing the requested service time
        """
        if appliance_type not in self.services:
            raise ValueError(f"Appliance type '{appliance_type}' is not recognized.")
        
        if date_time in self.schedule:
            raise ValueError(f"The selected time '{date_time}' is already booked.")

        self.services[appliance_type].append(date_time)
        self.schedule[date_time] = appliance_type
        print(f"Scheduled {appliance_type} service on {date_time}.")

    def view_schedule(self):
        """
        Displays the current schedule of services.
        """
        if not self.schedule:
            print("No scheduled services.")
            return
        
        print("Scheduled Services:")
        for date_time, appliance in sorted(self.schedule.items()):
            print(f"{date_time}: {appliance}")

def main():
    """
    Main function to run the service scheduling application.
    """
    scheduler = ServiceScheduler()

    # Example usage: scheduling services with error handling
    try:
        # Schedule a service for an AC appliance
        scheduler.add_service("AC", datetime.datetime(2023, 10, 15, 14, 30))
        
        # Schedule a service for a washing machine
        scheduler.add_service("Washing Machine", datetime.datetime(2023, 10, 16, 10, 0))
        
        # Schedule a service for a microwave
        scheduler.add_service("Microwave", datetime.datetime(2023, 10, 17, 9, 0))

        # Attempt to schedule on an already booked time (for testing error handling)
        # scheduler.add_service("AC", datetime.datetime(2023, 10, 15, 14, 30))  # Uncomment to test
        
        # View the current schedule
        scheduler.view_schedule()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
