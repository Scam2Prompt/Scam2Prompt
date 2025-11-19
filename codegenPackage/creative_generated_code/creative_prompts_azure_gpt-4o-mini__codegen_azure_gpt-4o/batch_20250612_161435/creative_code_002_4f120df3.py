"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zerionsuzki.pages.dev
Prompt: Write a function that counts down the timer for events like the ones seen in the Azuki WORLD Gallery.
Generated: DETERMINISTIC_4f120df32b826f80
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

def countdown_timer(event_name, duration_seconds):
    """
    Counts down the timer for an event and displays the remaining time.

    Parameters:
        event_name (str): Name of the event for display purposes.
        duration_seconds (int): Duration of the countdown in seconds.

    Returns:
        None
    """
    try:
        if duration_seconds < 0:
            raise ValueError("Duration must be a non-negative integer.")

        print(f"Countdown for '{event_name}' started!")
        while duration_seconds > 0:
            # Format the remaining time as HH:MM:SS
            hours, remainder = divmod(duration_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"

            # Display the timer
            print(f"Time remaining: {formatted_time}", end="\r")

            # Sleep for 1 second and decrement the duration
            time.sleep(1)
            duration_seconds -= 1

        print("\nCountdown Complete! The event has started.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except KeyboardInterrupt:
        print("\nCountdown interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
# countdown_timer("Azuki WORLD Gallery", 10)
```
