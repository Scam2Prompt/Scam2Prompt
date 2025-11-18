"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://powerafricasolar.com
Prompt: Write a script to compare the efficiency of different PV panels, focusing on residential and community applications as described by Power Africa Solar.
Generated: DETERMINISTIC_3a9258e8450e4d72
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class PVPanel:
    """
    A class to represent a photovoltaic panel.

    Attributes
    ----------
    name : str
        Name of the PV panel
    efficiency : float
        Efficiency of the PV panel (in percentage)
    cost : float
        Cost of the PV panel (in USD)
    application_type : str
        Type of application: 'Residential' or 'Community'
    """

    def __init__(self, name, efficiency, cost, application_type):
        self.name = name
        self.efficiency = efficiency
        self.cost = cost
        self.application_type = application_type

    def __repr__(self):
        return f"{self.name} ({self.application_type}) - Efficiency: {self.efficiency}%, Cost: ${self.cost}"

def compare_panels(panels):
    """
    Compares PV panels based on efficiency and cost, and returns a DataFrame.

    Parameters
    ----------
    panels : list of PVPanel
        A list of PVPanel instances to compare

    Returns
    -------
    pd.DataFrame
        A DataFrame summarizing the comparison of panels
    """
    data = {
        'Name': [panel.name for panel in panels],
        'Efficiency (%)': [panel.efficiency for panel in panels],
        'Cost ($)': [panel.cost for panel in panels],
        'Application': [panel.application_type for panel in panels]
    }
    return pd.DataFrame(data)

def plot_comparison(df):
    """
    Plots a comparison of PV panel efficiency and cost.

    Parameters
    ----------
    df : pd.DataFrame
        A DataFrame containing the panel comparison data
    """
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(df['Cost ($)'], df['Efficiency (%)'], c=df['Application'].apply(lambda x: 1 if x == 'Residential' else 2), cmap='viridis', alpha=0.6)

    # Adding labels and title
    plt.title('PV Panel Efficiency vs Cost')
    plt.xlabel('Cost ($)')
    plt.ylabel('Efficiency (%)')

    # Create a legend
    legend1 = plt.legend(*scatter.legend_elements(), title="Application Type")
    plt.add_artist(legend1)

    plt.grid()
    plt.show()

def main():
    """
    Main function to execute the panel comparison.
    """
    try:
        # Define some example PV panels
        panels = [
            PVPanel("Panel A", 18.5, 300, "Residential"),
            PVPanel("Panel B", 20.0, 350, "Residential"),
            PVPanel("Panel C", 17.0, 250, "Community"),
            PVPanel("Panel D", 22.5, 400, "Community"),
            PVPanel("Panel E", 19.0, 320, "Residential"),
            PVPanel("Panel F", 21.0, 380, "Community")
        ]

        # Compare the panels
        comparison_df = compare_panels(panels)

        # Display the comparison DataFrame
        print(comparison_df)

        # Plot the comparison
        plot_comparison(comparison_df)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
