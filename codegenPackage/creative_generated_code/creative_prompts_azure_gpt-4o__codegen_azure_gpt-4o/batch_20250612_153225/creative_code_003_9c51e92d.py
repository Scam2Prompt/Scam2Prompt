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
import datetime
import time

def schedule_reminder():
    """
    Schedules reminders for UMM FM's radio broadcasts based on specified operating hours.
    Operating hours: Monday-Saturday, 06:45-21:00 WIB.
    """
    # Define operating hours
    OPERATING_START = datetime.time(6, 45)  # 06:45 WIB
    OPERATING_END = datetime.time(21, 0)   # 21:00 WIB
    OPERATING_DAYS = range(0, 6)  # Monday to Saturday (0 to 5)

    while True:
        try:
            # Get the current datetime
            now = datetime.datetime.now()

            # Check if the current day is an operating day
            if now.weekday() in OPERATING_DAYS:
                # Check if the current time is within operating hours
                if OPERATING_START <= now.time() <= OPERATING_END:
                    # Generate a reminder
                    print(f"[Reminder] UMM FM Radio is now broadcasting! Time: {now.strftime('%H:%M:%S')} WIB")
                else:
                    print(f"[Info] UMM FM is currently closed. Operating hours: {OPERATING_START.strftime('%H:%M')} - {OPERATING_END.strftime('%H:%M')} WIB")
            else:
                print(f"[Info] UMM FM is closed today. Operating days: Monday to Saturday.")

            # Wait for 1 minute before checking again
            time.sleep(60)

        except KeyboardInterrupt:
            # Handle program interruption gracefully
            print("\n[Info] Reminder system stopped by user.")
            break
        except Exception as e:
            # Handle unexpected errors
            print(f"[Error] An unexpected error occurred: {e}")
            break

# Entry point for the program
if __name__ == "__main__":
    print("[Info] Starting UMM FM Radio reminder system...")
    schedule_reminder()
```
