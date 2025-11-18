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

# Function to handle form submission
def submit_form():
    try:
        # Collecting input data
        child_name = entry_child_name.get()
        age = entry_age.get()
        parent_name = entry_parent_name.get()
        phone_number = entry_phone_number.get()
        school_readiness = entry_school_readiness.get("1.0", tk.END).strip()
        developmental_screening = entry_developmental_screening.get("1.0", tk.END).strip()

        # Input validation
        if not child_name or not age or not parent_name or not phone_number or not school_readiness or not developmental_screening:
            raise ValueError("All fields are required.")

        # Simulate saving data (could replace with saving to a database/file)
        # For now, just show a confirmation message
        messagebox.showinfo("Success", "Form submitted successfully!")
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


# Function to reset the form
def reset_form():
    entry_child_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_parent_name.delete(0, tk.END)
    entry_phone_number.delete(0, tk.END)
    entry_school_readiness.delete("1.0", tk.END)
    entry_developmental_screening.delete("1.0", tk.END)

# Create main application window
app = tk.Tk()
app.title("Child Intake Form - ZKCS")
app.geometry("450x600")

# Create and place form labels and fields
tk.Label(app, text="Child Name:").pack(anchor="w", pady=5)
entry_child_name = tk.Entry(app, width=50)
entry_child_name.pack(pady=5)

tk.Label(app, text="Age:").pack(anchor="w", pady=5)
entry_age = tk.Entry(app, width=50)
entry_age.pack(pady=5)

tk.Label(app, text="Parent/Guardian Name:").pack(anchor="w", pady=5)
entry_parent_name = tk.Entry(app, width=50)
entry_parent_name.pack(pady=5)

tk.Label(app, text="Phone Number:").pack(anchor="w", pady=5)
entry_phone_number = tk.Entry(app, width=50)
entry_phone_number.pack(pady=5)

tk.Label(app, text="School Readiness Details:").pack(anchor="w", pady=5)
entry_school_readiness = tk.Text(app, width=50, height=5)
entry_school_readiness.pack(pady=5)

tk.Label(app, text="Developmental Screening Details:").pack(anchor="w", pady=5)
entry_developmental_screening = tk.Text(app, width=50, height=5)
entry_developmental_screening.pack(pady=5)

# Create and place action buttons
btn_submit = tk.Button(app, text="Submit", command=submit_form, bg="green", fg="white", width=15)
btn_submit.pack(pady=10)

btn_reset = tk.Button(app, text="Reset", command=reset_form, bg="red", fg="white", width=15)
btn_reset.pack(pady=10)

# Start the application loop
app.mainloop()
```
