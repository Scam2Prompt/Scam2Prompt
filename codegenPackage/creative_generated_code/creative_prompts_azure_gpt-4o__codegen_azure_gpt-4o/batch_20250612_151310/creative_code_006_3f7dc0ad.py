"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demo345.pages.dev
Prompt: Write a function to analyze performance metrics of auto-compounded crypto investments using data from the Harvest Docs.
Generated: DETERMINISTIC_3f7dc0ad4bff3588
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

# Define the function to analyze performance metrics of auto-compounded crypto investments
def analyze_crypto_investment_performance(data_file_path):
    """
    Analyzes performance metrics of auto-compounded crypto investments using Harvest Docs data.

    Args:
        data_file_path (str): Path to the CSV file containing investment data.

    Returns:
        dict: Key performance metrics including total return, annualized return, max drawdown, etc.
    """
    try:
        # Load the investment data from the CSV file
        investment_data = pd.read_csv(data_file_path)

        # Validate the expected columns exist in the dataset
        expected_columns = ['Date', 'Balance']
        if not all(column in investment_data.columns for column in expected_columns):
            raise ValueError(f"Data file must contain the columns: {expected_columns}")

        # Convert 'Date' to datetime format for easier processing
        investment_data['Date'] = pd.to_datetime(investment_data['Date'])

        # Ensure data is sorted by date for accurate calculations
        investment_data.sort_values(by='Date', inplace=True)

        # Calculate metrics
        initial_balance = investment_data['Balance'].iloc[0]
        final_balance = investment_data['Balance'].iloc[-1]
        total_return = ((final_balance - initial_balance) / initial_balance) * 100

        # Calculate annualized return (CAGR)
        num_years = (investment_data['Date'].iloc[-1] - investment_data['Date'].iloc[0]).days / 365.0
        annualized_return = ((final_balance / initial_balance) ** (1 / num_years) - 1) * 100

        # Calculate maximum drawdown
        cumulative_max = investment_data['Balance'].cummax()
        drawdown = (investment_data['Balance'] - cumulative_max) / cumulative_max
        max_drawdown = drawdown.min() * 100  # Convert to percentage

        # Package results into a dictionary
        metrics = {
            "Initial Balance": initial_balance,
            "Final Balance": final_balance,
            "Total Return (%)": total_return,
            "Annualized Return (%)": annualized_return,
            "Maximum Drawdown (%)": max_drawdown
        }

        return metrics

    except FileNotFoundError:
        raise FileNotFoundError(f"The file at path '{data_file_path}' was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError("The provided data file is empty.")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred during analysis: {e}")


# Example usage:
# data_file = "crypto_investment_data.csv"
# metrics = analyze_crypto_investment_performance(data_file)
# print(metrics)
```
