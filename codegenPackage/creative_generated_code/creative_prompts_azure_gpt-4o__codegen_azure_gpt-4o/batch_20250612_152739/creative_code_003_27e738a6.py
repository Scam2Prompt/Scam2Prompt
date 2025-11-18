"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://slidesgeek.com
Prompt: Write a script to generate circular infographic designs for educational presentations, inspired by the templates available on SlidesGeek.
Generated: DETERMINISTIC_27e738a68ca88cac
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Here's the code for generating circular infographic designs using Python's `matplotlib`. This code is designed to create circular graphs with customizable sections and labels for educational presentations.

```python
import matplotlib.pyplot as plt
import numpy as np

def generate_circular_infographic(sections, colors, labels, title="Circular Infographic"):
    """
    Generate a circular infographic design.

    Parameters:
        sections (list): A list of values representing the size of each section (e.g., percentages or weights).
        colors (list): A list of colors corresponding to each section (hex codes or named colors).
        labels (list): A list of labels for each section.
        title (str): The title of the infographic.
    """
    try:
        # Validate input lengths
        if not (len(sections) == len(colors) == len(labels)):
            raise ValueError("Sections, colors, and labels must have the same length.")
        
        # Validate input types
        if not all(isinstance(i, (int, float)) for i in sections):
            raise ValueError("Sections must contain numeric values.")
        if not all(isinstance(c, str) for c in colors):
            raise ValueError("Colors must contain string values (hex codes or named colors).")
        if not all(isinstance(l, str) for l in labels):
            raise ValueError("Labels must contain string values.")
        
        # Normalize sections to ensure they sum to 1
        total = sum(sections)
        if total == 0:
            raise ValueError("Section values must not all be zero.")
        normalized_sections = [s / total for s in sections]

        # Generate the pie chart
        fig, ax = plt.subplots(figsize=(8, 8))
        wedges, texts = ax.pie(
            normalized_sections,
            colors=colors,
            labels=None,  # Labels will be handled separately for better customization
            startangle=90,
            counterclock=False
        )

        # Add labels to the pie chart
        for wedge, label in zip(wedges, labels):
            # Position labels slightly outside the wedges
            x, y = wedge.r
            ax.text(
                x * 1.2, y * 1.2, label,
                ha="center", va="center", fontsize=12, weight="bold"
            )

        # Add title
        plt.title(title, fontsize=16, weight="bold")

        # Show the infographic
        plt.show()

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Example data
    sections = [30, 20, 50]  # Values representing the size of sections
    colors = ["#FF5733", "#33FF57", "#3357FF"]  # Colors for each section
    labels = ["Science", "Math", "History"]  # Labels for each section

    # Generate the infographic
    generate_circular_infographic(sections, colors, labels, title="Subjects Overview")
```

This code is built to handle errors gracefully, provides meaningful comments, and ensures high readability. You can integrate it into your presentation workflow and customize it as needed.
