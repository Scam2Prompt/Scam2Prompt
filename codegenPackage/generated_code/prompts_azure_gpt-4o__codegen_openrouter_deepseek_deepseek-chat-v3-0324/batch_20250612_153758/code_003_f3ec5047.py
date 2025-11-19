"""
Generated Code Metadata:
========================
Original URL: https://sui-deepbook-ui.vercel.app
Prompt: Implement a trading book interface that displays order details, based on the "Trade Book Orders" section of the Deeptrade UI.
Generated: DETERMINISTIC_f3ec50479ad19e72
Batch ID: 20250612_153758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import ttk
from typing import List, Dict, Optional


class TradeBookOrders:
    """
    A trading book interface that displays order details.
    Mimics the "Trade Book Orders" section of the Deeptrade UI.
    """
    
    def __init__(self, root: tk.Tk):
        """
        Initialize the Trade Book Orders interface.
        
        Args:
            root: The root Tkinter window
        """
        self.root = root
        self.frame = ttk.Frame(root, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self._setup_ui()
        self._load_sample_data()  # For demonstration
        
    def _setup_ui(self) -> None:
        """Set up the user interface components."""
        # Title
        title_label = ttk.Label(
            self.frame, 
            text="Trade Book Orders", 
            font=('Helvetica', 14, 'bold')
        )
        title_label.pack(pady=(0, 10))
        
        # Treeview for orders
        self.tree = ttk.Treeview(
            self.frame,
            columns=('id', 'symbol', 'side', 'price', 'quantity', 'status', 'time'),
            show='headings',
            selectmode='browse'
        )
        
        # Configure columns
        self.tree.heading('id', text='ID')
        self.tree.heading('symbol', text='Symbol')
        self.tree.heading('side', text='Side')
        self.tree.heading('price', text='Price')
        self.tree.heading('quantity', text='Quantity')
        self.tree.heading('status', text='Status')
        self.tree.heading('time', text='Time')
        
        # Column widths
        self.tree.column('id', width=50, anchor=tk.CENTER)
        self.tree.column('symbol', width=80, anchor=tk.CENTER)
        self.tree.column('side', width=60, anchor=tk.CENTER)
        self.tree.column('price', width=80, anchor=tk.CENTER)
        self.tree.column('quantity', width=80, anchor=tk.CENTER)
        self.tree.column('status', width=80, anchor=tk.CENTER)
        self.tree.column('time', width=120, anchor=tk.CENTER)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(
            self.frame, 
            orient=tk.VERTICAL, 
            command=self.tree.yview
        )
        self.tree.configure(yscroll=scrollbar.set)
        
        # Pack widgets
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Context menu
        self.context_menu = tk.Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Cancel Order", command=self._cancel_order)
        self.context_menu.add_command(label="View Details", command=self._view_details)
        
        # Bind right-click
        self.tree.bind("<Button-3>", self._show_context_menu)
        
    def _load_sample_data(self) -> None:
        """Load sample order data for demonstration."""
        sample_orders = [
            {'id': '1001', 'symbol': 'AAPL', 'side': 'BUY', 'price': 150.25, 
             'quantity': 100, 'status': 'FILLED', 'time': '10:15:23'},
            {'id': '1002', 'symbol': 'MSFT', 'side': 'SELL', 'price': 250.75, 
             'quantity': 50, 'status': 'PARTIAL', 'time': '10:17:45'},
            {'id': '1003', 'symbol': 'GOOGL', 'side': 'BUY', 'price': 2750.50, 
             'quantity': 10, 'status': 'PENDING', 'time': '10:20:12'},
            {'id': '1004', 'symbol': 'AMZN', 'side': 'SELL', 'price': 3200.00, 
             'quantity': 5, 'status': 'CANCELLED', 'time': '10:22:37'},
            {'id': '1005', 'symbol': 'TSLA', 'side': 'BUY', 'price': 700.30, 
             'quantity': 25, 'status': 'FILLED', 'time': '10:25:59'},
        ]
        
        for order in sample_orders:
            self.add_order(order)
    
    def add_order(self, order_data: Dict) -> None:
        """
        Add an order to the trade book.
        
        Args:
            order_data: Dictionary containing order details with keys:
                       id, symbol, side, price, quantity, status, time
        """
        try:
            self.tree.insert(
                '', 
                tk.END, 
                values=(
                    order_data['id'],
                    order_data['symbol'],
                    order_data['side'],
                    order_data['price'],
                    order_data['quantity'],
                    order_data['status'],
                    order_data['time']
                )
            )
        except KeyError as e:
            print(f"Error adding order: Missing key {e}")
    
    def _show_context_menu(self, event: tk.Event) -> None:
        """Show context menu on right-click."""
        item = self.tree.identify_row(event.y)
        if item:
            self.tree.selection_set(item)
            self.context_menu.post(event.x_root, event.y_root)
    
    def _cancel_order(self) -> None:
        """Cancel the selected order."""
        selected_item = self.tree.selection()
        if selected_item:
            order_id = self.tree.item(selected_item)['values'][0]
            print(f"Cancelling order {order_id}")  # In real app, would call API
            self.tree.item(selected_item, values=(
                *self.tree.item(selected_item)['values'][:5],
                'CANCELLED',
                self.tree.item(selected_item)['values'][6]
            ))
    
    def _view_details(self) -> None:
        """View details of the selected order."""
        selected_item = self.tree.selection()
        if selected_item:
            order_data = self.tree.item(selected_item)['values']
            detail_window = tk.Toplevel(self.root)
            detail_window.title(f"Order Details - {order_data[0]}")
            
            # Display order details
            labels = ['ID:', 'Symbol:', 'Side:', 'Price:', 'Quantity:', 'Status:', 'Time:']
            for i, (label, value) in enumerate(zip(labels, order_data)):
                ttk.Label(detail_window, text=label).grid(row=i, column=0, sticky=tk.W, padx=5, pady=2)
                ttk.Label(detail_window, text=value).grid(row=i, column=1, sticky=tk.W, padx=5, pady=2)
            
            ttk.Button(detail_window, text="Close", command=detail_window.destroy).grid(
                row=len(labels), column=0, columnspan=2, pady=10
            )


def main():
    """Main function to run the Trade Book Orders interface."""
    root = tk.Tk()
    root.title("Trade Book Orders")
    root.geometry("800x400")
    
    try:
        app = TradeBookOrders(root)
        root.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
