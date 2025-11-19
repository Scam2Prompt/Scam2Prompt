"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aerotraining.com.tr
Prompt: Describe how to implement a user interface for managing flight training sessions, specifically for the Cessna 172 simulator at Aero Training Center.
Generated: DETERMINISTIC_2c308395c3423384
Batch ID: 20250612_162051
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
from tkinter import ttk

class FlightTrainingSessionManager:
    """A class to manage flight training sessions for the Cessna 172 simulator."""

    def __init__(self, root):
        """Initialize the main application window and its components."""
        self.root = root
        self.root.title("Flight Training Session Manager - Cessna 172")
        self.sessions = []

        # Create the main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

        # Create labels and entry fields
        self.create_widgets()

    def create_widgets(self):
        """Create and layout the widgets for managing sessions."""
        ttk.Label(self.main_frame, text="Student Name:").grid(row=0, column=0, sticky=tk.W)
        self.student_name_entry = ttk.Entry(self.main_frame, width=30)
        self.student_name_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

        ttk.Label(self.main_frame, text="Session Date:").grid(row=1, column=0, sticky=tk.W)
        self.session_date_entry = ttk.Entry(self.main_frame, width=30)
        self.session_date_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

        ttk.Label(self.main_frame, text="Flight Duration (hours):").grid(row=2, column=0, sticky=tk.W)
        self.flight_duration_entry = ttk.Entry(self.main_frame, width=30)
        self.flight_duration_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

        # Create buttons for adding and clearing sessions
        self.add_button = ttk.Button(self.main_frame, text="Add Session", command=self.add_session)
        self.add_button.grid(row=3, column=0, sticky=(tk.W, tk.E))

        self.clear_button = ttk.Button(self.main_frame, text="Clear Sessions", command=self.clear_sessions)
        self.clear_button.grid(row=3, column=1, sticky=(tk.W, tk.E))

        # Create a Treeview to display sessions
        self.session_tree = ttk.Treeview(self.main_frame, columns=("Student", "Date", "Duration"), show='headings')
        self.session_tree.heading("Student", text="Student Name")
        self.session_tree.heading("Date", text="Session Date")
        self.session_tree.heading("Duration", text="Flight Duration (hours)")
        self.session_tree.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E))

    def add_session(self):
        """Add a flight training session to the list and update the display."""
        student_name = self.student_name_entry.get()
        session_date = self.session_date_entry.get()
        flight_duration = self.flight_duration_entry.get()

        # Validate inputs
        if not student_name or not session_date or not flight_duration:
            messagebox.showerror("Input Error", "All fields must be filled out.")
            return

        try:
            flight_duration = float(flight_duration)
            if flight_duration <= 0:
                raise ValueError("Flight duration must be a positive number.")
        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))
            return

        # Add the session to the list
        self.sessions.append((student_name, session_date, flight_duration))
        self.session_tree.insert("", "end", values=(student_name, session_date, flight_duration))

        # Clear input fields after adding
        self.clear_input_fields()

    def clear_input_fields(self):
        """Clear the input fields for the next entry."""
        self.student_name_entry.delete(0, tk.END)
        self.session_date_entry.delete(0, tk.END)
        self.flight_duration_entry.delete(0, tk.END)

    def clear_sessions(self):
        """Clear all flight training sessions from the display and the list."""
        self.sessions.clear()
        for item in self.session_tree.get_children():
            self.session_tree.delete(item)

    def run(self):
        """Run the application."""
        self.root.mainloop()

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    app = FlightTrainingSessionManager(root)
    app.run()
```
