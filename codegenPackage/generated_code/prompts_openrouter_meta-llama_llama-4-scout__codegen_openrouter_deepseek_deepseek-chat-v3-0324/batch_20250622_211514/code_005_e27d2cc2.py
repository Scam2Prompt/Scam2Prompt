"""
Generated Code Metadata:
========================
Original URL: https://traceybaptiste.com
Prompt: Develop a plot for a new young adult novel that combines elements of science, history, and fantasy, inspired by Tracey Baptiste's writing style.
Generated: DETERMINISTIC_e27d2cc282a49723
Batch ID: 20250622_211514
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
from datetime import datetime
import random

# Constants for plot structure
PLOT_POINTS = 5  # Key plot points to visualize
CHAPTERS = 12    # Total chapters in the novel

# Define the protagonist's emotional arc (values between -1 to 1)
def generate_emotional_arc(chapters):
    """Generate a realistic emotional arc for the protagonist."""
    arc = np.linspace(0, 1, chapters)
    # Add some randomness to make it organic
    for i in range(1, chapters-1):
        arc[i] += random.uniform(-0.2, 0.2)
    return np.clip(arc, -0.5, 1)  # Keep within bounds

# Define key plot points with their chapter positions
def get_plot_points(chapters):
    """Return dictionary of key plot points and their chapter positions."""
    return {
        'Inciting Incident': int(chapters * 0.15),
        'First Major Twist': int(chapters * 0.35),
        'Midpoint Revelation': int(chapters * 0.5),
        'Darkest Moment': int(chapters * 0.75),
        'Climax': int(chapters * 0.9)
    }

# Generate plot data
chapters = np.arange(1, CHAPTERS + 1)
emotional_arc = generate_emotional_arc(CHAPTERS)
plot_points = get_plot_points(CHAPTERS)

# Create the plot
plt.figure(figsize=(12, 6))

# Plot emotional arc
plt.plot(chapters, emotional_arc, 
         label='Protagonist Emotional Arc', 
         color='royalblue', 
         linewidth=2.5,
         marker='o')

# Highlight key plot points
for point, chap in plot_points.items():
    plt.scatter(chap, emotional_arc[chap-1], 
                s=150, 
                zorder=5,
                label=f'{point} (Ch. {chap})')

# Add scientific/historical elements as background
plt.axhline(y=0, color='black', linestyle='--', alpha=0.3)
plt.fill_between(chapters, emotional_arc, 0, 
                 where=(emotional_arc > 0), 
                 color='green', alpha=0.1,
                 label='Scientific Discovery')
plt.fill_between(chapters, emotional_arc, 0, 
                 where=(emotional_arc < 0), 
                 color='red', alpha=0.1,
                 label='Historical Conflict')

# Formatting
plt.title('YA Novel Plot Structure\n(Science, History & Fantasy)', 
          fontsize=14, pad=20)
plt.xlabel('Chapter Number', fontsize=12)
plt.ylabel('Emotional Intensity', fontsize=12)
plt.xticks(chapters)
plt.grid(alpha=0.2)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Add subtitle with current date
today = datetime.now().strftime('%Y-%m-%d')
plt.suptitle(f'Plot generated on {today}', 
             y=0.02, x=0.15, 
             fontsize=9, 
             alpha=0.5)

plt.tight_layout()
plt.show()
```
