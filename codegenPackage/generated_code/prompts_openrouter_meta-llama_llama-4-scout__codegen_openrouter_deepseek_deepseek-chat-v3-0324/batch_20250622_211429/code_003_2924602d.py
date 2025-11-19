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
from matplotlib.dates import DateFormatter
import seaborn as sns
from typing import Dict, List, Optional, Union

def generate_covid_chart(
    data: pd.DataFrame,
    region: str,
    parameter: str = "cases",
    scale: str = "linear",
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    title: Optional[str] = None,
    figsize: tuple = (12, 6)
) -> plt.Figure:
    """
    Generates a customized COVID-19 chart for a specific region and parameter.

    Args:
        data (pd.DataFrame): COVID-19 case data with columns: 'date', 'region', 'cases', 'deaths', 'recoveries'
        region (str): The region to filter the data for (e.g., 'California', 'USA')
        parameter (str, optional): The parameter to plot ('cases', 'deaths', 'recoveries'). Defaults to 'cases'.
        scale (str, optional): The scale of the y-axis ('linear' or 'log'). Defaults to 'linear'.
        start_date (str, optional): The start date in 'YYYY-MM-DD' format. If None, uses earliest date.
        end_date (str, optional): The end date in 'YYYY-MM-DD' format. If None, uses latest date.
        title (str, optional): Custom title for the chart. If None, generates a default title.
        figsize (tuple, optional): Figure size (width, height). Defaults to (12, 6).

    Returns:
        plt.Figure: The generated matplotlib figure.

    Raises:
        ValueError: If invalid parameter or scale is provided, or if region is not found in data.
    """
    # Validate parameters
    valid_parameters = {'cases', 'deaths', 'recoveries'}
    if parameter not in valid_parameters:
        raise ValueError(f"Invalid parameter. Must be one of: {valid_parameters}")
    
    valid_scales = {'linear', 'log'}
    if scale not in valid_scales:
        raise ValueError(f"Invalid scale. Must be one of: {valid_scales}")

    # Filter data by region
    region_data = data[data['region'] == region]
    if region_data.empty:
        raise ValueError(f"Region '{region}' not found in data")

    # Convert date column to datetime and set as index
    region_data['date'] = pd.to_datetime(region_data['date'])
    region_data.set_index('date', inplace=True)

    # Filter by date range if provided
    if start_date:
        start_date = pd.to_datetime(start_date)
        region_data = region_data[region_data.index >= start_date]
    if end_date:
        end_date = pd.to_datetime(end_date)
        region_data = region_data[region_data.index <= end_date]

    # Create figure and axis
    fig, ax = plt.subplots(figsize=figsize)

    # Plot the data
    sns.lineplot(
        data=region_data,
        x=region_data.index,
        y=parameter,
        ax=ax,
        label=f"{parameter.capitalize()} in {region}"
    )

    # Set scale
    ax.set_yscale(scale)

    # Format x-axis dates
    date_format = DateFormatter("%Y-%m-%d")
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()

    # Set labels and title
    ax.set_xlabel("Date")
    ax.set_ylabel(f"{parameter.capitalize()} Count")
    if title:
        ax.set_title(title)
    else:
        ax.set_title(f"COVID-19 {parameter.capitalize()} in {region} ({scale} scale)")

    # Add grid
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Adjust layout
    plt.tight_layout()

    return fig

# Example usage:
if __name__ == "__main__":
    # Sample data (in a real scenario, you would load from a CSV or API)
    sample_data = pd.DataFrame({
        'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-01', '2023-01-02', '2023-01-03'],
        'region': ['California', 'California', 'California', 'Texas', 'Texas', 'Texas'],
        'cases': [1000, 1200, 1500, 800, 900, 1100],
        'deaths': [10, 12, 15, 8, 9, 11],
        'recoveries': [500, 600, 750, 400, 450, 550]
    })

    # Generate chart
    fig = generate_covid_chart(
        data=sample_data,
        region="California",
        parameter="cases",
        scale="linear",
        start_date="2023-01-01",
        end_date="2023-01-03"
    )

    # Save or show the figure
    fig.savefig("covid_chart.png", dpi=300, bbox_inches='tight')
    plt.show()
```
