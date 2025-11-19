"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etfswap-in.pages.dev
Prompt: Construct a user interface component that allows users to browse the ETF index screener on the ETFSwap platform.
Generated: DETERMINISTIC_baaeecd62a14fea7
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
from tkinter import ttk, messagebox

class ETFSwapScreener(tk.Tk):
    """
    A simple User Interface component for browsing the ETF index screener on the ETFSwap platform.
    """

    def __init__(self):
        super().__init__()
        self.title("ETFSwap ETF Index Screener")
        self.geometry("600x400")
        
        # Create and pack the search frame
        self.search_frame = ttk.Frame(self)
        self.search_frame.pack(pady=10, padx=10, fill='x')

        # Search label
        self.search_label = ttk.Label(self.search_frame, text="Search ETFs:")
        self.search_label.pack(side='left')

        # Search entry
        self.search_entry = ttk.Entry(self.search_frame, width=40)
        self.search_entry.pack(side='left', padx=5)

        # Search button
        self.search_button = ttk.Button(self.search_frame, text="Search", command=self.search_etfs)
        self.search_button.pack(side='left')

        # Results Treeview
        self.results_tree = ttk.Treeview(self, columns=("Name", "Ticker", "Price"), show='headings')
        self.results_tree.heading("Name", text="ETF Name")
        self.results_tree.heading("Ticker", text="Ticker")
        self.results_tree.heading("Price", text="Price")
        self.results_tree.pack(pady=10, padx=10, fill='both', expand=True)

        # Add a vertical scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.results_tree.yview)
        self.results_tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.pack(side='right', fill='y')

    def search_etfs(self):
        """
        Searches for ETFs based on the user input in the search entry.
        """
        query = self.search_entry.get().strip()
        if not query:
            messagebox.showwarning("Input Error", "Please enter a search term.")
            return
        
        # Clear previous results
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)

        # Simulating ETF data retrieval (in production, this could be an API call)
        etfs_data = self.get_etf_data(query)

        # Populate results in the Treeview
        for etf in etfs_data:
            self.results_tree.insert("", "end", values=(etf["name"], etf["ticker"], etf["price"]))

    def get_etf_data(self, query):
        """
        Simulates fetching ETF data based on the query. In a real application, this would involve 
        fetching data from an external source (e.g., an API).

        Args:
            query (str): The search term provided by the user.

        Returns:
            list: A list of dictionaries containing ETF data.
        """
        # Example ETF data (in a real application, this would come from an API)
        example_data = [
            {"name": "SPDR S&P 500 ETF Trust", "ticker": "SPY", "price": 430.12},
            {"name": "Invesco QQQ Trust", "ticker": "QQQ", "price": 350.45},
            {"name": "Vanguard Total Stock Market ETF", "ticker": "VTI", "price": 220.75},
        ]

        # Filter example data based on the query (case-insensitive)
        filtered_data = [
            etf for etf in example_data if query.lower() in etf["name"].lower() or query.lower() in etf["ticker"].lower()
        ]

        return filtered_data

if __name__ == "__main__":
    try:
        app = ETFSwapScreener()
        app.mainloop()
    except Exception as e:
        messagebox.showerror("Application Error", f"An error occurred: {e}")
```
