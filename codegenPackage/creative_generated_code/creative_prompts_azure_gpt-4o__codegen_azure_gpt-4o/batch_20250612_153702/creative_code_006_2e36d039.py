"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hawksight-v2.vercel.app
Prompt: Create a dashboard that displays HawkFi pool metrics, including TVL, fees, and balance, with options to refresh and sort data.
Generated: DETERMINISTIC_2e36d039f7bb3c9b
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

class HawkFiDashboard:
    def __init__(self, root):
        """
        Initialize the HawkFi Dashboard GUI application.
        
        Args:
            root: The root Tkinter window instance.
        """
        self.root = root
        self.root.title("HawkFi Pool Metrics Dashboard")
        self.root.geometry("600x400")
        
        # Metrics Data
        self.metrics = [
            {"pool": "Pool A", "tvl": random.uniform(100000, 500000), "fees": random.uniform(1000, 5000), "balance": random.uniform(20000, 100000)},
            {"pool": "Pool B", "tvl": random.uniform(100000, 500000), "fees": random.uniform(1000, 5000), "balance": random.uniform(20000, 100000)},
            {"pool": "Pool C", "tvl": random.uniform(100000, 500000), "fees": random.uniform(1000, 5000), "balance": random.uniform(20000, 100000)},
        ]
        
        # Create UI elements
        self.create_widgets()
        
    def create_widgets(self):
        """
        Create the UI elements for the dashboard.
        """
        # Title Label
        title = tk.Label(self.root, text="HawkFi Pool Metrics", font=("Arial", 20))
        title.pack(pady=10)
        
        # Treeview for displaying metrics
        columns = ("pool", "tvl", "fees", "balance")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        self.tree.heading("pool", text="Pool Name")
        self.tree.heading("tvl", text="TVL")
        self.tree.heading("fees", text="Fees")
        self.tree.heading("balance", text="Balance")
        self.tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Populate initial data
        self.refresh_data()
        
        # Control Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        refresh_button = tk.Button(button_frame, text="Refresh", command=self.refresh_data, width=10)
        refresh_button.grid(row=0, column=0, padx=5)
        
        sort_button = tk.Button(button_frame, text="Sort by TVL", command=self.sort_by_tvl, width=15)
        sort_button.grid(row=0, column=1, padx=5)
        
    def refresh_data(self):
        """
        Refresh the metrics data and update the dashboard.
        """
        try:
            # Simulate fetching updated metrics data
            for metric in self.metrics:
                metric["tvl"] = random.uniform(100000, 500000)
                metric["fees"] = random.uniform(1000, 5000)
                metric["balance"] = random.uniform(20000, 100000)
            
            # Clear existing rows
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # Insert updated rows
            for metric in self.metrics:
                self.tree.insert("", tk.END, values=(metric["pool"], f"${metric['tvl']:.2f}", f"${metric['fees']:.2f}", f"${metric['balance']:.2f}"))
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to refresh data: {e}")
    
    def sort_by_tvl(self):
        """
        Sort the metrics data by TVL in descending order and update the dashboard.
        """
        try:
            # Sort data by TVL
            self.metrics.sort(key=lambda x: x["tvl"], reverse=True)
            
            # Clear existing rows
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # Insert sorted rows
            for metric in self.metrics:
                self.tree.insert("", tk.END, values=(metric["pool"], f"${metric['tvl']:.2f}", f"${metric['fees']:.2f}", f"${metric['balance']:.2f}"))
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to sort data: {e}")

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    # Instantiate the dashboard
    app = HawkFiDashboard(root)
    # Run the Tkinter event loop
    root.mainloop()
```
