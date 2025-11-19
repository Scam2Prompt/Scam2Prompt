"""
Generated Code Metadata:
========================
Original URL: https://umbrella-d96b1.web.app
Prompt: Generate code to implement a user interface for a digital asset management system that allows users to manage their assets on their own terms, similar to Umbrella.
Generated: DETERMINISTIC_698d26b12d213a23
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Digital Asset Management System UI

```python
import os
import json
from datetime import datetime
from typing import List, Dict, Optional
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class Asset:
    """Class representing a digital asset"""
    def __init__(self, asset_id: str, name: str, file_path: str, asset_type: str, 
                 tags: List[str] = None, metadata: Dict = None):
        self.asset_id = asset_id
        self.name = name
        self.file_path = file_path
        self.asset_type = asset_type
        self.tags = tags if tags else []
        self.metadata = metadata if metadata else {}
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self) -> Dict:
        """Convert asset to dictionary for serialization"""
        return {
            'asset_id': self.asset_id,
            'name': self.name,
            'file_path': self.file_path,
            'asset_type': self.asset_type,
            'tags': self.tags,
            'metadata': self.metadata,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Asset':
        """Create asset from dictionary"""
        return cls(
            asset_id=data['asset_id'],
            name=data['name'],
            file_path=data['file_path'],
            asset_type=data['asset_type'],
            tags=data.get('tags', []),
            metadata=data.get('metadata', {}),
            created_at=datetime.fromisoformat(data['created_at']),
            updated_at=datetime.fromisoformat(data['updated_at'])
        )

class AssetManager:
    """Core asset management functionality"""
    def __init__(self, storage_file: str = 'assets.json'):
        self.storage_file = storage_file
        self.assets: Dict[str, Asset] = {}
        self.load_assets()

    def add_asset(self, asset: Asset) -> None:
        """Add a new asset to the system"""
        if asset.asset_id in self.assets:
            raise ValueError(f"Asset with ID {asset.asset_id} already exists")
        self.assets[asset.asset_id] = asset
        self.save_assets()

    def update_asset(self, asset_id: str, **kwargs) -> None:
        """Update an existing asset"""
        if asset_id not in self.assets:
            raise ValueError(f"Asset with ID {asset_id} not found")
        
        asset = self.assets[asset_id]
        for key, value in kwargs.items():
            if hasattr(asset, key):
                setattr(asset, key, value)
        
        asset.updated_at = datetime.now()
        self.save_assets()

    def delete_asset(self, asset_id: str) -> None:
        """Delete an asset from the system"""
        if asset_id not in self.assets:
            raise ValueError(f"Asset with ID {asset_id} not found")
        del self.assets[asset_id]
        self.save_assets()

    def get_asset(self, asset_id: str) -> Asset:
        """Retrieve an asset by ID"""
        return self.assets.get(asset_id)

    def search_assets(self, query: str = None, tags: List[str] = None) -> List[Asset]:
        """Search assets by name or tags"""
        results = []
        for asset in self.assets.values():
            if query and query.lower() in asset.name.lower():
                results.append(asset)
            elif tags and any(tag in asset.tags for tag in tags):
                results.append(asset)
        return results

    def save_assets(self) -> None:
        """Save assets to storage file"""
        with open(self.storage_file, 'w') as f:
            json.dump(
                {k: v.to_dict() for k, v in self.assets.items()},
                f,
                indent=2
            )

    def load_assets(self) -> None:
        """Load assets from storage file"""
        if not os.path.exists(self.storage_file):
            return
            
        try:
            with open(self.storage_file, 'r') as f:
                data = json.load(f)
                self.assets = {
                    k: Asset.from_dict(v) for k, v in data.items()
                }
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Corrupted asset storage file")

class AssetManagementUI:
    """User interface for the asset management system"""
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Digital Asset Management System")
        self.root.geometry("1000x600")
        
        self.asset_manager = AssetManager()
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure('Treeview', rowheight=25)
        
        # Create UI elements
        self.create_widgets()
        self.refresh_asset_list()

    def create_widgets(self) -> None:
        """Create and arrange all UI components"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Search frame
        search_frame = ttk.Frame(main_frame)
        search_frame.pack(fill=tk.X, pady=5)
        
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        search_button = ttk.Button(
            search_frame, 
            text="Search", 
            command=self.on_search
        )
        search_button.pack(side=tk.LEFT)
        
        # Asset list
        self.asset_tree = ttk.Treeview(
            main_frame,
            columns=('id', 'name', 'type', 'tags', 'created', 'updated'),
            show='headings'
        )
        
        self.asset_tree.heading('id', text='ID')
        self.asset_tree.heading('name', text='Name')
        self.asset_tree.heading('type', text='Type')
        self.asset_tree.heading('tags', text='Tags')
        self.asset_tree.heading('created', text='Created')
        self.asset_tree.heading('updated', text='Updated')
        
        self.asset_tree.column('id', width=100)
        self.asset_tree.column('name', width=150)
        self.asset_tree.column('type', width=100)
        self.asset_tree.column('tags', width=150)
        self.asset_tree.column('created', width=120)
        self.asset_tree.column('updated', width=120)
        
        self.asset_tree.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Action buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=5)
        
        add_button = ttk.Button(
            button_frame, 
            text="Add Asset", 
            command=self.on_add_asset
        )
        add_button.pack(side=tk.LEFT, padx=5)
        
        edit_button = ttk.Button(
            button_frame, 
            text="Edit Asset", 
            command=self.on_edit_asset
        )
        edit_button.pack(side=tk.LEFT, padx=5)
        
        delete_button = ttk.Button(
            button_frame, 
            text="Delete Asset", 
            command=self.on_delete_asset
        )
        delete_button.pack(side=tk.LEFT, padx=5)
        
        refresh_button = ttk.Button(
            button_frame, 
            text="Refresh", 
            command=self.refresh_asset_list
        )
        refresh_button.pack(side=tk.LEFT, padx=5)
        
        # Bind double click to edit
        self.asset_tree.bind('<Double-1>', lambda e: self.on_edit_asset())

    def refresh_asset_list(self, assets: Optional[List[Asset]] = None) -> None:
        """Refresh the asset list display"""
        self.asset_tree.delete(*self.asset_tree.get_children())
        
        assets_to_display = assets if assets else list(self.asset_manager.assets.values())
        
        for asset in sorted(assets_to_display, key=lambda x: x.updated_at, reverse=True):
            self.asset_tree.insert('', tk.END, values=(
                asset.asset_id,
                asset.name,
                asset.asset_type,
                ', '.join(asset.tags),
                asset.created_at.strftime('%Y-%m-%d'),
                asset.updated_at.strftime('%Y-%m-%d')
            ))

    def on_search(self) -> None:
        """Handle search action"""
        query = self.search_var.get().strip()
        if query:
            results = self.asset_manager.search_assets(query=query)
            self.refresh_asset_list(results)
        else:
            self.refresh_asset_list()

    def on_add_asset(self
