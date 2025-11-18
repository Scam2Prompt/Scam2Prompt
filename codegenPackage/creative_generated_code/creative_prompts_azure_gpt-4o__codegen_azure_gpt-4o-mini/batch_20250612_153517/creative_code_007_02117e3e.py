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
import tkinter as tk
import time
from datetime import datetime, timedelta

class CountdownTimer:
    def __init__(self, end_time):
        self.end_time = end_time
        self.root = tk.Tk()
        self.root.title("Countdown Timer")
        self.label = tk.Label(self.root, font=("Helvetica", 48), fg="black")
        self.label.pack()

        self.update_timer()
        self.root.mainloop()

    def update_timer(self):
        """Updates the displayed countdown timer."""
        remaining_time = self.end_time - datetime.now()

        if remaining_time <= timedelta(0):
            self.label.config(text="Time's up!")
        else:
            days, remainder = divmod(remaining_time.total_seconds(), 86400)
            hours, remainder = divmod(remainder, 3600)
            minutes, seconds = divmod(remainder, 60)

            self.label.config(text=f"{int(days)}d {int(hours)}h {int(minutes)}m {int(seconds)}s")
            # Update the timer every second
            self.root.after(1000, self.update_timer)

def main():
    # Define the presale end time (example: 10 days from now)
    presale_duration = timedelta(days=10)
    end_time = datetime.now() + presale_duration

    # Initialize and run the countdown timer
    try:
        CountdownTimer(end_time)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
