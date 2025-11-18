"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cosmicrewards.com
Prompt: Write code to create a user-friendly interface for redeeming rewards and tracking earned Stardust, inspired by Cosmic Rewards' functionality.
Generated: DETERMINISTIC_ce1b46ad3b692d37
Batch ID: 20250612_151445
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

class StardustRewardTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("Stardust Reward Tracker")
        
        # Initialize rewards and stardust
        self.rewards = {
            '100 Stardust': 10,
            '500 Stardust': 25,
            '1000 Stardust': 50
        }
        self.earned_stardust = 0
        
        # Create UI elements
        self.create_widgets()
    
    def create_widgets(self):
        # Label for earned Stardust
        self.stardust_label = tk.Label(self.master, text="Earned Stardust: 0")
        self.stardust_label.pack(pady=10)
        
        # Dropdown for rewards
        self.reward_var = tk.StringVar(self.master)
        self.reward_var.set("Select Reward")
        
        self.reward_menu = tk.OptionMenu(self.master, self.reward_var, *self.rewards.keys())
        self.reward_menu.pack(pady=10)
        
        # Redeem button
        self.redeem_button = tk.Button(self.master, text="Redeem Reward", command=self.redeem_reward)
        self.redeem_button.pack(pady=10)
        
        # Add stardust button
        self.add_stardust_entry = tk.Entry(self.master)
        self.add_stardust_entry.pack(pady=10)
        self.add_stardust_button = tk.Button(self.master, text="Add Stardust", command=self.add_stardust)
        self.add_stardust_button.pack(pady=10)

    def redeem_reward(self):
        """Redeem a selected reward if enough stardust is available."""
        selected_reward = self.reward_var.get()
        
        # Check if a reward is selected
        if selected_reward not in self.rewards:
            messagebox.showwarning("Warning", "Please select a valid reward.")
            return
        
        reward_cost = self.rewards[selected_reward]
        
        # Check if the user has enough stardust
        if self.earned_stardust >= reward_cost:
            self.earned_stardust -= reward_cost
            self.stardust_label.config(text=f"Earned Stardust: {self.earned_stardust}")
            messagebox.showinfo("Success", f"You have redeemed {selected_reward}!")
        else:
            messagebox.showerror("Error", "Insufficient Stardust to redeem this reward.")

    def add_stardust(self):
        """Add stardust to the user's total, with error handling for non-integer inputs."""
        try:
            stardust_to_add = int(self.add_stardust_entry.get())
            if stardust_to_add < 0:
                raise ValueError("Stardust cannot be negative.")
            self.earned_stardust += stardust_to_add
            self.stardust_label.config(text=f"Earned Stardust: {self.earned_stardust}")
            self.add_stardust_entry.delete(0, tk.END)  # Clear entry after adding
        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StardustRewardTracker(root)
    root.mainloop()
```
