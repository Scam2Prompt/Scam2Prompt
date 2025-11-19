"""
Generated Code Metadata:
========================
Original URL: https://amplatinumconsulting.com
Prompt: Generate code to visualize consulting project timelines using Python libraries like matplotlib or seaborn.
Generated: DETERMINISTIC_4873955226d9f564
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data for consulting project timelines
data = {
    'Project': ['Project A', 'Project B', 'Project C', 'Project D'],
    'Start Date': ['2023-01-01', '2023-02-15', '2023-03-01', '2023-04-10'],
    'End Date': ['2023-03-01', '2023-04-15', '2023-05-15', '2023-06-30']
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Convert date strings to datetime objects
df['Start Date'] = pd.to_datetime(df['Start Date'])
df['End Date'] = pd.to_datetime(df['End Date'])

# Calculate the duration of each project
df['Duration'] = (df['End Date'] - df['Start Date']).dt.days

# Create a horizontal bar plot to visualize project timelines
plt.figure(figsize=(10, 6))
plt.barh(df['Project'], df['Duration'], left=df['Start Date'].map(pd.Timestamp.timestamp), color='skyblue')

# Set the x-axis to show dates
plt.xticks(ticks=np.arange(df['Start Date'].min().timestamp(), df['End Date'].max().timestamp(), 86400),
           labels=pd.date_range(start=df['Start Date'].min(), end=df['End Date'].max(), freq='D').date,
           rotation=45)

# Add labels and title
plt.xlabel('Timeline')
plt.ylabel('Projects')
plt.title('Consulting Project Timelines')
plt.grid(axis='x')

# Error handling for displaying the plot
try:
    plt.tight_layout()
    plt.show()
except Exception as e:
    print(f"An error occurred while displaying the plot: {e}")
```
