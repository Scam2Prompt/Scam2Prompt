"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safesteth.com
Prompt: Write code for integrating a timer-based pop-up system that displays healthcare-related information, as described on SafeSteth.com.
Generated: DETERMINISTIC_efed4909394fb41f
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tkinter as tk
from threading import Timer
import random

# A list of healthcare-related tips to display in the pop-up
HEALTHCARE_TIPS = [
    "Drink plenty of water to stay hydrated.",
    "Take breaks to stretch and relax your muscles.",
    "Maintain a balanced diet rich in fruits and vegetables.",
    "Get regular exercise to improve overall health.",
    "Wash your hands frequently to prevent infections.",
    "Get enough sleep to boost immunity and mental health.",
    "Schedule regular checkups with your healthcare provider.",
]

# Function to display the pop-up window
def show_popup():
    try:
        # Create a new top-level window
        popup = tk.Toplevel()
        popup.title("Healthcare Tip")
        popup.geometry("300x150")
        popup.resizable(False, False)

        # Select a random tip to display
        tip = random.choice(HEALTHCARE_TIPS)

        # Add a label to show the healthcare tip
        label = tk.Label(popup, text=tip, wraplength=250, justify="center", font=("Arial", 12))
        label.pack(pady=20)

        # Add a button to close the pop-up
        close_button = tk.Button(popup, text="Close", command=popup.destroy)
        close_button.pack(pady=10)

        # Ensure the pop-up window appears above other windows
        popup.attributes("-topmost", True)
        popup.mainloop()
    except Exception as e:
        print(f"Error in showing pop-up: {e}")

# Function to schedule the timed pop-up
def schedule_popup(interval_seconds):
    try:
        # Function to create and schedule the next timer
        def timer_task():
            show_popup()
            schedule_popup(interval_seconds)

        # Start a timer that will trigger the timer_task function
        Timer(interval_seconds, timer_task).start()
    except Exception as e:
        print(f"Error in scheduling pop-up: {e}")

# Main application window
def main():
    try:
        # Create the main tkinter window
        root = tk.Tk()
        root.title("SafeSteth Healthcare Info")
        root.geometry("400x200")
        root.resizable(False, False)

        # Welcome label
        welcome_label = tk.Label(
            root,
            text="Welcome to SafeSteth!\nStay informed with healthcare tips.",
            wraplength=300,
            justify="center",
            font=("Arial", 14)
        )
        welcome_label.pack(pady=20)

        # Start button to begin displaying timed pop-ups
        start_button = tk.Button(
            root,
            text="Start Timer-Based Pop-Ups",
            command=lambda: schedule_popup(30)  # Set interval to 30 seconds
        )
        start_button.pack(pady=10)

        # Quit button to close the application
        quit_button = tk.Button(root, text="Quit", command=root.destroy)
        quit_button.pack(pady=10)

        # Start the main GUI loop
        root.mainloop()
    except Exception as e:
        print(f"Error in main application: {e}")

# Run the application
if __name__ == "__main__":
    main()
```
