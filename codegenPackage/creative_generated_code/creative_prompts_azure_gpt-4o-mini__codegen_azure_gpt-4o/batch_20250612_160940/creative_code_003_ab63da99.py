"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onchaincoin-presale.pages.dev
Prompt: Develop a script that checks the presale status and displays a countdown timer for the Onchain Coin presale.
Generated: DETERMINISTIC_ab63da996aeccf2f
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from datetime import datetime, timedelta

def check_presale_status(start_time, end_time):
    """
    Checks if the presale is active, upcoming, or has ended.
    
    Parameters:
        start_time (datetime): The start time of the presale.
        end_time (datetime): The end time of the presale.
    
    Returns:
        str: Status of the presale ("upcoming", "active", "ended").
    """
    current_time = datetime.now()

    if current_time < start_time:
        return "upcoming"
    elif start_time <= current_time <= end_time:
        return "active"
    else:
        return "ended"

def display_countdown(target_time):
    """
    Displays a countdown timer to the target time.
    
    Parameters:
        target_time (datetime): The time to count down to.
    """
    while True:
        current_time = datetime.now()
        remaining_time = target_time - current_time

        if remaining_time.total_seconds() <= 0:
            print("Countdown complete!")
            break

        # Format remaining time as hours, minutes, seconds
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        print(f"Countdown: {remaining_time.days} days, {hours:02}:{minutes:02}:{seconds:02}", end="\r")
        time.sleep(1)

def main():
    """
    Main function to check presale status and display countdown if needed.
    """
    try:
        # Define presale start and end times (example values)
        presale_start = datetime(2023, 11, 1, 12, 0, 0)  # YYYY, MM, DD, HH, MM, SS
        presale_end = datetime(2023, 11, 10, 12, 0, 0)

        # Check presale status
        status = check_presale_status(presale_start, presale_end)
        
        if status == "upcoming":
            print("The Onchain Coin presale is upcoming.")
            print("Countdown to presale start:")
            display_countdown(presale_start)
        elif status == "active":
            print("The Onchain Coin presale is active. Get your coins now!")
        else:
            print("The Onchain Coin presale has ended. Stay tuned for future opportunities.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
