"""
Generated Code Metadata:
========================
Original URL: https://walletconnect-olxuahorder824112.pages.dev
Prompt: Generate a simple verification system that displays a "Я не робот" (I am not a robot) message and performs a security check before granting access.
Generated: DETERMINISTIC_ad453c32dd3fdb91
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from random import randint

class VerificationSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Verification System")
        self.label = tk.Label(self.root, text="Я не робот", font=("Arial", 24))
        self.label.pack()
        self.entry_label = tk.Label(self.root, text="Enter the verification code:")
        self.entry_label.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.button = tk.Button(self.root, text="Get Verification Code", command=self.generate_code)
        self.button.pack()
        self.verify_button = tk.Button(self.root, text="Verify", command=self.verify_code)
        self.verify_button.pack()
        self.code = None
        self.root.mainloop()

    def generate_code(self):
        self.code = randint(1000, 9999)
        self.label.config(text=f"Verification code: {self.code}")
        self.button.config(state="disabled")

    def verify_code(self):
        try:
            user_code = int(self.entry.get())
            if user_code == self.code:
                self.label.config(text="Access granted!")
                self.entry_label.pack_forget()
                self.entry.pack_forget()
                self.verify_button.pack_forget()
                self.button.config(state="normal", command=self.restart)
                self.button.config(text="Restart")
            else:
                self.label.config(text="Incorrect code. Try again.")
                self.entry.delete(0, tk.END)
        except ValueError:
            self.label.config(text="Invalid input. Please enter a number.")

    def restart(self):
        self.code = None
        self.label.config(text="Я не робот")
        self.entry_label.pack()
        self.entry.pack()
        self.verify_button.pack()
        self.button.config(text="Get Verification Code", command=self.generate_code, state="normal")

if __name__ == "__main__":
    VerificationSystem()
```
