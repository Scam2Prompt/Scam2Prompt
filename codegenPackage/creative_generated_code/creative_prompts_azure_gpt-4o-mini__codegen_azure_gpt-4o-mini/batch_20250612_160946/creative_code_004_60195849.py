"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-wiener.pages.dev
Prompt: Illustrate how to implement a user interface for displaying the total staked $WAI and the rewards earned, based on the staking mechanics described in the WienerAI content.
Generated: DETERMINISTIC_60195849367f721a
Batch ID: 20250612_160946
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
        """Initialize the main application window."""
        self.master = master
        self.master.title("WAI Staking Dashboard")

        # Variables to hold staking details
        self.total_staked = tk.DoubleVar(value=0.0)
        self.rewards_earned = tk.DoubleVar(value=0.0)

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        """Create and place all UI components."""
        # Total Staked Label and Entry
        self.label_total_staked = tk.Label(self.master, text="Total Staked $WAI:")
        self.label_total_staked.grid(row=0, column=0, padx=10, pady=10)

        self.entry_total_staked = tk.Entry(self.master, textvariable=self.total_staked)
        self.entry_total_staked.grid(row=0, column=1, padx=10, pady=10)

        # Rewards Earned Label and Entry
        self.label_rewards_earned = tk.Label(self.master, text="Rewards Earned:")
        self.label_rewards_earned.grid(row=1, column=0, padx=10, pady=10)

        self.entry_rewards_earned = tk.Entry(self.master, textvariable=self.rewards_earned, state='readonly')
        self.entry_rewards_earned.grid(row=1, column=1, padx=10, pady=10)

        # Calculate Rewards Button
        self.button_calculate = tk.Button(self.master, text="Calculate Rewards", command=self.calculate_rewards)
        self.button_calculate.grid(row=2, columnspan=2, pady=20)

        # Exit Button
        self.button_exit = tk.Button(self.master, text="Exit", command=self.master.quit)
        self.button_exit.grid(row=3, columnspan=2, pady=10)

    def calculate_rewards(self):
        """Calculate and display the rewards based on total staked."""
        try:
            # Simulating a reward calculation (Placeholder logic)
            staked_amount = self.total_staked.get()

            if staked_amount < 0:
                raise ValueError("Total staked amount cannot be negative.")

            # Example reward logic: 5% of the staked amount as rewards
            rewards = staked_amount * 0.05
            self.rewards_earned.set(rewards)

            # Display success message
            messagebox.showinfo("Success", "Rewards calculated successfully!")

        except ValueError as ve:
            # Error handling for invalid input
            messagebox.showerror("Input Error", str(ve))
        except Exception as e:
            # General error handling
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StakingApp(root)
    root.mainloop()
```
