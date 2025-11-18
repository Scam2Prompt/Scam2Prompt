"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smarts-invests.net
Prompt: Develop a dashboard in Python to display statistics like total invested amount, total withdrawn amount, and active investor accounts, similar to Smarts-invests' statistics section.
Generated: DETERMINISTIC_0052cb13be4c0977
Batch ID: 20250612_145831
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
import sqlite3

class InvestmentDashboard:
    """A dashboard for displaying investment statistics."""

    def __init__(self, master):
        """Initialize the dashboard."""
        self.master = master
        self.master.title("Investment Dashboard")
        
        # Create database connection
        self.conn = self.create_connection("investments.db")
        
        # Create UI elements
        self.create_widgets()
        
        # Load statistics
        self.load_statistics()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error connecting to database: {e}")
        return conn

    def create_widgets(self):
        """Create the UI elements for the dashboard."""
        # Title Label
        title_label = tk.Label(self.master, text="Investment Statistics", font=("Arial", 16))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Total Invested Amount
        self.total_invested_label = tk.Label(self.master, text="Total Invested Amount: $0")
        self.total_invested_label.grid(row=1, column=0, padx=10, pady=5)

        # Total Withdrawn Amount
        self.total_withdrawn_label = tk.Label(self.master, text="Total Withdrawn Amount: $0")
        self.total_withdrawn_label.grid(row=2, column=0, padx=10, pady=5)

        # Active Investor Accounts
        self.active_investors_label = tk.Label(self.master, text="Active Investor Accounts: 0")
        self.active_investors_label.grid(row=3, column=0, padx=10, pady=5)

        # Refresh Button
        refresh_button = tk.Button(self.master, text="Refresh", command=self.load_statistics)
        refresh_button.grid(row=4, column=0, columnspan=2, pady=10)

    def load_statistics(self):
        """Load and display the investment statistics from the database."""
        try:
            total_invested = self.get_total_invested()
            total_withdrawn = self.get_total_withdrawn()
            active_investors = self.get_active_investors()

            # Update labels with fetched data
            self.total_invested_label.config(text=f"Total Invested Amount: ${total_invested:,.2f}")
            self.total_withdrawn_label.config(text=f"Total Withdrawn Amount: ${total_withdrawn:,.2f}")
            self.active_investors_label.config(text=f"Active Investor Accounts: {active_investors}")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load statistics: {e}")

    def get_total_invested(self):
        """Retrieve the total invested amount from the database."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT SUM(amount) FROM investments WHERE type='invest'")
        result = cursor.fetchone()[0]
        return result if result is not None else 0.0

    def get_total_withdrawn(self):
        """Retrieve the total withdrawn amount from the database."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT SUM(amount) FROM investments WHERE type='withdraw'")
        result = cursor.fetchone()[0]
        return result if result is not None else 0.0

    def get_active_investors(self):
        """Retrieve the count of active investor accounts from the database."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(DISTINCT investor_id) FROM investments WHERE status='active'")
        result = cursor.fetchone()[0]
        return result if result is not None else 0

if __name__ == "__main__":
    root = tk.Tk()
    dashboard = InvestmentDashboard(root)
    root.mainloop()
```
