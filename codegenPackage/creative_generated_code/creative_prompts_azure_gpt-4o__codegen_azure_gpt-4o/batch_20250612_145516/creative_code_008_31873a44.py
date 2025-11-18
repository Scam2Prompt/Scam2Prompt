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

# Sample data for the quarterly asset allocation percentages
# Replace with actual percentages as necessary
data = {
    "Q1": {"Stocks": 50, "Bonds": 30, "Real Estate": 10, "Cash": 10},
    "Q2": {"Stocks": 55, "Bonds": 25, "Real Estate": 15, "Cash": 5},
    "Q3": {"Stocks": 60, "Bonds": 20, "Real Estate": 15, "Cash": 5},
    "Q4": {"Stocks": 65, "Bonds": 15, "Real Estate": 10, "Cash": 10},
}

# Prepare data for the stacked bar chart
quarters = list(data.keys())
categories = list(data[quarters[0]].keys())
values = {category: [data[q][category] for q in quarters] for category in categories}

# Generate x positions for the bars
x_positions = np.arange(len(quarters))

# Initialize the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create the stacked bar chart
bottom_values = np.zeros(len(quarters))
for category in categories:
    ax.bar(
        x_positions,
        values[category],
        label=category,
        bottom=bottom_values
    )
    bottom_values += values[category]  # Update bottom values for the next stack

# Customize the chart
ax.set_title("Quarterly Asset Allocation Percentages - SUI Strategies", fontsize=16)
ax.set_xlabel("Quarters", fontsize=12)
ax.set_ylabel("Percentage (%)", fontsize=12)
ax.set_xticks(x_positions)
ax.set_xticklabels(quarters)
ax.legend(title="Categories", loc="upper left", fontsize=10)
ax.grid(axis="y", linestyle="--", alpha=0.7)

# Add percentage labels on each stack
for i, quarter in enumerate(quarters):
    y_offset = 0
    for category in categories:
        percentage = values[category][i]
        if percentage > 0:
            ax.text(
                x=i,
                y=y_offset + percentage / 2,
                s=f"{percentage}%",
                ha="center",
                va="center",
                fontsize=9,
                color="white" if percentage > 15 else "black"
            )
        y_offset += percentage

# Adjust layout to fit the chart
plt.tight_layout()

# Show the plot
plt.show()
```
