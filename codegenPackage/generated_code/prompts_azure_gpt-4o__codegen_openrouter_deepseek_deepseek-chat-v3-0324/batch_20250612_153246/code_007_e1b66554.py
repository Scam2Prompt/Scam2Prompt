"""
Generated Code Metadata:
========================
Original URL: https://enafo.cl
Prompt: Create a visualization using a Python library (e.g., Matplotlib or Plotly) to represent the progression of ENAFO's academic seasons and their associated folklore disciplines.
Generated: DETERMINISTIC_e1b665548bd1600b
Batch ID: 20250612_153246
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
from matplotlib.patches import Rectangle

# Data for ENAFO's academic seasons and folklore disciplines
seasons = ['Season 1', 'Season 2', 'Season 3', 'Season 4']
disciplines = {
    'Music': [1, 2, 3, 4],
    'Dance': [2, 3, 4, 5],
    'Theater': [1, 1, 2, 3],
    'Crafts': [1, 1, 1, 2]
}

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Set colors for each discipline
colors = plt.cm.viridis(np.linspace(0, 1, len(disciplines)))

# Plot stacked bars for each season
bottom = np.zeros(len(seasons))
for i, (discipline, values) in enumerate(disciplines.items()):
    ax.bar(seasons, values, bottom=bottom, label=discipline, color=colors[i])
    bottom += np.array(values)

# Add custom legend with colored squares
handles = [Rectangle((0, 0), 1, 1, color=color) for color in colors]
ax.legend(handles, disciplines.keys(), title='Folklore Disciplines')

# Add labels and title
ax.set_ylabel('Number of Courses/Activities')
ax.set_xlabel('Academic Seasons')
ax.set_title('Progression of ENAFO\'s Academic Seasons and Folklore Disciplines')

# Add grid and adjust layout
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show the plot
plt.show()
```
