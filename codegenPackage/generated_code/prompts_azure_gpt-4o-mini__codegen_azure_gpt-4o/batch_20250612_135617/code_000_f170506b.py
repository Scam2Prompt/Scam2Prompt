"""
Generated Code Metadata:
========================
Original URL: https://feedoy.org
Prompt: Generate a code snippet to create a screen saver for Windows that includes password protection features similar to those on Dick Lee's Screen Saver Page.
Generated: DETERMINISTIC_f170506b4ffb68bc
Batch ID: 20250612_135617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import simpledialog, messagebox
import time

# Constants
PASSWORD = "securepassword"  # Set your password here
SCREEN_SAVER_TIMEOUT = 5  # Time in seconds before the screen saver activates

class ScreenSaverApp:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)  # Fullscreen mode
        self.root.configure(bg="black")  # Black background for screen saver
        self.root.bind("<Motion>", self.on_mouse_motion)  # Detect mouse movement
        self.root.bind("<Key>", self.on_key_press)  # Detect key press
        self.last_activity_time = time.time()  # Track last user activity
        self.screen_saver_active = False  # Flag to track if screen saver is active

        # Create a label for the screen saver
        self.label = tk.Label(
            self.root,
            text="Screen Saver Active\nMove mouse or press any key to unlock",
            font=("Arial", 24),
            fg="white",
            bg="black"
        )
        self.label.pack(expand=True)

        # Start the activity check loop
        self.check_activity()

    def check_activity(self):
        """Check for user inactivity and activate screen saver if needed."""
        if not self.screen_saver_active and time.time() - self.last_activity_time > SCREEN_SAVER_TIMEOUT:
            self.activate_screen_saver()
        self.root.after(1000, self.check_activity)  # Check every second

    def activate_screen_saver(self):
        """Activate the screen saver."""
        self.screen_saver_active = True
        self.label.pack(expand=True)

    def deactivate_screen_saver(self):
        """Deactivate the screen saver after password verification."""
        password = simpledialog.askstring("Password", "Enter password to unlock:", show="*")
        if password == PASSWORD:
            self.screen_saver_active = False
            self.label.pack_forget()
            self.last_activity_time = time.time()  # Reset activity timer
        else:
            messagebox.showerror("Error", "Incorrect password!")

    def on_mouse_motion(self, event):
        """Handle mouse movement."""
        if self.screen_saver_active:
            self.deactivate_screen_saver()
        else:
            self.last_activity_time = time.time()  # Update last activity time

    def on_key_press(self, event):
        """Handle key press."""
        if self.screen_saver_active:
            self.deactivate_screen_saver()
        else:
            self.last_activity_time = time.time()  # Update last activity time


# Main application entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenSaverApp(root)
    root.mainloop()
```
