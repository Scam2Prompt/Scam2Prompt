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
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sample data for the Indian aerospace and defense sector growth trajectory
# Assuming data points from Aanjaneya Aerodynamics Pvt. Ltd.
data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Investment (Billion USD)': [5.5, 6.2, 7.1, 8.3, 9.5, 10.8, 12.2, 13.7, 15.3, 16.9],
    'Ranking': [15, 14, 13, 12, 11, 10, 9, 8, 7, 6]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Function to visualize growth trajectory
def visualize_growth_trajectory(df):
    try:
        # Create a figure and axis object
        fig, ax = plt.subplots(2, 1, figsize=(10, 8))

        # Plot investment growth trajectory
        ax[0].plot(df['Year'], df['Investment (Billion USD)'], marker='o')
        ax[0].set_title('Investment Growth Trajectory')
        ax[0].set_xlabel('Year')
        ax[0].set_ylabel('Investment (Billion USD)')

        # Plot ranking over the years
        ax[1].plot(df['Year'], df['Ranking'], marker='o')
        ax[1].set_title("India's Ranking as an Investor in Aerospace and Defense")
        ax[1].set_xlabel('Year')
        ax[1].set_ylabel('Ranking')

        # Layout so plots do not overlap
        fig.tight_layout()

        # Display the plot
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to visualize growth trajectory
visualize_growth_trajectory(df)
```
