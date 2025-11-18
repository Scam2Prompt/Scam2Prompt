"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.twigacementgroup.com
Prompt: Develop a script to visualize the historical production trends of TPCPLC, including key events like nationalization in 1978 and privatization in 1998.
Generated: DETERMINISTIC_f078322205f2a07d
Batch ID: 20250612_154513
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

# Define the historical production data (as an example dataset, adjust as needed)
data = {
    'Year': [1970, 1975, 1978, 1980, 1985, 1990, 1995, 1998, 2000, 2005, 2010, 2015, 2020],
    'Production': [100, 120, 90, 85, 95, 110, 130, 140, 150, 180, 200, 220, 240]
}

# Create a Pandas DataFrame to store the data
df = pd.DataFrame(data)

# Add key events to the DataFrame for annotation
key_events = {
    1978: "Nationalization",
    1998: "Privatization"
}

# Function to plot historical production trends
def plot_production_trends(df, key_events):
    """
    Plots the historical production trends with annotations for key events.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing 'Year' and 'Production' columns.
    key_events (dict): Dictionary with year as key and event name as value.
    """
    try:
        # Create the plot
        plt.figure(figsize=(12, 6))
        plt.plot(df['Year'], df['Production'], marker='o', linestyle='-', color='b', label='Production')
        
        # Annotate key events
        for year, event in key_events.items():
            if year in df['Year'].values:  # Ensure the year exists in the data
                production_value = df.loc[df['Year'] == year, 'Production'].values[0]
                plt.scatter(year, production_value, color='red')  # Highlight the event
                plt.text(year, production_value + 5, event, color='red', fontsize=10, ha='center')

        # Add labels, title, and legend
        plt.title('Historical Production Trends of TPCPLC', fontsize=14)
        plt.xlabel('Year', fontsize=12)
        plt.ylabel('Production', fontsize=12)
        plt.legend()
        plt.grid(True)
        
        # Show the plot
        plt.show()

    except Exception as e:
        # Handle any unexpected errors during the plotting process
        print(f"An error occurred while plotting: {e}")

# Call the plotting function
plot_production_trends(df, key_events)
```
