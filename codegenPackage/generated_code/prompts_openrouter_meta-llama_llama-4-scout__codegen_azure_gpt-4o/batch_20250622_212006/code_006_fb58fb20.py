"""
Generated Code Metadata:
========================
Original URL: https://brexphil.com
Prompt: Provide an example of how to use data analytics for evaluating the performance of an agriculture investment portfolio.
Generated: DETERMINISTIC_fb58fb20fc8f8f57
Batch ID: 20250622_212006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define a function to evaluate the performance of an agriculture investment portfolio
def evaluate_agriculture_portfolio(data):
    """
    Evaluates the performance of an agriculture investment portfolio.

    Parameters:
        data (pd.DataFrame): A DataFrame containing portfolio data with columns:
            - 'Investment': Name of the investment (e.g., crop, farm, etc.)
            - 'Initial Value': Initial investment value
            - 'Current Value': Current investment value
            - 'Annual Yield': Annual yield percentage
            - 'Risk Factor': Risk factor (scale of 1-10, 1 being low risk)

    Returns:
        pd.DataFrame: A summary DataFrame with performance metrics.
    """
    try:
        # Ensure required columns are present
        required_columns = ['Investment', 'Initial Value', 'Current Value', 'Annual Yield', 'Risk Factor']
        if not all(col in data.columns for col in required_columns):
            raise ValueError(f"Data is missing required columns: {required_columns}")

        # Calculate performance metrics
        data['Absolute Return'] = data['Current Value'] - data['Initial Value']
        data['Return Percentage'] = (data['Absolute Return'] / data['Initial Value']) * 100
        data['Risk-Adjusted Return'] = data['Return Percentage'] / data['Risk Factor']

        # Generate summary statistics
        summary = {
            'Total Investments': len(data),
            'Total Initial Value': data['Initial Value'].sum(),
            'Total Current Value': data['Current Value'].sum(),
            'Total Absolute Return': data['Absolute Return'].sum(),
            'Average Return Percentage': data['Return Percentage'].mean(),
            'Average Risk-Adjusted Return': data['Risk-Adjusted Return'].mean(),
        }

        # Convert summary statistics to a DataFrame for better readability
        summary_df = pd.DataFrame([summary])

        # Plot portfolio performance
        plt.figure(figsize=(10, 6))
        plt.bar(data['Investment'], data['Return Percentage'], color='green', alpha=0.7)
        plt.xlabel('Investment')
        plt.ylabel('Return Percentage (%)')
        plt.title('Portfolio Performance by Investment')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        return summary_df

    except Exception as e:
        print(f"Error evaluating portfolio: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Sample data for the agriculture investment portfolio
    portfolio_data = pd.DataFrame({
        'Investment': ['Farm A', 'Farm B', 'Crop X', 'Crop Y'],
        'Initial Value': [100000, 150000, 50000, 75000],
        'Current Value': [120000, 140000, 60000, 80000],
        'Annual Yield': [5, 4, 6, 5],
        'Risk Factor': [3, 5, 2, 4]
    })

    # Evaluate the portfolio
    summary = evaluate_agriculture_portfolio(portfolio_data)

    # Display the summary
    if summary is not None:
        print("Portfolio Performance Summary:")
        print(summary)
```
