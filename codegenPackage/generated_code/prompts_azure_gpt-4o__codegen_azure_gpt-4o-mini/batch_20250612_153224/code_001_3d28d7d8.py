"""
Generated Code Metadata:
========================
Original URL: https://aerotraining.com.tr
Prompt: Generate code to create a virtual cockpit interface for an Airbus A320 flight simulator, incorporating emergency scenarios and online flight capabilities as detailed on the Aero Training Center webpage.
Generated: DETERMINISTIC_3d28d7d8c9ea936c
Batch ID: 20250612_153224
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
import random

class VirtualCockpit:
    def __init__(self, master):
        """Initialize the virtual cockpit interface."""
        self.master = master
        self.master.title("Airbus A320 Virtual Cockpit")
        self.master.geometry("800x600")

        # Create UI elements
        self.create_ui()

        # Initialize flight status
        self.is_flying = False
        self.emergency_mode = False

    def create_ui(self):
        """Create the user interface components."""
        # Flight Status Label
        self.status_label = tk.Label(self.master, text="Flight Status: Grounded", font=("Arial", 16))
        self.status_label.pack(pady=20)

        # Start Flight Button
        self.start_button = tk.Button(self.master, text="Start Flight", command=self.start_flight, width=20)
        self.start_button.pack(pady=10)

        # Emergency Button
        self.emergency_button = tk.Button(self.master, text="Trigger Emergency", command=self.trigger_emergency, width=20)
        self.emergency_button.pack(pady=10)

        # Landing Button
        self.landing_button = tk.Button(self.master, text="Land", command=self.land, width=20)
        self.landing_button.pack(pady=10)

        # Exit Button
        self.exit_button = tk.Button(self.master, text="Exit", command=self.exit_simulation, width=20)
        self.exit_button.pack(pady=10)

    def start_flight(self):
        """Start the flight simulation."""
        if not self.is_flying:
            self.is_flying = True
            self.status_label.config(text="Flight Status: In Flight")
            messagebox.showinfo("Flight Status", "You are now in flight.")
        else:
            messagebox.warning("Flight Status", "Already in flight.")

    def trigger_emergency(self):
        """Simulate an emergency scenario."""
        if self.is_flying:
            self.emergency_mode = True
            emergency_type = random.choice(["Engine Failure", "Cabin Pressure Loss", "Fuel Leak"])
            messagebox.showwarning("Emergency Alert", f"Emergency: {emergency_type}!")
            self.status_label.config(text="Flight Status: Emergency Mode Activated")
        else:
            messagebox.warning("Flight Status", "Cannot trigger emergency while grounded.")

    def land(self):
        """Land the aircraft."""
        if self.is_flying:
            self.is_flying = False
            self.emergency_mode = False
            self.status_label.config(text="Flight Status: Grounded")
            messagebox.showinfo("Flight Status", "You have successfully landed.")
        else:
            messagebox.warning("Flight Status", "You are already grounded.")

    def exit_simulation(self):
        """Exit the flight simulation."""
        if messagebox.askokcancel("Exit", "Do you really want to exit?"):
            self.master.quit()

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    cockpit = VirtualCockpit(root)
    root.mainloop()
```
