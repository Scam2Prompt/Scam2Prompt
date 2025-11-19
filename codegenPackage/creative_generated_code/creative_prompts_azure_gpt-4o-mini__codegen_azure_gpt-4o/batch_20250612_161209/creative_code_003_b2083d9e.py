"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starmissteenindia.com
Prompt: How can I design a user interface for a registration page that captures details like height, weight, and audition city for a competition like Star Miss Teen India 2025?
Generated: DETERMINISTIC_b2083d9e1b7806b4
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox

# Function to handle form submission
def submit_form():
    try:
        # Extract input values
        height = height_var.get()
        weight = weight_var.get()
        audition_city = audition_city_var.get()

        # Basic validation
        if not height or not weight or not audition_city:
            raise ValueError("All fields are required.")
        
        if not height.isdigit() or not weight.isdigit():
            raise ValueError("Height and Weight must be numeric values.")

        # Display success message
        messagebox.showinfo("Success", "Registration submitted successfully!")
        
        # Clear the fields after submission
        height_var.set("")
        weight_var.set("")
        audition_city_var.set("")

    except ValueError as e:
        # Display error message for invalid inputs
        messagebox.showerror("Error", str(e))
    except Exception as e:
        # Display generic error message
        messagebox.showerror("Error", "An unexpected error occurred.")

# Initialize the Tkinter application window
app = Tk()
app.title("Star Miss Teen India 2025 Registration")
app.geometry("400x300")  # Set the window size

# Define StringVar variables for capturing user input
height_var = StringVar()
weight_var = StringVar()
audition_city_var = StringVar()

# Create and place UI components
Label(app, text="Registration Form", font=("Arial", 16)).pack(pady=10)

# Height input
Label(app, text="Height (cm):", font=("Arial", 12)).pack(pady=5)
Entry(app, textvariable=height_var, width=30).pack()

# Weight input
Label(app, text="Weight (kg):", font=("Arial", 12)).pack(pady=5)
Entry(app, textvariable=weight_var, width=30).pack()

# Audition City input
Label(app, text="Audition City:", font=("Arial", 12)).pack(pady=5)
Entry(app, textvariable=audition_city_var, width=30).pack()

# Submit button
Button(app, text="Submit", font=("Arial", 12), command=submit_form).pack(pady=20)

# Run the application
app.mainloop()
```
