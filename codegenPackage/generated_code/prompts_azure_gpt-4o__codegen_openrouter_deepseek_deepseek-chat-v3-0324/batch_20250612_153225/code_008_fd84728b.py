"""
Generated Code Metadata:
========================
Original URL: https://scienceartthinking.de
Prompt: Develop a program that visualizes the "Morphology of Reality" concept from ScienceArtThinking.de. Use Python and graphical libraries to create dynamic, interactive models of perception.
Generated: DETERMINISTIC_fd84728bbc1f5b0b
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button
import matplotlib.patches as patches
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LinearSegmentedColormap

class RealityMorphologyVisualizer:
    """
    A dynamic visualization of the "Morphology of Reality" concept.
    Creates interactive models of perception with adjustable parameters.
    """
    
    def __init__(self):
        self.fig = plt.figure(figsize=(12, 8))
        self.setup_ui()
        self.setup_plots()
        self.update_plots()
        plt.tight_layout()
        
    def setup_ui(self):
        """Create interactive UI controls."""
        # Add space for sliders
        self.fig.subplots_adjust(bottom=0.35)
        
        # Create sliders
        ax_complexity = plt.axes([0.2, 0.25, 0.6, 0.03])
        ax_perspective = plt.axes([0.2, 0.20, 0.6, 0.03])
        ax_entropy = plt.axes([0.2, 0.15, 0.6, 0.03])
        ax_connectivity = plt.axes([0.2, 0.10, 0.6, 0.03])
        
        self.slider_complexity = Slider(
            ax_complexity, 'Complexity', 1, 10, valinit=5, valstep=1
        )
        self.slider_perspective = Slider(
            ax_perspective, 'Perspective', 0, 2*np.pi, valinit=np.pi/4
        )
        self.slider_entropy = Slider(
            ax_entropy, 'Entropy', 0, 1, valinit=0.3
        )
        self.slider_connectivity = Slider(
            ax_connectivity, 'Connectivity', 0.1, 1, valinit=0.7
        )
        
        # Add reset button
        reset_ax = plt.axes([0.8, 0.02, 0.1, 0.04])
        self.reset_button = Button(reset_ax, 'Reset', color='lightgoldenrodyellow')
        
        # Connect callbacks
        self.slider_complexity.on_changed(self.update_plots)
        self.slider_perspective.on_changed(self.update_plots)
        self.slider_entropy.on_changed(self.update_plots)
        self.slider_connectivity.on_changed(self.update_plots)
        self.reset_button.on_clicked(self.reset)
        
    def setup_plots(self):
        """Initialize the visualization plots."""
        # 2D plot
        self.ax_2d = self.fig.add_subplot(121)
        self.ax_2d.set_title("Perceptual Field")
        self.ax_2d.set_xlim(-5, 5)
        self.ax_2d.set_ylim(-5, 5)
        
        # 3D plot
        self.ax_3d = self.fig.add_subplot(122, projection='3d')
        self.ax_3d.set_title("Reality Morphology")
        self.ax_3d.set_xlim(-5, 5)
        self.ax_3d.set_ylim(-5, 5)
        self.ax_3d.set_zlim(-5, 5)
        
        # Initialize plot elements
        self.scatter_2d = self.ax_2d.scatter([], [], c=[], cmap='viridis', alpha=0.7)
        self.scatter_3d = self.ax_3d.scatter([], [], [], c=[], cmap='viridis', alpha=0.7)
        self.lines_3d = [self.ax_3d.plot([], [], [], 'gray', alpha=0.3)[0] for _ in range(20)]
        
    def generate_data(self):
        """Generate visualization data based on current parameters."""
        complexity = int(self.slider_complexity.val)
        perspective = self.slider_perspective.val
        entropy = self.slider_entropy.val
        connectivity = self.slider_connectivity.val
        
        # Generate base points
        n_points = 50 + complexity * 20
        theta = np.linspace(0, 2*np.pi, n_points)
        r = np.linspace(0.5, 5, n_points)
        
        # Apply perspective transformation
        x = r * np.cos(theta + perspective)
        y = r * np.sin(theta + perspective)
        
        # Add entropy (randomness)
        x += np.random.normal(0, entropy, n_points)
        y += np.random.normal(0, entropy, n_points)
        
        # Generate z values based on connectivity
        z = np.sin(connectivity * np.sqrt(x**2 + y**2))
        
        # Generate colors based on position
        colors = np.arctan2(y, x)
        
        # Generate connections between points
        connections = []
        for i in range(n_points):
            for j in range(i+1, min(i+1 + int(connectivity*10), n_points)):
                if np.random.random() < connectivity:
                    connections.append((i, j))
        
        return x, y, z, colors, connections
    
    def update_plots(self, val=None):
        """Update all plots with new data."""
        x, y, z, colors, connections = self.generate_data()
        
        # Update 2D plot
        self.scatter_2d.set_offsets(np.column_stack([x, y]))
        self.scatter_2d.set_array(colors)
        self.scatter_2d.set_clim(colors.min(), colors.max())
        
        # Update 3D plot
        self.scatter_3d._offsets3d = (x, y, z)
        self.scatter_3d.set_array(colors)
        self.scatter_3d.set_clim(colors.min(), colors.max())
        
        # Update connections in 3D plot
        for i, line in enumerate(self.lines_3d):
            if i < len(connections):
                idx1, idx2 = connections[i]
                line.set_data([x[idx1], x[idx2]], [y[idx1], y[idx2]])
                line.set_3d_properties([z[idx1], z[idx2]])
            else:
                line.set_data([], [])
                line.set_3d_properties([])
        
        self.fig.canvas.draw_idle()
    
    def reset(self, event):
        """Reset all parameters to default values."""
        self.slider_complexity.reset()
        self.slider_perspective.reset()
        self.slider_entropy.reset()
        self.slider_connectivity.reset()

def main():
    try:
        visualizer = RealityMorphologyVisualizer()
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    main()
```
