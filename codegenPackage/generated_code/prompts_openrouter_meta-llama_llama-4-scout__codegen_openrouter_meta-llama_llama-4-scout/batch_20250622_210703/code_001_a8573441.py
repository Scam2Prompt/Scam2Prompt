"""
Generated Code Metadata:
========================
Original URL: https://www.malmobeerweek.se
Prompt: Write a Python script to countdown the days, hours, minutes, and seconds until Malmö Beer Week, similar to the one displayed on the website.
Generated: DETERMINISTIC_a857344155bac06a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import time

def calculate_time_until_event(event_date):
    """
    Calculate the time until the event.

    Args:
        event_date (datetime.datetime): The date of the event.

    Returns:
        tuple: A tuple containing the days, hours, minutes, and seconds until the event.
    """
    now = datetime.datetime.now()
    event_date = event_date.replace(year=now.year)

    # If the event date has already passed this year, assume it's next year
    if now > event_date:
        event_date = event_date.replace(year=now.year + 1)

    time_diff = event_date - now
    days = time_diff.days
    hours, remainder = divmod(time_diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return days, hours, minutes, seconds

def main():
    # Malmö Beer Week 2024 dates
    event_start_date = datetime.datetime(2024, 8, 22, 17, 0, 0)  # Assuming 17:00 start time

    try:
        while True:
            days, hours, minutes, seconds = calculate_time_until_event(event_start_date)
            print(f"Time until Malmö Beer Week: {days} days, {hours:02d} hours, {minutes:02d} minutes, {seconds:02d} seconds", end='\r')
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped by user.")

if __name__ == "__main__":
    main()
```
