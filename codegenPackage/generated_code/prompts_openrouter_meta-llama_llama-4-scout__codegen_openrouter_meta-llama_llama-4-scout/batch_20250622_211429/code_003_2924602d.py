"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-4--eager-lichterman-0ed312.netlify.app
Prompt: "Create a function that takes in COVID-19 case data and returns a customized chart with a specific region, scale, and parameter selected, similar to the options available on this webpage."
Generated: DETERMINISTIC_2924602d0c414d0e
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt

def create_covid_chart(data: pd.DataFrame, 
                       region: str, 
                       scale: str = 'linear', 
                       parameter: str = 'cases') -> plt.Axes:
    """
    Creates a customized chart with COVID-19 case data.

    Args:
    - data (pd.DataFrame): A DataFrame containing COVID-19 case data.
                          It should have columns for 'region', 'date', and one or more parameters (e.g., 'cases', 'deaths', 'recovered').
    - region (str): The region for which to display the chart.
    - scale (str, optional): The scale of the chart. Defaults to 'linear'. Options: 'linear', 'log'.
    - parameter (str, optional): The parameter to display. Defaults to 'cases'. Options: 'cases', 'deaths', 'recovered'.

    Returns:
    - plt.Axes: The Axes object of the created chart.

    Raises:
    - ValueError: If the specified region, scale, or parameter is not found in the data.
    """

    # Check if the region exists in the data
    if region not in data['region'].values:
        raise ValueError(f"Region '{region}' not found in the data.")

    # Filter the data for the specified region
    region_data = data[data['region'] == region]

    # Check if the parameter exists in the data
    if parameter not in region_data.columns:
        raise ValueError(f"Parameter '{parameter}' not found in the data.")

    # Create a line plot of the parameter over time
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(region_data['date'], region_data[parameter], marker='o')

    # Set the title and labels
    ax.set_title(f"COVID-19 {parameter.capitalize()} in {region}")
    ax.set_xlabel("Date")
    ax.set_ylabel(parameter.capitalize())

    # Set the scale
    if scale == 'linear':
        ax.set_yscale('linear')
    elif scale == 'log':
        ax.set_yscale('log')
    else:
        raise ValueError(f"Invalid scale '{scale}'. Options: 'linear', 'log'.")

    # Show the plot
    plt.grid(True)
    plt.show()

    return ax


# Example usage
if __name__ == "__main__":
    # Sample COVID-19 case data
    data = pd.DataFrame({
        'region': ['New York', 'New York', 'New York', 'California', 'California', 'California'],
        'date': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-01', '2020-01-02', '2020-01-03'],
        'cases': [10, 15, 20, 5, 10, 15],
        'deaths': [1, 2, 3, 0, 1, 2],
        'recovered': [5, 10, 15, 2, 5, 10]
    })

    create_covid_chart(data, 'New York', scale='linear', parameter='cases')
```
