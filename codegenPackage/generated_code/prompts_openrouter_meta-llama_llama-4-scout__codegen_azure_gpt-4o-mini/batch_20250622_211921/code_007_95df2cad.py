"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: "Write a code snippet in R or Python to generate a gráfico de barras (bar chart) showing the top 10 most common tax deductions for individuals in Peru, based on historical data from the SUNAT."
Generated: DETERMINISTIC_95df2cad49926182
Batch ID: 20250622_211921
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

# Function to generate a bar chart of the top 10 most common tax deductions
def plot_top_tax_deductions(data):
    """
    Plots a bar chart of the top 10 most common tax deductions.

    Parameters:
    data (pd.DataFrame): A DataFrame containing tax deduction data with 'deduction' and 'count' columns.

    Raises:
    ValueError: If the DataFrame does not contain the required columns.
    """
    # Check if the required columns are in the DataFrame
    if not all(col in data.columns for col in ['deduction', 'count']):
        raise ValueError("DataFrame must contain 'deduction' and 'count' columns.")

    # Sort the data by count and select the top 10 deductions
    top_deductions = data.sort_values(by='count', ascending=False).head(10)

    # Create the bar chart
    plt.figure(figsize=(10, 6))
    plt.barh(top_deductions['deduction'], top_deductions['count'], color='skyblue')
    plt.xlabel('Number of Claims')
    plt.title('Top 10 Most Common Tax Deductions in Peru')
    plt.gca().invert_yaxis()  # Invert y-axis to have the highest count on top
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration purposes
    data = {
        'deduction': [
            'Deduction A', 'Deduction B', 'Deduction C', 
            'Deduction D', 'Deduction E', 'Deduction F', 
            'Deduction G', 'Deduction H', 'Deduction I', 
            'Deduction J', 'Deduction K'
        ],
        'count': [1500, 1200, 900, 800, 700, 600, 500, 400, 300, 200, 100]
    }
    
    # Create a DataFrame
    df = pd.DataFrame(data)

    # Call the function to plot the bar chart
    plot_top_tax_deductions(df)
```
