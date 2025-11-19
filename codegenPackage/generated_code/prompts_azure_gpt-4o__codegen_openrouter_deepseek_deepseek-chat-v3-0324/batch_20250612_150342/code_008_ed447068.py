"""
Generated Code Metadata:
========================
Original URL: https://graphpool.net
Prompt: Generate code to visualize graph structures with interactive features, based on examples or libraries highlighted on graphpool.net.
Generated: DETERMINISTIC_ed447068d26a00ff
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np

class InteractiveGraphVisualizer:
    """
    Interactive graph visualization tool with NetworkX and Matplotlib.
    Features:
    - Zoom in/out
    - Node dragging
    - Node selection
    - Edge highlighting
    """
    
    def __init__(self, graph=None):
        self.fig, self.ax = plt.subplots(figsize=(10, 8))
        plt.subplots_adjust(bottom=0.2)
        
        # Initialize graph
        self.graph = graph if graph else nx.karate_club_graph()
        self.pos = nx.spring_layout(self.graph)
        
        # Visualization parameters
        self.node_size = 300
        self.edge_width = 1.5
        self.selected_node = None
        self.dragging = False
        self.zoom_factor = 1.0
        
        # Initialize UI elements
        self._init_ui()
        
        # Draw the initial graph
        self._draw_graph()
        
        # Connect event handlers
        self._connect_events()
    
    def _init_ui(self):
        """Initialize UI buttons."""
        ax_zoom_in = plt.axes([0.3, 0.05, 0.1, 0.075])
        ax_zoom_out = plt.axes([0.41, 0.05, 0.1, 0.075])
        ax_reset = plt.axes([0.52, 0.05, 0.1, 0.075])
        
        self.btn_zoom_in = Button(ax_zoom_in, 'Zoom In')
        self.btn_zoom_out = Button(ax_zoom_out, 'Zoom Out')
        self.btn_reset = Button(ax_reset, 'Reset')
        
        self.btn_zoom_in.on_clicked(self._zoom_in)
        self.btn_zoom_out.on_clicked(self._zoom_out)
        self.btn_reset.on_clicked(self._reset_view)
    
    def _draw_graph(self):
        """Draw the graph with current parameters."""
        self.ax.clear()
        
        # Draw edges
        nx.draw_networkx_edges(
            self.graph, 
            self.pos, 
            ax=self.ax,
            width=self.edge_width,
            edge_color='gray'
        )
        
        # Draw nodes
        node_colors = ['red' if node == self.selected_node else 'skyblue' 
                      for node in self.graph.nodes()]
        nx.draw_networkx_nodes(
            self.graph, 
            self.pos, 
            ax=self.ax,
            node_size=self.node_size,
            node_color=node_colors
        )
        
        # Draw labels
        nx.draw_networkx_labels(
            self.graph, 
            self.pos, 
            ax=self.ax,
            font_size=10
        )
        
        # Highlight edges connected to selected node
        if self.selected_node is not None:
            edges = list(self.graph.edges(self.selected_node))
            nx.draw_networkx_edges(
                self.graph, 
                self.pos, 
                ax=self.ax,
                edgelist=edges,
                width=2.5,
                edge_color='orange'
            )
        
        self.ax.set_title("Interactive Graph Visualization")
        self.ax.set_axis_off()
        plt.draw()
    
    def _connect_events(self):
        """Connect matplotlib event handlers."""
        self.fig.canvas.mpl_connect('button_press_event', self._on_click)
        self.fig.canvas.mpl_connect('button_release_event', self._on_release)
        self.fig.canvas.mpl_connect('motion_notify_event', self._on_motion)
        self.fig.canvas.mpl_connect('scroll_event', self._on_scroll)
    
    def _on_click(self, event):
        """Handle mouse click events."""
        if event.inaxes != self.ax:
            return
            
        # Find closest node
        nodes = np.array(list(self.pos.values()))
        if len(nodes) == 0:
            return
            
        dist = np.sum((nodes - [event.xdata, event.ydata])**2, axis=1)
        closest_node = list(self.graph.nodes())[np.argmin(dist)]
        
        if np.min(dist) < 0.1:  # Threshold for node selection
            self.selected_node = closest_node
            self.dragging = True
        else:
            self.selected_node = None
        
        self._draw_graph()
    
    def _on_release(self, event):
        """Handle mouse release events."""
        self.dragging = False
    
    def _on_motion(self, event):
        """Handle mouse motion events."""
        if not self.dragging or self.selected_node is None or event.inaxes != self.ax:
            return
            
        # Update node position
        self.pos[self.selected_node] = [event.xdata, event.ydata]
        self._draw_graph()
    
    def _on_scroll(self, event):
        """Handle scroll events for zooming."""
        if event.inaxes != self.ax:
            return
            
        # Zoom in or out
        if event.button == 'up':
            self._zoom_in(None)
        elif event.button == 'down':
            self._zoom_out(None)
    
    def _zoom_in(self, event):
        """Zoom in the view."""
        self.zoom_factor *= 1.1
        self._apply_zoom()
    
    def _zoom_out(self, event):
        """Zoom out the view."""
        self.zoom_factor /= 1.1
        self._apply_zoom()
    
    def _apply_zoom(self):
        """Apply zoom transformation."""
        self.ax.set_xlim(-1/self.zoom_factor, 1/self.zoom_factor)
        self.ax.set_ylim(-1/self.zoom_factor, 1/self.zoom_factor)
        plt.draw()
    
    def _reset_view(self, event):
        """Reset the view to default."""
        self.zoom_factor = 1.0
        self.pos = nx.spring_layout(self.graph)
        self.selected_node = None
        self._draw_graph()
        self._apply_zoom()
    
    def show(self):
        """Display the interactive visualization."""
        plt.show()

# Example usage
if __name__ == "__main__":
    # Create a sample graph
    G = nx.Graph()
    G.add_edges_from([
        (1, 2), (1, 3), (2, 3), (3, 4), 
        (4, 5), (4, 6), (5, 6), (6, 7)
    ])
    
    # Create and show the visualizer
    visualizer = InteractiveGraphVisualizer(G)
    visualizer.show()
```
