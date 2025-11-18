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
import time
import datetime
import tkinter as tk
from tkinter import messagebox

# Constants
DEADLINE = datetime.datetime(2024, 7, 27, 12, 0)  # Registration deadline
BONUS_ALLOCATION = {
    30: "10% bonus",
    20: "5% bonus",
    10: "2% bonus",
    0: "No bonus"
}

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Project Dragon - Event 1 Countdown Timer")
        
        self.time_label = tk.Label(root, font=("Helvetica", 48), fg="blue")
        self.time_label.pack(pady=20)

        self.bonus_label = tk.Label(root, font=("Helvetica", 24), fg="green")
        self.bonus_label.pack(pady=20)

        self.update_timer()  # Start the countdown

    def update_timer(self):
        """Update the countdown timer and bonus allocation."""
        now = datetime.datetime.now()
        remaining_time = DEADLINE - now
        
        # Check if the deadline has been reached
        if remaining_time.total_seconds() <= 0:
            self.time_label.config(text="Registration Closed")
            self.bonus_label.config(text="")
            return
        
        # Calculate days, hours, minutes, and seconds
        days, remainder = divmod(remaining_time.total_seconds(), 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        # Format and display the remaining time
        time_str = f"{int(days)}d {int(hours)}h {int(minutes)}m {int(seconds)}s"
        self.time_label.config(text=time_str)

        # Update the bonus allocation based on remaining days
        self.update_bonus(int(days))
        
        # Schedule the next update after 1 second
        self.root.after(1000, self.update_timer)

    def update_bonus(self, days_remaining):
        """Update the bonus allocation based on days remaining."""
        for threshold, bonus in sorted(BONUS_ALLOCATION.items()):
            if days_remaining >= threshold:
                self.bonus_label.config(text=f"Early Registration Bonus: {bonus}")
                break

def main():
    """Main function to run the countdown timer application."""
    root = tk.Tk()
    
    try:
        CountdownTimer(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
