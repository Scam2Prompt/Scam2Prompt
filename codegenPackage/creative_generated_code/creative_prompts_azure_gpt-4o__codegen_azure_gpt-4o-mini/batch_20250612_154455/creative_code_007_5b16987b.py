"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financestargate.com
Prompt: Provide a step-by-step guide to create accessible charts for people with visual impairments, using the tweaks highlighted on Finance StarGate.
Generated: DETERMINISTIC_5b16987bf3aec1bc
Batch ID: 20250612_154455
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

def create_accessible_chart(data, title="Accessible Chart", labels=None):
    """
    Creates an accessible chart using Matplotlib.

    Parameters:
    - data: List of numerical values to plot.
    - title: Title of the chart (default is "Accessible Chart").
    - labels: List of labels for each data point (optional).

    Raises:
    - ValueError: If 'data' is not a list or has less than two elements.
    """

    # Validate input data
    if not isinstance(data, list) or len(data) < 2:
        raise ValueError("Data must be a list with at least two elements.")

    # Define a color palette that is friendly for colorblind individuals
    color_palette = ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Create a bar chart
    ax.bar(range(len(data)), data, color=color_palette)

    # Set title and labels
    ax.set_title(title, fontsize=16, fontweight='bold', color='black')
    ax.set_xticks(range(len(data)))
    
    # Use labels if provided; otherwise, default to indices
    if labels:
        ax.set_xticklabels(labels, fontsize=12)
    else:
        ax.set_xticklabels([str(i) for i in range(len(data))], fontsize=12)

    # Add gridlines for better visibility
    ax.yaxis.grid(True, linestyle='--', alpha=0.7)
    
    # Set axis labels
    ax.set_ylabel("Values", fontsize=14)
    ax.set_xlabel("Categories", fontsize=14)

    # Save chart as a file with an accessible name
    try:
        plt.savefig("accessible_chart.png", bbox_inches='tight', dpi=300)
        print("Chart saved as 'accessible_chart.png'")
    except Exception as e:
        print(f"Error saving the chart: {e}")

    # Display the chart
    plt.show()

# Example usage
if __name__ == "__main__":
    # Sample data
    sample_data = [10, 20, 30, 40, 50]
    sample_labels = ["Item A", "Item B", "Item C", "Item D", "Item E"]

    try:
        create_accessible_chart(sample_data, title="Sample Accessible Chart", labels=sample_labels)
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
