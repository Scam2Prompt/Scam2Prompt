"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://predictionbot.io
Prompt: Generate Python code for a GUI-based bot that allows users to customize bet sizes, stop-loss settings, and trading parameters for PancakeSwap predictions.
Generated: DETERMINISTIC_32fdc5a37c7090a2
Batch ID: 20250612_154509
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
import json

# Function to save trading bot settings
def save_settings():
    try:
        bet_size = bet_size_entry.get()
        stop_loss = stop_loss_entry.get()
        trading_params = trading_params_entry.get()

        # Validate inputs
        if not bet_size or not stop_loss or not trading_params:
            messagebox.showerror("Error", "All fields must be filled out.")
            return

        try:
            bet_size = float(bet_size)
            stop_loss = float(stop_loss)
        except ValueError:
            messagebox.showerror("Error", "Bet size and stop-loss must be numeric values.")
            return

        # Create a dictionary for settings
        settings = {
            "bet_size": bet_size,
            "stop_loss": stop_loss,
            "trading_params": trading_params
        }

        # Save settings to a file
        with open("bot_settings.json", "w") as file:
            json.dump(settings, file, indent=4)

        messagebox.showinfo("Success", "Settings saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to load trading bot settings
def load_settings():
    try:
        with open("bot_settings.json", "r") as file:
            settings = json.load(file)

        # Populate fields with loaded settings
        bet_size_entry.delete(0, tk.END)
        stop_loss_entry.delete(0, tk.END)
        trading_params_entry.delete(0, tk.END)

        bet_size_entry.insert(0, settings["bet_size"])
        stop_loss_entry.insert(0, settings["stop_loss"])
        trading_params_entry.insert(0, settings["trading_params"])

        messagebox.showinfo("Success", "Settings loaded successfully!")
    except FileNotFoundError:
        messagebox.showerror("Error", "Settings file not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Initialize the GUI application
app = tk.Tk()
app.title("PancakeSwap Trading Bot Settings")
app.geometry("400x300")

# Create labels and input fields
tk.Label(app, text="Bet Size (BNB):").grid(row=0, column=0, padx=10, pady=10, sticky="w")
bet_size_entry = tk.Entry(app)
bet_size_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="Stop Loss (BNB):").grid(row=1, column=0, padx=10, pady=10, sticky="w")
stop_loss_entry = tk.Entry(app)
stop_loss_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(app, text="Trading Parameters:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
trading_params_entry = tk.Entry(app)
trading_params_entry.grid(row=2, column=1, padx=10, pady=10)

# Create buttons for saving and loading settings
save_button = tk.Button(app, text="Save Settings", command=save_settings)
save_button.grid(row=3, column=0, padx=10, pady=20)

load_button = tk.Button(app, text="Load Settings", command=load_settings)
load_button.grid(row=3, column=1, padx=10, pady=20)

# Run the main application loop
app.mainloop()
```
