"""
Generated Code Metadata:
========================
Original URL: https://anima.art.br
Prompt: Generate a Python script that uses digital painting techniques for beginners, inspired by the courses offered at Ânima Academia de Arte.
Generated: DETERMINISTIC_2e7cdaccc1bfbd7c
Batch ID: 20250612_164021
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
from matplotlib.widgets import Slider, Button
from matplotlib.patches import Rectangle

class DigitalPaintingCanvas:
    """
    A simple digital painting canvas for beginners, inspired by Ânima Academia de Arte courses.
    Features include:
    - Basic brush strokes
    - Adjustable brush size and color
    - Clear canvas functionality
    - Save artwork as an image
    """
    
    def __init__(self):
        # Initialize the canvas
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        plt.title("Digital Painting Canvas for Beginners", pad=20)
        
        # Set up the canvas background
        self.canvas = np.ones((500, 500, 3))  # White background
        self.ax.imshow(self.canvas)
        self.ax.axis('off')
        
        # Default brush settings
        self.brush_size = 5
        self.brush_color = np.array([0.0, 0.0, 0.0])  # Default: black
        
        # UI controls
        self._setup_ui()
        
        # Connect event handlers
        self.fig.canvas.mpl_connect('motion_notify_event', self._on_mouse_move)
        self.fig.canvas.mpl_connect('button_press_event', self._on_mouse_press)
        
    def _setup_ui(self):
        """Set up the UI controls for brush settings."""
        # Adjust figure layout to make space for controls
        plt.subplots_adjust(bottom=0.25)
        
        # Create axes for sliders and buttons
        ax_color = plt.axes([0.25, 0.15, 0.5, 0.03])
        ax_size = plt.axes([0.25, 0.1, 0.5, 0.03])
        ax_clear = plt.axes([0.25, 0.05, 0.1, 0.04])
        ax_save = plt.axes([0.65, 0.05, 0.1, 0.04])
        
        # Color sliders
        self.slider_red = Slider(ax_color, 'Red', 0.0, 1.0, valinit=self.brush_color[0])
        self.slider_green = Slider(ax_color, 'Green', 0.0, 1.0, valinit=self.brush_color[1])
        self.slider_blue = Slider(ax_color, 'Blue', 0.0, 1.0, valinit=self.brush_color[2])
        
        # Brush size slider
        self.slider_size = Slider(ax_size, 'Brush Size', 1, 50, valinit=self.brush_size, valstep=1)
        
        # Buttons
        self.btn_clear = Button(ax_clear, 'Clear Canvas')
        self.btn_save = Button(ax_save, 'Save Artwork')
        
        # Register update functions
        self.slider_red.on_changed(self._update_color)
        self.slider_green.on_changed(self._update_color)
        self.slider_blue.on_changed(self._update_color)
        self.slider_size.on_changed(self._update_size)
        self.btn_clear.on_clicked(self._clear_canvas)
        self.btn_save.on_clicked(self._save_artwork)
        
    def _update_color(self, val):
        """Update the brush color based on slider values."""
        self.brush_color = np.array([
            self.slider_red.val,
            self.slider_green.val,
            self.slider_blue.val
        ])
        
    def _update_size(self, val):
        """Update the brush size based on slider value."""
        self.brush_size = int(val)
        
    def _on_mouse_press(self, event):
        """Handle mouse press events to start drawing."""
        if event.inaxes != self.ax:
            return
        self._paint(event.xdata, event.ydata)
        
    def _on_mouse_move(self, event):
        """Handle mouse movement to draw continuous lines."""
        if event.inaxes != self.ax or not event.button:
            return
        self._paint(event.xdata, event.ydata)
        
    def _paint(self, x, y):
        """
        Paint on the canvas at position (x, y) with current brush settings.
        
        Args:
            x (float): X coordinate on canvas
            y (float): Y coordinate on canvas
        """
        if x is None or y is None:
            return
            
        size = self.brush_size
        x, y = int(x), int(y)
        
        # Create a circular brush effect
        for i in range(max(0, x - size), min(self.canvas.shape[1], x + size + 1)):
            for j in range(max(0, y - size), min(self.canvas.shape[0], y + size + 1)):
                if (i - x)**2 + (j - y)**2 <= size**2:
                    self.canvas[j, i] = self.brush_color
        
        self.ax.imshow(self.canvas)
        self.fig.canvas.draw_idle()
        
    def _clear_canvas(self, event):
        """Reset the canvas to white."""
        self.canvas = np.ones_like(self.canvas)
        self.ax.imshow(self.canvas)
        self.fig.canvas.draw_idle()
        
    def _save_artwork(self, event):
        """
        Save the current artwork as a PNG file.
        Handles potential errors during file saving.
        """
        try:
            plt.imsave('artwork.png', self.canvas)
            print("Artwork successfully saved as 'artwork.png'")
        except Exception as e:
            print(f"Error saving artwork: {str(e)}")
            
    def show(self):
        """Show the painting canvas."""
        plt.show()

# Create and display the painting canvas
if __name__ == "__main__":
    canvas = DigitalPaintingCanvas()
    canvas.show()
```
