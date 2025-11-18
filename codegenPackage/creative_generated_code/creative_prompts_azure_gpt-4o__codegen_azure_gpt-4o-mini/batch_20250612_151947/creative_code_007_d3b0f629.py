"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socialimpactheroes.com
Prompt: Write code to visualize the frequency of articles published in different categories like "Social Impact Investors" and "Stars Making a Social Impact" using Matplotlib.
Generated: DETERMINISTIC_d3b0f629e6c231d9
Batch ID: 20250612_151947
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

# Sample data for articles published in different categories
data = {
    'Category': ['Social Impact Investors', 'Stars Making a Social Impact', 'Social Impact Investors', 
                 'Stars Making a Social Impact', 'Social Impact Investors'],
    'Count': [10, 5, 7, 8, 12]
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Group by category to get the total count of articles published in each
category_counts = df.groupby('Category').sum().reset_index()

# Check if the DataFrame is empty before proceeding
if category_counts.empty:
    raise ValueError("No data available to visualize.")

# Plotting the frequency of articles by category
plt.figure(figsize=(10, 6))
plt.bar(category_counts['Category'], category_counts['Count'], color=['#1f77b4', '#ff7f0e'])
plt.title('Frequency of Articles Published by Category', fontsize=16)
plt.xlabel('Category', fontsize=14)
plt.ylabel('Number of Articles', fontsize=14)
plt.xticks(rotation=15)  # Rotate x-axis labels for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add grid for better visualization

# Show the plot
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
```
