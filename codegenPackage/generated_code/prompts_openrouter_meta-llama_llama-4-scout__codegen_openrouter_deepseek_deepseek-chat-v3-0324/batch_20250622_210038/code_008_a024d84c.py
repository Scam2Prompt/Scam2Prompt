"""
Generated Code Metadata:
========================
Original URL: https://artyfact-game-6gr.pages.dev
Prompt: "Suggest improvements to the user interface for Artyfact's virtual events, such as NFT exhibitions and eSport tournaments, to enhance user engagement."
Generated: DETERMINISTIC_a024d84ce74fb39d
Batch ID: 20250622_210038
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
import webbrowser
from PIL import Image, ImageTk
import json
import os

class VirtualEventUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Artyfact Virtual Events")
        self.root.geometry("1200x800")
        self.root.configure(bg="#1a1a2e")
        
        # Load configuration
        self.load_config()
        
        # Initialize UI
        self.setup_ui()
        
    def load_config(self):
        """Load UI configuration from file"""
        try:
            with open('config.json') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = {
                "theme": "dark",
                "font_size": 12,
                "default_view": "featured"
            }
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid configuration file")
            self.config = {
                "theme": "dark",
                "font_size": 12,
                "default_view": "featured"
            }
    
    def setup_ui(self):
        """Setup main UI components"""
        # Header
        self.header_frame = tk.Frame(self.root, bg="#16213e")
        self.header_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.logo_img = self.load_image("logo.png", (150, 50))
        self.logo_label = tk.Label(self.header_frame, image=self.logo_img, bg="#16213e")
        self.logo_label.pack(side=tk.LEFT, padx=10)
        
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(
            self.header_frame,
            textvariable=self.search_var,
            width=40
        )
        self.search_entry.pack(side=tk.LEFT, padx=10)
        self.search_entry.bind("<Return>", self.search_events)
        
        self.search_btn = ttk.Button(
            self.header_frame,
            text="Search",
            command=self.search_events
        )
        self.search_btn.pack(side=tk.LEFT, padx=5)
        
        # Navigation
        self.nav_frame = tk.Frame(self.root, bg="#1a1a2e")
        self.nav_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.nav_buttons = []
        for tab in ["Featured", "NFT Exhibitions", "eSports", "Live Events", "My Tickets"]:
            btn = ttk.Button(
                self.nav_frame,
                text=tab,
                command=lambda t=tab.lower().replace(" ", "_"): self.show_tab(t)
            )
            btn.pack(side=tk.LEFT, padx=5)
            self.nav_buttons.append(btn)
        
        # Main content
        self.content_frame = tk.Frame(self.root, bg="#1a1a2e")
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        self.status_bar = ttk.Label(
            self.root,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_bar.pack(fill=tk.X, padx=10, pady=5)
        
        # Show default tab
        self.show_tab(self.config["default_view"])
    
    def load_image(self, path, size):
        """Load and resize image"""
        try:
            img = Image.open(path)
            img = img.resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img)
        except FileNotFoundError:
            # Return placeholder if image not found
            img = Image.new('RGB', size, color="#16213e")
            return ImageTk.PhotoImage(img)
    
    def show_tab(self, tab_name):
        """Display content for selected tab"""
        # Clear current content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Show appropriate content
        if tab_name == "featured":
            self.show_featured()
        elif tab_name == "nft_exhibitions":
            self.show_nft_exhibitions()
        elif tab_name == "esports":
            self.show_esports()
        elif tab_name == "live_events":
            self.show_live_events()
        elif tab_name == "my_tickets":
            self.show_my_tickets()
        
        self.status_var.set(f"Showing {tab_name.replace('_', ' ')}")
    
    def show_featured(self):
        """Display featured events"""
        title = ttk.Label(
            self.content_frame,
            text="Featured Events",
            font=("Helvetica", 16, "bold"),
            background="#1a1a2e",
            foreground="#ffffff"
        )
        title.pack(pady=10)
        
        # Event cards container
        cards_frame = tk.Frame(self.content_frame, bg="#1a1a2e")
        cards_frame.pack(fill=tk.BOTH, expand=True)
        
        # Sample featured events
        featured_events = [
            {
                "title": "Digital Art Gallery",
                "type": "NFT Exhibition",
                "date": "Oct 15-30, 2023",
                "image": "event1.jpg"
            },
            {
                "title": "Global eSports Championship",
                "type": "Tournament",
                "date": "Nov 5-7, 2023",
                "image": "event2.jpg"
            },
            {
                "title": "Metaverse Concert",
                "type": "Live Event",
                "date": "Dec 10, 2023",
                "image": "event3.jpg"
            }
        ]
        
        for i, event in enumerate(featured_events):
            card = self.create_event_card(cards_frame, event)
            card.grid(row=0, column=i, padx=10, pady=5, sticky="nsew")
            cards_frame.columnconfigure(i, weight=1)
    
    def create_event_card(self, parent, event_data):
        """Create an event card widget"""
        card = tk.Frame(
            parent,
            bg="#16213e",
            bd=2,
            relief=tk.RAISED
        )
        
        try:
            img = self.load_image(event_data["image"], (250, 150))
            img_label = tk.Label(card, image=img, bg="#16213e")
            img_label.image = img  # Keep reference
            img_label.pack(padx=5, pady=5)
        except Exception as e:
            print(f"Error loading image: {e}")
            placeholder = tk.Label(card, text="Image not available", bg="#16213e", fg="white")
            placeholder.pack(padx=5, pady=5)
        
        title = tk.Label(
            card,
            text=event_data["title"],
            bg="#16213e",
            fg="white",
            font=("Helvetica", 12, "bold"),
            wraplength=240
        )
        title.pack(padx=5, pady=(5, 0))
        
        event_type = tk.Label(
            card,
            text=event_data["type"],
            bg="#16213e",
            fg="#4cc9f0",
            font=("Helvetica", 10)
        )
        event_type.pack(padx=5)
        
        date = tk.Label(
            card,
            text=event_data["date"],
            bg="#16213e",
            fg="#a5a5a5",
            font=("Helvetica", 10)
        )
        date.pack(padx=5, pady=(0, 5))
        
        btn = ttk.Button(
            card,
            text="View Details",
            command=lambda: self.show_event_details(event_data)
        )
        btn.pack(padx=5, pady=(0, 10))
        
        return card
    
    def show_event_details(self, event_data):
        """Show detailed view for an event"""
        # Clear current content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Back button
        back_btn = ttk.Button(
            self.content_frame,
            text="← Back",
            command=lambda: self.show_tab(self.config["default_view"])
        )
        back_btn.pack(anchor=tk.NW, padx=10, pady=10)
        
        # Event details container
        details_frame = tk.Frame(self.content_frame, bg="#1a1a2e")
        details_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Left column - image
        img_frame = tk.Frame(details_frame, bg="#1a1a2e")
        img_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10
