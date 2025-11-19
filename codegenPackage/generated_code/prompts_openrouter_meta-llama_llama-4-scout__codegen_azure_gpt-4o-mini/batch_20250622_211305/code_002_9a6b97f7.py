"""
Generated Code Metadata:
========================
Original URL: https://tradegpt360-evix.com
Prompt: "Generate a code example for a user-friendly cryptocurrency trading interface that allows users to customize autonomy and support settings, similar to the TradeGPT 360 Evix application."
Generated: DETERMINISTIC_9a6b97f7881b6921
Batch ID: 20250622_211305
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
import json

class CryptoTradingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Crypto Trading Interface")
        self.master.geometry("400x300")

        # User settings
        self.settings = {
            "autonomy": "manual",
            "support": True
        }

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Autonomy setting
        self.autonomy_label = tk.Label(self.master, text="Select Autonomy:")
        self.autonomy_label.pack(pady=10)

        self.autonomy_var = tk.StringVar(value=self.settings["autonomy"])
        self.manual_radio = tk.Radiobutton(self.master, text="Manual", variable=self.autonomy_var, value="manual")
        self.auto_radio = tk.Radiobutton(self.master, text="Auto", variable=self.autonomy_var, value="auto")
        self.manual_radio.pack()
        self.auto_radio.pack()

        # Support setting
        self.support_var = tk.BooleanVar(value=self.settings["support"])
        self.support_check = tk.Checkbutton(self.master, text="Enable Support", variable=self.support_var)
        self.support_check.pack(pady=10)

        # Save settings button
        self.save_button = tk.Button(self.master, text="Save Settings", command=self.save_settings)
        self.save_button.pack(pady=20)

    def save_settings(self):
        """Save user settings to a JSON file."""
        self.settings["autonomy"] = self.autonomy_var.get()
        self.settings["support"] = self.support_var.get()

        try:
            with open("user_settings.json", "w") as settings_file:
                json.dump(self.settings, settings_file)
            messagebox.showinfo("Success", "Settings saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save settings: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoTradingApp(root)
    root.mainloop()
```
