"""
Generated Code Metadata:
========================
Original URL: https://jsebastiao.com
Prompt: Write code for a healthcare wearable onboarding experience similar to the MyCite app case study described by J. Sebastião. Include UX design principles to improve user engagement and accessibility.
Generated: DETERMINISTIC_f76e831dc318bb3a
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# healthcare_wearable_onboarding.py

import tkinter as tk
from tkinter import messagebox

class OnboardingApp:
    def __init__(self, master):
        """Initialize the onboarding application."""
        self.master = master
        self.master.title("Healthcare Wearable Onboarding")
        self.master.geometry("400x600")
        
        # Create a welcome label
        self.welcome_label = tk.Label(master, text="Welcome to MyCite!", font=("Helvetica", 16))
        self.welcome_label.pack(pady=20)

        # Create a description label
        self.description_label = tk.Label(master, text="Let's get started with your onboarding experience.", wraplength=300)
        self.description_label.pack(pady=10)

        # Create a start button
        self.start_button = tk.Button(master, text="Start Onboarding", command=self.start_onboarding)
        self.start_button.pack(pady=20)

        # Create a quit button
        self.quit_button = tk.Button(master, text="Quit", command=self.quit_app)
        self.quit_button.pack(pady=10)

    def start_onboarding(self):
        """Start the onboarding process."""
        try:
            self.clear_window()
            self.show_user_info_form()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def clear_window(self):
        """Clear the current window content."""
        for widget in self.master.winfo_children():
            widget.destroy()

    def show_user_info_form(self):
        """Display the user information form."""
        self.user_info_label = tk.Label(self.master, text="Please enter your information:", font=("Helvetica", 14))
        self.user_info_label.pack(pady=20)

        # Create entry fields for user information
        self.name_label = tk.Label(self.master, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.master)
        self.name_entry.pack(pady=5)

        self.age_label = tk.Label(self.master, text="Age:")
        self.age_label.pack()
        self.age_entry = tk.Entry(self.master)
        self.age_entry.pack(pady=5)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit_info)
        self.submit_button.pack(pady=20)

        self.back_button = tk.Button(self.master, text="Back", command=self.back_to_welcome)
        self.back_button.pack(pady=10)

    def submit_info(self):
        """Handle the submission of user information."""
        name = self.name_entry.get()
        age = self.age_entry.get()

        if not name or not age.isdigit():
            messagebox.showwarning("Input Error", "Please enter valid name and age.")
            return

        # Process the user information (e.g., save to database)
        messagebox.showinfo("Success", f"Welcome, {name}! Your age is {age}.")
        self.clear_window()
        self.show_next_steps()

    def back_to_welcome(self):
        """Return to the welcome screen."""
        self.clear_window()
        self.__init__(self.master)

    def show_next_steps(self):
        """Display the next steps after onboarding."""
        next_steps_label = tk.Label(self.master, text="Next Steps:", font=("Helvetica", 14))
        next_steps_label.pack(pady=20)

        steps = [
            "1. Connect your wearable device.",
            "2. Set up your health goals.",
            "3. Start tracking your health."
        ]

        for step in steps:
            step_label = tk.Label(self.master, text=step)
            step_label.pack(anchor='w', padx=20)

        finish_button = tk.Button(self.master, text="Finish", command=self.quit_app)
        finish_button.pack(pady=20)

    def quit_app(self):
        """Quit the application."""
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = OnboardingApp(root)
    root.mainloop()
```
