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
import numpy as np

# Function to validate data input
def validate_data(data):
    """Validates that the data is correctly formatted and non-empty."""
    if not data or not all(isinstance(i, (int, float)) for i in data):
        raise ValueError("Data must be a non-empty list of numbers.")

# Data: hypothetical statistics inspired by the Soulart Blog
# Percentage of heart health improvement over time (in months) based on the Mediterranean diet
months = list(range(1, 13))  # 1 to 12 months
diet_impact = [5, 8, 12, 15, 20, 25, 30, 35, 38, 40, 42, 45]  # Improvement percentages

# Validate the data
validate_data(months)
validate_data(diet_impact)

# Plotting the data
plt.figure(figsize=(10, 6))  # Set figure size

plt.plot(months, diet_impact, marker='o', color='green', linestyle='-', label="Mediterranean Diet Impact")

# Adding annotations, labels, and title to make the graph informative
plt.title("Impact of Mediterranean Diet on Heart Health Over Time", fontsize=14)
plt.xlabel("Months on Mediterranean Diet", fontsize=12)
plt.ylabel("Heart Health Improvement (%)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)  # Add grid for better readability
plt.legend(fontsize=12)  # Add legend

# Highlight maximum improvement for better visualization
max_improvement = max(diet_impact)
max_month = months[diet_impact.index(max_improvement)]
plt.annotate(f"Max Improvement: {max_improvement}%", 
             xy=(max_month, max_improvement), 
             xytext=(max_month+1, max_improvement+5),
             arrowprops=dict(facecolor='blue', shrink=0.05),
             fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()
```
