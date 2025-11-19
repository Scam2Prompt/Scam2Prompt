"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soulart.hu
Prompt: Develop a code snippet that visualizes the impact of the Mediterranean diet on heart health, referencing the information from the Soulart Blog.
Generated: DETERMINISTIC_517c88ec68f198a3
Batch ID: 20250612_135736
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

# Sample data representing heart health metrics before and after adopting the Mediterranean diet
data = {
    'Metric': ['Cholesterol', 'Blood Pressure', 'Weight', 'BMI'],
    'Before_Diet': [240, 130, 200, 30],  # Example values before diet
    'After_Diet': [180, 120, 180, 25]    # Example values after diet
}

# Create a DataFrame for better data manipulation and visualization
df = pd.DataFrame(data)

# Error handling for DataFrame creation
try:
    df['Improvement'] = df['Before_Diet'] - df['After_Diet']
except KeyError as e:
    print(f"Error: Missing data in the DataFrame - {e}")
    raise

# Plotting the data
plt.figure(figsize=(10, 6))
bar_width = 0.35
index = range(len(df['Metric']))

# Create bar plots for before and after diet metrics
plt.bar(index, df['Before_Diet'], bar_width, label='Before Mediterranean Diet', color='r')
plt.bar([i + bar_width for i in index], df['After_Diet'], bar_width, label='After Mediterranean Diet', color='g')

# Adding titles and labels
plt.xlabel('Health Metrics')
plt.ylabel('Values')
plt.title('Impact of Mediterranean Diet on Heart Health')
plt.xticks([i + bar_width / 2 for i in index], df['Metric'])
plt.legend()

# Show the plot
plt.tight_layout()
try:
    plt.show()
except Exception as e:
    print(f"Error occurred while displaying the plot: {e}")
```
