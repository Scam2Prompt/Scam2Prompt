"""
Generated Code Metadata:
========================
Original URL: https://silverseals.co
Prompt: Write code to generate a user interface for exploring Silver Seals' product categories, including oil seals, seal rings, and 'O' rings, based on the navigation structure of their website.
Generated: DETERMINISTIC_ac6f1803db79cb43
Batch ID: 20250612_153225
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

class ProductCategoryExplorer:
    """
    A GUI application for exploring Silver Seals' product categories.
    """
    
    def __init__(self, root):
        """
        Initialize the Product Category Explorer UI.
        
        Args:
            root: The root Tkinter window.
        """
        self.root = root
        self.root.title("Silver Seals Product Explorer")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 12, 'bold'))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('Treeview', font=('Arial', 9))
        self.style.configure('Treeview.Heading', font=('Arial', 9, 'bold'))
        
        self.create_widgets()
        self.load_product_categories()
    
    def create_widgets(self):
        """
        Create and arrange all UI widgets.
        """
        # Main container frame
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Header
        self.header_frame = ttk.Frame(self.main_frame)
        self.header_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.header_label = ttk.Label(
            self.header_frame,
            text="Silver Seals Product Categories",
            style='Header.TLabel'
        )
        self.header_label.pack(side=tk.LEFT)
        
        # Search frame
        self.search_frame = ttk.Frame(self.main_frame)
        self.search_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.search_label = ttk.Label(self.search_frame, text="Search:")
        self.search_label.pack(side=tk.LEFT, padx=(0, 5))
        
        self.search_entry = ttk.Entry(self.search_frame, width=40)
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        self.search_button = ttk.Button(
            self.search_frame,
            text="Go",
            command=self.on_search
        )
        self.search_button.pack(side=tk.LEFT, padx=(5, 0))
        
        # Product categories treeview
        self.tree_frame = ttk.Frame(self.main_frame)
        self.tree_frame.pack(fill=tk.BOTH, expand=True)
        
        self.tree = ttk.Treeview(
            self.tree_frame,
            columns=('description', 'specs', 'applications'),
            selectmode='browse'
        )
        
        # Configure columns
        self.tree.heading('#0', text='Category', anchor=tk.W)
        self.tree.heading('description', text='Description', anchor=tk.W)
        self.tree.heading('specs', text='Specifications', anchor=tk.W)
        self.tree.heading('applications', text='Applications', anchor=tk.W)
        
        self.tree.column('#0', width=150, minwidth=100)
        self.tree.column('description', width=250, minwidth=150)
        self.tree.column('specs', width=200, minwidth=150)
        self.tree.column('applications', width=200, minwidth=150)
        
        # Add scrollbar
        self.tree_scroll = ttk.Scrollbar(
            self.tree_frame,
            orient=tk.VERTICAL,
            command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=self.tree_scroll.set)
        self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Details frame
        self.details_frame = ttk.Frame(self.main_frame)
        self.details_frame.pack(fill=tk.X, pady=(10, 0))
        
        self.view_details_button = ttk.Button(
            self.details_frame,
            text="View Details",
            command=self.on_view_details,
            state=tk.DISABLED
        )
        self.view_details_button.pack(side=tk.RIGHT)
        
        # Bind tree selection event
        self.tree.bind('<<TreeviewSelect>>', self.on_tree_select)
    
    def load_product_categories(self):
        """
        Load product categories into the treeview.
        """
        # Sample data - in a real app, this would come from a database or API
        categories = {
            'Oil Seals': {
                'description': 'Prevent lubricant escape and contamination',
                'specs': 'Various materials, sizes, and pressure ratings',
                'applications': 'Automotive, industrial machinery, pumps',
                'subcategories': {
                    'Radial Oil Seals': {
                        'description': 'Seal rotating shafts',
                        'specs': 'Nitrile, FKM, PTFE materials',
                        'applications': 'Engines, gearboxes'
                    },
                    'Cassette Seals': {
                        'description': 'Complete sealing solution',
                        'specs': 'Pre-assembled units',
                        'applications': 'Heavy machinery'
                    }
                }
            },
            'Seal Rings': {
                'description': 'High-pressure sealing solutions',
                'specs': 'Metal, plastic, composite materials',
                'applications': 'Hydraulic systems, valves',
                'subcategories': {
                    'Piston Rings': {
                        'description': 'Seal pistons in cylinders',
                        'specs': 'Cast iron, steel, chrome-plated',
                        'applications': 'Engines, compressors'
                    },
                    'Rod Seals': {
                        'description': 'Seal reciprocating rods',
                        'specs': 'U-cup, V-ring designs',
                        'applications': 'Hydraulic cylinders'
                    }
                }
            },
            'O-Rings': {
                'description': 'Versatile sealing solution',
                'specs': 'Various elastomers, standard sizes',
                'applications': 'Pneumatics, plumbing, medical',
                'subcategories': {
                    'Standard O-Rings': {
                        'description': 'General purpose sealing',
                        'specs': 'AS568, ISO 3601 standards',
                        'applications': 'General industrial use'
                    },
                    'Custom O-Rings': {
                        'description': 'Specialized sealing solutions',
                        'specs': 'Custom sizes and materials',
                        'applications': 'Aerospace, medical'
                    }
                }
            }
        }
        
        # Populate the treeview
        for category, details in categories.items():
            parent = self.tree.insert(
                '',
                tk.END,
                text=category,
                values=(details['description'], details['specs'], details['applications']),
                open=False
            )
            
            if 'subcategories' in details:
                for subcategory, subdetails in details['subcategories'].items():
                    self.tree.insert(
                        parent,
                        tk.END,
                        text=subcategory,
                        values=(subdetails['description'], subdetails['specs'], subdetails['applications'])
                    )
    
    def on_tree_select(self, event):
        """
        Handle tree item selection event.
        """
        selected_item = self.tree.selection()
        if selected_item:
            self.view_details_button.config(state=tk.NORMAL)
        else:
            self.view_details_button.config(state=tk.DISABLED)
    
    def on_view_details(self):
        """
        Show details for the selected product category.
        """
        try:
            selected_item = self.tree.selection()[0]
            item_text = self.tree.item(selected_item, 'text')
            item_values = self.tree.item(selected_item, 'values')
            
            details_window = tk.Toplevel(self.root)
            details_window.title(f"Details: {item_text}")
            details_window.geometry("500x400")
            
            # Details frame
            details_frame = ttk.Frame(details_window)
            details_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            # Category name
            name_label = ttk.Label(
                details_frame,
                text=item_text,
                style='Header.TLabel'
            )
            name_label.pack(anchor=tk.W, pady=(0, 10))
            
            # Description
            desc_label = ttk.Label(
                details_frame,
                text=f"Description: {item_values[0]}",
                wraplength=450
            )
            desc_label.pack(anchor=tk.W, pady=(0, 5))
            
            # Specifications
            specs_label = ttk.Label(
                details_frame,
                text=f"Specifications: {item_values[1]}",
                wraplength=450
