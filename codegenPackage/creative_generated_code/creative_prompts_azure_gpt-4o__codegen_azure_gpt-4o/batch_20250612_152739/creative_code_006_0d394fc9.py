"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://slidesgeek.com
Prompt: Write code to design a funnel diagram presentation slide using Python, based on the infographic styles described on SlidesGeek.
Generated: DETERMINISTIC_0d394fc9eb2cd085
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def create_funnel_diagram(data, colors, title="Funnel Diagram"):
    """
    Creates a funnel diagram presentation slide.
    
    Parameters:
        data (list of tuples): Each tuple contains (label, value).
        colors (list of str): List of color codes for each funnel layer.
        title (str): Title of the funnel diagram.
    """
    # Validate inputs
    if not data or not isinstance(data, list) or not all(isinstance(i, tuple) and len(i) == 2 for i in data):
        raise ValueError("Data must be a list of tuples with (label, value).")
    if not colors or len(colors) != len(data):
        raise ValueError("Colors must be a list of valid colors with the same length as data.")
    
    # Extract labels and values
    labels = [item[0] for item in data]
    values = [item[1] for item in data]
    
    # Normalize values for scaling the funnel levels
    max_value = max(values)
    normalized_values = [v / max_value for v in values]
    
    # Initialize plot
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, len(data))
    ax.axis("off")  # Hide axes
    
    # Create funnel layers
    for i in range(len(data)):
        width_top = normalized_values[i] if i == 0 else normalized_values[i - 1]
        width_bottom = normalized_values[i]
        top_y = len(data) - i - 1
        bottom_y = len(data) - i - 0.5
        
        # Create a trapezoid (polygon) for the funnel layer
        funnel_layer = Polygon(
            [
                ((1 - width_top) / 2, top_y),  # Top left
                ((1 + width_top) / 2, top_y),  # Top right
                ((1 + width_bottom) / 2, bottom_y),  # Bottom right
                ((1 - width_bottom) / 2, bottom_y),  # Bottom left
            ],
            closed=True,
            color=colors[i]
        )
        ax.add_patch(funnel_layer)
        
        # Add labels inside the funnel layers
        ax.text(0.5, (top_y + bottom_y) / 2, f"{labels[i]}: {values[i]}", 
                ha="center", va="center", fontsize=10, color="white")
    
    # Add title
    plt.title(title, fontsize=14, weight="bold")
    
    # Show plot
    plt.tight_layout()
    plt.show()

# Example usage
data = [("Awareness", 1000), ("Interest", 750), ("Consideration", 500), ("Intent", 300), ("Purchase", 150)]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
create_funnel_diagram(data, colors, title="Customer Journey Funnel")
```
