"""
Generated Code Metadata:
========================
Original URL: https://wowtemplates.in
Prompt: "Generate a resume template using a rectangular chain ribbon design."
Generated: DETERMINISTIC_e5189ca334c37044
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
from matplotlib.text import Text
import numpy as np

def create_resume_template():
    """
    Creates a resume template with a rectangular chain ribbon design.
    """
    # Set up the figure and axis
    fig, ax = plt.subplots(figsize=(8.5, 11))  # Letter size
    ax.set_xlim(0, 8.5)
    ax.set_ylim(0, 11)
    ax.axis('off')  # Hide axes
    
    # Background color
    fig.patch.set_facecolor('#f5f5f5')
    ax.set_facecolor('#f5f5f5')
    
    # Main resume rectangle
    resume_rect = Rectangle((0.5, 0.5), 7.5, 10, 
                           facecolor='white', edgecolor='black', linewidth=1.5)
    ax.add_patch(resume_rect)
    
    # Ribbon design parameters
    ribbon_width = 0.8
    ribbon_height = 0.3
    ribbon_color = '#4682b4'
    num_ribbons = 5
    
    # Create chain ribbon design on left side
    for i in range(num_ribbons):
        y_pos = 9.5 - i * 1.5
        # Main ribbon rectangle
        ribbon_rect = Rectangle((0.5, y_pos), ribbon_width, ribbon_height,
                               facecolor=ribbon_color, edgecolor='black', linewidth=0.5)
        ax.add_patch(ribbon_rect)
        
        # Ribbon connector (triangle)
        if i < num_ribbons - 1:
            connector = Polygon([[0.5 + ribbon_width, y_pos],
                                [0.5 + ribbon_width + 0.2, y_pos - 0.2],
                                [0.5 + ribbon_width, y_pos - 0.4]],
                               facecolor=ribbon_color, edgecolor='black', linewidth=0.5)
            ax.add_patch(connector)
    
    # Add resume sections
    sections = [
        ("CONTACT", 7.0),
        ("SUMMARY", 6.0),
        ("EXPERIENCE", 5.0),
        ("EDUCATION", 3.5),
        ("SKILLS", 2.0)
    ]
    
    for section, y_pos in sections:
        ax.text(1.0, y_pos, section, 
                fontsize=12, fontweight='bold', color=ribbon_color)
        # Section underline
        ax.plot([1.0, 3.0], [y_pos - 0.2, y_pos - 0.2], 
                color=ribbon_color, linewidth=1)
    
    # Add sample content
    ax.text(3.5, 7.0, "John Doe\n123 Main St\nCity, State 12345\n(123) 456-7890\njohndoe@email.com", 
            fontsize=10, va='top')
    ax.text(3.5, 6.0, "Experienced professional with 5+ years in...", 
            fontsize=10, va='top')
    
    # Save the template
    plt.savefig('resume_template.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_resume_template()
```
