"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suistrategies.com
Prompt: Create a Python program that uses Matplotlib or Plotly to generate a stacked bar chart illustrating the quarterly asset allocation percentages described by SUI Strategies.
Generated: DETERMINISTIC_31873a4494d2ca19
Batch ID: 20250612_145516
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

# Sample data: Quarterly asset allocation percentages for SUI Strategies
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
strategies = ['Equities', 'Bonds', 'Real Estate', 'Cash']
allocation_percentages = np.array([
    [40, 30, 20, 10],  # Equities
    [30, 40, 20, 10],  # Bonds
    [20, 20, 30, 30],  # Real Estate
    [10, 10, 30, 50]   # Cash
])

# Check if the percentages sum to 100 for each quarter
if not np.all(np.isclose(allocation_percentages.sum(axis=0), 100)):
    raise ValueError("Asset allocation percentages must sum to 100 for each quarter.")

# Create a stacked bar chart
fig, ax = plt.subplots()

# Create bars for each strategy
bottom_values = np.zeros(len(quarters))  # Initialize bottom values for stacking
for i, strategy in enumerate(strategies):
    ax.bar(quarters, allocation_percentages[i], label=strategy, bottom=bottom_values)
    bottom_values += allocation_percentages[i]  # Update bottom values for next bar

# Adding labels and title
ax.set_xlabel('Quarters')
ax.set_ylabel('Allocation Percentage (%)')
ax.set_title('Quarterly Asset Allocation Percentages by SUI Strategies')
ax.legend(title='Strategies')

# Display the grid
ax.yaxis.grid(True)

# Show the plot
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()
```
