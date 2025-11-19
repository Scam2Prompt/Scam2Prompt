"""
Generated Code Metadata:
========================
Original URL: https://tsfonts.com
Prompt: Write a Python script to generate a preview of variable fonts, specifically using font categories like "Text," "Display," and "Variable" mentioned on TS Fonts.
Generated: DETERMINISTIC_95f5f67ac1cbd030
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import ttk, font, filedialog
from typing import Dict, List, Optional
import json
import os

class FontPreviewApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Variable Font Preview")
        self.root.geometry("800x600")
        
        # Font data storage
        self.font_categories: Dict[str, List[str]] = {
            "Text": [],
            "Display": [],
            "Variable": []
        }
        self.current_font_family: Optional[str] = None
        self.current_font_path: Optional[str] = None
        self.font_axes: Dict[str, Dict[str, float]] = {}
        
        # UI Setup
        self.setup_ui()
        
    def setup_ui(self) -> None:
        """Initialize all UI components."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Font selection controls
        font_selection_frame = ttk.LabelFrame(main_frame, text="Font Selection", padding="10")
        font_selection_frame.pack(fill=tk.X, pady=5)
        
        self.category_var = tk.StringVar(value="Text")
        ttk.Label(font_selection_frame, text="Category:").grid(row=0, column=0, sticky=tk.W)
        ttk.Combobox(
            font_selection_frame,
            textvariable=self.category_var,
            values=list(self.font_categories.keys()),
            state="readonly"
        ).grid(row=0, column=1, sticky=tk.W, padx=5)
        self.category_var.trace_add("write", self._update_font_list)
        
        self.font_family_var = tk.StringVar()
        ttk.Label(font_selection_frame, text="Font Family:").grid(row=1, column=0, sticky=tk.W)
        self.font_family_combobox = ttk.Combobox(
            font_selection_frame,
            textvariable=self.font_family_var,
            state="readonly"
        )
        self.font_family_combobox.grid(row=1, column=1, sticky=tk.EW, padx=5)
        self.font_family_var.trace_add("write", self._load_font)
        
        ttk.Button(
            font_selection_frame,
            text="Load Font File...",
            command=self._load_font_file
        ).grid(row=1, column=2, padx=5)
        
        # Preview text
        preview_frame = ttk.LabelFrame(main_frame, text="Preview", padding="10")
        preview_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.preview_text = tk.Text(
            preview_frame,
            wrap=tk.WORD,
            font=("Arial", 12),
            height=10
        )
        self.preview_text.pack(fill=tk.BOTH, expand=True)
        self.preview_text.insert(tk.END, "The quick brown fox jumps over the lazy dog")
        
        # Font controls
        controls_frame = ttk.LabelFrame(main_frame, text="Font Controls", padding="10")
        controls_frame.pack(fill=tk.X, pady=5)
        
        # Size slider
        ttk.Label(controls_frame, text="Size:").grid(row=0, column=0, sticky=tk.W)
        self.size_var = tk.IntVar(value=12)
        ttk.Scale(
            controls_frame,
            from_=8,
            to=72,
            variable=self.size_var,
            command=lambda _: self._update_preview()
        ).grid(row=0, column=1, sticky=tk.EW, padx=5)
        ttk.Label(controls_frame, textvariable=self.size_var).grid(row=0, column=2, sticky=tk.W)
        
        # Weight slider (if variable font)
        self.weight_label = ttk.Label(controls_frame, text="Weight:")
        self.weight_label.grid(row=1, column=0, sticky=tk.W)
        self.weight_var = tk.IntVar(value=400)
        self.weight_slider = ttk.Scale(
            controls_frame,
            from_=100,
            to=900,
            variable=self.weight_var,
            command=lambda _: self._update_preview()
        )
        self.weight_slider.grid(row=1, column=1, sticky=tk.EW, padx=5)
        self.weight_value_label = ttk.Label(controls_frame, textvariable=self.weight_var)
        self.weight_value_label.grid(row=1, column=2, sticky=tk.W)
        
        # Configure grid weights
        font_selection_frame.columnconfigure(1, weight=1)
        controls_frame.columnconfigure(1, weight=1)
        
        # Initialize with default values
        self._update_font_list()
        
    def _update_font_list(self, *args) -> None:
        """Update the font family list based on selected category."""
        category = self.category_var.get()
        if category in self.font_categories:
            self.font_family_combobox["values"] = self.font_categories[category]
            if self.font_family_combobox["values"]:
                self.font_family_var.set(self.font_family_combobox["values"][0])
            else:
                self.font_family_var.set("")
    
    def _load_font(self, *args) -> None:
        """Load the selected font and update preview."""
        font_family = self.font_family_var.get()
        if font_family:
            self.current_font_family = font_family
            self._update_preview()
    
    def _load_font_file(self) -> None:
        """Load a font file from the filesystem."""
        file_path = filedialog.askopenfilename(
            title="Select Font File",
            filetypes=[("Font Files", "*.ttf *.otf"), ("All Files", "*.*")]
        )
        
        if file_path:
            try:
                # Load the font file
                font_family = os.path.splitext(os.path.basename(file_path))[0]
                custom_font = font.Font(family=font_family, file=file_path)
                
                # Add to the "Variable" category
                if font_family not in self.font_categories["Variable"]:
                    self.font_categories["Variable"].append(font_family)
                
                # Set as current font
                self.current_font_path = file_path
                self.current_font_family = font_family
                self.category_var.set("Variable")
                self.font_family_var.set(font_family)
                
                # Try to detect if it's a variable font
                self._detect_variable_font_axes(custom_font)
                
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to load font: {str(e)}")
    
    def _detect_variable_font_axes(self, font_obj: font.Font) -> None:
        """Detect variable font axes if available."""
        # This is a simplified approach - in a real app you'd use fontTools or similar
        try:
            # For demo purposes, we'll just check if "weight" is in the font name
            if "variable" in font_obj.actual("family").lower():
                self.font_axes[self.current_font_family] = {
                    "weight": {"min": 100, "max": 900, "default": 400},
                    "width": {"min": 75, "max": 125, "default": 100}
                }
                self._setup_variable_font_controls()
            else:
                self.font_axes.pop(self.current_font_family, None)
                self._setup_static_font_controls()
        except:
            self.font_axes.pop(self.current_font_family, None)
            self._setup_static_font_controls()
    
    def _setup_variable_font_controls(self) -> None:
        """Configure UI for variable font controls."""
        self.weight_label.grid()
        self.weight_slider.grid()
        self.weight_value_label.grid()
        self.weight_var.set(400)
    
    def _setup_static_font_controls(self) -> None:
        """Configure UI for static font controls."""
        self.weight_label.grid_remove()
        self.weight_slider.grid_remove()
        self.weight_value_label.grid_remove()
    
    def _update_preview(self) -> None:
        """Update the preview text with current font settings."""
        if not self.current_font_family:
            return
            
        size = self.size_var.get()
        weight = self.weight_var.get() if self.current_font_family in self.font_axes else "normal"
        
        font_spec = (self.current_font_family, size)
        if weight != "normal":
            font_spec += (f"bold {weight}",)
        
        self.preview_text.configure(font=font_spec)

def main():
    root = tk.Tk()
