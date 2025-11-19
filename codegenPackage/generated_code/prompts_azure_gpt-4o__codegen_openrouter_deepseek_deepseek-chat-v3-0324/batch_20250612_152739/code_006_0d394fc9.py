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
from matplotlib.patches import Wedge

def create_funnel_diagram():
    """
    Creates a funnel diagram presentation slide using matplotlib.
    The design is inspired by infographic styles from SlidesGeek.
    """
    try:
        # Set up the figure and axis
        fig, ax = plt.subplots(figsize=(10, 8))
        fig.patch.set_facecolor('#f5f5f5')
        ax.set_facecolor('#f5f5f5')
        
        # Remove axes
        ax.axis('off')
        
        # Title
        plt.suptitle('Sales Funnel', fontsize=24, fontweight='bold', y=0.95, color='#333333')
        
        # Funnel parameters
        levels = ['Awareness', 'Interest', 'Consideration', 'Intent', 'Evaluation', 'Purchase']
        values = [10000, 7500, 5000, 3000, 1500, 500]
        colors = ['#FF6B6B', '#FF8E8E', '#FFB3B3', '#FFD8D8', '#FFECEC', '#FFFFFF']
        
        # Calculate funnel segments
        max_width = 0.8
        center = 0.5
        height = 0.15
        bottom = 0.7
        
        # Draw funnel segments
        for i, (level, value, color) in enumerate(zip(levels, values, colors)):
            width = max_width * (values[0] / value) / (values[0] / values[-1])
            left = center - width/2
            
            # Draw rectangle for each level
            rect = plt.Rectangle((left, bottom - i*height), width, height, 
                                facecolor=color, edgecolor='#333333', linewidth=1.5)
            ax.add_patch(rect)
            
            # Add level text
            plt.text(center, bottom - i*height + height/2, level, 
                    ha='center', va='center', fontsize=14, fontweight='bold')
            
            # Add value text
            plt.text(center + width/2 + 0.05, bottom - i*height + height/2, 
                    f'{value:,}', ha='left', va='center', fontsize=12)
        
        # Add connecting lines between segments
        for i in range(len(levels)-1):
            top_left = center - (max_width * (values[0] / values[i]) / (values[0] / values[-1]))/2
            top_right = center + (max_width * (values[0] / values[i]) / (values[0] / values[-1]))/2
            bottom_left = center - (max_width * (values[0] / values[i+1]) / (values[0] / values[-1]))/2
            bottom_right = center + (max_width * (values[0] / values[i+1]) / (values[0] / values[-1]))/2
            
            plt.plot([top_left, bottom_left], [bottom - i*height, bottom - (i+1)*height], 
                    color='#333333', linewidth=1.5)
            plt.plot([top_right, bottom_right], [bottom - i*height, bottom - (i+1)*height], 
                    color='#333333', linewidth=1.5)
        
        # Add decorative elements
        # Top arrow
        ax.arrow(center, bottom + 0.1, 0, -0.05, head_width=0.05, head_length=0.02, 
                fc='#333333', ec='#333333')
        
        # Footer note
        plt.figtext(0.5, 0.05, 'Data as of Q1 2023 | Source: Internal Analytics', 
                   ha='center', fontsize=10, color='#666666')
        
        # Adjust layout
        plt.tight_layout()
        
        # Save the figure
        plt.savefig('funnel_diagram.png', dpi=300, bbox_inches='tight')
        print("Funnel diagram saved as 'funnel_diagram.png'")
        
    except Exception as e:
        print(f"Error creating funnel diagram: {e}")

if __name__ == "__main__":
    create_funnel_diagram()
```
