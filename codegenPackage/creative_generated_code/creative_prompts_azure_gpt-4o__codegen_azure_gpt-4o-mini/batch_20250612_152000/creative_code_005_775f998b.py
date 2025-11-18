"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aanjaneya-aero.com
Prompt: Write code to visualize the growth trajectory of the Indian aerospace and defense sector, incorporating data points such as India's ranking as the 10th largest investor globally, as mentioned by Aanjaneya Aerodynamics Pvt. Ltd.
Generated: DETERMINISTIC_775f998b70270504
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define the data for the Indian aerospace and defense sector growth trajectory
data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Investment (in billion USD)': [12, 14, 16, 18, 20, 22, 25, 28, 30],
    'Global Ranking': [10, 9, 8, 7, 6, 5, 4, 3, 2]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Check for missing values and handle them
if df.isnull().values.any():
    raise ValueError("Data contains missing values, please check the input data.")

# Set the Year as the index for better plotting
df.set_index('Year', inplace=True)

# Create a figure and axis for the plots
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot investment growth
ax1.set_title('Growth Trajectory of Indian Aerospace and Defense Sector',
             fontsize=14)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Investment (in billion USD)', fontsize=12, color='tab:blue')
ax1.plot(df.index, df['Investment (in billion USD)'], color='tab:blue', marker='o', label='Investment')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Create a second y-axis for the global ranking
ax2 = ax1.twinx()
ax2.set_ylabel('Global Ranking', fontsize=12, color='tab:red')
ax2.plot(df.index, df['Global Ranking'], color='tab:red', marker='s', linestyle='--', label='Global Ranking')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Add grid, legend, and show the plot
ax1.grid()
fig.tight_layout()
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.show()
```
