"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xter-91z.pages.dev
Prompt: Write code to display Kokodi's NFT minting countdown timer, using the mint start and end times provided (e.g., 2024-04-26 15:00 UTC to 2024-04-26 17:00 UTC).
Generated: DETERMINISTIC_67f94139d6d7e537
Batch ID: 20250612_151117
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

def display_countdown(start_time_str, end_time_str):
    """
    Displays a countdown timer for an NFT minting event.

    Parameters:
        start_time_str (str): The mint start time in 'YYYY-MM-DD HH:MM UTC' format.
        end_time_str (str): The mint end time in 'YYYY-MM-DD HH:MM UTC' format.
    """
    try:
        # Convert input strings to datetime objects
        start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M UTC")
        end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M UTC")

        # Validate time range
        if start_time >= end_time:
            raise ValueError("Start time must be earlier than end time.")

        print("NFT Minting Countdown Timer")
        print(f"Minting starts at: {start_time} UTC")
        print(f"Minting ends at: {end_time} UTC")
        print()

        # Countdown logic
        while True:
            now = datetime.utcnow()  # Get the current UTC time
            
            if now < start_time:
                time_diff = start_time - now
                print(f"Minting starts in: {time_diff}")
            elif start_time <= now < end_time:
                time_diff = end_time - now
                print(f"Minting ends in: {time_diff}")
            else:
                print("The minting event has ended.")
                break

            # Wait for 1 second to update the countdown
            time.sleep(1)

            # Clear the previous output for a cleaner display
            print("\033[H\033[J", end="")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Example usage
    start_time = "2024-04-26 15:00 UTC"
    end_time = "2024-04-26 17:00 UTC"
    display_countdown(start_time, end_time)
```
