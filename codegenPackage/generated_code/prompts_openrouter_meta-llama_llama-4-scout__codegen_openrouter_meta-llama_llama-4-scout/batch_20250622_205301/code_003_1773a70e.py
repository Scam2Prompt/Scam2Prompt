"""
Generated Code Metadata:
========================
Original URL: https://www.misphits-mint.xyz
Prompt: Write a Python script to display a "SOLD OUT" message for an NFT project, inspired by the Misphits Mint page.
Generated: DETERMINISTIC_1773a70ee5d7783e
Batch ID: 20250622_205301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nft_sold_out.py

import tkinter as tk
from tkinter import messagebox

class NFTSoldOutPage:
    def __init__(self, root):
        """
        Initialize the NFT Sold Out page.

        Args:
            root (tkinter.Tk): The root window of the application.
        """
        self.root = root
        self.root.title("Mispfits Mint Page - SOLD OUT")

        # Create a main frame to hold the sold out message
        self.main_frame = tk.Frame(self.root, bg="#1a1d23")
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Create a label to display the sold out message
        self.sold_out_label = tk.Label(
            self.main_frame,
            text="SOLD OUT",
            font=("Arial", 48, "bold"),
            bg="#1a1d23",
            fg="#ffffff",
        )
        self.sold_out_label.pack(pady=20)

        # Create a sub-label to display a message
        self.sub_label = tk.Label(
            self.main_frame,
            text="All NFTs have been minted! Thank you for your support.",
            font=("Arial", 18),
            bg="#1a1d23",
            fg="#ffffff",
            wraplength=400,
        )
        self.sub_label.pack(pady=10)

    def run(self):
        """
        Run the application.
        """
        try:
            self.root.mainloop()
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = NFTSoldOutPage(root)
    app.run()
```
