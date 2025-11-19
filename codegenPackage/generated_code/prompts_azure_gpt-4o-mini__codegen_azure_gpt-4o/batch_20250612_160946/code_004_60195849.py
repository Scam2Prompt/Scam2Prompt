"""
Generated Code Metadata:
========================
Original URL: https://claim-wiener.pages.dev
Prompt: Illustrate how to implement a user interface for displaying the total staked $WAI and the rewards earned, based on the staking mechanics described in the WienerAI content.
Generated: DETERMINISTIC_60195849367f721a
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import tkinter as tk
from tkinter import messagebox

# Mock data for demonstration purposes
# In a real-world scenario, this data would be fetched from a backend or blockchain API
MOCK_USER_DATA = {
    "total_staked": 1500.0,  # Total staked $WAI
    "rewards_earned": 125.75  # Rewards earned in $WAI
}

def fetch_user_data():
    """
    Simulates fetching user staking data.
    In production, replace this with actual API calls or database queries.
    """
    try:
        # Simulate fetching data (replace with actual logic)
        return MOCK_USER_DATA
    except Exception as e:
        # Handle errors gracefully
        messagebox.showerror("Error", f"Failed to fetch user data: {str(e)}")
        return None

def refresh_data():
    """
    Refreshes the displayed staking data.
    """
    user_data = fetch_user_data()
    if user_data:
        total_staked_var.set(f"{user_data['total_staked']} $WAI")
        rewards_earned_var.set(f"{user_data['rewards_earned']} $WAI")

# Initialize the main application window
app = tk.Tk()
app.title("WienerAI Staking Dashboard")
app.geometry("400x200")  # Set window size

# Variables to hold displayed data
total_staked_var = tk.StringVar()
rewards_earned_var = tk.StringVar()

# Fetch initial data
refresh_data()

# Create UI elements
title_label = tk.Label(app, text="WienerAI Staking Dashboard", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

total_staked_label = tk.Label(app, text="Total Staked:", font=("Arial", 12))
total_staked_label.pack()

total_staked_value = tk.Label(app, textvariable=total_staked_var, font=("Arial", 12, "bold"))
total_staked_value.pack()

rewards_earned_label = tk.Label(app, text="Rewards Earned:", font=("Arial", 12))
rewards_earned_label.pack()

rewards_earned_value = tk.Label(app, textvariable=rewards_earned_var, font=("Arial", 12, "bold"))
rewards_earned_value.pack()

refresh_button = tk.Button(app, text="Refresh Data", command=refresh_data, font=("Arial", 12))
refresh_button.pack(pady=10)

# Run the application
app.mainloop()
```
