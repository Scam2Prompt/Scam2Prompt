"""
Generated Code Metadata:
========================
Original URL: https://accept-gummyonsol.pages.dev
Prompt: Generate a code snippet that demonstrates how to analyze the token distribution percentages (30%, 10%, 20%, 40%) for $Gummy as described in the Gummynomics content.
Generated: DETERMINISTIC_ab4d8dc15e4de51b
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt

def analyze_token_distribution(distribution):
    """
    Analyzes the token distribution percentages and visualizes them using a pie chart.

    Parameters:
    distribution (dict): A dictionary containing token categories and their corresponding percentages.

    Raises:
    ValueError: If the total percentage does not equal 100.
    """
    # Validate the total percentage
    total_percentage = sum(distribution.values())
    if total_percentage != 100:
        raise ValueError(f"Total percentage must equal 100, but got {total_percentage}.")

    # Prepare data for visualization
    labels = distribution.keys()
    sizes = distribution.values()
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']  # Define colors for each category

    # Create a pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
    plt.title('Token Distribution for $Gummy')
    plt.show()

# Token distribution for $Gummy
gummy_distribution = {
    'Category A': 30,
    'Category B': 10,
    'Category C': 20,
    'Category D': 40
}

# Analyze and visualize the token distribution
try:
    analyze_token_distribution(gummy_distribution)
except ValueError as e:
    print(f"Error: {e}")
```
