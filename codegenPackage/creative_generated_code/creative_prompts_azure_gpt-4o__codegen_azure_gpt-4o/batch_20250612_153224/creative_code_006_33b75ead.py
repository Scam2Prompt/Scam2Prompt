"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crestagile.com
Prompt: Develop a Python-based dashboard for tracking Agile certifications and course progress, as outlined in CrestAgile's offerings.
Generated: DETERMINISTIC_33b75eadc7b49409
Batch ID: 20250612_153224
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

# Define a class for the Agile Certification Dashboard
class AgileDashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agile Certification & Course Progress Tracker")
        self.root.geometry("800x600")

        # Initialize data structures for certifications and course progress
        self.certifications = {
            "Certified Scrum Master (CSM)": False,
            "Certified Scrum Product Owner (CSPO)": False,
            "Agile Certified Practitioner (ACP)": False,
            "Certified SAFe Agilist": False
        }
        self.course_progress = {
            "Scrum Fundamentals": 0,
            "Kanban Basics": 0,
            "SAFe Framework Overview": 0,
            "Advanced Agile Concepts": 0
        }

        # Create the UI components
        self.create_ui()

    def create_ui(self):
        # Create a frame for certifications
        certification_frame = tk.LabelFrame(self.root, text="Certifications", padx=10, pady=10)
        certification_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        # Add checkboxes for certifications
        self.certification_vars = {}
        for cert in self.certifications:
            var = tk.BooleanVar(value=self.certifications[cert])
            checkbox = tk.Checkbutton(certification_frame, text=cert, variable=var, command=self.update_certifications)
            checkbox.pack(anchor="w")
            self.certification_vars[cert] = var

        # Create a frame for course progress
        course_frame = tk.LabelFrame(self.root, text="Course Progress", padx=10, pady=10)
        course_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        # Add sliders for course progress
        self.course_vars = {}
        for course in self.course_progress:
            progress_label = tk.Label(course_frame, text=course)
            progress_label.pack(anchor="w")
            var = tk.IntVar(value=self.course_progress[course])
            slider = tk.Scale(course_frame, from_=0, to=100, orient="horizontal", variable=var, command=self.update_course_progress)
            slider.pack(fill="x", padx=10, pady=5)
            self.course_vars[course] = var

        # Add a button to display overall status
        status_button = tk.Button(self.root, text="Show Status", command=self.show_status)
        status_button.pack(pady=10)

    def update_certifications(self):
        """Update the certifications dictionary based on checkbox states."""
        for cert, var in self.certification_vars.items():
            self.certifications[cert] = var.get()

    def update_course_progress(self, value):
        """Update the course progress dictionary based on slider values."""
        for course, var in self.course_vars.items():
            self.course_progress[course] = var.get()

    def show_status(self):
        """Display the current certifications and course progress in a message box."""
        certs = "\n".join([f"{cert}: {'Completed' if completed else 'Not Completed'}" for cert, completed in self.certifications.items()])
        courses = "\n".join([f"{course}: {progress}% Complete" for course, progress in self.course_progress.items()])
        status_message = f"Certifications:\n{certs}\n\nCourse Progress:\n{courses}"
        messagebox.showinfo("Dashboard Status", status_message)


# Main application entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = AgileDashboardApp(root)
    root.mainloop()
```
