"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.somosfortic.es
Prompt: Suggest tools or libraries for visualizing architectural designs that incorporate Fortic's minimalist concrete beams, focusing on clean lines and light colors.
Generated: DETERMINISTIC_6d05ce7830cb082f
Batch ID: 20250612_153224
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
import matplotlib.patches as patches

# Function to visualize architectural designs with minimalist concrete beams
def visualize_architecture(beams, colors, title="Architectural Design Visualization"):
    """
    Visualizes an architectural design with provided beams and colors.

    Parameters:
    beams (list of tuples): List of beam specifications as (x, y, width, height)
    colors (list of str): List of color specifications for the beams
    title (str): Title of the plot
    """
    # Validate input lengths
    if len(beams) != len(colors):
        raise ValueError("The number of beams must match the number of colors.")

    # Create a new figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))

    # Set the limits and title of the plot
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.set_title(title)
    
    # Draw each beam on the plot
    for (x, y, width, height), color in zip(beams, colors):
        # Create a rectangle for each beam
        beam = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='black', facecolor=color)
        
        # Add the beam to the axis
        ax.add_patch(beam)

    # Set aspect of the plot to be equal
    ax.set_aspect('equal', adjustable='box')

    # Display the grid
    ax.grid(True)

    # Show the plot
    plt.show()

# Example usage of the visualization function
if __name__ == "__main__":
    try:
        # Define beam specifications and colors
        beams = [(1, 1, 2, 0.5), (4, 1, 3, 0.5), (8, 1, 1.5, 0.5)]
        colors = ['lightgray', 'whitesmoke', 'gainsboro']
        
        # Visualize the architectural design
        visualize_architecture(beams, colors)
    except Exception as e:
        print(f"An error occurred: {e}")
```
