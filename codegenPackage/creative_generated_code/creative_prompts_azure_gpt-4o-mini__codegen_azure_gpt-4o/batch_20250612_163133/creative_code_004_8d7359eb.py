"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astedrex.com
Prompt: How can I create a user interface that allows traders to switch between Simple Mode and Pro Mode on Aster?
Generated: DETERMINISTIC_8d7359eb6a21231e
Batch ID: 20250612_163133
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

# Constants for mode names
SIMPLE_MODE = "Simple Mode"
PRO_MODE = "Pro Mode"

class TradingUI:
    def __init__(self, root):
        """
        Initialize the trading UI with a mode toggle feature.
        :param root: The root Tkinter window object
        """
        self.root = root
        self.root.title("Aster Trading Interface")

        # Initialize current mode to Simple Mode
        self.current_mode = SIMPLE_MODE

        # Create and configure the mode label
        self.mode_label = tk.Label(
            self.root, text=f"Current Mode: {self.current_mode}", font=("Arial", 14)
        )
        self.mode_label.pack(pady=20)

        # Create the toggle mode button
        self.toggle_button = tk.Button(
            self.root, text="Switch Mode", command=self.toggle_mode, font=("Arial", 12)
        )
        self.toggle_button.pack(pady=10)

        # Configure the exit button
        self.exit_button = tk.Button(
            self.root, text="Exit", command=self.exit_application, font=("Arial", 12)
        )
        self.exit_button.pack(pady=10)

    def toggle_mode(self):
        """
        Toggle between Simple Mode and Pro Mode.
        """
        try:
            # Switch modes
            if self.current_mode == SIMPLE_MODE:
                self.current_mode = PRO_MODE
            else:
                self.current_mode = SIMPLE_MODE

            # Update the mode label to reflect the change
            self.mode_label.config(
                text=f"Current Mode: {self.current_mode}"
            )
        except Exception as e:
            # Display error message to the user if toggling fails
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def exit_application(self):
        """
        Exit the application gracefully after confirmation.
        """
        try:
            # Ask user for confirmation before exiting
            if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
                self.root.destroy()
        except Exception as e:
            # Display error message if exit process fails
            messagebox.showerror("Error", f"An error occurred while exiting: {str(e)}")


if __name__ == "__main__":
    # Create the main Tkinter window
    root = tk.Tk()

    # Instantiate the trading UI
    app = TradingUI(root)

    # Run the Tkinter event loop
    root.mainloop()
```
