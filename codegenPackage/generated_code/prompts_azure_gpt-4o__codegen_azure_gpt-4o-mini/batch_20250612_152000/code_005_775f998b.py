"""
Generated Code Metadata:
========================
Original URL: https://aanjaneya-aero.com
Prompt: Write code to visualize the growth trajectory of the Indian aerospace and defense sector, incorporating data points such as India's ranking as the 10th largest investor globally, as mentioned by Aanjaneya Aerodynamics Pvt. Ltd.
Generated: DETERMINISTIC_775f998b70270504
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import pandas as pd

# Sample data representing the growth trajectory of the Indian aerospace and defense sector
data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Investment (in Billion USD)': [10, 12, 15, 18, 20, 22, 25, 30, 35],
    'Global Ranking': [12, 11, 10, 10, 10, 10, 10, 10, 10]  # India's ranking as the 10th largest investor
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Function to visualize the growth trajectory
def visualize_growth(df):
    """
    Visualizes the growth trajectory of the Indian aerospace and defense sector.

    Parameters:
    df (DataFrame): A pandas DataFrame containing the growth data.

    Returns:
    None
    """
    try:
        # Create a figure and axis
        fig, ax1 = plt.subplots(figsize=(10, 6))

        # Plot investment data
        ax1.set_xlabel('Year')
        ax1.set_ylabel('Investment (in Billion USD)', color='tab:blue')
        ax1.plot(df['Year'], df['Investment (in Billion USD)'], color='tab:blue', marker='o', label='Investment')
        ax1.tick_params(axis='y', labelcolor='tab:blue')

        # Create a second y-axis for global ranking
        ax2 = ax1.twinx()
        ax2.set_ylabel('Global Ranking', color='tab:red')
        ax2.plot(df['Year'], df['Global Ranking'], color='tab:red', marker='x', linestyle='--', label='Global Ranking')
        ax2.tick_params(axis='y', labelcolor='tab:red')

        # Title and grid
        plt.title('Growth Trajectory of the Indian Aerospace and Defense Sector')
        ax1.grid()

        # Show legend
        fig.tight_layout()
        plt.legend(loc='upper left')
        
        # Display the plot
        plt.show()

    except Exception as e:
        print(f"An error occurred while visualizing the growth: {e}")

# Call the function to visualize the growth
visualize_growth(df)
```
