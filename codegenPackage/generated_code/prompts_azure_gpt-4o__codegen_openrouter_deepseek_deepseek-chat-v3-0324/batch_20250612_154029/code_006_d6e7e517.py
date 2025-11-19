"""
Generated Code Metadata:
========================
Original URL: https://wynn-seven.vercel.app
Prompt: Create a program to display a countdown timer for campaigns, like the time left for the $WYNN Hunt, using JavaScript or Python.
Generated: DETERMINISTIC_d6e7e5177c789f4b
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import sys
from datetime import datetime, timedelta

class CountdownTimer:
    """
    A countdown timer for campaigns that displays the time left until a specified end date.
    """
    
    def __init__(self, end_date):
        """
        Initialize the timer with the end date of the campaign.
        
        Args:
            end_date (str): The end date in 'YYYY-MM-DD HH:MM:SS' format.
        """
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
    
    def calculate_time_left(self):
        """
        Calculate the time remaining until the end date.
        
        Returns:
            timedelta: The time remaining until the end date.
        """
        current_time = datetime.now()
        return self.end_date - current_time
    
    def display_time_left(self):
        """
        Continuously display the time left until the end date, updating every second.
        """
        try:
            while True:
                time_left = self.calculate_time_left()
                if time_left.total_seconds() <= 0:
                    print("The campaign has ended!")
                    break
                
                days = time_left.days
                hours, remainder = divmod(time_left.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                
                sys.stdout.write(
                    f"\rTime left: {days}d {hours}h {minutes}m {seconds}s"
                )
                sys.stdout.flush()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nTimer stopped by user.")
    
    @staticmethod
    def validate_date(date_str):
        """
        Validate the input date format.
        
        Args:
            date_str (str): The date string to validate.
            
        Returns:
            bool: True if the date is valid, False otherwise.
        """
        try:
            datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
            return True
        except ValueError:
            return False

if __name__ == "__main__":
    print("Campaign Countdown Timer")
    print("-----------------------")
    
    while True:
        end_date = input("Enter the campaign end date (YYYY-MM-DD HH:MM:SS): ")
        if CountdownTimer.validate_date(end_date):
            break
        print("Invalid date format. Please try again.")
    
    timer = CountdownTimer(end_date)
    timer.display_time_left()
```
