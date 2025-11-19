"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shoppiday.site
Prompt: Generate code to create a user interface for displaying cashback offers and discounts, inspired by Shoppiday's features.
Generated: DETERMINISTIC_9f1868bc7098db25
Batch ID: 20250612_163308
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
from tkinter import ttk

class CashbackOffer:
    """Class to represent a cashback offer."""
    def __init__(self, title, description, discount_percentage):
        self.title = title
        self.description = description
        self.discount_percentage = discount_percentage

class CashbackApp:
    """Main application class for displaying cashback offers."""
    def __init__(self, root):
        self.root = root
        self.root.title("Cashback Offers")
        
        # Initialize the list of cashback offers
        self.offers = [
            CashbackOffer("Super Saver", "Get 20% cashback on your next purchase!", 20),
            CashbackOffer("Weekend Deal", "Enjoy 15% cashback this weekend only!", 15),
            CashbackOffer("New Customer Bonus", "Receive 25% cashback as a new customer!", 25)
        ]
        
        # Set up the user interface
        self.setup_ui()

    def setup_ui(self):
        """Set up the user interface components."""
        # Create a frame for the offer list
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Create a label for the title
        self.title_label = ttk.Label(self.frame, text="Cashback Offers", font=("Helvetica", 16))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Create a treeview to display offers
        self.tree = ttk.Treeview(self.frame, columns=("Description", "Discount"), show="headings")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Discount", text="Discount (%)")
        self.tree.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))

        # Add offers to the treeview
        self.populate_offers()

        # Create a button to refresh offers
        self.refresh_button = ttk.Button(self.frame, text="Refresh Offers", command=self.refresh_offers)
        self.refresh_button.grid(row=2, column=0, columnspan=2, pady=(10, 0))

        # Configure column width
        self.tree.column("Description", width=300)
        self.tree.column("Discount", width=100)

    def populate_offers(self):
        """Populate the treeview with cashback offers."""
        for offer in self.offers:
            self.tree.insert("", tk.END, values=(offer.description, offer.discount_percentage))

    def refresh_offers(self):
        """Refresh the cashback offers - in a real application this would fetch new data."""
        # For demonstration, we'll just clear and re-populate with the same offers
        self.tree.delete(*self.tree.get_children())
        self.populate_offers()

def main():
    """Main function to run the cashback application."""
    try:
        root = tk.Tk()
        app = CashbackApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Application Error", f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
