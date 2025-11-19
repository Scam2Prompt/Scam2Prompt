"""
Generated Code Metadata:
========================
Original URL: https://kroonation.com
Prompt: Generate a code snippet for a graphic design application that incorporates UI/UX principles as described by Kroo Nation.
Generated: DETERMINISTIC_f7ed2b45e6c8584d
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import messagebox, filedialog

class GraphicDesignApp:
    def __init__(self, master):
        """Initialize the main application window."""
        self.master = master
        self.master.title("Graphic Design Application")
        self.master.geometry("800x600")
        
        # Create a menu bar
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        # Add File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.quit)

        # Create a canvas for drawing
        self.canvas = tk.Canvas(self.master, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Bind mouse events for drawing
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)

        # Initialize drawing state
        self.last_x, self.last_y = None, None

    def start_draw(self, event):
        """Start drawing on the canvas."""
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        """Draw a line on the canvas."""
        if self.last_x is not None and self.last_y is not None:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill="black", width=2)
            self.last_x, self.last_y = event.x, event.y

    def open_file(self):
        """Open a file dialog to load a design."""
        try:
            file_path = filedialog.askopenfilename(title="Open Design File", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if file_path:
                # Load the design (placeholder for actual loading logic)
                messagebox.showinfo("Open File", f"Loaded design from {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {e}")

    def save_file(self):
        """Open a file dialog to save the current design."""
        try:
            file_path = filedialog.asksaveasfilename(title="Save Design File", defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if file_path:
                # Save the design (placeholder for actual saving logic)
                messagebox.showinfo("Save File", f"Design saved to {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphicDesignApp(root)
    root.mainloop()
```
