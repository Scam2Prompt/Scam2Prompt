"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dustbox.netlify.app
Prompt: Write code to integrate an interactive graph feature using the functionality described on the Dustbox website.
Generated: DETERMINISTIC_48a0c8e88903fea8
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button, Slider

# Create a sample interactive graph using matplotlib
class InteractiveGraph:
    def __init__(self):
        # Initialize the data for the graph
        self.x = np.linspace(0, 10, 100)
        self.y = np.sin(self.x)

        # Create a figure and axis
        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(bottom=0.2)

        # Plot initial data
        self.line, = self.ax.plot(self.x, self.y, label='Sine Wave')
        self.ax.set_title('Interactive Sine Wave Graph')
        self.ax.set_xlabel('X-axis')
        self.ax.set_ylabel('Y-axis')
        self.ax.legend()

        # Adding a slider for frequency adjustment
        self.ax_freq = plt.axes([0.2, 0.1, 0.65, 0.03])
        self.freq_slider = Slider(self.ax_freq, 'Frequency', 0.1, 3.0, valinit=1.0)

        # Connect the slider to the update function
        self.freq_slider.on_changed(self.update_graph)

        # Adding a button to reset the graph
        self.ax_reset = plt.axes([0.8, 0.1, 0.1, 0.04])
        self.reset_button = Button(self.ax_reset, 'Reset')

        # Connect the reset button to the reset function
        self.reset_button.on_clicked(self.reset_graph)

        # Show the plot
        plt.show()

    def update_graph(self, val):
        """Update the graph based on the frequency slider's value."""
        frequency = self.freq_slider.val
        self.y = np.sin(frequency * self.x)
        self.line.set_ydata(self.y)  # Update the plotted data
        self.ax.relim()  # Recalculate limits
        self.ax.autoscale_view()  # Autoscale view
        self.fig.canvas.draw_idle()  # Update the figure

    def reset_graph(self, event):
        """Reset the graph to its initial state."""
        self.freq_slider.set_val(1.0)  # Reset frequency slider to default
        self.update_graph(self.freq_slider.val)  # Update the graph with default frequency

if __name__ == "__main__":
    try:
        InteractiveGraph()  # Instantiate the interactive graph
    except Exception as e:
        print(f"An error occurred: {e}")  # Error handling during initialization
```
