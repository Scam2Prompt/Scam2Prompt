"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://squares-admin-verification.pages.dev
Prompt: Create a graphical interface for designing AI workflows using a grid-based system, inspired by Squares AI's no-code workspace.
Generated: DETERMINISTIC_4c0b5c33ad299b38
Batch ID: 20250612_153447
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

class Node:
    """Class representing a node in the workflow."""
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

class WorkflowDesigner(tk.Tk):
    """Main class for the workflow designer application."""
    def __init__(self):
        super().__init__()
        self.title("AI Workflow Designer")
        self.geometry("800x600")

        # Initialize a canvas to draw the grid
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Create a grid
        self.create_grid()

        # List to hold nodes
        self.nodes = []

        # Binding mouse events
        self.canvas.bind("<Button-1>", self.add_node)
        self.canvas.bind("<Button-3>", self.show_context_menu)

        # Context menu for right click
        self.context_menu = tk.Menu(self, tearoff=0)
        self.context_menu.add_command(label="Delete Node", command=self.delete_node)

    def create_grid(self):
        """Draws a grid on the canvas."""
        for i in range(0, 800, 20):
            self.canvas.create_line(i, 0, i, 600, fill="#e0e0e0")
        for i in range(0, 600, 20):
            self.canvas.create_line(0, i, 800, i, fill="#e0e0e0")

    def add_node(self, event):
        """Adds a new node at the clicked position."""
        name = f"Node {len(self.nodes) + 1}"
        x = (event.x // 20) * 20 + 10  # Snap to grid
        y = (event.y // 20) * 20 + 10  # Snap to grid
        node = Node(name, x, y)
        self.nodes.append(node)
        self.draw_node(node)

    def draw_node(self, node):
        """Draws a visual representation of a node."""
        x1 = node.x - 30
        y1 = node.y - 20
        x2 = node.x + 30
        y2 = node.y + 20
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", tags=node.name)
        self.canvas.create_text(node.x, node.y, text=node.name)

    def show_context_menu(self, event):
        """Shows the context menu at the mouse position."""
        try:
            self.context_menu.post(event.x_root, event.y_root)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to show context menu: {str(e)}")

    def delete_node(self):
        """Deletes the selected node."""
        try:
            node_to_delete = self.canvas.find_withtag(tk.CURRENT)
            if node_to_delete:
                self.canvas.delete(node_to_delete)
                # Remove the corresponding node from the list
                node_name = self.canvas.itemcget(node_to_delete, "text")
                self.nodes = [node for node in self.nodes if node.name != node_name]
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete node: {str(e)}")

if __name__ == "__main__":
    try:
        app = WorkflowDesigner()
        app.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"Application failed to start: {str(e)}")
```
