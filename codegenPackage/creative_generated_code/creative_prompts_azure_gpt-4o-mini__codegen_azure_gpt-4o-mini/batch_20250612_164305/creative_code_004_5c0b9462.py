"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testopolistomarta.pages.dev
Prompt: How can I design a user interface that displays daily rewards and check-in status, taking cues from the Notcoin x Dogs Dogs Notcoin page?
Generated: DETERMINISTIC_5c0b94627d5c6400
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class DailyRewardsApp:
    def __init__(self, master):
        """Initialize the main application window."""
        self.master = master
        self.master.title("Daily Rewards and Check-in Status")
        self.master.geometry("400x300")

        # Initialize variables
        self.last_check_in_date = None

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        """Create and lay out the UI elements."""
        # Title label
        self.title_label = tk.Label(self.master, text="Daily Rewards", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        # Rewards label
        self.rewards_label = tk.Label(self.master, text="You have earned: 0 Coins", font=("Helvetica", 14))
        self.rewards_label.pack(pady=10)

        # Check-in button
        self.check_in_button = tk.Button(self.master, text="Check-in", command=self.check_in)
        self.check_in_button.pack(pady=20)

        # Check-in status label
        self.status_label = tk.Label(self.master, text="", font=("Helvetica", 12))
        self.status_label.pack(pady=5)

        # Load previous check-in date if available
        self.load_check_in_status()

    def load_check_in_status(self):
        """Load the last check-in date from storage."""
        try:
            with open("last_check_in.txt", "r") as file:
                self.last_check_in_date = datetime.strptime(file.read().strip(), "%Y-%m-%d")
                self.update_status_label()
        except FileNotFoundError:
            # File does not exist, no previous check-in
            self.last_check_in_date = None
        except ValueError:
            # Handle potential value error from wrong date format
            self.last_check_in_date = None

    def update_status_label(self):
        """Update the status label based on the last check-in date."""
        if self.last_check_in_date is None:
            self.status_label.config(text="Status: Not Checked-in Yet")
        else:
            self.status_label.config(text=f"Status: Last Checked-in on {self.last_check_in_date.strftime('%Y-%m-%d')}")

    def check_in(self):
        """Handle user check-in and update rewards."""
        today = datetime.today().date()
        if self.last_check_in_date is None or self.last_check_in_date.date() < today:
            # Update rewards and check-in date
            self.last_check_in_date = today
            self.update_rewards()
            self.save_check_in_status()
            messagebox.showinfo("Check-in Successful", "You have successfully checked in and earned rewards!")
        else:
            # User has already checked in today
            messagebox.showwarning("Check-in Warning", "You have already checked in today.")

        self.update_status_label()

    def update_rewards(self):
        """Update the rewards label based on the check-in."""
        # For simplicity, increase rewards by 10 coins per check-in
        current_rewards = int(self.rewards_label.cget("text").split(": ")[1].split(" ")[0])
        self.rewards_label.config(text=f"You have earned: {current_rewards + 10} Coins")

    def save_check_in_status(self):
        """Save the last check-in date to storage."""
        with open("last_check_in.txt", "w") as file:
            file.write(self.last_check_in_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    root = tk.Tk()
    app = DailyRewardsApp(root)
    root.mainloop()
```

Note: This code snippet creates a basic user interface for tracking daily rewards and check-in status, with proper error handling and usability considerations. The data persistence is handled through a text file.
