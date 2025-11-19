"""
Generated Code Metadata:
========================
Original URL: https://rosario.gob.mx
Prompt: Create a data visualization dashboard using a library like D3.js or Matplotlib to display information about Rosario's environmental initiatives, such as the "Feria Ambiental" and "Programa de educación ambiental".
Generated: DETERMINISTIC_2b825d06a347cc59
Batch ID: 20250622_205751
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
from matplotlib.ticker import MaxNLocator
import numpy as np

# Load sample data (in a real scenario, this would come from a database/API)
data = {
    'Initiative': ['Feria Ambiental', 'Programa de educación ambiental', 'Reciclaje urbano', 'Huertas comunitarias'],
    'Participants': [1200, 3500, 8000, 1500],
    'Year': [2020, 2021, 2022, 2023],
    'Budget': [50000, 75000, 120000, 90000]
}
df = pd.DataFrame(data)

# Set up the dashboard figure
plt.figure(figsize=(14, 8))
plt.suptitle('Rosario Environmental Initiatives Dashboard', fontsize=16, y=1.02)

# First subplot: Participation by initiative
ax1 = plt.subplot(2, 2, 1)
bars = ax1.bar(df['Initiative'], df['Participants'], color=['#2ecc71', '#3498db', '#e74c3c', '#f39c12'])
ax1.set_title('Participation by Initiative')
ax1.set_ylabel('Number of Participants')
ax1.tick_params(axis='x', rotation=45)
ax1.yaxis.set_major_locator(MaxNLocator(integer=True))

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom')

# Second subplot: Budget allocation
ax2 = plt.subplot(2, 2, 2)
wedges, texts, autotexts = ax2.pie(df['Budget'], labels=df['Initiative'], 
                                  autopct='%1.1f%%', startangle=90,
                                  colors=['#2ecc71', '#3498db', '#e74c3c', '#f39c12'])
ax2.set_title('Budget Allocation')
ax2.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle

# Third subplot: Participation trend
ax3 = plt.subplot(2, 2, 3)
for i, initiative in enumerate(df['Initiative']):
    ax3.plot(df['Year'][i], df['Participants'][i], 'o', 
             label=initiative, color=['#2ecc71', '#3498db', '#e74c3c', '#f39c12'][i])
ax3.set_title('Participation Trend')
ax3.set_xlabel('Year')
ax3.set_ylabel('Participants')
ax3.legend()
ax3.grid(True, linestyle='--', alpha=0.7)

# Fourth subplot: Budget vs Participation
ax4 = plt.subplot(2, 2, 4)
scatter = ax4.scatter(df['Budget'], df['Participants'], 
                      c=df['Year'], s=100, cmap='viridis')
ax4.set_title('Budget vs Participation')
ax4.set_xlabel('Budget ($)')
ax4.set_ylabel('Participants')
ax4.grid(True, linestyle='--', alpha=0.7)

# Add colorbar for the year
cbar = plt.colorbar(scatter, ax=ax4)
cbar.set_label('Year')

# Adjust layout
plt.tight_layout()

# Save and show
plt.savefig('rosario_environmental_dashboard.png', bbox_inches='tight', dpi=300)
plt.show()
```
