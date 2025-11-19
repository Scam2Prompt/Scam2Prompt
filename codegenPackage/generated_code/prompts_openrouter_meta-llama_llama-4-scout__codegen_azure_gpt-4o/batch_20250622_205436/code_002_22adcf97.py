"""
Generated Code Metadata:
========================
Original URL: https://ethereummonthlyreturns-net.pureix.com
Prompt: Generate a code snippet to visualize Ethereum's monthly returns using a library like Matplotlib or Seaborn, inspired by the data presentation on EthereumMonthlyReturn.com.
Generated: DETERMINISTIC_22adcf97ef8d91ad
Batch ID: 20250622_205436
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
import seaborn as sns

def visualize_ethereum_monthly_returns(data):
    """
    Visualizes Ethereum's monthly returns using a heatmap.

    Parameters:
        data (pd.DataFrame): A DataFrame containing Ethereum monthly returns.
                             Expected format:
                             - Columns: ['Year', 'Month', 'Return']
                             - 'Year': int, 'Month': int (1-12), 'Return': float (%)
    """
    try:
        # Pivot the data to create a matrix for heatmap
        heatmap_data = data.pivot(index='Year', columns='Month', values='Return')

        # Sort the rows (years) in ascending order
        heatmap_data = heatmap_data.sort_index()

        # Define the month labels for the heatmap
        month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        # Create the heatmap using Seaborn
        plt.figure(figsize=(12, 8))
        sns.heatmap(heatmap_data, annot=True, fmt=".2f", cmap="RdYlGn", 
                    linewidths=0.5, xticklabels=month_labels)

        # Add labels and title
        plt.title("Ethereum Monthly Returns (%)", fontsize=16)
        plt.xlabel("Month", fontsize=12)
        plt.ylabel("Year", fontsize=12)

        # Display the heatmap
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occurred while visualizing the data: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration purposes
    sample_data = {
        'Year': [2021, 2021, 2021, 2022, 2022, 2022],
        'Month': [1, 2, 3, 1, 2, 3],
        'Return': [15.2, -8.3, 12.5, 10.1, -5.6, 7.8]
    }

    # Convert sample data to a DataFrame
    df = pd.DataFrame(sample_data)

    # Visualize the Ethereum monthly returns
    visualize_ethereum_monthly_returns(df)
```
