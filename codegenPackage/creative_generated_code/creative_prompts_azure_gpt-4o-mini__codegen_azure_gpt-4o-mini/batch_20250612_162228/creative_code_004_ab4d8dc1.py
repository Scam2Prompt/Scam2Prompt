"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accept-gummyonsol.pages.dev
Prompt: Generate a code snippet that demonstrates how to analyze the token distribution percentages (30%, 10%, 20%, 40%) for $Gummy as described in the Gummynomics content.
Generated: DETERMINISTIC_ab4d8dc15e4de51b
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt

def analyze_token_distribution(distribution):
    """
    Analyze the token distribution percentages for a given cryptocurrency.

    Parameters:
    distribution (dict): A dictionary containing token categories and their respective percentages.

    Raises:
    ValueError: If the total percentage does not equal 100.
    """
    # Validate the distribution percentages
    total_percentage = sum(distribution.values())
    
    if total_percentage != 100:
        raise ValueError(f"Total percentage must equal 100%, but got {total_percentage}%.")

    # Prepare data for visualization
    categories = list(distribution.keys())
    percentages = list(distribution.values())

    # Create a pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(percentages, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title('Token Distribution for $Gummy')
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.

    # Display the pie chart
    plt.show()

# Example token distribution for $Gummy
gummy_distribution = {
    'Category A': 30,
    'Category B': 10,
    'Category C': 20,
    'Category D': 40
}

# Analyze the token distribution
try:
    analyze_token_distribution(gummy_distribution)
except ValueError as e:
    print(f"Error: {e}")
```
