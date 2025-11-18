"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ordriomint.pages.dev
Prompt: Create a tool in Python to visualize the supply statistics (total supply, max supply, burned, divisibility) for Ord.io inscriptions using matplotlib or seaborn.
Generated: DETERMINISTIC_6b5bf565ae9a768d
Batch ID: 20250612_151038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class SupplyStatisticsVisualizer:
    def __init__(self, data):
        """
        Initializes the visualizer with supply statistics data.

        :param data: A dictionary containing supply statistics with keys:
                     'total_supply', 'max_supply', 'burned', 'divisibility'.
        """
        self.data = data
        self.validate_data()

    def validate_data(self):
        """
        Validates the input data to ensure all required fields are present and are numbers.
        Raises ValueError if validation fails.
        """
        required_keys = ['total_supply', 'max_supply', 'burned', 'divisibility']
        for key in required_keys:
            if key not in self.data:
                raise ValueError(f'Missing required data: {key}')
            if not isinstance(self.data[key], (int, float)):
                raise ValueError(f'Invalid data type for {key}: Expected int or float, got {type(self.data[key])}')

    def create_visualization(self):
        """
        Creates a bar plot to visualize the supply statistics.
        """
        # Prepare data for plotting
        labels = list(self.data.keys())
        values = list(self.data.values())
        
        # Set the aesthetics for seaborn
        sns.set(style='whitegrid')

        # Create the bar plot
        plt.figure(figsize=(10, 6))
        bar_plot = sns.barplot(x=labels, y=values, palette='viridis')
        
        # Add data labels on top of the bars
        for p in bar_plot.patches:
            bar_plot.annotate(f'{p.get_height():.2f}', 
                              (p.get_x() + p.get_width() / 2., p.get_height()), 
                              ha='center', va='baseline', 
                              color='black', 
                              fontsize=12, 
                              xytext=(0, 5), 
                              textcoords='offset points')

        # Set titles and labels
        plt.title('Ord.io Supply Statistics', fontsize=16)
        plt.xlabel('Statistics', fontsize=14)
        plt.ylabel('Values', fontsize=14)
        plt.xticks(rotation=45)
        plt.ylim(0, max(values) * 1.1)  # Slightly increase y-limit for better visibility

        # Show the plot
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Example data for visualization
    supply_data = {
        'total_supply': 1000000,
        'max_supply': 2000000,
        'burned': 150000,
        'divisibility': 8
    }
    
    try:
        visualizer = SupplyStatisticsVisualizer(supply_data)
        visualizer.create_visualization()
    except ValueError as e:
        print(f"Error: {e}")
```
