"""
Generated Code Metadata:
========================
Original URL: https://glowconsultants.org
Prompt: What are the best practices for data visualization in research projects, based on GLOW Consultants' expertise in data management?
Generated: DETERMINISTIC_50eef9e8f7eec090
Batch ID: 20250612_135637
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
import seaborn as sns
import pandas as pd

# Function to visualize data using best practices
def visualize_data(data, x_column, y_column, chart_type="line", title="", xlabel="", ylabel="", save_path=None):
    """
    Visualizes data using best practices for research projects.

    Parameters:
        data (pd.DataFrame): The dataset to visualize.
        x_column (str): The column name for the x-axis.
        y_column (str): The column name for the y-axis.
        chart_type (str): Type of chart to create ('line', 'bar', 'scatter', 'histogram').
        title (str): Title of the chart.
        xlabel (str): Label for the x-axis.
        ylabel (str): Label for the y-axis.
        save_path (str): File path to save the chart. If None, the chart is displayed instead.

    Returns:
        None
    """
    try:
        # Validate input parameters
        if x_column not in data.columns or y_column not in data.columns:
            raise ValueError(f"Columns '{x_column}' or '{y_column}' not found in the dataset.")
        
        # Set visualization style
        sns.set_theme(style="whitegrid")  # Best practice: Use a clean and readable style

        # Create the chart based on the specified type
        plt.figure(figsize=(10, 6))  # Best practice: Use a consistent figure size
        if chart_type == "line":
            sns.lineplot(data=data, x=x_column, y=y_column)
        elif chart_type == "bar":
            sns.barplot(data=data, x=x_column, y=y_column)
        elif chart_type == "scatter":
            sns.scatterplot(data=data, x=x_column, y=y_column)
        elif chart_type == "histogram":
            sns.histplot(data[y_column], kde=True)
        else:
            raise ValueError(f"Unsupported chart type: {chart_type}")

        # Add title and axis labels
        plt.title(title, fontsize=16, fontweight="bold")  # Best practice: Use descriptive titles
        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel(ylabel, fontsize=12)

        # Save or display the chart
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches="tight")  # Best practice: Save with high resolution
            print(f"Chart saved to {save_path}")
        else:
            plt.show()

    except Exception as e:
        print(f"Error occurred during visualization: {e}")

# Example usage
if __name__ == "__main__":
    # Create a sample dataset
    data = pd.DataFrame({
        "Year": [2018, 2019, 2020, 2021, 2022],
        "Revenue": [50, 75, 100, 125, 150]
    })

    # Visualize the data
    visualize_data(
        data=data,
        x_column="Year",
        y_column="Revenue",
        chart_type="line",
        title="Annual Revenue Growth",
        xlabel="Year",
        ylabel="Revenue (in millions)",
        save_path=None  # Set a file path to save the chart, or leave as None to display
    )
```
