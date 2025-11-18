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
import numpy as np

def create_funnel_diagram(data, labels, title="Funnel Diagram"):
    """
    Create a funnel diagram using Matplotlib.

    Parameters:
        data (list): A list of numerical values representing the size of each stage in the funnel.
        labels (list): A list of stage names corresponding to the data.
        title (str): The title of the funnel diagram.
    """
    
    # Validate input data
    if len(data) != len(labels):
        raise ValueError("Data and labels must have the same length.")
    
    if any(value < 0 for value in data):
        raise ValueError("Data values must be non-negative.")
    
    # Compute the positions for the funnel stages
    num_stages = len(data)
    widths = data / np.max(data) * 100  # Normalize widths for visualization
    heights = np.ones(num_stages)  # Uniform height for each stage

    fig, ax = plt.subplots(figsize=(8, 6))

    # Create the funnel shapes using patch collections
    for i in range(num_stages):
        # Define funnel polygon points
        if i == 0:
            top_left = (0, i)
            top_right = (widths[i], i)
            bottom_left = (0, i + heights[i])
            bottom_right = (widths[i], i + heights[i])
        else:
            top_left = (widths[i - 1], i)
            top_right = (widths[i], i)
            bottom_left = (widths[i - 1], i + heights[i])
            bottom_right = (widths[i], i + heights[i])

        # Create the polygon representing the funnel segment
        funnel_stage = np.array([top_left, top_right, bottom_right, bottom_left])
        ax.add_patch(plt.Polygon(funnel_stage, closed=True, color=plt.cm.Blues(i/num_stages), edgecolor='black'))

        # Annotate the labels
        ax.text(widths[i] / 2, i + heights[i] / 2, labels[i], horizontalalignment='center', verticalalignment='center', fontsize=10)

    # Set limits and labels
    ax.set_xlim(0, 100)
    ax.set_ylim(0, num_stages)
    ax.set_title(title)
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Show the funnel diagram
    plt.tight_layout()
    plt.show()

# Example usage:
if __name__ == "__main__":
    # Define the stages and their respective values
    stages = ['Awareness', 'Interest', 'Consideration', 'Intent', 'Purchase']
    values = [1000, 800, 500, 300, 150]
    
    try:
        create_funnel_diagram(values, stages)
    except Exception as e:
        print(f"An error occurred: {e}")
```
