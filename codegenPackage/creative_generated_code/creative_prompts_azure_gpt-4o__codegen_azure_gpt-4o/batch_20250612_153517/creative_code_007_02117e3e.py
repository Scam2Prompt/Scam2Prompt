"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-scapesmania.pages.dev
Prompt: Generate code to display a countdown timer for the presale period, showing days, hours, minutes, and seconds remaining until the price increase.
Generated: DETERMINISTIC_02117e3e18447cf7
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import time

def countdown_timer(end_time):
    """
    Displays a countdown timer for the given end_time.

    Parameters:
        end_time (datetime): The target time for the countdown to end.
    """
    try:
        while True:
            # Get the current time
            current_time = datetime.now()
            
            # Calculate the time remaining
            time_remaining = end_time - current_time
            
            # Break the loop if the countdown has ended
            if time_remaining.total_seconds() <= 0:
                print("Presale period has ended! 🚀")
                break
            
            # Extract days, hours, minutes, and seconds from the remaining time
            days = time_remaining.days
            hours, remainder = divmod(time_remaining.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            
            # Display the countdown timer
            print(f"Countdown: {days} days, {hours:02d}:{minutes:02d}:{seconds:02d}", end="\r")
            
            # Wait for 1 second before updating
            time.sleep(1)
    
    except KeyboardInterrupt:
        # Handle keyboard interruption gracefully
        print("\nCountdown timer interrupted.")
    except Exception as e:
        # Catch and display unexpected errors
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Define the target end time for the presale period
    presale_end_time = datetime.now() + timedelta(days=3, hours=10, minutes=30, seconds=15)
    
    print(f"Presale countdown starts now! Ends at: {presale_end_time}")
    # Start the countdown timer
    countdown_timer(presale_end_time)
```
