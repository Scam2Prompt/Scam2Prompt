"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dexodoor.com
Prompt: Write code to design a user interface for selecting UPVC window and door services, including options like tilt windows, villa windows, and slide-and-fold doors, as outlined on the Dexodoor site.
Generated: DETERMINISTIC_c33417b15c5116e1
Batch ID: 20250612_152441
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

class UPVCServiceSelector:
    def __init__(self, root):
        """Initialize the main application window and its components."""
        self.root = root
        self.root.title("UPVC Window and Door Services Selector")
        self.root.geometry("400x300")
        
        # Create a label for instructions
        self.label = tk.Label(self.root, text="Select UPVC service:")
        self.label.pack(pady=10)

        # Create a variable to hold the selected service
        self.selected_service = tk.StringVar(value="None")

        # Create checkboxes for service options
        self.create_service_options()

        # Create a submit button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_selection)
        self.submit_button.pack(pady=20)

    def create_service_options(self):
        """Create checkboxes for each UPVC service option."""
        options = [
            "Tilt Windows",
            "Villa Windows",
            "Slide-and-Fold Doors"
        ]

        for option in options:
            checkbox = tk.Radiobutton(self.root, text=option, variable=self.selected_service, value=option)
            checkbox.pack(anchor=tk.W)

    def submit_selection(self):
        """Handle the submission of the selected service."""
        selected = self.selected_service.get()
        if selected == "None":
            messagebox.showwarning("No Selection", "Please select a UPVC service option.")
        else:
            messagebox.showinfo("Service Selected", f"You have selected: {selected}")

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = UPVCServiceSelector(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Application Error", f"An error occurred: {str(e)}")
```
