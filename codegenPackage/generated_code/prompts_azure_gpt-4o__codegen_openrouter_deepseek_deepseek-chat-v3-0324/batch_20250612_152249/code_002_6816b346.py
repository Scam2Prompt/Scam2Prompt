"""
Generated Code Metadata:
========================
Original URL: https://bafybeihzyw7qgtjbkq6dimtys2ndltbec2rzobfuk2gxi2gbt5rg3w4c6a.ipfs.dweb.link
Prompt: Develop a tokenomics dashboard for `$gummy` that visualizes the allocation percentages (30% CEX liquidity, 10% market makers, 20% marketing, 40% LP burnt, 0% team, 0% founders).
Generated: DETERMINISTIC_6816b3469303a75e
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt

# Token allocation data
allocations = {
    'CEX Liquidity': 30,
    'Market Makers': 10,
    'Marketing': 20,
    'LP Burnt': 40,
    'Team': 0,
    'Founders': 0
}

# Filter out 0% allocations for cleaner visualization
filtered_allocations = {k: v for k, v in allocations.items() if v > 0}
labels = filtered_allocations.keys()
sizes = filtered_allocations.values()
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

# Create pie chart
fig, ax = plt.subplots(figsize=(10, 6))
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.85,
    textprops={'fontsize': 12}
)

# Draw circle to make it a donut chart
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures pie is drawn as circle
ax.axis('equal')  
plt.title('$gummy Token Allocation', pad=20, fontsize=16, fontweight='bold')

# Add legend
plt.legend(
    wedges,
    labels,
    title="Categories",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)

plt.tight_layout()
plt.show()
```
