"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://otherside-lb1.pages.dev
Prompt: Develop a script to display a countdown timer for the "Project Dragon - Event 1" registration deadline (July 27th, 2024, 12pm ET) and dynamically update the bonus allocation for early registrants as described on the Otherside site.
Generated: DETERMINISTIC_87e31fc025784ff5
Batch ID: 20250612_151333
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

def calculate_bonus(days_left):
    """
    Calculates bonus allocation based on the number of days left until the registration deadline.
    Bonus tiers:
    - 0-7 days: 5% bonus
    - 8-21 days: 10% bonus
    - 22-60 days: 15% bonus
    - >60 days: 20% bonus
    """
    if days_left <= 7:
        return "5%"
    elif days_left <= 21:
        return "10%"
    elif days_left <= 60:
        return "15%"
    else:
        return "20%"

def display_countdown_and_bonus(deadline):
    """
    Displays a countdown timer to the registration deadline and dynamically updates
    the bonus allocation based on the remaining time.
    """
    while True:
        current_time = datetime.datetime.now()
        
        # Calculate the time remaining
        time_left = deadline - current_time
        days_left = time_left.days
        
        # If the deadline has passed, stop the timer
        if days_left < 0:
            print("Registration deadline has passed.")
            break
        
        # Calculate hours, minutes, and seconds remaining
        hours_left = time_left.seconds // 3600
        minutes_left = (time_left.seconds % 3600) // 60
        seconds_left = time_left.seconds % 60
        
        # Calculate the bonus for early registrants
        bonus = calculate_bonus(days_left)
        
        # Display countdown and bonus
        print(f"Time remaining: {days_left} days, {hours_left} hours, {minutes_left} minutes, {seconds_left} seconds")
        print(f"Current Bonus Allocation: {bonus}")
        
        # Update every second
        time.sleep(1)

if __name__ == "__main__":
    try:
        # Define the registration deadline (July 27th, 2024, 12pm ET)
        registration_deadline = datetime.datetime(2024, 7, 27, 12, 0)
        
        print("Countdown Timer for 'Project Dragon - Event 1' Registration Deadline")
        print("---------------------------------------------------------------")
        
        # Start the countdown timer
        display_countdown_and_bonus(registration_deadline)
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
```
