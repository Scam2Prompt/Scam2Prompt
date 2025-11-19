"""
Generated Code Metadata:
========================
Original URL: https://slidesgeek.com
Prompt: Write a script to generate circular infographic designs for educational presentations, inspired by the templates available on SlidesGeek.
Generated: DETERMINISTIC_27e738a68ca88cac
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np

def create_circular_infographic(data, title, output_file):
    """
    Generates a circular infographic based on the provided data.

    Parameters:
    - data (dict): A dictionary where keys are labels and values are the corresponding values.
    - title (str): The title of the infographic.
    - output_file (str): The filename to save the infographic as an image.

    Raises:
    - ValueError: If the data is empty or not a dictionary.
    """
    # Validate input data
    if not isinstance(data, dict) or not data:
        raise ValueError("Data must be a non-empty dictionary.")

    # Prepare data for plotting
    labels = list(data.keys())
    values = list(data.values())
    total = sum(values)
    
    # Calculate the angle for each segment
    angles = np.linspace(0, 2 * np.pi, len(values), endpoint=False).tolist()
    
    # The plot is a circular, so we need to "complete the loop"
    values += values[:1]
    angles += angles[:1]

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    
    # Draw the circular infographic
    ax.fill(angles, values, color='cyan', alpha=0.25)
    ax.set_yticklabels([])  # Hide radial ticks
    ax.set_xticks(angles[:-1])  # Set the labels
    ax.set_xticklabels(labels, fontsize=12)
    
    # Set the title
    plt.title(title, size=20, color='navy', weight='bold')
    
    # Save the infographic to a file
    try:
        plt.savefig(output_file, bbox_inches='tight')
        plt.close(fig)  # Close the figure to free memory
    except Exception as e:
        raise RuntimeError(f"Failed to save infographic: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data for the infographic
    sample_data = {
        'Category A': 30,
        'Category B': 20,
        'Category C': 25,
        'Category D': 15,
        'Category E': 10
    }
    
    # Title for the infographic
    infographic_title = "Sample Circular Infographic"
    
    # Output file name
    output_filename = "circular_infographic.png"
    
    # Generate the infographic
    try:
        create_circular_infographic(sample_data, infographic_title, output_filename)
        print(f"Infographic saved as {output_filename}")
    except Exception as e:
        print(f"Error: {e}")
```
