"""
Generated Code Metadata:
========================
Original URL: https://feedoy.org
Prompt: Write a Python script to create a Windows screen saver that displays a password-protected interface, similar to those offered on Dick Lee's Screen Saver Page.
Generated: DETERMINISTIC_86293f58a24d4b49
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
import ctypes
import tkinter as tk
from tkinter import simpledialog, messagebox

# Constants for screen saver settings
SCREENSAVER_TIMEOUT = 300  # 5 minutes
PASSWORD = "your_password"  # Set your desired password here

# Function to check if the screensaver is active
def is_screensaver_active():
    user32 = ctypes.windll.User32
    return user32.GetForegroundWindow() == 0

# Function to create the password dialog
def show_password_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    password = simpledialog.askstring("Password Required", "Enter the password:", show='*')
    return password

# Function to validate the entered password
def validate_password(input_password):
    if input_password == PASSWORD:
        return True
    else:
        messagebox.showerror("Error", "Incorrect password!")
        return False

# Main function to run the screensaver
def run_screensaver():
    # Create a simple GUI for the screensaver
    screensaver_window = tk.Tk()
    screensaver_window.title("Screensaver")
    screensaver_window.geometry("800x600")
    screensaver_window.configure(bg='black')

    # Label to display a message
    label = tk.Label(screensaver_window, text="Screensaver Active", fg='white', bg='black', font=("Helvetica", 32))
    label.pack(expand=True)

    # Function to handle mouse movement
    def on_mouse_move(event):
        screensaver_window.destroy()  # Close screensaver on mouse movement

    # Bind mouse movement to the screensaver window
    screensaver_window.bind("<Motion>", on_mouse_move)

    # Show the screensaver window
    screensaver_window.attributes('-fullscreen', True)
    screensaver_window.after(SCREENSAVER_TIMEOUT * 1000, show_password)

    screensaver_window.mainloop()

# Function to show the password dialog and validate
def show_password():
    if is_screensaver_active():
        input_password = show_password_dialog()
        if input_password and validate_password(input_password):
            messagebox.showinfo("Access Granted", "Welcome back!")
            sys.exit(0)  # Exit the screensaver if password is correct
        else:
            run_screensaver()  # Restart screensaver if password is incorrect

# Entry point of the script
if __name__ == "__main__":
    try:
        run_screensaver()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        sys.exit(1)
```

**Note:** Replace `"your_password"` with the desired password for the screensaver. This script creates a simple password-protected screensaver using Tkinter. Make sure to run this script in an environment where Tkinter is supported.
