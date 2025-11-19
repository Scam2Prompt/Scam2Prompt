"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duolingo.wiki
Prompt: Provide code to create a user-friendly interface that helps users copy their Duolingo username or email for Super membership sign-up.
Generated: DETERMINISTIC_168ceabda036c2a1
Batch ID: 20250612_162742
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

class DuolingoCopyApp:
    """A simple GUI application to help users copy their Duolingo username or email for Super membership sign-up."""

    def __init__(self, master):
        """Initialize the main application window."""
        self.master = master
        self.master.title("Duolingo Username/Email Copier")
        self.master.geometry("400x200")
        
        # Label for instructions
        self.label = tk.Label(master, text="Enter your Duolingo Username or Email:")
        self.label.pack(pady=10)
        
        # Entry widget for user input
        self.entry = tk.Entry(master, width=50)
        self.entry.pack(pady=10)
        
        # Copy button
        self.copy_button = tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=10)

        # Exit button
        self.exit_button = tk.Button(master, text="Exit", command=master.quit)
        self.exit_button.pack(pady=10)

    def copy_to_clipboard(self):
        """Copy the entered username or email to the clipboard."""
        try:
            username_or_email = self.entry.get()
            if username_or_email:
                # Clear the clipboard and set the new value
                self.master.clipboard_clear()
                self.master.clipboard_append(username_or_email)
                messagebox.showinfo("Success", "Username/Email copied to clipboard!")
            else:
                messagebox.showwarning("Input Error", "Please enter a username or email.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    app = DuolingoCopyApp(root)
    # Start the application
    root.mainloop()
```
