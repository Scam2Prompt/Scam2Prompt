"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blackder.pages.dev
Prompt: How do I create a user interface that displays staking information such as shares and rewards for a cryptocurrency staking platform?
Generated: DETERMINISTIC_4bcd1dff3bd765db
Batch ID: 20250612_162346
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

class StakingApp:
    def __init__(self, master):
        """Initialize the StakingApp with the main window."""
        self.master = master
        master.title("Cryptocurrency Staking Information")

        # Labels for user interface
        self.shares_label = tk.Label(master, text="Shares:")
        self.shares_label.grid(row=0, column=0, padx=10, pady=10)

        self.rewards_label = tk.Label(master, text="Rewards:")
        self.rewards_label.grid(row=1, column=0, padx=10, pady=10)

        # Entry fields for shares and rewards
        self.shares_entry = tk.Entry(master)
        self.shares_entry.grid(row=0, column=1, padx=10, pady=10)

        self.rewards_entry = tk.Entry(master)
        self.rewards_entry.grid(row=1, column=1, padx=10, pady=10)

        # Button to display staking information
        self.display_button = tk.Button(master, text="Display Staking Info", command=self.display_info)
        self.display_button.grid(row=2, columnspan=2, pady=20)

    def display_info(self):
        """Display the staking information in a message box."""
        try:
            shares = float(self.shares_entry.get())
            rewards = float(self.rewards_entry.get())

            # Validate that shares and rewards are non-negative
            if shares < 0 or rewards < 0:
                raise ValueError("Shares and rewards must be non-negative.")

            # Create a message to show the staking information
            info_message = f"Shares: {shares}\nRewards: {rewards}"
            messagebox.showinfo("Staking Information", info_message)

        except ValueError as e:
            # Handle invalid input gracefully
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            # Handle any other unexpected errors
            messagebox.showerror("Unexpected Error", "An unexpected error occurred: " + str(e))

if __name__ == "__main__":
    root = tk.Tk()
    staking_app = StakingApp(root)
    root.mainloop()
```
