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

class CryptoTradingApp:
    def __init__(self, root):
        """
        Initialize the cryptocurrency trading application interface.
        :param root: The root Tkinter window.
        """
        self.root = root
        self.root.title("Crypto Trading Interface")
        self.root.geometry("500x400")
        
        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        """
        Create and layout the widgets for the trading interface.
        """
        # Title Label
        title_label = tk.Label(self.root, text="Crypto Trading Interface", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Autonomy Settings
        autonomy_frame = tk.LabelFrame(self.root, text="Autonomy Settings", padx=10, pady=10)
        autonomy_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        tk.Label(autonomy_frame, text="Trading Autonomy Level:").grid(row=0, column=0, sticky="w")
        self.autonomy_var = tk.StringVar(value="Manual")
        autonomy_options = ["Manual", "Semi-Autonomous", "Fully Autonomous"]
        self.autonomy_menu = tk.OptionMenu(autonomy_frame, self.autonomy_var, *autonomy_options)
        self.autonomy_menu.grid(row=0, column=1, sticky="w")

        # Support Settings
        support_frame = tk.LabelFrame(self.root, text="Support Settings", padx=10, pady=10)
        support_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        tk.Label(support_frame, text="Enable Support Notifications:").grid(row=0, column=0, sticky="w")
        self.support_var = tk.BooleanVar(value=True)
        self.support_checkbox = tk.Checkbutton(support_frame, variable=self.support_var)
        self.support_checkbox.grid(row=0, column=1, sticky="w")

        tk.Label(support_frame, text="Support Level:").grid(row=1, column=0, sticky="w")
        self.support_level_var = tk.StringVar(value="Basic")
        support_options = ["Basic", "Intermediate", "Advanced"]
        self.support_menu = tk.OptionMenu(support_frame, self.support_level_var, *support_options)
        self.support_menu.grid(row=1, column=1, sticky="w")

        # Submit Button
        submit_button = tk.Button(self.root, text="Save Settings", command=self.save_settings)
        submit_button.pack(pady=20)

    def save_settings(self):
        """
        Save the user's settings and display a confirmation message.
        """
        try:
            autonomy_level = self.autonomy_var.get()
            support_notifications = "Enabled" if self.support_var.get() else "Disabled"
            support_level = self.support_level_var.get()

            # Display confirmation message
            messagebox.showinfo(
                "Settings Saved",
                f"Your settings have been saved:\n\n"
                f"Autonomy Level: {autonomy_level}\n"
                f"Support Notifications: {support_notifications}\n"
                f"Support Level: {support_level}"
            )
        except Exception as e:
            # Handle unexpected errors
            messagebox.showerror("Error", f"An error occurred while saving settings: {e}")

# Main application entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoTradingApp(root)
    root.mainloop()
```
