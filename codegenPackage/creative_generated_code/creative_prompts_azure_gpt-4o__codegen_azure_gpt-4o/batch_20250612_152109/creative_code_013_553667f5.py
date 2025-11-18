"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meatmaster.pe
Prompt: Write code to generate a comparison chart of Caja China models based on their dimensions, weight, and meat capacity, using data from Meat Master.
Generated: DETERMINISTIC_553667f5a6607906
Batch ID: 20250612_152109
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

# Define the data from Meat Master for Caja China models
models = [
    {"name": "Caja China Model 1", "dimensions": (48, 24, 20), "weight": 55, "meat_capacity": 70},
    {"name": "Caja China Model 2", "dimensions": (60, 30, 24), "weight": 75, "meat_capacity": 100},
    {"name": "Caja China Model 3", "dimensions": (72, 36, 30), "weight": 95, "meat_capacity": 130},
]

# Extract data for the chart
model_names = [model["name"] for model in models]
weights = [model["weight"] for model in models]
meat_capacities = [model["meat_capacity"] for model in models]

# Generate a comparison chart
def generate_comparison_chart(model_names, weights, meat_capacities):
    """
    Generates a comparison chart of Caja China models based on their weight and meat capacity.

    Args:
        model_names (list): Names of the Caja China models.
        weights (list): Weight of each model.
        meat_capacities (list): Meat capacity of each model.

    Returns:
        None
    """
    try:
        # Define positions for the bars
        x = np.arange(len(model_names))

        # Set the width for bars
        bar_width = 0.35

        # Create the figure and axis
        fig, ax = plt.subplots(figsize=(10, 6))

        # Add bars for weights
        weight_bars = ax.bar(x - bar_width/2, weights, bar_width, label='Weight (lbs)', color='steelblue')

        # Add bars for meat capacities
        capacity_bars = ax.bar(x + bar_width/2, meat_capacities, bar_width, label='Meat Capacity (lbs)', color='darkorange')

        # Add labels, title, and legend
        ax.set_xlabel('Caja China Models', fontsize=12)
        ax.set_ylabel('Values (lbs)', fontsize=12)
        ax.set_title('Comparison Chart of Caja China Models', fontsize=16)
        ax.set_xticks(x)
        ax.set_xticklabels(model_names, rotation=45, ha="right", fontsize=10)
        ax.legend()

        # Display value labels above bars
        def add_value_labels(bars):
            """Adds value labels to bars in a chart."""
            for bar in bars:
                height = bar.get_height()
                ax.annotate('{}'.format(height),
                            xy=(bar.get_x() + bar.get_width()/2, height),
                            xytext=(0, 3),  # Offset for the label
                            textcoords="offset points",
                            ha='center', va='bottom', fontsize=10)
        
        add_value_labels(weight_bars)
        add_value_labels(capacity_bars)

        # Adjust layout and show the plot
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occurred while generating the chart: {e}")

# Call the function to generate the chart
generate_comparison_chart(model_names, weights, meat_capacities)
```
