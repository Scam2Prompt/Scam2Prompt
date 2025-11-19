"""
Generated Code Metadata:
========================
Original URL: https://slidesgeek.com
Prompt: Write code to design a funnel diagram presentation slide using Python, based on the infographic styles described on SlidesGeek.
Generated: DETERMINISTIC_0d394fc9eb2cd085
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

def create_funnel_diagram(data, title='Funnel Diagram', output_file='funnel_diagram.png'):
    """
    Creates a funnel diagram based on the provided data.

    Parameters:
    - data (list of tuples): Each tuple contains the label and the corresponding value.
    - title (str): The title of the funnel diagram.
    - output_file (str): The filename for saving the output image.

    Raises:
    - ValueError: If data is empty or not in the correct format.
    """
    # Validate input data
    if not data or not all(isinstance(item, tuple) and len(item) == 2 for item in data):
        raise ValueError("Data must be a non-empty list of tuples (label, value).")

    # Extract labels and values
    labels, values = zip(*data)

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(8, 6))

    # Calculate the width of each section of the funnel
    num_sections = len(values)
    widths = np.array(values) / max(values) * 100  # Normalize widths to a percentage of the max value

    # Create the funnel shape
    for i in range(num_sections):
        ax.fill_betweenx([i, i + 1], 50 - widths[i] / 2, 50 + widths[i] / 2, label=labels[i])

    # Set the title and labels
    ax.set_title(title, fontsize=16)
    ax.set_yticks(np.arange(num_sections) + 0.5)
    ax.set_yticklabels(labels)
    ax.set_xlim(0, 100)
    ax.set_xticks([])  # Hide x ticks

    # Add a grid for better readability
    ax.grid(axis='x', linestyle='--', alpha=0.7)

    # Save the figure
    plt.tight_layout()
    plt.savefig(output_file, format='png')
    plt.close(fig)  # Close the figure to free memory

# Example usage
if __name__ == "__main__":
    # Sample data for the funnel diagram
    funnel_data = [
        ('Stage 1', 1000),
        ('Stage 2', 800),
        ('Stage 3', 600),
        ('Stage 4', 400),
        ('Stage 5', 200)
    ]

    try:
        create_funnel_diagram(funnel_data, title='Sales Funnel', output_file='sales_funnel.png')
        print("Funnel diagram created successfully and saved as 'sales_funnel.png'.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
