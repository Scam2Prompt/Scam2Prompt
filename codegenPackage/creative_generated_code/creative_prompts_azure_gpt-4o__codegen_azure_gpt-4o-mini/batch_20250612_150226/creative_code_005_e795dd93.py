"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rplanet-io.vercel.app
Prompt: Write a Python script to visualize the faction distribution (Masterminds, Warriors, Renegades) on the R-Planet map using matplotlib.
Generated: DETERMINISTIC_e795dd93e1c2fe54
Batch ID: 20250612_150226
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

# Define factions and their respective distribution on the R-Planet map
factions = ['Masterminds', 'Warriors', 'Renegades']
distribution = [40, 35, 25]  # Example distribution percentages

# Check if the distribution sums up to 100
if sum(distribution) != 100:
    raise ValueError("Distribution must sum up to 100%")

# Function to visualize faction distribution
def visualize_faction_distribution(factions, distribution):
    """
    Visualizes the distribution of factions on the R-Planet map using a pie chart.
    
    Parameters:
    - factions: List of faction names.
    - distribution: List of percentage distribution for each faction.
    
    Raises:
    - ValueError: If the distribution does not sum to 100.
    """
    
    # Create a pie chart
    plt.figure(figsize=(8, 8))
    wedges, texts, autotexts = plt.pie(
        distribution,
        labels=factions,
        autopct='%1.1f%%',
        startangle=90,
        colors=plt.cm.tab10.colors
    )
    
    # Beautify the plot
    plt.setp(autotexts, size=12, weight="bold", color="white")
    plt.setp(texts, size=12)
    
    # Equal aspect ratio ensures that pie chart is circular
    plt.axis('equal')

    # Title for the plot
    plt.title('Faction Distribution on the R-Planet Map', fontsize=16, weight='bold')
    
    # Display the plot
    plt.show()

# Execute the visualization function
if __name__ == "__main__":
    try:
        visualize_faction_distribution(factions, distribution)
    except Exception as e:
        print(f"An error occurred: {e}")
```
