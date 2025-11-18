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
import string
import tkinter as tk
from tkinter import messagebox

class CaptchaApp:
    def __init__(self, master):
        """Initialize the main window and setup the CAPTCHA."""
        self.master = master
        master.title("Verify Yourself CAPTCHA")

        self.captcha_text = self.generate_captcha()
        
        self.label = tk.Label(master, text="Please verify you are human")
        self.label.pack()

        self.captcha_label = tk.Label(master, text=self.captcha_text, font=("Arial", 24))
        self.captcha_label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(master, text="Submit", command=self.verify_captcha)
        self.submit_button.pack(pady=20)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_captcha)
        self.reset_button.pack(pady=5)

    def generate_captcha(self, length=6):
        """Generate a random CAPTCHA string."""
        characters = string.ascii_uppercase + string.digits
        captcha = ''.join(random.choice(characters) for _ in range(length))
        return captcha

    def verify_captcha(self):
        """Verify the user's input against the generated CAPTCHA."""
        user_input = self.entry.get().strip()
        if user_input == self.captcha_text:
            messagebox.showinfo("Success", "Verification successful!")
        else:
            messagebox.showerror("Error", "Incorrect CAPTCHA. Please try again.")

    def reset_captcha(self):
        """Reset the CAPTCHA by generating a new one and clearing the entry."""
        self.captcha_text = self.generate_captcha()
        self.captcha_label.config(text=self.captcha_text)
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    try:
        root = tk.Tk()
        captcha_app = CaptchaApp(root)
        root.mainloop()
    except Exception as e:
        # Handle any unexpected exceptions gracefully
        print(f"An error occurred: {e}")
```
