"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://934ummfm.com
Prompt: Create a program to schedule reminders for UMM FM's radio broadcasts based on their operating hours (Monday-Saturday, 06:45-21:00 WIB).
Generated: DETERMINISTIC_9c51e92d83fdbfb4
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import schedule
import time
import datetime
import logging
from datetime import timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReminderScheduler:
    def __init__(self, start_time, end_time, days):
        self.start_time = start_time
        self.end_time = end_time
        self.days = days

    def schedule_reminders(self):
        """Schedules reminders based on defined operating hours and days."""
        for day in self.days:
            # Schedule reminders to be sent every hour within the operating hours
            schedule.every().day.at(self.start_time).do(self.send_reminder, day)
            schedule.every().day.at(self.end_time).do(self.send_reminder_end, day)

    def send_reminder(self, day):
        """Send a reminder for the broadcast start."""
        logging.info(f'Reminder: UMM FM is now live on {day}! Tune in!')

    def send_reminder_end(self, day):
        """Send a reminder for the broadcast end."""
        logging.info(f'Reminder: UMM FM broadcast is ending today on {day}. Tune in tomorrow!')

    def run(self):
        """Runs the scheduler."""
        try:
            logging.info('Scheduler started. Waiting for reminders...')
            while True:
                schedule.run_pending()
                time.sleep(1)  # Check for pending tasks every second
        except KeyboardInterrupt:
            logging.info("Scheduler stopped by user.")
        except Exception as e:
            logging.error(f"An error occurred: {e}")

def main():
    # Define the operating hours and days for UMM FM
    start_time = '06:45'
    end_time = '21:00'
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

    # Create a ReminderScheduler instance
    reminder_scheduler = ReminderScheduler(start_time, end_time, days)

    # Schedule the reminders
    reminder_scheduler.schedule_reminders()

    # Run the scheduler
    reminder_scheduler.run()

if __name__ == "__main__":
    main()
```
