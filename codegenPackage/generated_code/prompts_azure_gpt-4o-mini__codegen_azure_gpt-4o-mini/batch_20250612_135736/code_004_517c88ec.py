"""
Generated Code Metadata:
========================
Original URL: https://soulart.hu
Prompt: Develop a code snippet that visualizes the impact of the Mediterranean diet on heart health, referencing the information from the Soulart Blog.
Generated: DETERMINISTIC_517c88ec68f198a3
Batch ID: 20250612_135736
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

# Sample data representing heart health metrics before and after adopting the Mediterranean diet
data = {
    'Metric': ['Cholesterol', 'Blood Pressure', 'Weight', 'Triglycerides'],
    'Before_Diet': [220, 130, 180, 150],  # Example values
    'After_Diet': [180, 120, 160, 130]     # Example values
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Calculate the change in metrics
df['Change'] = df['Before_Diet'] - df['After_Diet']

# Set up the plot
plt.figure(figsize=(10, 6))
bar_width = 0.35
index = np.arange(len(df['Metric']))

# Create bars for before and after diet metrics
bars1 = plt.bar(index, df['Before_Diet'], bar_width, label='Before Diet', color='lightcoral')
bars2 = plt.bar(index + bar_width, df['After_Diet'], bar_width, label='After Diet', color='lightgreen')

# Adding labels and title
plt.xlabel('Health Metrics')
plt.ylabel('Values')
plt.title('Impact of Mediterranean Diet on Heart Health')
plt.xticks(index + bar_width / 2, df['Metric'])
plt.legend()

# Adding value annotations on top of the bars
def add_value_labels(bars):
    """Add value labels on top of the bars."""
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')

add_value_labels(bars1)
add_value_labels(bars2)

# Show the plot
plt.tight_layout()
try:
    plt.show()
except Exception as e:
    print(f"An error occurred while displaying the plot: {e}")
```
