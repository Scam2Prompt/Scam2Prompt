"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://topgraininteriors.com
Prompt: Generate a code snippet for a custom kitchen design application that allows users to visualize built-in cabinets and wine cellars, similar to the services offered by Top Grain Interiors.
Generated: DETERMINISTIC_0ac1509dc5ac4a25
Batch ID: 20250612_162051
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

class KitchenDesignApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Custom Kitchen Design Application")
        
        # Frame for user inputs
        self.input_frame = tk.Frame(master)
        self.input_frame.pack(pady=10)

        self.cabinet_label = tk.Label(self.input_frame, text="Enter Number of Cabinets:")
        self.cabinet_label.grid(row=0, column=0)

        self.cabinet_entry = tk.Entry(self.input_frame)
        self.cabinet_entry.grid(row=0, column=1)

        self.wine_cellar_label = tk.Label(self.input_frame, text="Enter Size of Wine Cellar (sq ft):")
        self.wine_cellar_label.grid(row=1, column=0)

        self.wine_cellar_entry = tk.Entry(self.input_frame)
        self.wine_cellar_entry.grid(row=1, column=1)

        # Button to visualize the design
        self.visualize_button = tk.Button(master, text="Visualize Design", command=self.visualize_design)
        self.visualize_button.pack(pady=10)

        # Canvas for drawing the design
        self.canvas = tk.Canvas(master, width=600, height=400, bg='white')
        self.canvas.pack(pady=10)

    def visualize_design(self):
        """Visualizes the kitchen design based on user inputs."""
        try:
            # Clear the canvas
            self.canvas.delete("all")

            # Get user inputs
            num_cabinets = int(self.cabinet_entry.get())
            wine_cellar_size = int(self.wine_cellar_entry.get())

            # Validate inputs
            if num_cabinets < 0 or wine_cellar_size < 0:
                raise ValueError("Number of cabinets and size of wine cellar must be non-negative.")

            # Draw cabinets
            cabinet_width = 50
            cabinet_height = 30
            
            for i in range(num_cabinets):
                x0 = 10 + (i * (cabinet_width + 10))
                y0 = 10
                x1 = x0 + cabinet_width
                y1 = y0 + cabinet_height
                self.canvas.create_rectangle(x0, y0, x1, y1, fill='brown', outline='black')
                self.canvas.create_text(x0 + cabinet_width / 2, y0 + cabinet_height / 2, text="Cabinet")

            # Draw wine cellar
            wine_cellar_width = 100
            wine_cellar_height = 50
            x0 = 10
            y0 = 60
            x1 = x0 + wine_cellar_width
            y1 = y0 + wine_cellar_height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill='red', outline='black')
            self.canvas.create_text(x0 + wine_cellar_width / 2, y0 + wine_cellar_height / 2, 
                                    text=f"Wine Cellar\n{wine_cellar_size} sq ft")

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Unexpected Error", "An unexpected error occurred: " + str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = KitchenDesignApp(root)
    root.mainloop()
```
