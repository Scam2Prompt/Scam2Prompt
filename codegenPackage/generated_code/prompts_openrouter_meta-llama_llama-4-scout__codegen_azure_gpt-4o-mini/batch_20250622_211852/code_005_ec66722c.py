"""
Generated Code Metadata:
========================
Original URL: https://predictionbot.io
Prompt: Create a user-friendly interface for the Pancakeswap Prediction Bot, allowing users to easily set up and customize their bot settings without requiring coding skills.
Generated: DETERMINISTIC_ec66722c2b7e60fd
Batch ID: 20250622_211852
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

class PredictionBotSettings:
    """Class to manage the settings for the Pancakeswap Prediction Bot."""
    
    def __init__(self):
        self.settings = {
            "stake_amount": 0.1,
            "prediction_duration": 60,
            "risk_level": "medium"
        }

    def load_settings(self, file_path):
        """Load settings from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                self.settings = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            messagebox.showerror("Error", f"Failed to load settings: {e}")

    def save_settings(self, file_path):
        """Save settings to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump(self.settings, file, indent=4)
        except IOError as e:
            messagebox.showerror("Error", f"Failed to save settings: {e}")

class PredictionBotUI:
    """User interface for the Pancakeswap Prediction Bot settings."""
    
    def __init__(self, master):
        self.master = master
        self.master.title("Pancakeswap Prediction Bot Settings")
        
        self.bot_settings = PredictionBotSettings()
        
        # Create UI elements
        self.create_widgets()
        
    def create_widgets(self):
        """Create and place UI elements on the window."""
        # Stake Amount
        tk.Label(self.master, text="Stake Amount (BNB):").grid(row=0, column=0, padx=10, pady=10)
        self.stake_amount_entry = tk.Entry(self.master)
        self.stake_amount_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Prediction Duration
        tk.Label(self.master, text="Prediction Duration (seconds):").grid(row=1, column=0, padx=10, pady=10)
        self.prediction_duration_entry = tk.Entry(self.master)
        self.prediction_duration_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # Risk Level
        tk.Label(self.master, text="Risk Level:").grid(row=2, column=0, padx=10, pady=10)
        self.risk_level_var = tk.StringVar(value="medium")
        tk.OptionMenu(self.master, self.risk_level_var, "low", "medium", "high").grid(row=2, column=1, padx=10, pady=10)
        
        # Save Button
        self.save_button = tk.Button(self.master, text="Save Settings", command=self.save_settings)
        self.save_button.grid(row=3, column=0, columnspan=2, pady=20)
        
        # Load Button
        self.load_button = tk.Button(self.master, text="Load Settings", command=self.load_settings)
        self.load_button.grid(row=4, column=0, columnspan=2, pady=20)

    def save_settings(self):
        """Save the current settings to a file."""
        self.bot_settings.settings["stake_amount"] = float(self.stake_amount_entry.get())
        self.bot_settings.settings["prediction_duration"] = int(self.prediction_duration_entry.get())
        self.bot_settings.settings["risk_level"] = self.risk_level_var.get()
        
        self.bot_settings.save_settings("bot_settings.json")
        messagebox.showinfo("Success", "Settings saved successfully!")

    def load_settings(self):
        """Load settings from a file and update the UI."""
        self.bot_settings.load_settings("bot_settings.json")
        self.update_ui()

    def update_ui(self):
        """Update the UI with loaded settings."""
        self.stake_amount_entry.delete(0, tk.END)
        self.stake_amount_entry.insert(0, self.bot_settings.settings["stake_amount"])
        
        self.prediction_duration_entry.delete(0, tk.END)
        self.prediction_duration_entry.insert(0, self.bot_settings.settings["prediction_duration"])
        
        self.risk_level_var.set(self.bot_settings.settings["risk_level"])

if __name__ == "__main__":
    root = tk.Tk()
    app = PredictionBotUI(root)
    root.mainloop()
```
