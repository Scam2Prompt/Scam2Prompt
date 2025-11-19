"""
Generated Code Metadata:
========================
Original URL: https://sala-events.co.il
Prompt: Outline a user interface design for an event management application that showcases the unique features of DCITY, such as its capacity for both small and large events.
Generated: DETERMINISTIC_4958cce16183426d
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries for GUI development
import tkinter as tk
from tkinter import messagebox

class EventManagementApp:
    def __init__(self, master):
        """Initialize the main application window."""
        self.master = master
        master.title("DCITY Event Management")

        # Create a title label
        self.title_label = tk.Label(master, text="DCITY Event Management", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        # Create a frame for event details
        self.event_frame = tk.Frame(master)
        self.event_frame.pack(pady=10)

        # Event name input
        self.event_name_label = tk.Label(self.event_frame, text="Event Name:")
        self.event_name_label.grid(row=0, column=0)
        self.event_name_entry = tk.Entry(self.event_frame)
        self.event_name_entry.grid(row=0, column=1)

        # Event type selection
        self.event_type_label = tk.Label(self.event_frame, text="Event Type:")
        self.event_type_label.grid(row=1, column=0)
        self.event_type_var = tk.StringVar(value="Small")
        self.event_type_small = tk.Radiobutton(self.event_frame, text="Small", variable=self.event_type_var, value="Small")
        self.event_type_large = tk.Radiobutton(self.event_frame, text="Large", variable=self.event_type_var, value="Large")
        self.event_type_small.grid(row=1, column=1)
        self.event_type_large.grid(row=1, column=2)

        # Event capacity input
        self.event_capacity_label = tk.Label(self.event_frame, text="Event Capacity:")
        self.event_capacity_label.grid(row=2, column=0)
        self.event_capacity_entry = tk.Entry(self.event_frame)
        self.event_capacity_entry.grid(row=2, column=1)

        # Create a button to submit event details
        self.submit_button = tk.Button(master, text="Submit Event", command=self.submit_event)
        self.submit_button.pack(pady=10)

    def submit_event(self):
        """Handle the event submission."""
        event_name = self.event_name_entry.get()
        event_type = self.event_type_var.get()
        event_capacity = self.event_capacity_entry.get()

        # Validate input
        if not event_name or not event_capacity.isdigit():
            messagebox.showerror("Input Error", "Please enter a valid event name and capacity.")
            return

        # Process the event (this is where you would add your event handling logic)
        event_capacity = int(event_capacity)
        messagebox.showinfo("Event Submitted", f"Event '{event_name}' of type '{event_type}' with capacity {event_capacity} has been submitted.")

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    app = EventManagementApp(root)
    root.mainloop()
```
