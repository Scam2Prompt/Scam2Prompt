"""
Generated Code Metadata:
========================
Original URL: https://sweans360.com
Prompt: Write a Python script to display a "Site Under Maintenance" message with a scheduled maintenance timer.
Generated: DETERMINISTIC_de54cb708177b4af
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import time
import tkinter as tk
from threading import Thread

class SiteUnderMaintenance:
    def __init__(self, maintenance_time):
        self.maintenance_time = maintenance_time
        self.root = tk.Tk()
        self.root.title("Site Under Maintenance")

    def display_maintenance_message(self):
        self.label = tk.Label(self.root, text="Site Under Maintenance", font=('Helvetica', 24))
        self.label.pack()

        self.time_label = tk.Label(self.root, text="", font=('Helvetica', 48))
        self.time_label.pack()

        self.update_timer()

    def update_timer(self):
        time_diff = self.maintenance_time - datetime.datetime.now()
        if time_diff.total_seconds() < 0:
            self.time_label['text'] = "Site is back online!"
        else:
            days = time_diff.days
            hours, remainder = divmod(time_diff.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.time_label['text'] = f"{days} days, {hours:02}:{minutes:02}:{seconds:02}"
            self.root.after(1000, self.update_timer)

    def run(self):
        self.display_maintenance_message()
        self.root.mainloop()

def main():
    try:
        # Schedule maintenance time (year, month, day, hour, minute, second)
        maintenance_time = datetime.datetime(2024, 9, 17, 10, 0, 0)
        site = SiteUnderMaintenance(maintenance_time)
        site.run()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
