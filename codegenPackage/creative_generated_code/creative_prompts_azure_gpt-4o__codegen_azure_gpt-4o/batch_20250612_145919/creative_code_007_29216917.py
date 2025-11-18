"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unstake-myblend.pages.dev
Prompt: Create a script to display countdown timers for staking durations (e.g., 10 days) and reward expiration dates on a platform like "Unstake | Blend."
Generated: DETERMINISTIC_292169178375bbc5
Batch ID: 20250612_145919
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

def display_countdown(duration_seconds, label):
    """
    Display a countdown timer for a given duration in seconds with a label.
    :param duration_seconds: Total duration in seconds for the countdown.
    :param label: A label to describe the countdown.
    """
    try:
        if duration_seconds <= 0:
            raise ValueError("Duration must be greater than zero.")
        
        print(f"{label} Countdown Starts:")
        while duration_seconds > 0:
            # Calculate remaining time components
            days = duration_seconds // 86400
            hours = (duration_seconds % 86400) // 3600
            minutes = (duration_seconds % 3600) // 60
            seconds = duration_seconds % 60
            
            # Clear the screen (optional, for better readability in terminal)
            print("\033[H\033[J", end="")
            
            # Display the countdown timer
            print(f"{label}: {days} Days, {hours} Hours, {minutes} Minutes, {seconds} Seconds remaining.")
            
            # Wait for 1 second before updating
            time.sleep(1)
            
            # Decrease countdown time
            duration_seconds -= 1
        
        # Countdown completion message
        print(f"{label} has ended!")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    """
    Main function to demonstrate countdown timers for staking durations and reward expirations.
    """
    try:
        # Example: Staking duration countdown (e.g., 10 days)
        staking_duration_seconds = 10 * 24 * 3600  # 10 days in seconds
        display_countdown(staking_duration_seconds, "Staking Duration")
        
        # Example: Reward expiration countdown (e.g., 2 days)
        reward_expiration_seconds = 2 * 24 * 3600  # 2 days in seconds
        display_countdown(reward_expiration_seconds, "Reward Expiration")
    
    except Exception as e:
        print(f"An error occurred in the main function: {e}")


if __name__ == "__main__":
    main()
```
