"""
Generated Code Metadata:
========================
Original URL: https://buildonbeam-7h0.pages.dev
Prompt: Design a user interface for the Beam Market, BeamOS's native marketplace.
Generated: DETERMINISTIC_74484bf9239fb7f4
Batch ID: 20250622_205117
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
from PIL import Image, ImageTk
import os

class BeamMarketApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Beam Market - BeamOS Marketplace")
        self.root.geometry("1200x800")
        self.root.resizable(True, True)
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TButton', padding=6, font=('Helvetica', 10))
        self.style.configure('TLabel', background='#f0f0f0', font=('Helvetica', 10))
        self.style.configure('Header.TLabel', font=('Helvetica', 14, 'bold'))
        
        # Create main container
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        self.create_header()
        
        # Main content
        self.create_main_content()
        
        # Footer
        self.create_footer()
        
        # Load sample data
        self.apps = self.load_sample_data()
        self.update_app_list()
    
    def create_header(self):
        header_frame = ttk.Frame(self.main_frame, style='TFrame')
        header_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Logo
        logo_image = Image.new('RGB', (50, 50), color='#4a90e2')
        logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = ttk.Label(header_frame, image=logo_photo)
        logo_label.image = logo_photo
        logo_label.pack(side=tk.LEFT)
        
        # Title
        title_label = ttk.Label(header_frame, text="Beam Market", style='Header.TLabel')
        title_label.pack(side=tk.LEFT, padx=10)
        
        # Search bar
        search_frame = ttk.Frame(header_frame)
        search_frame.pack(side=tk.RIGHT, fill=tk.X, expand=True)
        
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        search_button = ttk.Button(search_frame, text="Search", command=self.on_search)
        search_button.pack(side=tk.LEFT)
    
    def create_main_content(self):
        content_frame = ttk.Frame(self.main_frame)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Categories sidebar
        sidebar_frame = ttk.Frame(content_frame, width=200)
        sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        categories = ["All", "Productivity", "Games", "Utilities", "Development", "Education"]
        for category in categories:
            btn = ttk.Button(sidebar_frame, text=category, 
                            command=lambda c=category: self.filter_by_category(c))
            btn.pack(fill=tk.X, pady=2)
        
        # Apps list
        apps_frame = ttk.Frame(content_frame)
        apps_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
        
        # Canvas and scrollbar for apps
        self.canvas = tk.Canvas(apps_frame, borderwidth=0)
        scrollbar = ttk.Scrollbar(apps_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mousewheel to scroll
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)
    
    def create_footer(self):
        footer_frame = ttk.Frame(self.main_frame)
        footer_frame.pack(fill=tk.X, padx=10, pady=10)
        
        status_label = ttk.Label(footer_frame, text="Beam Market v1.0 - © 2023 BeamOS")
        status_label.pack(side=tk.LEFT)
        
        update_button = ttk.Button(footer_frame, text="Check for Updates", command=self.check_for_updates)
        update_button.pack(side=tk.RIGHT)
    
    def load_sample_data(self):
        return [
            {"name": "Beam Writer", "category": "Productivity", "rating": 4.5, "price": 0, "installed": False},
            {"name": "Beam Terminal", "category": "Utilities", "rating": 4.8, "price": 0, "installed": True},
            {"name": "Space Explorer", "category": "Games", "rating": 4.2, "price": 9.99, "installed": False},
            {"name": "Code Beam", "category": "Development", "rating": 4.7, "price": 0, "installed": False},
            {"name": "Math Tutor", "category": "Education", "rating": 3.9, "price": 4.99, "installed": False},
            {"name": "Beam Browser", "category": "Utilities", "rating": 4.3, "price": 0, "installed": True},
            {"name": "Pixel Painter", "category": "Productivity", "rating": 4.0, "price": 2.99, "installed": False},
            {"name": "System Monitor", "category": "Utilities", "rating": 4.6, "price": 0, "installed": False},
        ]
    
    def update_app_list(self, apps=None):
        # Clear current apps
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        apps_to_show = apps if apps else self.apps
        
        for app in apps_to_show:
            self.create_app_card(app)
    
    def create_app_card(self, app):
        card_frame = ttk.Frame(self.scrollable_frame, borderwidth=1, relief="solid", padding=10)
        card_frame.pack(fill=tk.X, pady=5)
        
        # App icon
        icon_image = Image.new('RGB', (64, 64), color='#e0e0e0')
        icon_photo = ImageTk.PhotoImage(icon_image)
        icon_label = ttk.Label(card_frame, image=icon_photo)
        icon_label.image = icon_photo
        icon_label.pack(side=tk.LEFT)
        
        # App info
        info_frame = ttk.Frame(card_frame)
        info_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
        
        name_label = ttk.Label(info_frame, text=app["name"], font=('Helvetica', 12, 'bold'))
        name_label.pack(anchor=tk.W)
        
        category_label = ttk.Label(info_frame, text=f"Category: {app['category']}")
        category_label.pack(anchor=tk.W)
        
        rating_label = ttk.Label(info_frame, text=f"Rating: {'★' * int(app['rating'])} ({app['rating']})")
        rating_label.pack(anchor=tk.W)
        
        price_text = "Free" if app["price"] == 0 else f"${app['price']}"
        price_label = ttk.Label(info_frame, text=f"Price: {price_text}")
        price_label.pack(anchor=tk.W)
        
        # Action buttons
        action_frame = ttk.Frame(card_frame)
        action_frame.pack(side=tk.RIGHT, fill=tk.Y)
        
        if app["installed"]:
            action_button = ttk.Button(action_frame, text="Uninstall", 
                                     command=lambda a=app: self.uninstall_app(a))
        else:
            action_button = ttk.Button(action_frame, text="Install", 
                                    command=lambda a=app: self.install_app(a))
        
        action_button.pack(pady=5)
        
        details_button = ttk.Button(action_frame, text="Details", 
                                  command=lambda a=app: self.show_app_details(a))
        details_button.pack(pady=5)
    
    def filter_by_category(self, category):
        if category == "All":
            self.update_app_list()
        else:
            filtered_apps = [app for app
