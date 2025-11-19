"""
Generated Code Metadata:
========================
Original URL: https://shoppiday.site
Prompt: Generate code to create a user interface for displaying cashback offers and discounts, inspired by Shoppiday's features.
Generated: DETERMINISTIC_9f1868bc7098db25
Batch ID: 20250612_163308
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

# Function to simulate fetching cashback offers and discounts
def fetch_offers():
    try:
        # Simulated data (In production, this would be fetched from an API or database)
        offers = [
            {"store": "Amazon", "cashback": "5%", "discount": "10% off on electronics"},
            {"store": "eBay", "cashback": "3%", "discount": "15% off on fashion"},
            {"store": "Walmart", "cashback": "2%", "discount": "5% off on groceries"},
            {"store": "Target", "cashback": "4%", "discount": "20% off on home appliances"},
        ]
        return offers
    except Exception as e:
        # Handle any errors that occur during fetching
        messagebox.showerror("Error", f"Failed to fetch offers: {str(e)}")
        return []

# Function to populate the UI with offers
def populate_offers():
    offers = fetch_offers()
    if not offers:
        return

    # Clear existing offers
    for widget in offers_frame.winfo_children():
        widget.destroy()

    # Display each offer in the UI
    for offer in offers:
        store_label = tk.Label(offers_frame, text=f"Store: {offer['store']}", font=("Arial", 12, "bold"))
        cashback_label = tk.Label(offers_frame, text=f"Cashback: {offer['cashback']}", font=("Arial", 10))
        discount_label = tk.Label(offers_frame, text=f"Discount: {offer['discount']}", font=("Arial", 10))
        
        store_label.pack(anchor="w", pady=2)
        cashback_label.pack(anchor="w", pady=2)
        discount_label.pack(anchor="w", pady=2)

# Function to refresh offers
def refresh_offers():
    populate_offers()
    messagebox.showinfo("Info", "Offers refreshed successfully!")

# Create the main application window
app = tk.Tk()
app.title("Cashback Offers and Discounts")
app.geometry("400x400")

# Header label
header_label = tk.Label(app, text="Cashback Offers and Discounts", font=("Arial", 16, "bold"))
header_label.pack(pady=10)

# Frame to display offers
offers_frame = tk.Frame(app)
offers_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Refresh button
refresh_button = tk.Button(app, text="Refresh Offers", command=refresh_offers, font=("Arial", 12))
refresh_button.pack(pady=10)

# Populate the UI with initial offers
populate_offers()

# Start the application
app.mainloop()
```
