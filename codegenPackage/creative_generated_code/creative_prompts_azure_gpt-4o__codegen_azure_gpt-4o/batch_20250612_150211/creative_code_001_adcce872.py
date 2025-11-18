"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ye-8lg.pages.dev
Prompt: Generate code to implement a presale countdown timer for a cryptocurrency token sale, similar to the $YE Token presale page.
Generated: DETERMINISTIC_adcce872f8dedb61
Batch ID: 20250612_150211
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


class PreSaleCountdown:
    def __init__(self, end_time):
        """
        Initializes the countdown timer with an end time.

        :param end_time: A string in "YYYY-MM-DD HH:MM:SS" format representing the presale end time.
        """
        try:
            self.end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        except ValueError as ve:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD HH:MM:SS'.") from ve

    def get_time_remaining(self):
        """
        Calculates the time remaining until the presale ends.

        :return: A dictionary with days, hours, minutes, and seconds remaining.
        """
        now = datetime.now()
        if now >= self.end_time:
            return {"days": 0, "hours": 0, "minutes": 0, "seconds": 0}

        delta = self.end_time - now
        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        return {"days": days, "hours": hours, "minutes": minutes, "seconds": seconds}

    def start_countdown(self):
        """
        Starts the countdown timer and updates the remaining time every second.

        Prints the countdown to the console in real-time.
        """
        while True:
            time_remaining = self.get_time_remaining()
            if time_remaining["days"] == 0 and time_remaining["hours"] == 0 and \
               time_remaining["minutes"] == 0 and time_remaining["seconds"] == 0:
                print("Presale has ended!")
                break

            # Display the countdown timer
            print(
                f"Time Remaining: {time_remaining['days']} Days, "
                f"{time_remaining['hours']:02} Hours, "
                f"{time_remaining['minutes']:02} Minutes, "
                f"{time_remaining['seconds']:02} Seconds"
            )

            # Wait for 1 second before updating the countdown
            time.sleep(1)


if __name__ == "__main__":
    try:
        # Example: Set presale end time to 1 day from now
        end_time = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
        countdown = PreSaleCountdown(end_time)

        print(f"Presale ends on: {end_time}")
        countdown.start_countdown()
    except Exception as e:
        print(f"Error: {e}")
```
