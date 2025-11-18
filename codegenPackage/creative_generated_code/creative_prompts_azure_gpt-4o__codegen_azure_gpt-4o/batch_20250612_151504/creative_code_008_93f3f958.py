"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.himsdemo.bste.live
Prompt: Generate code to display VAT registration details (`VAT Registration No.:310934547900003`) and license information in a healthcare management system interface.
Generated: DETERMINISTIC_93f3f9584af5c678
Batch ID: 20250612_151504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules
import tkinter as tk
from tkinter import messagebox


def display_license_info():
    """
    Function to display VAT registration details and license information in a popup.
    """
    try:
        # Define VAT registration number and license information
        vat_registration_number = "310934547900003"
        license_information = "Healthcare Management System Version 1.0\nLicensed to XYZ Healthcare Pvt Ltd"

        # Display the information in a popup window
        messagebox.showinfo(
            "License Information",
            f"VAT Registration No.: {vat_registration_number}\n\n{license_information}"
        )
    except Exception as e:
        # Handle unexpected errors
        messagebox.showerror("Error", f"An error occurred while displaying the information: {str(e)}")


# Create the main application window
def create_app():
    """
    Function to create the main interface of the Healthcare Management System.
    """
    # Initialize the Tkinter application
    app = tk.Tk()
    app.title("Healthcare Management System")
    app.geometry("400x300")  # Set window size
    app.resizable(False, False)  # Disable resizing

    # Add a title label
    title_label = tk.Label(app, text="Healthcare Management System", font=("Arial", 16, "bold"))
    title_label.pack(pady=20)

    # Add a button to display VAT and license information
    license_button = tk.Button(
        app,
        text="View License Information",
        font=("Arial", 12),
        command=display_license_info,
        bg="#4CAF50",
        fg="white"
    )
    license_button.pack(pady=10)

    # Add a footer label
    footer_label = tk.Label(app, text="© XYZ Healthcare Pvt Ltd", font=("Arial", 10))
    footer_label.pack(side=tk.BOTTOM, pady=10)

    # Run the application event loop
    app.mainloop()


# Entry point of the program
if __name__ == "__main__":
    create_app()
```
