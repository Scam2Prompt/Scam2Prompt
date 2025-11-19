"""
Generated Code Metadata:
========================
Original URL: https://meteora-app-git-feat-permissioned-vault-wowcats.vercel.app
Prompt: "Design a basic UI component for displaying pool information, including LM APR and 365d Yield / TVL, from the Meteora Pools data."
Generated: DETERMINISTIC_c33608f02f66e30b
Batch ID: 20250622_212031
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

class PoolInfoUI:
    """
    A simple UI component for displaying pool information including 
    LM APR and 365d Yield / TVL from the Meteora Pools data.
    """

    def __init__(self, master):
        """
        Initializes the UI component.

        :param master: The parent window or frame.
        """
        self.master = master
        self.master.title("Pool Information")

        # Create labels for displaying pool information
        self.label_lm_apr = tk.Label(master, text="LM APR:")
        self.label_lm_apr.grid(row=0, column=0, padx=10, pady=10)

        self.label_yield_tvl = tk.Label(master, text="365d Yield / TVL:")
        self.label_yield_tvl.grid(row=1, column=0, padx=10, pady=10)

        # Create entry fields for pool information
        self.entry_lm_apr = tk.Entry(master)
        self.entry_lm_apr.grid(row=0, column=1, padx=10, pady=10)

        self.entry_yield_tvl = tk.Entry(master)
        self.entry_yield_tvl.grid(row=1, column=1, padx=10, pady=10)

        # Create a button to display the pool information
        self.button_display = tk.Button(master, text="Display Info", command=self.display_info)
        self.button_display.grid(row=2, columnspan=2, pady=20)

    def display_info(self):
        """
        Displays the pool information entered by the user.
        """
        try:
            lm_apr = self.entry_lm_apr.get()
            yield_tvl = self.entry_yield_tvl.get()

            if not lm_apr or not yield_tvl:
                raise ValueError("Both fields must be filled out.")

            # Display the pool information in a message box
            messagebox.showinfo("Pool Information", f"LM APR: {lm_apr}\n365d Yield / TVL: {yield_tvl}")

        except ValueError as e:
            # Handle value errors and show an error message
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            # Handle any other unexpected errors
            messagebox.showerror("Unexpected Error", f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    app = PoolInfoUI(root)
    root.mainloop()
```
