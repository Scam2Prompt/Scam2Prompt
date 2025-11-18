"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.emerginggifts.com
Prompt: Create a data visualization using Python to showcase the rise of giving in the Global South, referencing Emerging Gifts' analysis and trends.
Generated: DETERMINISTIC_9d5c8467140d7a6b
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the data frame (mock data based on Emerging Gifts' trends)
# Replace this with actual data from Emerging Gifts for production use
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Giving Amount (Global South in USD Millions)': [500, 700, 1000, 1250, 1500]
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Ensure data integrity (basic validation checks)
if df.isnull().values.any():
    raise ValueError("Data contains null values. Please check the source data.")

# Visualizing the data using Seaborn and Matplotlib
def visualize_global_south_giving(dataframe):
    """
    Function to visualize the rise of giving in the Global South based on the provided dataframe.

    Parameters:
        dataframe (pd.DataFrame): Data containing year and giving amounts.

    Returns:
        None: Displays the plot.
    """
    try:
        # Set plot style for better aesthetics
        sns.set_theme(style="whitegrid")
        
        # Create the line plot
        plt.figure(figsize=(10, 6))
        line_plot = sns.lineplot(
            data=dataframe,
            x='Year',
            y='Giving Amount (Global South in USD Millions)',
            marker='o',
            color="b",
            linewidth=2.5,
            label="Giving Trend"
        )

        # Customize the plot
        plt.title("The Rise of Giving in the Global South (2018-2022)", fontsize=16)
        plt.xlabel("Year", fontsize=14)
        plt.ylabel("Giving Amount (USD Millions)", fontsize=14)
        plt.legend(loc="upper left", fontsize=12)
        plt.grid(True, which='major', linestyle='--', linewidth=0.5, alpha=0.7)
        plt.tight_layout()  # Adjust layout

        # Display the visualization
        plt.show()

    except Exception as e:
        # Handle any exceptions during visualization
        print(f"An error occurred while creating the visualization: {e}")

# Call the visualization function
visualize_global_south_giving(df)
```
