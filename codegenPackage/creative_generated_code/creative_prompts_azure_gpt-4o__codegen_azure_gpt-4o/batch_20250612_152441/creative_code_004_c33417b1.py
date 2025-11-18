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

# Function to handle service selection
def handle_selection(service):
    try:
        messagebox.showinfo("Selection", f"You selected: {service}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Initialize the main application window
root = tk.Tk()
root.title("UPVC Window and Door Services")
root.geometry("400x300")  # Set the window size

# Application title
title_label = tk.Label(root, text="Select UPVC Services", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

# Frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Service options
services = [
    "Tilt Windows",
    "Villa Windows",
    "Slide-and-Fold Doors"
]

# Generate buttons dynamically for each service
for service in services:
    button = tk.Button(button_frame, text=service, font=("Arial", 12), width=20,
                        command=lambda s=service: handle_selection(s))
    button.pack(pady=5)

# Exit button to close the application
exit_button = tk.Button(root, text="Exit", font=("Arial", 12), width=10, command=root.destroy)
exit_button.pack(pady=20)

# Start the application
if __name__ == "__main__":
    try:
        root.mainloop()
    except Exception as e:
        print(f"Application encountered an error: {e}")
```
