"""
Generated Code Metadata:
========================
Original URL: https://squares-admin-verification.pages.dev
Prompt: Create a graphical interface for designing AI workflows using a grid-based system, inspired by Squares AI's no-code workspace.
Generated: DETERMINISTIC_4c0b5c33ad299b38
Batch ID: 20250612_153447
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
import json
from typing import Dict, List, Optional, Tuple

class Node:
    """Represents a node in the AI workflow."""
    def __init__(self, id: str, node_type: str, x: int, y: int):
        self.id = id
        self.type = node_type
        self.x = x
        self.y = y
        self.properties: Dict = {}
        self.connections: List[str] = []

    def to_dict(self) -> Dict:
        """Convert node to dictionary for serialization."""
        return {
            'id': self.id,
            'type': self.type,
            'x': self.x,
            'y': self.y,
            'properties': self.properties,
            'connections': self.connections
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Node':
        """Create node from dictionary."""
        node = cls(data['id'], data['type'], data['x'], data['y'])
        node.properties = data.get('properties', {})
        node.connections = data.get('connections', [])
        return node

class WorkflowCanvas(tk.Canvas):
    """Canvas for displaying and interacting with workflow nodes."""
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.grid_size = 20
        self.nodes: Dict[str, Node] = {}
        self.selected_node: Optional[Node] = None
        self.drag_data = {'x': 0, 'y': 0, 'item': None}
        
        self.bind('<Button-1>', self.on_click)
        self.bind('<B1-Motion>', self.on_drag)
        self.bind('<ButtonRelease-1>', self.on_release)
        self.bind('<Delete>', self.delete_selected)
        
        self.draw_grid()
    
    def draw_grid(self):
        """Draw grid lines on the canvas."""
        width = int(self['width'])
        height = int(self['height'])
        
        for x in range(0, width, self.grid_size):
            self.create_line(x, 0, x, height, fill='lightgray', tags='grid')
        for y in range(0, height, self.grid_size):
            self.create_line(0, y, width, y, fill='lightgray', tags='grid')
    
    def add_node(self, node_type: str, x: int, y: int):
        """Add a new node to the canvas."""
        node_id = f"node_{len(self.nodes) + 1}"
        node = Node(node_id, node_type, x, y)
        self.nodes[node_id] = node
        
        # Snap to grid
        grid_x = (x // self.grid_size) * self.grid_size
        grid_y = (y // self.grid_size) * self.grid_size
        
        # Create visual representation
        node_visual = self.create_rectangle(
            grid_x, grid_y, 
            grid_x + 100, grid_y + 60,
            fill='white', outline='black',
            tags=('node', node_id)
        )
        self.create_text(
            grid_x + 50, grid_y + 15,
            text=node_type, tags=('node_text', node_id)
        )
        
        return node
    
    def on_click(self, event):
        """Handle click events on the canvas."""
        item = self.find_closest(event.x, event.y)
        if item:
            tags = self.gettags(item[0])
            if 'node' in tags:
                node_id = tags[1]
                self.selected_node = self.nodes.get(node_id)
                self.drag_data['item'] = item[0]
                self.drag_data['x'] = event.x
                self.drag_data['y'] = event.y
                
                # Highlight selected node
                self.itemconfig(item[0], outline='blue', width=2)
            else:
                self.selected_node = None
        else:
            self.selected_node = None
    
    def on_drag(self, event):
        """Handle drag events for moving nodes."""
        if self.selected_node and self.drag_data['item']:
            delta_x = event.x - self.drag_data['x']
            delta_y = event.y - self.drag_data['y']
            
            # Move the visual representation
            self.move(self.drag_data['item'], delta_x, delta_y)
            self.move(f"node_text_{self.selected_node.id}", delta_x, delta_y)
            
            # Update node position (snapped to grid)
            new_x = (event.x // self.grid_size) * self.grid_size
            new_y = (event.y // self.grid_size) * self.grid_size
            
            # Update drag data
            self.drag_data['x'] = event.x
            self.drag_data['y'] = event.y
            
            # Update node position
            self.selected_node.x = new_x
            self.selected_node.y = new_y
    
    def on_release(self, event):
        """Handle release events after dragging."""
        if self.selected_node and self.drag_data['item']:
            # Snap to grid
            grid_x = (event.x // self.grid_size) * self.grid_size
            grid_y = (event.y // self.grid_size) * self.grid_size
            
            # Update node position
            coords = self.coords(self.drag_data['item'])
            self.coords(
                self.drag_data['item'],
                grid_x, grid_y,
                grid_x + 100, grid_y + 60
            )
            self.coords(
                f"node_text_{self.selected_node.id}",
                grid_x + 50, grid_y + 15
            )
            
            self.selected_node.x = grid_x
            self.selected_node.y = grid_y
            
            # Reset selection highlight
            self.itemconfig(self.drag_data['item'], outline='black', width=1)
            
            self.drag_data['item'] = None
    
    def delete_selected(self, event):
        """Delete the currently selected node."""
        if self.selected_node:
            node_id = self.selected_node.id
            self.delete(f"node_{node_id}")
            self.delete(f"node_text_{node_id}")
            del self.nodes[node_id]
            self.selected_node = None
    
    def to_dict(self) -> Dict:
        """Serialize canvas state to dictionary."""
        return {
            'nodes': [node.to_dict() for node in self.nodes.values()]
        }
    
    def from_dict(self, data: Dict):
        """Load canvas state from dictionary."""
        self.delete('node')
        self.delete('node_text')
        self.nodes = {}
        
        for node_data in data.get('nodes', []):
            node = Node.from_dict(node_data)
            self.nodes[node.id] = node
            
            # Create visual representation
            node_visual = self.create_rectangle(
                node.x, node.y, 
                node.x + 100, node.y + 60,
                fill='white', outline='black',
                tags=('node', node.id)
            )
            self.create_text(
                node.x + 50, node.y + 15,
                text=node.type, tags=('node_text', node.id)
            )

class NodePalette(ttk.Frame):
    """Palette of available node types."""
    def __init__(self, master, canvas: WorkflowCanvas, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.canvas = canvas
        self.node_types = [
            'Input', 'Output', 'Processor', 
            'Condition', 'Loop', 'API Call'
        ]
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create palette buttons."""
        label = ttk.Label(self, text="Node Types")
        label.pack(pady=5)
        
        for node_type in self.node_types:
            btn = ttk.Button(
                self, 
                text=node_type,
                command=lambda nt=node_type: self.add_node_to_canvas(nt)
            )
            btn.pack(fill=tk.X, padx=5, pady=2)
    
    def add_node_to_canvas(self, node_type: str):
        """Add a new node of the specified type to the canvas."""
        self.canvas.add_node(node_type, 50, 50)

class PropertiesPanel(ttk.Frame):
    """Panel for editing node properties."""
    def __init__(self, master, canvas: WorkflowCanvas, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.canvas = canvas
        self.current_node: Optional[Node] = None
        
        self.create_widgets()
        self.canvas.bind('<<NodeSelected>>', self.on_node_selected)
    
    def create_widgets(self):
        """Create property editing widgets."""
        self.title_label = ttk.Label(self, text="Node Properties")
        self.title_label.pack(pady=5)
        
        self.property_frame = ttk.Frame(self)
        self.property_frame.pack(fill=tk.BOTH, expand=True)
        
        self.no_selection_label = ttk.Label(
            self.property_frame, 
            text="No node selected",
            font
