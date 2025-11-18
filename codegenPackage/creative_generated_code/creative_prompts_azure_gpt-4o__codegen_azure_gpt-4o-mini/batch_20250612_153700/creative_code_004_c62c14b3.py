"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://private-gomble.pages.dev
Prompt: Generate code for tracking and displaying an airdrop schedule, including countdown timers for events like "Heat the Balloon" and "Get your Mystery Marbles," as described on the GOMBLE website.
Generated: DETERMINISTIC_c62c14b333547678
Batch ID: 20250612_153700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tkinter as tk
from datetime import datetime, timedelta
import time

class AirdropEvent:
    """Class to represent an airdrop event with a countdown timer."""
    
    def __init__(self, name, event_time):
        """
        Initializes the AirdropEvent object.
        
        :param name: Name of the airdrop event.
        :param event_time: The scheduled time for the event (datetime).
        """
        self.name = name
        self.event_time = event_time

    def time_remaining(self):
        """Calculates the remaining time until the event."""
        now = datetime.now()
        remaining_time = self.event_time - now
        return remaining_time

    def format_time(self, remaining_time):
        """Formats the remaining time into a readable string."""
        seconds = int(remaining_time.total_seconds())
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

class AirdropApp(tk.Tk):
    """Main application class to display airdrop events and countdowns."""
    
    def __init__(self, events):
        """
        Initializes the AirdropApp.
        
        :param events: List of AirdropEvent objects.
        """
        super().__init__()
        self.title("Airdrop Schedule Tracker")
        self.geometry("300x200")
        self.events = events
        self.labels = []

        self.create_widgets()
        self.update_countdown()

    def create_widgets(self):
        """Creates the countdown display widgets."""
        for event in self.events:
            label = tk.Label(self, text="", font=("Helvetica", 14))
            label.pack(pady=10)
            self.labels.append((event, label))

    def update_countdown(self):
        """Updates the countdown timers and refreshes the display."""
        for event, label in self.labels:
            remaining_time = event.time_remaining()
            if remaining_time.total_seconds() > 0:
                time_str = event.format_time(remaining_time)
                label.config(text=f"{event.name}: {time_str}")
            else:
                label.config(text=f"{event.name}: Event has started!")

        # Reschedule countdown update
        self.after(1000, self.update_countdown)

def main():
    """Main function to start the Airdrop application."""
    try:
        # Define airdrop events
        events = [
            AirdropEvent("Heat the Balloon", datetime(2023, 10, 25, 14, 0)),
            AirdropEvent("Get your Mystery Marbles", datetime(2023, 10, 26, 16, 30)),
        ]
        
        # Start the application
        app = AirdropApp(events)
        app.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
