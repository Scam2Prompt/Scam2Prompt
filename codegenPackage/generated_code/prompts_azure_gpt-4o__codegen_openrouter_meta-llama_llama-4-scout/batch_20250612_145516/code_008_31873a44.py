"""
Generated Code Metadata:
========================
Original URL: https://suistrategies.com
Prompt: Create a Python program that uses Matplotlib or Plotly to generate a stacked bar chart illustrating the quarterly asset allocation percentages described by SUI Strategies.
Generated: DETERMINISTIC_31873a4494d2ca19
Batch ID: 20250612_145516
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

def generate_stacked_bar_chart():
    """
    Generate a stacked bar chart illustrating the quarterly asset allocation percentages described by SUI Strategies.
    """
    
    # Define SUI Strategies asset allocation percentages
    sui_strategies = {
        'Conservative': {'Q1': [40, 30, 30], 'Q2': [45, 25, 30], 'Q3': [50, 20, 30], 'Q4': [55, 15, 30]},
        'Moderate': {'Q1': [30, 40, 30], 'Q2': [35, 35, 30], 'Q3': [40, 30, 30], 'Q4': [45, 25, 30]},
        'Aggressive': {'Q1': [20, 50, 30], 'Q2': [25, 45, 30], 'Q3': [30, 40, 30], 'Q4': [35, 35, 30]}
    }

    # Define asset classes
    asset_classes = ['Fixed Income', 'Equity', 'Alternatives']

    # Create a figure and axis object
    fig, ax = plt.subplots(len(sui_strategies), 1, figsize=(10, 6*len(sui_strategies)))

    # Check if there is only one strategy
    if len(sui_strategies) == 1:
        ax = [ax]

    # Iterate over SUI Strategies
    for i, (strategy, quarters) in enumerate(sui_strategies.items()):
        # Initialize bottom values
        bottom = np.zeros(4)

        # Iterate over quarters
        for j, (quarter, percentages) in enumerate(quarters.items()):
            # Plot stacked bar chart
            ax[i].bar(['Q1', 'Q2', 'Q3', 'Q4'], percentages, bottom=bottom, label=asset_classes[j] if i == 0 else None)

            # Update bottom values
            bottom += np.array(percentages)

        # Set title and labels
        ax[i].set_title(f'{strategy} Asset Allocation')
        ax[i].set_xlabel('Quarter')
        ax[i].set_ylabel('Percentage')
        ax[i].legend()

    # Layout so plots do not overlap
    fig.tight_layout()

    # Display the plot
    plt.show()

if __name__ == "__main__":
    try:
        generate_stacked_bar_chart()
    except Exception as e:
        print(f"An error occurred: {e}")
```
