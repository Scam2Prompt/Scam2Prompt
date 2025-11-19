"""
Generated Code Metadata:
========================
Original URL: https://sjkjs-2ct.pages.dev
Prompt: Create a user interface component for displaying a list of verified guilds, with features like filtering and sorting, similar to the Guildhall explore page.
Generated: DETERMINISTIC_fe49920ffe1241dd
Batch ID: 20250622_212724
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

class GuildExplorer:
    """
    A UI component for displaying and exploring verified guilds with filtering and sorting capabilities.
    """
    
    def __init__(self, master: tk.Tk, guilds_data: List[Dict]):
        """
        Initialize the GuildExplorer component.
        
        Args:
            master: The parent tkinter window
            guilds_data: List of guild dictionaries containing guild information
        """
        self.master = master
        self.guilds_data = guilds_data
        self.filtered_guilds = guilds_data.copy()
        
        self.setup_ui()
        self.populate_guilds()
    
    def setup_ui(self) -> None:
        """Setup the main UI components."""
        self.frame = ttk.Frame(self.master, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Filter controls
        filter_frame = ttk.LabelFrame(self.frame, text="Filters", padding="10")
        filter_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Category filter
        ttk.Label(filter_frame, text="Category:").grid(row=0, column=0, sticky=tk.W)
        self.category_var = tk.StringVar()
        self.category_dropdown = ttk.Combobox(
            filter_frame,
            textvariable=self.category_var,
            state="readonly"
        )
        self.category_dropdown.grid(row=0, column=1, sticky=tk.EW, padx=5)
        self.category_dropdown.bind("<<ComboboxSelected>>", self.apply_filters)
        
        # Language filter
        ttk.Label(filter_frame, text="Language:").grid(row=1, column=0, sticky=tk.W)
        self.language_var = tk.StringVar()
        self.language_dropdown = ttk.Combobox(
            filter_frame,
            textvariable=self.language_var,
            state="readonly"
        )
        self.language_dropdown.grid(row=1, column=1, sticky=tk.EW, padx=5)
        self.language_dropdown.bind("<<ComboboxSelected>>", self.apply_filters)
        
        # Search filter
        ttk.Label(filter_frame, text="Search:").grid(row=2, column=0, sticky=tk.W)
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(filter_frame, textvariable=self.search_var)
        search_entry.grid(row=2, column=1, sticky=tk.EW, padx=5)
        search_entry.bind("<KeyRelease>", self.apply_filters)
        
        # Initialize filter options
        self.initialize_filter_options()
        
        # Sort controls
        sort_frame = ttk.LabelFrame(self.frame, text="Sort", padding="10")
        sort_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(sort_frame, text="Sort by:").grid(row=0, column=0, sticky=tk.W)
        self.sort_var = tk.StringVar(value="name")
        sort_options = ["name", "members", "created_date"]
        self.sort_dropdown = ttk.Combobox(
            sort_frame,
            textvariable=self.sort_var,
            values=sort_options,
            state="readonly"
        )
        self.sort_dropdown.grid(row=0, column=1, sticky=tk.EW, padx=5)
        self.sort_dropdown.bind("<<ComboboxSelected>>", self.sort_guilds)
        
        self.sort_order_var = tk.StringVar(value="asc")
        ttk.Radiobutton(
            sort_frame,
            text="Ascending",
            variable=self.sort_order_var,
            value="asc",
            command=self.sort_guilds
        ).grid(row=0, column=2, padx=5)
        ttk.Radiobutton(
            sort_frame,
            text="Descending",
            variable=self.sort_order_var,
            value="desc",
            command=self.sort_guilds
        ).grid(row=0, column=3, padx=5)
        
        # Guilds display
        self.guilds_frame = ttk.Frame(self.frame)
        self.guilds_frame.pack(fill=tk.BOTH, expand=True)
        
        # Treeview for guild listing
        columns = ("name", "category", "language", "members", "created")
        self.tree = ttk.Treeview(
            self.guilds_frame,
            columns=columns,
            show="headings",
            selectmode="browse"
        )
        
        # Configure columns
        self.tree.heading("name", text="Name", command=lambda: self.sort_guilds("name"))
        self.tree.heading("category", text="Category", command=lambda: self.sort_guilds("category"))
        self.tree.heading("language", text="Language", command=lambda: self.sort_guilds("language"))
        self.tree.heading("members", text="Members", command=lambda: self.sort_guilds("members"))
        self.tree.heading("created", text="Created", command=lambda: self.sort_guilds("created_date"))
        
        self.tree.column("name", width=200)
        self.tree.column("category", width=150)
        self.tree.column("language", width=100)
        self.tree.column("members", width=80)
        self.tree.column("created", width=100)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.guilds_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status_var = tk.StringVar(value=f"Showing {len(self.filtered_guilds)} guilds")
        ttk.Label(self.frame, textvariable=self.status_var).pack(side=tk.BOTTOM, fill=tk.X)
    
    def initialize_filter_options(self) -> None:
        """Initialize the available filter options from guild data."""
        categories = sorted({guild.get("category", "") for guild in self.guilds_data if guild.get("category")})
        languages = sorted({guild.get("language", "") for guild in self.guilds_data if guild.get("language")})
        
        self.category_dropdown["values"] = ["All"] + categories
        self.category_var.set("All")
        
        self.language_dropdown["values"] = ["All"] + languages
        self.language_var.set("All")
    
    def apply_filters(self, event: Optional[tk.Event] = None) -> None:
        """Apply all active filters to the guild list."""
        category_filter = self.category_var.get()
        language_filter = self.language_var.get()
        search_term = self.search_var.get().lower()
        
        self.filtered_guilds = [
            guild for guild in self.guilds_data
            if (category_filter == "All" or guild.get("category", "") == category_filter)
            and (language_filter == "All" or guild.get("language", "") == language_filter)
            and (search_term == "" or search_term in guild.get("name", "").lower())
        ]
        
        self.sort_guilds()
        self.update_status()
    
    def sort_guilds(self, sort_key: Optional[str] = None) -> None:
        """Sort the guilds based on the current sort criteria."""
        if sort_key is None:
            sort_key = self.sort_var.get()
        else:
            self.sort_var.set(sort_key)
        
        reverse = self.sort_order_var.get() == "desc"
        
        if sort_key == "name":
            self.filtered_guilds.sort(key=lambda x: x.get("name", "").lower(), reverse=reverse)
        elif sort_key == "category":
            self.filtered_guilds.sort(key=lambda x: x.get("category", "").lower(), reverse=reverse)
        elif sort_key == "language":
            self.filtered_guilds.sort(key=lambda x: x.get("language", "").lower(), reverse=reverse)
        elif sort_key == "members":
            self.filtered_guilds.sort(key=lambda x: x.get("members", 0), reverse=reverse)
        elif sort_key == "created_date":
            self.filtered_guilds.sort(key=lambda x: x.get("created_date", ""), reverse=reverse)
        
        self.populate_guilds()
    
    def populate_guilds(self) -> None:
        """Populate the treeview with the filtered and sorted guilds."""
        self.tree.delete(*self.tree.get_children())
        
        for guild in self.filtered_guilds:
            self.tree.insert("", tk.END, values=(
                guild.get("name", ""),
                guild.get("category", ""),
                guild.get("language", ""),
                guild.get("members", 0),
                guild.get("created_date", "")
            ))
    
    def update_status(self) -> None:
        """
