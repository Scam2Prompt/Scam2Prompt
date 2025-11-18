"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-aevo2.pages.dev
Prompt: Create a script to display the countdown for "END OF FARM BOOST" in the format 7D 8H 15M 45S, as described on the Aevo webpage.
Generated: DETERMINISTIC_37597d62145a4623
Batch ID: 20250612_152109
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

def display_countdown(target_time):
    """
    Displays a countdown in the format 'XD YH ZM WS', where:
    X = Days
    Y = Hours
    Z = Minutes
    W = Seconds

    Args:
        target_time (datetime): The target end time for the countdown.
    """
    try:
        while True:
            # Calculate the remaining time
            now = datetime.now()
            remaining_time = target_time - now
            
            if remaining_time.total_seconds() <= 0:
                print("END OF FARM BOOST")
                break
            
            # Extract days, hours, minutes, and seconds
            days = remaining_time.days
            hours, remainder = divmod(remaining_time.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            
            # Format and display countdown
            countdown_str = f"{days}D {hours}H {minutes}M {seconds}S"
            print(countdown_str, end='\r')  # Print on the same line
            
            time.sleep(1)  # Wait for 1 second before updating
            
    except KeyboardInterrupt:
        print("\nCountdown interrupted.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Define the target end time for the countdown
    # Example: 7 days from the current time
    target_end_time = datetime.now() + timedelta(days=7, hours=8, minutes=15, seconds=45)

    print("Starting countdown to END OF FARM BOOST...")
    display_countdown(target_end_time)
```
