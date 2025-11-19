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
import tkinter as tk
from tkinter import messagebox

# Main application class
class EventManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DCITY Event Management")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # Create the main UI layout
        self.create_main_ui()

    def create_main_ui(self):
        # Header
        header = tk.Label(self.root, text="Welcome to DCITY Event Management", font=("Arial", 20, "bold"))
        header.pack(pady=20)

        # Event size selection
        size_frame = tk.Frame(self.root)
        size_frame.pack(pady=10)

        tk.Label(size_frame, text="Select Event Size:", font=("Arial", 14)).grid(row=0, column=0, padx=10)
        self.event_size_var = tk.StringVar(value="small")
        tk.Radiobutton(size_frame, text="Small Event", variable=self.event_size_var, value="small", font=("Arial", 12)).grid(row=0, column=1, padx=10)
        tk.Radiobutton(size_frame, text="Large Event", variable=self.event_size_var, value="large", font=("Arial", 12)).grid(row=0, column=2, padx=10)

        # Event details form
        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=20)

        tk.Label(form_frame, text="Event Name:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.event_name_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.event_name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Date (YYYY-MM-DD):", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.event_date_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.event_date_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Number of Attendees:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.attendees_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.attendees_entry.grid(row=2, column=1, padx=10, pady=5)

        # Submit button
        submit_button = tk.Button(self.root, text="Submit Event", font=("Arial", 14), bg="blue", fg="white", command=self.submit_event)
        submit_button.pack(pady=20)

        # Footer
        footer = tk.Label(self.root, text="DCITY: Your Partner for Events of All Sizes", font=("Arial", 12, "italic"))
        footer.pack(side="bottom", pady=10)

    def submit_event(self):
        # Retrieve form data
        event_name = self.event_name_entry.get().strip()
        event_date = self.event_date_entry.get().strip()
        attendees = self.attendees_entry.get().strip()
        event_size = self.event_size_var.get()

        # Validate form data
        if not event_name or not event_date or not attendees:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            attendees = int(attendees)
            if attendees <= 0:
                raise ValueError("Number of attendees must be positive.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid number of attendees: {e}")
            return

        # Display success message
        messagebox.showinfo("Success", f"Event '{event_name}' ({event_size.capitalize()} Event) scheduled for {event_date} with {attendees} attendees.")
        self.clear_form()

    def clear_form(self):
        # Clear form fields
        self.event_name_entry.delete(0, tk.END)
        self.event_date_entry.delete(0, tk.END)
        self.attendees_entry.delete(0, tk.END)
        self.event_size_var.set("small")


# Main entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = EventManagementApp(root)
    root.mainloop()
```
