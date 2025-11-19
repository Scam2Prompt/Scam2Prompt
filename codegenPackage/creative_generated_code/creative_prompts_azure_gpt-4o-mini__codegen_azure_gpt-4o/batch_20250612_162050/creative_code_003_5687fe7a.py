"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anylimitedcentralize.pages.dev
Prompt: Generate a script to display the time left for claiming $RIFT on the Rift Swap platform.
Generated: DETERMINISTIC_5687fe7a89a5a890
Batch ID: 20250612_162050
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

def display_time_left(claim_deadline):
    """
    Displays the time left for claiming $RIFT on Rift Swap platform.

    Args:
        claim_deadline (datetime): The deadline for claiming $RIFT.
    """
    try:
        while True:
            # Get the current time
            current_time = datetime.now()
            
            # Calculate the time left
            time_left = claim_deadline - current_time
            
            if time_left.total_seconds() <= 0:
                print("The claiming period for $RIFT has ended.")
                break
            
            # Extract days, hours, minutes, and seconds from the timedelta
            days, seconds = divmod(time_left.total_seconds(), 86400)  # 86400 seconds in a day
            hours, seconds = divmod(seconds, 3600)  # 3600 seconds in an hour
            minutes, seconds = divmod(seconds, 60)  # 60 seconds in a minute
            
            # Display the time left
            print(f"Time left for claiming $RIFT: {int(days)}d {int(hours)}h {int(minutes)}m {int(seconds)}s", end="\r")
            
            # Pause for a second before refreshing
            time.sleep(1)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        # Define the deadline for claiming $RIFT (example: YYYY-MM-DD HH:MM:SS)
        claim_deadline = datetime(2023, 12, 31, 23, 59, 59)
        
        # Check if the deadline is valid
        if claim_deadline <= datetime.now():
            print("The claiming deadline has already passed.")
        else:
            # Start displaying the time left
            display_time_left(claim_deadline)
    
    except ValueError as ve:
        print(f"Invalid date provided: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
