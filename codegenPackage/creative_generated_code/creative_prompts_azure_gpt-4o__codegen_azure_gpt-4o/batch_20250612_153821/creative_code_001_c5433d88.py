"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mhfgy-722.com
Prompt: Create a Python script to simulate a "Verify Yourself" CAPTCHA system with a user-friendly interface.
Generated: DETERMINISTIC_c5433d882a2fb230
Batch ID: 20250612_153821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import tkinter as tk
from tkinter import messagebox

class CaptchaApp:
    def __init__(self, root):
        """
        Initialize the CAPTCHA application.
        Args:
            root (tk.Tk): Reference to the Tkinter root window.
        """
        self.root = root
        self.root.title("Verify Yourself - CAPTCHA")

        # Generate a random CAPTCHA
        self.captcha_text = self.generate_captcha()

        # Create UI components
        self.create_widgets()

    def generate_captcha(self):
        """
        Generate a random CAPTCHA string consisting of letters and digits.
        Returns:
            str: Random CAPTCHA string.
        """
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        return ''.join(random.choices(characters, k=6))

    def create_widgets(self):
        """
        Create and place the UI components in the Tkinter window.
        """
        # Instructions label
        self.label_instruction = tk.Label(self.root, text="Enter the text shown below to verify yourself:",
                                           font=("Arial", 12))
        self.label_instruction.pack(pady=10)

        # CAPTCHA display label
        self.label_captcha = tk.Label(self.root, text=self.captcha_text, font=("Courier", 16, "bold"),
                                      fg="blue")
        self.label_captcha.pack(pady=10)

        # Input field for user to type the CAPTCHA
        self.entry_captcha = tk.Entry(self.root, font=("Arial", 14))
        self.entry_captcha.pack(pady=10)

        # Submit button
        self.button_submit = tk.Button(self.root, text="Verify", font=("Arial", 12),
                                       command=self.verify_captcha)
        self.button_submit.pack(pady=10)

    def verify_captcha(self):
        """
        Verify the CAPTCHA entered by the user.
        """
        user_input = self.entry_captcha.get()

        if user_input == self.captcha_text:
            # If CAPTCHA matches, show success message
            messagebox.showinfo("Success", "Verification successful!")
            self.root.destroy()  # Close the application
        else:
            # If CAPTCHA doesn't match, show error message
            messagebox.showerror("Error", "Incorrect CAPTCHA. Please try again.")
            self.captcha_text = self.generate_captcha()  # Generate new CAPTCHA
            self.label_captcha.config(text=self.captcha_text)  # Update CAPTCHA display
            self.entry_captcha.delete(0, tk.END)  # Clear input field

if __name__ == "__main__":
    try:
        # Create the main Tkinter window
        root = tk.Tk()
        app = CaptchaApp(root)
        root.mainloop()
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")
```
