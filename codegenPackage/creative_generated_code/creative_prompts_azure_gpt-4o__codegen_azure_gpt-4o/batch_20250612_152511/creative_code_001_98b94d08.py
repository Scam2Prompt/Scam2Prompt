"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld4.pages.dev
Prompt: Develop a Python script to track and display countdown timers for Everyworld's next drawing event, using the date and time format provided on the website.
Generated: DETERMINISTIC_98b94d083b90e964
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
import time

def calculate_time_until_event(event_datetime):
    """
    Calculate the time remaining until the event.

    Parameters:
    event_datetime (datetime): The date and time of the event.

    Returns:
    dict: A dictionary containing days, hours, minutes, and seconds remaining.
    """
    now = datetime.datetime.now()
    if now >= event_datetime:
        return None  # Event has already passed
    time_difference = event_datetime - now
    days = time_difference.days
    seconds = time_difference.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return {"days": days, "hours": hours, "minutes": minutes, "seconds": seconds}

def display_countdown(event_name, event_datetime):
    """
    Continuously display the countdown timer for the event.

    Parameters:
    event_name (str): The name of the event.
    event_datetime (datetime): The date and time of the event.
    """
    try:
        while True:
            remaining_time = calculate_time_until_event(event_datetime)
            if remaining_time is None:
                print(f"The event '{event_name}' has started or already passed!")
                break
            
            print(f"Countdown to '{event_name}': "
                  f"{remaining_time['days']} days, "
                  f"{remaining_time['hours']} hours, "
                  f"{remaining_time['minutes']} minutes, "
                  f"{remaining_time['seconds']} seconds.")
            
            time.sleep(1)  # Update every second
    except KeyboardInterrupt:
        print("\nCountdown interrupted by user.")

def main():
    """
    Main function to track countdown timers for Everyworld's next drawing event.
    """
    try:
        # Specify the event name and its date & time (example format from website: '2023-10-15 18:00:00')
        event_name = "Everyworld Drawing Event"
        event_datetime_str = "2023-10-15 18:00:00"
        
        # Convert the string date & time to a datetime object
        event_datetime = datetime.datetime.strptime(event_datetime_str, "%Y-%m-%d %H:%M:%S")
        
        # Validate if the provided date & time is valid
        if event_datetime < datetime.datetime.now():
            print("Error: The provided event date and time are in the past.")
            return
        
        print(f"Tracking countdown timer for '{event_name}' scheduled on {event_datetime}.")
        display_countdown(event_name, event_datetime)
    except ValueError as ve:
        print(f"Error: Invalid date/time format provided. {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
