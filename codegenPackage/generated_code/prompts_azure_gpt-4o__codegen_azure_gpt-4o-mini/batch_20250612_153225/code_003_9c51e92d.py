"""
Generated Code Metadata:
========================
Original URL: https://934ummfm.com
Prompt: Create a program to schedule reminders for UMM FM's radio broadcasts based on their operating hours (Monday-Saturday, 06:45-21:00 WIB).
Generated: DETERMINISTIC_9c51e92d83fdbfb4
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import schedule
import time
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReminderScheduler:
    def __init__(self, start_time, end_time, days):
        """
        Initialize the ReminderScheduler with operating hours and days.

        :param start_time: The start time of the schedule (HH:MM format).
        :param end_time: The end time of the schedule (HH:MM format).
        :param days: List of days to schedule reminders (e.g., ['Monday', 'Tuesday']).
        """
        self.start_time = start_time
        self.end_time = end_time
        self.days = days

    def schedule_reminders(self):
        """
        Schedule reminders for the specified days and times.
        """
        for day in self.days:
            schedule.every().day.at(self.start_time).do(self.send_reminder)
            schedule.every().day.at(self.end_time).do(self.send_reminder)

    def send_reminder(self):
        """
        Send a reminder notification.
        """
        current_time = datetime.now().strftime("%H:%M")
        logging.info(f"Reminder: UMM FM Radio Broadcast at {current_time}")

    def run(self):
        """
        Run the scheduler to check for reminders.
        """
        while True:
            schedule.run_pending()
            time.sleep(1)

def main():
    # Define operating hours and days for UMM FM
    start_time = "06:45"
    end_time = "21:00"
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

    # Create a ReminderScheduler instance
    reminder_scheduler = ReminderScheduler(start_time, end_time, days)

    # Schedule reminders
    reminder_scheduler.schedule_reminders()

    # Start the scheduler
    try:
        logging.info("Starting the reminder scheduler...")
        reminder_scheduler.run()
    except KeyboardInterrupt:
        logging.info("Scheduler stopped by user.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
