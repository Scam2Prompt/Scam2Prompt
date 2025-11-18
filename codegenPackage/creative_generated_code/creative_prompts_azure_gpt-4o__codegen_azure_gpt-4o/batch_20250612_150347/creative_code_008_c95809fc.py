"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchaineden.pages.dev
Prompt: Create a roadmap visualization tool for blockchain projects, using the Pepe Unchained roadmap as an example.
Generated: DETERMINISTIC_c95809fc3921617c
Batch ID: 20250612_150347
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

class RoadmapVisualizationApp:
    """
    A Roadmap Visualization Tool for Blockchain Projects
    """

    def __init__(self, root):
        """
        Initializes the roadmap visualization tool.

        Args:
            root (Tk): The root Tkinter object.
        """
        self.root = root
        self.root.title("Blockchain Roadmap Visualization - Pepe Unchained")
        self.root.geometry("800x600")
        
        # Title Label
        self.title_label = tk.Label(root, text="Pepe Unchained Roadmap", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=20)
        
        # Canvas for Visualization
        self.canvas = tk.Canvas(root, width=750, height=400, bg="#f8f9fa")
        self.canvas.pack(pady=10)
        
        # Draw the roadmap
        self.draw_roadmap()
        
        # Quit Button
        self.quit_button = tk.Button(root, text="Exit", command=self.quit_application, bg="#dc3545", fg="white")
        self.quit_button.pack(pady=10)
    
    def draw_roadmap(self):
        """
        Draws the roadmap visualization on the canvas.
        """
        roadmap_data = [
            {"phase": "Phase 1", "title": "Foundation Setup", "description": "Launch Pepe token and build community", "color": "#28a745"},
            {"phase": "Phase 2", "title": "Platform Development", "description": "Develop Pepe Unchained DApp and wallet integration", "color": "#17a2b8"},
            {"phase": "Phase 3", "title": "Ecosystem Expansion", "description": "Integrate NFTs and marketplace functionality", "color": "#ffc107"},
            {"phase": "Phase 4", "title": "Global Outreach", "description": "Expand Pepe Unchained to worldwide adoption", "color": "#007bff"},
        ]
        
        x_start = 50
        y_start = 50
        box_width = 650
        box_height = 75
        margin = 20
        
        for index, phase in enumerate(roadmap_data):
            y_position = y_start + index * (box_height + margin)
            
            # Create a rectangle for each phase
            self.canvas.create_rectangle(
                x_start, y_position, x_start + box_width, y_position + box_height,
                fill=phase["color"], outline="black"
            )
            
            # Add phase title
            self.canvas.create_text(
                x_start + 10, y_position + 15,
                anchor="nw", font=("Arial", 16, "bold"), text=phase["phase"], fill="white"
            )
            
            # Add phase description
            self.canvas.create_text(
                x_start + 10, y_position + 40,
                anchor="nw", font=("Arial", 12), text=phase["description"], fill="white"
            )
    
    def quit_application(self):
        """
        Handles application exit.
        """
        result = messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit?")
        if result:
            self.root.destroy()


# Main application entry point
if __name__ == "__main__":
    try:
        # Create the Tkinter root window
        root = tk.Tk()
        
        # Initialize the roadmap visualization tool and run it
        app = RoadmapVisualizationApp(root)
        root.mainloop()
    except Exception as e:
        # Handle unexpected errors
        messagebox.showerror("Application Error", f"An unexpected error occurred: {e}")
```
