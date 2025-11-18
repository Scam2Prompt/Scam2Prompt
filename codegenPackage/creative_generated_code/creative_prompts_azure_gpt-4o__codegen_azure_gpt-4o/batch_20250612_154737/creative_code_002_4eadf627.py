"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gra-pro-canv.webflow.io
Prompt: Generate a script to visualize roles and responsibilities in a grants program using Gitcoin's Grants Program Canvas framework.
Generated: DETERMINISTIC_4eadf627d4ad2214
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to visualize roles and responsibilities in a grants program
using Gitcoin's Grants Program Canvas framework.

This script uses Matplotlib to create a visual representation
of the responsibilities and relationships between roles in the grants program.

Ensure you have the required dependencies installed:
pip install matplotlib
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def draw_canvas():
    """
    Draws Gitcoin's Grants Program Canvas framework with sample roles and responsibilities.
    Each section represents a component of the grants program.
    """
    # Define the framework structure
    sections = [
        {"title": "Grant Applicants", "description": "Submit grant proposals for funding.", "x": 0, "y": 8},
        {"title": "Review Committee", "description": "Evaluate and score grant proposals.", "x": 0, "y": 4},
        {"title": "Funders", "description": "Provide funding for approved grants.", "x": 0, "y": 0},
        {"title": "Community", "description": "Provide feedback and support to improve grant proposals.", "x": 6, "y": 8},
        {"title": "Program Managers", "description": "Oversee the program and ensure compliance.", "x": 6, "y": 4},
        {"title": "Auditors", "description": "Validate proper use of funds and transparency.", "x": 6, "y": 0}
    ]

    # Initialize the plot
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(-1, 12)
    ax.set_ylim(-1, 12)
    ax.axis("off")  # Turn off the axis

    # Draw sections and add text
    for section in sections:
        # Draw a rounded rectangle for each role
        box = FancyBboxPatch((section["x"], section["y"]), 5, 3,
                             boxstyle="round,pad=0.3", fc="skyblue", edgecolor="navy")
        ax.add_patch(box)

        # Add title and description inside the box
        ax.text(section["x"] + 2.5, section["y"] + 2,
                section["title"], color="navy", ha="center", va="center", fontsize=12, fontweight="bold")
        ax.text(section["x"] + 2.5, section["y"] + 1,
                section["description"], color="black", ha="center", va="center", fontsize=10)

    # Add title to the canvas
    ax.text(6, 11, "Gitcoin Grants Program Canvas", ha="center", va="center",
            fontsize=16, fontweight="bold", color="navy")

    # Display the visualization
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    try:
        # Execute the canvas visualization
        draw_canvas()
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")
```
