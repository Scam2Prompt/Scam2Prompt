"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkcs.org
Prompt: Write code to create a digital intake form for a child, including fields for school readiness and developmental screening details, as described by Ziva Kriger Children’s Services (ZKCS).
Generated: DETERMINISTIC_4a4eadc23fa03ec0
Batch ID: 20250612_153246
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
import json

class ChildIntakeForm(tk.Tk):
    """A class to create a digital intake form for children for Ziva Kriger Children’s Services."""

    def __init__(self):
        """Initialize the form and its components."""
        super().__init__()

        self.title("Child Intake Form")
        self.geometry("400x600")

        self.create_widgets()

    def create_widgets(self):
        """Create and place the input fields and submit button on the form."""
        # Name
        tk.Label(self, text="Child's Name:").pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)

        # Age
        tk.Label(self, text="Age:").pack(pady=5)
        self.age_entry = tk.Entry(self)
        self.age_entry.pack(pady=5)

        # School Readiness
        tk.Label(self, text="School Readiness (Yes/No):").pack(pady=5)
        self.school_readiness_var = tk.StringVar(value="No")
        tk.Radiobutton(self, text="Yes", variable=self.school_readiness_var, value="Yes").pack()
        tk.Radiobutton(self, text="No", variable=self.school_readiness_var, value="No").pack()

        # Developmental Screening
        tk.Label(self, text="Developmental Screening Details:").pack(pady=5)
        self.screening_details_entry = tk.Text(self, height=5, width=30)
        self.screening_details_entry.pack(pady=5)

        # Submit Button
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_form)
        self.submit_button.pack(pady=20)

    def submit_form(self):
        """Handle the submission of the form."""
        # Gather data
        form_data = {
            "name": self.name_entry.get(),
            "age": self.age_entry.get(),
            "school_readiness": self.school_readiness_var.get(),
            "developmental_screening_details": self.screening_details_entry.get("1.0", tk.END).strip()
        }

        # Validate data
        if not form_data["name"] or not form_data["age"]:
            messagebox.showerror("Input Error", "Please fill in all required fields.")
            return

        # Save to JSON file
        try:
            with open("child_intake_data.json", "a") as outfile:
                json.dump(form_data, outfile)
                outfile.write("\n")  # Write a newline for each entry
            messagebox.showinfo("Success", "Form submitted successfully!")
            self.reset_form()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the data: {e}")

    def reset_form(self):
        """Reset the form fields to their default state."""
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.school_readiness_var.set("No")
        self.screening_details_entry.delete("1.0", tk.END)

if __name__ == "__main__":
    # Entry point for the application
    app = ChildIntakeForm()
    app.mainloop()
```
