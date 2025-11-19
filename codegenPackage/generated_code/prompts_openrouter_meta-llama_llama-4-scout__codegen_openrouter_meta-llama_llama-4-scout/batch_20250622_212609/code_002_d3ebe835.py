"""
Generated Code Metadata:
========================
Original URL: https://shrimohinirajdevasthan.com
Prompt: Generate a daily program schedule for a religious institution like the Shrimohiniraj Devastan, including darshan, seva, and other religious activities.
Generated: DETERMINISTIC_d3ebe835700db0b6
Batch ID: 20250622_212609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class ProgramSchedule:
    def __init__(self):
        self.schedule = []

    def add_activity(self, name, start_time, end_time):
        """Add a religious activity to the schedule."""
        self.schedule.append({
            'name': name,
            'start_time': start_time,
            'end_time': end_time
        })

    def view_schedule(self):
        """Display the daily program schedule."""
        print("Daily Program Schedule:")
        for i, activity in enumerate(self.schedule, 1):
            print(f"{i}. {activity['name']}: {activity['start_time'].strftime('%I:%M %p')} - {activity['end_time'].strftime('%I:%M %p')}")

    def save_schedule(self, filename):
        """Save the schedule to a file."""
        try:
            with open(filename, 'w') as f:
                for activity in self.schedule:
                    f.write(f"{activity['name']}: {activity['start_time'].strftime('%I:%M %p')} - {activity['end_time'].strftime('%I:%M %p')}\n")
            print(f"Schedule saved to {filename}")
        except Exception as e:
            print(f"Error saving schedule: {str(e)}")


def main():
    schedule = ProgramSchedule()

    # Define daily activities
    darshan_start = datetime.strptime('08:00 AM', '%I:%M %p')
    darshan_end = datetime.strptime('09:00 AM', '%I:%M %p')
    seva_start = datetime.strptime('09:30 AM', '%I:%M %p')
    seva_end = datetime.strptime('10:30 AM', '%I:%M %p')
    puja_start = datetime.strptime('11:00 AM', '%I:%M %p')
    puja_end = datetime.strptime('12:00 PM', '%I:%M %p')
    lunch_break_start = datetime.strptime('12:00 PM', '%I:%M %p')
    lunch_break_end = datetime.strptime('01:30 PM', '%I:%M %p')
    aarti_start = datetime.strptime('06:00 PM', '%I:%M %p')
    aarti_end = datetime.strptime('07:00 PM', '%I:%M %p')

    # Add activities to schedule
    schedule.add_activity('Darshan', darshan_start, darshan_end)
    schedule.add_activity('Seva', seva_start, seva_end)
    schedule.add_activity('Puja', puja_start, puja_end)
    schedule.add_activity('Lunch Break', lunch_break_start, lunch_break_end)
    schedule.add_activity('Aarti', aarti_start, aarti_end)

    # Display schedule
    schedule.view_schedule()

    # Save schedule to file
    schedule.save_schedule('daily_schedule.txt')


if __name__ == "__main__":
    main()
```
