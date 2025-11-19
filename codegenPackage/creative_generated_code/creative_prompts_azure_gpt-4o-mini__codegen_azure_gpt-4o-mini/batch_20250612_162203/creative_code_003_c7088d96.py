"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrica17.vercel.app
Prompt: Generate a script that allows users to select between Solana, Ethereum, and Polygon networks during login.
Generated: DETERMINISTIC_c7088d9651f88e9b
Batch ID: 20250612_162203
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

class NetworkSelectorApp:
    def __init__(self, master):
        self.master = master
        master.title("Network Selector")

        # Label for the app
        self.label = tk.Label(master, text="Select a Blockchain Network:")
        self.label.pack(pady=10)

        # Dropdown menu for network selection
        self.network_var = tk.StringVar()
        self.network_var.set("Select Network")  # Default value

        self.network_options = ["Solana", "Ethereum", "Polygon"]
        self.network_menu = tk.OptionMenu(master, self.network_var, *self.network_options)
        self.network_menu.pack(pady=10)

        # Login button
        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        # Get the selected network
        selected_network = self.network_var.get()

        # Check if a valid network is selected
        if selected_network == "Select Network":
            messagebox.showerror("Error", "Please select a network to proceed.")
        else:
            # Proceed with login process (placeholder for actual login logic)
            self.process_login(selected_network)

    def process_login(self, network):
        # Placeholder for login logic
        messagebox.showinfo("Login Successful", f"You are now logged in to {network} network.")

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    app = NetworkSelectorApp(root)

    # Start the GUI event loop
    try:
        root.mainloop()
    except Exception as e:
        # Handle unexpected errors gracefully
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
```
