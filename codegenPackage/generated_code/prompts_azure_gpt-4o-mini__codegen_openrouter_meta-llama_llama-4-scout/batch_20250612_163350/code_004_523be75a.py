"""
Generated Code Metadata:
========================
Original URL: https://rahelesadeghi.ir
Prompt: Develop a simple mobile app interface that allows users to book individual or child counseling sessions, reflecting the offerings of Dr. Raheleh Sadeghi.
Generated: DETERMINISTIC_523be75affbcfe17
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class CounselingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Counseling Session Booking")

        # Create main notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        # Create frames for notebook
        self.individual_frame = tk.Frame(self.notebook)
        self.child_frame = tk.Frame(self.notebook)

        # Add frames to notebook
        self.notebook.add(self.individual_frame, text="Individual Counseling")
        self.notebook.add(self.child_frame, text="Child Counseling")

        # Individual counseling frame
        self.create_individual_frame()

        # Child counseling frame
        self.create_child_frame()

    def create_individual_frame(self):
        # Create and grid individual counseling form
        tk.Label(self.individual_frame, text="Book Individual Counseling Session").grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        tk.Label(self.individual_frame, text="Name:").grid(row=1, column=0, padx=10, pady=5)
        self.individual_name = tk.StringVar()
        tk.Entry(self.individual_frame, textvariable=self.individual_name).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.individual_frame, text="Date (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=5)
        self.individual_date = tk.StringVar()
        tk.Entry(self.individual_frame, textvariable=self.individual_date).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.individual_frame, text="Time:").grid(row=3, column=0, padx=10, pady=5)
        self.individual_time = tk.StringVar()
        tk.Entry(self.individual_frame, textvariable=self.individual_time).grid(row=3, column=1, padx=10, pady=5)

        tk.Button(self.individual_frame, text="Book Session", command=self.book_individual_session).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def create_child_frame(self):
        # Create and grid child counseling form
        tk.Label(self.child_frame, text="Book Child Counseling Session").grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        tk.Label(self.child_frame, text="Child's Name:").grid(row=1, column=0, padx=10, pady=5)
        self.child_name = tk.StringVar()
        tk.Entry(self.child_frame, textvariable=self.child_name).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.child_frame, text="Parent's Name:").grid(row=2, column=0, padx=10, pady=5)
        self.parent_name = tk.StringVar()
        tk.Entry(self.child_frame, textvariable=self.parent_name).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.child_frame, text="Date (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=5)
        self.child_date = tk.StringVar()
        tk.Entry(self.child_frame, textvariable=self.child_date).grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.child_frame, text="Time:").grid(row=4, column=0, padx=10, pady=5)
        self.child_time = tk.StringVar()
        tk.Entry(self.child_frame, textvariable=self.child_time).grid(row=4, column=1, padx=10, pady=5)

        tk.Button(self.child_frame, text="Book Session", command=self.book_child_session).grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def book_individual_session(self):
        try:
            name = self.individual_name.get()
            date = self.individual_date.get()
            time = self.individual_time.get()

            if not name or not date or not time:
                messagebox.showerror("Error", "Please fill in all fields.")
                return

            # Validate date
            datetime.strptime(date, "%Y-%m-%d")

            # Here you would add code to actually book the session (e.g., database insertion, API call)
            messagebox.showinfo("Success", f"Individual counseling session booked for {name} on {date} at {time}.")
            self.individual_name.set("")
            self.individual_date.set("")
            self.individual_time.set("")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")

    def book_child_session(self):
        try:
            child_name = self.child_name.get()
            parent_name = self.parent_name.get()
            date = self.child_date.get()
            time = self.child_time.get()

            if not child_name or not parent_name or not date or not time:
                messagebox.showerror("Error", "Please fill in all fields.")
                return

            # Validate date
            datetime.strptime(date, "%Y-%m-%d")

            # Here you would add code to actually book the session (e.g., database insertion, API call)
            messagebox.showinfo("Success", f"Child counseling session booked for {child_name} (Parent: {parent_name}) on {date} at {time}.")
            self.child_name.set("")
            self.parent_name.set("")
            self.child_date.set("")
            self.child_time.set("")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CounselingApp(root)
    root.mainloop()
```
