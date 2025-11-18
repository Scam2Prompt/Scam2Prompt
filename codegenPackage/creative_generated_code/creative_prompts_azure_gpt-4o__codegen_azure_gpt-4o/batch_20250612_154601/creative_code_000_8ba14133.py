"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://henio.digital
Prompt: Write a script to calculate the countdown timer for a cryptocurrency airdrop, similar to the one displayed on the HENLO Airdrop webpage.
Generated: DETERMINISTIC_8ba1413316f2ea2e
Batch ID: 20250612_154601
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

def calculate_countdown(end_time):
    """
    Function to calculate the countdown timer for an event.
    
    Args:
        end_time (datetime): The end time of the event.
        
    Returns:
        str: A formatted string representing the time remaining in days, hours, minutes, and seconds.
    """
    # Get current time
    current_time = datetime.now()

    # Calculate the time difference
    time_difference = end_time - current_time

    if time_difference.total_seconds() <= 0:
        return "Airdrop has ended!"

    # Extract days, hours, minutes, and seconds
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Format the countdown string
    return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds remaining."

def main():
    """
    Main function to run the countdown timer script.
    """
    try:
        # Define the end time for the airdrop event (example: Oct 15, 2023 at 23:59:59)
        end_time = datetime(2023, 10, 15, 23, 59, 59)

        # Loop to continuously display the countdown timer
        while True:
            countdown = calculate_countdown(end_time)
            print(countdown, end="\r", flush=True)

            # Break the loop if the airdrop has ended
            if "ended" in countdown:
                break
            
            # Update every second
            time.sleep(1)
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
