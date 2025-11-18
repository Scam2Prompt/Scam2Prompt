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


class CosmicRewardsApp:
    def __init__(self, root):
        """Initialize the Cosmic Rewards application."""
        self.root = root
        self.root.title("Cosmic Rewards")
        self.root.geometry("400x300")

        # Initialize Stardust balance
        self.stardust_balance = 0

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        """Create and place UI components."""
        # Title label
        tk.Label(self.root, text="Cosmic Rewards", font=("Arial", 16)).pack(pady=10)

        # Stardust balance display
        self.balance_label = tk.Label(self.root, text=f"Stardust Balance: {self.stardust_balance}", font=("Arial", 14))
        self.balance_label.pack(pady=5)

        # Earn Stardust button
        tk.Button(self.root, text="Earn Stardust", command=self.earn_stardust, width=20).pack(pady=5)

        # Redeem Rewards button
        tk.Button(self.root, text="Redeem Rewards", command=self.redeem_reward, width=20).pack(pady=5)

        # Exit button
        tk.Button(self.root, text="Exit", command=self.root.quit, width=20).pack(pady=20)

    def earn_stardust(self):
        """Handle earning Stardust functionality."""
        try:
            # Increment Stardust balance
            self.stardust_balance += 10
            self.update_balance()
            # Notify the user
            messagebox.showinfo("Success", "You earned 10 Stardust!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to earn Stardust: {e}")

    def redeem_reward(self):
        """Handle redeeming rewards functionality."""
        try:
            if self.stardust_balance >= 50:
                # Deduct Stardust for redemption
                self.stardust_balance -= 50
                self.update_balance()
                # Notify the user
                messagebox.showinfo("Success", "Reward redeemed successfully!")
            else:
                # Notify insufficient Stardust
                messagebox.showwarning("Insufficient Stardust", "You need at least 50 Stardust to redeem a reward.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to redeem reward: {e}")

    def update_balance(self):
        """Update the Stardust balance label."""
        self.balance_label.config(text=f"Stardust Balance: {self.stardust_balance}")


# Main application entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = CosmicRewardsApp(root)
    root.mainloop()
```
