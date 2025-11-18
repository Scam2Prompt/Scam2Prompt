"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meme-indexs.pages.dev
Prompt: Develop a dashboard to visualize the percentage allocations of meme coin indices such as "Meme Titan Index" and "Meme Moonshot Index" using `$MEMEX` data.
Generated: DETERMINISTIC_6299f70cbdd42691
Batch ID: 20250612_145633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Define the function to visualize meme coin indices allocation
def visualize_meme_indices(data):
    """
    Visualizes the percentage allocation of meme coin indices using bar chart.
    
    Parameters:
    data (dict): A dictionary containing indices as keys and their allocations as values. 
                 e.g., {'Meme Titan Index': 60, 'Meme Moonshot Index': 40}
    
    Returns:
    None
    """
    try:
        # Validate data is a dictionary
        if not isinstance(data, dict):
            raise TypeError("Input data must be a dictionary with index names as keys and their allocations as values.")
        
        # Validate allocations add up to 100
        total_allocation = sum(data.values())
        if total_allocation != 100:
            raise ValueError("The total allocation percentages must add up to 100.")
        
        # Extract indices and allocations for plotting
        indices = list(data.keys())
        allocations = list(data.values())
        
        # Plot the data
        plt.figure(figsize=(8, 6))
        plt.bar(indices, allocations, color=['#FF5733', '#33C3F0'], edgecolor='black')
        plt.gca().yaxis.set_major_formatter(PercentFormatter())  # Format y-axis as percentages
        plt.title('Meme Coin Indices Allocation', fontsize=16, fontweight='bold')
        plt.ylabel('Percentage Allocation (%)', fontsize=14)
        plt.xlabel('Indices', fontsize=14)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        
        # Show the plot
        plt.show()
    except Exception as e:
        # Catch and log any exceptions
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    # Example data for `$MEMEX` allocations
    meme_index_data = {
        'Meme Titan Index': 60,  # 60% allocation
        'Meme Moonshot Index': 40  # 40% allocation
    }
    
    # Call the visualization function
    visualize_meme_indices(meme_index_data)
```
