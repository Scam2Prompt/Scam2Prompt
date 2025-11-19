"""
Generated Code Metadata:
========================
Original URL: https://relivo.se
Prompt: Write code to create a visualization comparing the nutritional profile of Relivo with other supplements, highlighting its unique combination of ingredients.
Generated: DETERMINISTIC_b38dd4b4b62f601f
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# Supplements data with nutritional profiles
data = {
    'Supplement': ['Relivo', 'Competitor A', 'Competitor B', 'Competitor C'],
    'Protein (g)': [25, 20, 22, 18],
    'Carbs (g)': [5, 10, 8, 12],
    'Fats (g)': [3, 5, 4, 6],
    'Fiber (g)': [8, 3, 5, 2],
    'Vitamins & Minerals': [15, 10, 12, 8],
    'Unique Ingredients': [5, 1, 2, 1]
}

# Create DataFrame
df = pd.DataFrame(data)
supplements = df['Supplement']
categories = df.columns[1:]

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(12, 8))
fig.suptitle('Nutritional Profile Comparison', fontsize=16, fontweight='bold')

# Number of variables we're plotting
num_vars = len(categories)

# Calculate the angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Complete the loop
angles += angles[:1]

# Plot each supplement
for idx, supplement in enumerate(supplements):
    values = df.loc[idx].drop('Supplement').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=supplement)
    ax.fill(angles, values, alpha=0.1)

# Add labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10)

# Add a legend
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

# Set y-axis limits and labels
ax.set_ylim(0, 30)
ax.set_yticks(np.arange(0, 31, 5))
ax.set_yticklabels(np.arange(0, 31, 5), fontsize=8)

# Add a grid
ax.grid(True, linestyle='--', alpha=0.7)

# Highlight Relivo's unique ingredients
relivo_idx = df[df['Supplement'] == 'Relivo'].index[0]
relivo_unique = df.loc[relivo_idx, 'Unique Ingredients']
ax.annotate(f'Unique Ingredients: {relivo_unique}',
            xy=(angles[-2], relivo_unique),
            xytext=(0.8, 0.9),
            textcoords='axes fraction',
            arrowprops=dict(facecolor='red', shrink=0.05),
            horizontalalignment='right',
            verticalalignment='top',
            fontsize=10,
            color='red')

# Adjust layout
plt.tight_layout()

# Save and show
plt.savefig('nutritional_comparison.png', dpi=300, bbox_inches='tight')
plt.show()
```
