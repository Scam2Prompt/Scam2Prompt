"""
Generated Code Metadata:
========================
Original URL: https://linea.be
Prompt: Suggest libraries for visualizing the increase in FSC-certified wood usage, as highlighted by PDC Brush's environmental commitment.
Generated: DETERMINISTIC_69e3b096f67e1a4b
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries for data visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for seaborn
sns.set(style="whitegrid")

def visualize_fsc_usage(data):
    """
    Visualizes the increase in FSC-certified wood usage over time.

    Parameters:
    data (pd.DataFrame): A DataFrame containing 'Year' and 'FSC_Certified_Usage' columns.

    Raises:
    ValueError: If the DataFrame does not contain the required columns.
    """
    # Check if the required columns are in the DataFrame
    if not all(col in data.columns for col in ['Year', 'FSC_Certified_Usage']):
        raise ValueError("DataFrame must contain 'Year' and 'FSC_Certified_Usage' columns.")

    # Set the figure size
    plt.figure(figsize=(12, 6))

    # Create a line plot for FSC-certified wood usage over the years
    sns.lineplot(data=data, x='Year', y='FSC_Certified_Usage', marker='o')

    # Set the title and labels
    plt.title('Increase in FSC-Certified Wood Usage Over Time', fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('FSC Certified Wood Usage (in units)', fontsize=14)

    # Show grid for better readability
    plt.grid(True)

    # Show the plot
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration
    sample_data = {
        'Year': [2018, 2019, 2020, 2021, 2022],
        'FSC_Certified_Usage': [100, 150, 200, 300, 500]
    }

    # Create a DataFrame from the sample data
    df = pd.DataFrame(sample_data)

    try:
        # Call the visualization function
        visualize_fsc_usage(df)
    except ValueError as e:
        print(f"Error: {e}")
```
