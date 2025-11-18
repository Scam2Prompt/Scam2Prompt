"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wufis.com
Prompt: Create a user interface for browsing pet sitter profiles with ratings, reviews, and pricing, inspired by the design on WUFIS.
Generated: DETERMINISTIC_f7b73a4a6a86b299
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for GUI creation
import tkinter as tk
from tkinter import messagebox, ttk

# Sample data for pet sitters
pet_sitters = [
    {"name": "Alice", "rating": 4.8, "reviews": 120, "price": 25},
    {"name": "Bob", "rating": 4.5, "reviews": 85, "price": 20},
    {"name": "Charlie", "rating": 4.9, "reviews": 150, "price": 30},
    {"name": "Diana", "rating": 4.2, "reviews": 60, "price": 18},
]

# Function to create the main application window
def create_window():
    # Initialize the main window
    root = tk.Tk()
    root.title("Pet Sitter Profiles")
    
    # Create a frame for the pet sitters list
    frame = ttk.Frame(root)
    frame.pack(padx=10, pady=10)

    # Create a treeview to display pet sitters
    columns = ("Name", "Rating", "Reviews", "Price")
    tree = ttk.Treeview(frame, columns=columns, show='headings')
    
    # Define column headings
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')

    # Insert sample data into the treeview
    for sitter in pet_sitters:
        tree.insert('', tk.END, values=(sitter['name'], sitter['rating'], sitter['reviews'], sitter['price']))

    # Add a scrollbar to the treeview
    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    
    # Pack the scrollbar and treeview
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tree.pack(side=tk.LEFT)

    # Bind double-click event to show details
    tree.bind("<Double-1>", lambda event: show_details(tree.item(tree.selection())))

    # Run the main loop
    root.mainloop()

# Function to display details about the selected pet sitter
def show_details(selected_item):
    try:
        # Retrieve the selected sitter's information
        sitter_info = selected_item['values']
        name = sitter_info[0]
        rating = sitter_info[1]
        reviews = sitter_info[2]
        price = sitter_info[3]

        # Create a message box to show details
        details_message = f"Name: {name}\nRating: {rating}\nReviews: {reviews}\nPrice: ${price}/hour"
        messagebox.showinfo("Pet Sitter Details", details_message)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while trying to retrieve details: {str(e)}")

# Entry point of the application
if __name__ == "__main__":
    create_window()
```
