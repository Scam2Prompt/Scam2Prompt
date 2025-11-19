"""
Generated Code Metadata:
========================
Original URL: https://bafybeiaoni35loah6mxudvrxltj6qkb5afmoqjqbg2spapid2kltvnqvby.ipfs.dweb.link
Prompt: "Design a simple user interface for a DeFi lending platform using NAVI Protocol's features, including supply limits, debt ceilings, and multiple oracle security."
Generated: DETERMINISTIC_4cb8a3b7a4323827
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import ttk, messagebox
from typing import Dict, Optional

class NAVIDeFiLendingUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("NAVI Protocol DeFi Lending Platform")
        self.root.geometry("800x600")
        
        # Initialize protocol parameters
        self.supply_limits: Dict[str, float] = {}
        self.debt_ceilings: Dict[str, float] = {}
        self.oracles: Dict[str, bool] = {}  # Oracle name: is_active
        
        self.setup_ui()
        self.load_default_values()
    
    def setup_ui(self):
        """Initialize all UI components."""
        # Main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Notebook for different sections
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Supply Limits Tab
        self.setup_supply_limits_tab()
        
        # Debt Ceilings Tab
        self.setup_debt_ceilings_tab()
        
        # Oracle Security Tab
        self.setup_oracle_security_tab()
        
        # Status Bar
        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN)
        self.status_bar.pack(fill=tk.X)
        self.update_status("Ready")
    
    def setup_supply_limits_tab(self):
        """Configure the supply limits management tab."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Supply Limits")
        
        # Treeview for displaying supply limits
        columns = ("asset", "limit")
        self.supply_tree = ttk.Treeview(tab, columns=columns, show="headings")
        self.supply_tree.heading("asset", text="Asset")
        self.supply_tree.heading("limit", text="Supply Limit")
        self.supply_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Controls frame
        controls_frame = ttk.Frame(tab)
        controls_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(controls_frame, text="Asset:").pack(side=tk.LEFT)
        self.asset_entry = ttk.Entry(controls_frame, width=15)
        self.asset_entry.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(controls_frame, text="Limit:").pack(side=tk.LEFT)
        self.limit_entry = ttk.Entry(controls_frame, width=15)
        self.limit_entry.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            controls_frame, 
            text="Set Limit", 
            command=self.set_supply_limit
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            controls_frame,
            text="Remove Asset",
            command=self.remove_supply_limit
        ).pack(side=tk.LEFT, padx=5)
    
    def setup_debt_ceilings_tab(self):
        """Configure the debt ceilings management tab."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Debt Ceilings")
        
        # Treeview for displaying debt ceilings
        columns = ("asset", "ceiling")
        self.debt_tree = ttk.Treeview(tab, columns=columns, show="headings")
        self.debt_tree.heading("asset", text="Asset")
        self.debt_tree.heading("ceiling", text="Debt Ceiling")
        self.debt_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Controls frame
        controls_frame = ttk.Frame(tab)
        controls_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(controls_frame, text="Asset:").pack(side=tk.LEFT)
        self.debt_asset_entry = ttk.Entry(controls_frame, width=15)
        self.debt_asset_entry.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(controls_frame, text="Ceiling:").pack(side=tk.LEFT)
        self.ceiling_entry = ttk.Entry(controls_frame, width=15)
        self.ceiling_entry.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            controls_frame, 
            text="Set Ceiling", 
            command=self.set_debt_ceiling
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            controls_frame,
            text="Remove Asset",
            command=self.remove_debt_ceiling
        ).pack(side=tk.LEFT, padx=5)
    
    def setup_oracle_security_tab(self):
        """Configure the oracle security management tab."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Oracle Security")
        
        # Treeview for displaying oracles
        columns = ("oracle", "status")
        self.oracle_tree = ttk.Treeview(tab, columns=columns, show="headings")
        self.oracle_tree.heading("oracle", text="Oracle")
        self.oracle_tree.heading("status", text="Status")
        self.oracle_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Controls frame
        controls_frame = ttk.Frame(tab)
        controls_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(controls_frame, text="Oracle:").pack(side=tk.LEFT)
        self.oracle_entry = ttk.Entry(controls_frame, width=15)
        self.oracle_entry.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            controls_frame, 
            text="Add Oracle", 
            command=self.add_oracle
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            controls_frame,
            text="Toggle Status",
            command=self.toggle_oracle_status
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            controls_frame,
            text="Remove Oracle",
            command=self.remove_oracle
        ).pack(side=tk.LEFT, padx=5)
    
    def load_default_values(self):
        """Load default values for demonstration purposes."""
        # Default supply limits
        self.supply_limits = {
            "ETH": 10000.0,
            "BTC": 5000.0,
            "USDC": 50000.0
        }
        self.update_supply_tree()
        
        # Default debt ceilings
        self.debt_ceilings = {
            "ETH": 5000.0,
            "BTC": 2500.0,
            "USDC": 25000.0
        }
        self.update_debt_tree()
        
        # Default oracles
        self.oracles = {
            "Chainlink": True,
            "Band Protocol": True,
            "NAVI Oracle": False
        }
        self.update_oracle_tree()
    
    def update_supply_tree(self):
        """Update the supply limits treeview with current data."""
        self.supply_tree.delete(*self.supply_tree.get_children())
        for asset, limit in self.supply_limits.items():
            self.supply_tree.insert("", tk.END, values=(asset, limit))
    
    def update_debt_tree(self):
        """Update the debt ceilings treeview with current data."""
        self.debt_tree.delete(*self.debt_tree.get_children())
        for asset, ceiling in self.debt_ceilings.items():
            self.debt_tree.insert("", tk.END, values=(asset, ceiling))
    
    def update_oracle_tree(self):
        """Update the oracle treeview with current data."""
        self.oracle_tree.delete(*self.oracle_tree.get_children())
        for oracle, status in self.oracles.items():
            status_text = "Active" if status else "Inactive"
            self.oracle_tree.insert("", tk.END, values=(oracle, status_text))
    
    def update_status(self, message: str):
        """Update the status bar with the given message."""
        self.status_var.set(message)
    
    def validate_float_input(self, value: str) -> Optional[float]:
        """Validate and convert string input to float."""
        try:
            return float(value)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number")
            return None
    
    def set_supply_limit(self):
        """Set a new supply limit for an asset."""
        asset = self
