"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-gmt-marketplace.pages.dev
Prompt: Develop a dashboard interface to display GoMining miner statistics, including rewards, energy efficiency, and ROI, with sorting and filtering options.
Generated: DETERMINISTIC_ffe2a6aa1e8e502e
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

class MiningDashboard:
    def __init__(self, root):
        """Initialize the dashboard interface."""
        self.root = root
        self.root.title("GoMining Dashboard")
        
        self.data = self.load_data()  # Load mining data
        
        # Create UI components
        self.create_widgets()

    def load_data(self):
        """Load miner statistics from a CSV file."""
        try:
            data = pd.read_csv('mining_statistics.csv')
            return data
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")
            return pd.DataFrame(columns=['Miner', 'Rewards', 'Energy Efficiency', 'ROI'])

    def create_widgets(self):
        """Create and layout the dashboard widgets."""
        self.tree = ttk.Treeview(self.root, columns=('Miner', 'Rewards', 'Energy Efficiency', 'ROI'), show='headings')
        self.tree.heading('Miner', text='Miner')
        self.tree.heading('Rewards', text='Rewards')
        self.tree.heading('Energy Efficiency', text='Energy Efficiency')
        self.tree.heading('ROI', text='ROI')

        self.tree.bind("<Double-1>", self.on_item_select)  # Double-click to view details
        
        self.sort_button = tk.Button(self.root, text="Sort by Rewards", command=self.sort_by_rewards)
        
        self.filter_entry = tk.Entry(self.root)
        self.filter_button = tk.Button(self.root, text="Filter", command=self.filter_data)

        # Layout
        self.tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.sort_button.pack(side=tk.LEFT)
        self.filter_entry.pack(side=tk.LEFT)
        self.filter_button.pack(side=tk.LEFT)

        self.populate_tree()

    def populate_tree(self):
        """Populate the tree view with mining data."""
        for index, row in self.data.iterrows():
            self.tree.insert('', 'end', values=(row['Miner'], row['Rewards'], row['Energy Efficiency'], row['ROI']))

    def sort_by_rewards(self):
        """Sort the displayed data by rewards."""
        self.data.sort_values(by='Rewards', ascending=False, inplace=True)
        self.refresh_tree()

    def filter_data(self):
        """Filter the displayed data based on user input."""
        filter_value = self.filter_entry.get().strip()
        if filter_value:
            filtered_data = self.data[self.data['Miner'].str.contains(filter_value, case=False)]
            self.update_tree(filtered_data)
        else:
            self.update_tree(self.data)

    def update_tree(self, data):
        """Update the tree view with new data."""
        self.tree.delete(*self.tree.get_children())  # Clear existing data
        for index, row in data.iterrows():
            self.tree.insert('', 'end', values=(row['Miner'], row['Rewards'], row['Energy Efficiency'], row['ROI']))

    def refresh_tree(self):
        """Refresh the tree view with sorted data."""
        self.update_tree(self.data)

    def on_item_select(self, event):
        """Handle item selection event."""
        selected_item = self.tree.selection()[0]
        miner_info = self.tree.item(selected_item, 'values')
        messagebox.showinfo("Miner Details", f"Miner: {miner_info[0]}\nRewards: {miner_info[1]}\nEnergy Efficiency: {miner_info[2]}\nROI: {miner_info[3]}")

if __name__ == "__main__":
    root = tk.Tk()
    dashboard = MiningDashboard(root)
    root.mainloop()
```

### Note:
To run this code, ensure you have a CSV file named `mining_statistics.csv` with the columns: `Miner`, `Rewards`, `Energy Efficiency`, `ROI`. Adjust the file path accordingly if necessary.
