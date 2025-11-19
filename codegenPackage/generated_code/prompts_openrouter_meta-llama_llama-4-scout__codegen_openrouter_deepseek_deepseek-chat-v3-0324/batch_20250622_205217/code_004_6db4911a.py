"""
Generated Code Metadata:
========================
Original URL: https://www.brothernz.com
Prompt: Develop a simple program to design and send embroidery patterns to a Brother embroidery machine using the PE Design software.
Generated: DETERMINISTIC_6db4911a2bde96d5
Batch ID: 20250622_205217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import struct
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageTk

class EmbroideryPatternDesigner:
    """
    A simple GUI application to design and export embroidery patterns
    compatible with Brother PE Design software.
    """
    
    def __init__(self, root):
        self.root = root
        self.root.title("Embroidery Pattern Designer")
        self.root.geometry("800x600")
        
        # Canvas setup
        self.canvas = tk.Canvas(self.root, width=600, height=500, bg="white")
        self.canvas.pack(side=tk.LEFT, padx=10, pady=10)
        
        # Control panel
        self.control_panel = tk.Frame(self.root)
        self.control_panel.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Tools
        self.current_tool = "stitch"
        self.color = "black"
        self.stitches = []
        
        # Initialize UI
        self._init_ui()
        
        # Bind events
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<B1-Motion>", self.on_canvas_drag)
        
    def _init_ui(self):
        """Initialize the user interface components."""
        # Tool selection
        tk.Label(self.control_panel, text="Tools").pack()
        self.tool_var = tk.StringVar(value="stitch")
        tk.Radiobutton(self.control_panel, text="Stitch", variable=self.tool_var, 
                      value="stitch", command=self.select_tool).pack(anchor=tk.W)
        tk.Radiobutton(self.control_panel, text="Move", variable=self.tool_var, 
                      value="move", command=self.select_tool).pack(anchor=tk.W)
        
        # Color selection
        tk.Label(self.control_panel, text="Color").pack()
        self.color_var = tk.StringVar(value="black")
        colors = ["black", "red", "blue", "green", "yellow"]
        for color in colors:
            tk.Radiobutton(self.control_panel, text=color.capitalize(), 
                          variable=self.color_var, value=color, 
                          command=self.select_color).pack(anchor=tk.W)
        
        # Action buttons
        tk.Button(self.control_panel, text="Clear Canvas", 
                 command=self.clear_canvas).pack(fill=tk.X, pady=5)
        tk.Button(self.control_panel, text="Save Pattern", 
                 command=self.save_pattern).pack(fill=tk.X, pady=5)
        tk.Button(self.control_panel, text="Load Image", 
                 command=self.load_image).pack(fill=tk.X, pady=5)
    
    def select_tool(self):
        """Set the current tool."""
        self.current_tool = self.tool_var.get()
    
    def select_color(self):
        """Set the current color."""
        self.color = self.color_var.get()
    
    def on_canvas_click(self, event):
        """Handle canvas click events."""
        if self.current_tool == "stitch":
            x, y = event.x, event.y
            self.stitches.append((x, y, self.color))
            self.draw_stitch(x, y, self.color)
    
    def on_canvas_drag(self, event):
        """Handle canvas drag events."""
        if self.current_tool == "stitch":
            x, y = event.x, event.y
            self.stitches.append((x, y, self.color))
            self.draw_stitch(x, y, self.color)
    
    def draw_stitch(self, x, y, color):
        """Draw a stitch on the canvas."""
        self.canvas.create_oval(x-2, y-2, x+2, y+2, fill=color, outline=color)
    
    def clear_canvas(self):
        """Clear the canvas and reset stitches."""
        self.canvas.delete("all")
        self.stitches = []
    
    def load_image(self):
        """Load an image to trace."""
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
        )
        if file_path:
            try:
                img = Image.open(file_path)
                img.thumbnail((600, 500))
                self.tk_image = ImageTk.PhotoImage(img)
                self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image: {str(e)}")
    
    def save_pattern(self):
        """Save the pattern in PES format."""
        if not self.stitches:
            messagebox.showwarning("Warning", "No stitches to save!")
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pes",
            filetypes=[("PE Design Files", "*.pes")]
        )
        
        if file_path:
            try:
                with open(file_path, 'wb') as f:
                    self._write_pes_header(f)
                    self._write_stitches(f)
                messagebox.showinfo("Success", "Pattern saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save pattern: {str(e)}")
    
    def _write_pes_header(self, file):
        """Write the PES file header."""
        # PES file signature
        file.write(b"#PES0001")
        
        # Placeholder for header data
        header = bytearray(512)
        
        # Basic header information
        header[0x0A:0x0C] = struct.pack("<H", 1)  # Embroidery hoop size
        header[0x0C:0x10] = struct.pack("<I", len(self.stitches))  # Number of stitches
        
        # Write header
        file.write(header)
    
    def _write_stitches(self, file):
        """Write stitch data to file."""
        for x, y, color in self.stitches:
            # Convert coordinates to PES format (scaled and offset)
            px = int(x * 10)
            py = int(y * 10)
            
            # Write stitch command (normal stitch)
            file.write(b"\x00\x00")
            
            # Write coordinates
            file.write(struct.pack("<hh", px, py))
        
        # End of design
        file.write(b"\x00\x00\x00\x00")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmbroideryPatternDesigner(root)
    root.mainloop()
```
