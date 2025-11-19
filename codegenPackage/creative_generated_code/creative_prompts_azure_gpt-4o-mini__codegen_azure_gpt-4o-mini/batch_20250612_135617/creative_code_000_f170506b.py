"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://feedoy.org
Prompt: Generate a code snippet to create a screen saver for Windows that includes password protection features similar to those on Dick Lee's Screen Saver Page.
Generated: DETERMINISTIC_f170506b4ffb68bc
Batch ID: 20250612_135617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ctypes
import os
import sys
import time
import threading
from getpass import getpass
from tkinter import Tk, Label, Entry, Button, StringVar

# Constants for screen saver settings
SCRNSAVE_TIMEOUT = 60  # Time in seconds before screen saver activates
SCRNSAVE_PATH = os.path.dirname(os.path.abspath(__file__))
PASSWORD_FILE = os.path.join(SCRNSAVE_PATH, "password.txt")

# Function to retrieve the user's password from a file
def load_password():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'r') as file:
            return file.read().strip()
    return None

# Function to save the user's password to a file
def save_password(password):
    with open(PASSWORD_FILE, 'w') as file:
        file.write(password)

# Class for the screen saver application
class ScreenSaver:
    def __init__(self):
        self.root = Tk()
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')

        # Label to show the screen saver text
        self.label = Label(self.root, text="Screen Saver", font=("Helvetica", 50), bg='black', fg='white')
        self.label.pack(expand=True)

        # Password entry setup
        self.password_var = StringVar()
        self.password_entry = Entry(self.root, textvariable=self.password_var, show='*', font=("Helvetica", 24))
        self.password_entry.pack(pady=20)

        self.submit_button = Button(self.root, text="Unlock", command=self.check_password, font=("Helvetica", 24))
        self.submit_button.pack(pady=20)

        # Load the saved password if it exists
        self.saved_password = load_password()
        self.screen_saver_active = True

    # Function to check the entered password
    def check_password(self):
        if self.password_var.get() == self.saved_password:
            self.hide_screensaver()
        else:
            self.label.config(text="Incorrect Password", fg='red')

    # Function to show the screen saver
    def show_screensaver(self):
        self.label.config(text="Screen Saver")
        self.root.deiconify()
        self.password_entry.focus_set()
        self.password_entry.delete(0, 'end')

    # Function to hide the screen saver
    def hide_screensaver(self):
        self.root.withdraw()
        self.screen_saver_active = False

    # Function to run the screen saver logic
    def run(self):
        last_active_time = time.time()

        while True:
            if self.screen_saver_active:
                time.sleep(1)
                # Check if the system has been idle for longer than the timeout
                if time.time() - last_active_time > SCRNSAVE_TIMEOUT:
                    self.show_screensaver()
            else:
                time.sleep(1)

            # Reset the last active time if there's user interaction
            if ctypes.windll.user32.GetLastInputInfo:
                last_active_time = time.time()

# Function to start the screen saver in a separate thread
def start_screensaver():
    screensaver = ScreenSaver()
    screensaver.run()

# Function to setup the password
def setup_password():
    password = getpass("Set your screen saver password: ")
    save_password(password)
    print("Password saved successfully.")

# Main execution
if __name__ == "__main__":
    if not os.path.exists(PASSWORD_FILE):
        setup_password()

    # Run the screen saver in a separate thread
    screen_saver_thread = threading.Thread(target=start_screensaver, daemon=True)
    screen_saver_thread.start()

    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting screen saver.")
        sys.exit(0)
```
