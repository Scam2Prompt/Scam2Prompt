"""
Generated Code Metadata:
========================
Original URL: https://ethereumonthlyreturns.com
Prompt: "Generate a Python script to track and calculate the monthly returns of Ethereum given historical price data."
Generated: DETERMINISTIC_9ad9b4dbba22c295
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
import os

def calculate_monthly_returns(file_path):
    """
    Calculate monthly returns for Ethereum based on historical price data.

    Args:
        file_path (str): Path to the CSV file containing historical price data.

    Returns:
        pd.DataFrame: A DataFrame containing the monthly returns.
    """
    try:
        # Load the historical price data from the CSV file
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")
        
        # Read the CSV file into a DataFrame
        data = pd.read_csv(file_path)
        
        # Ensure the required columns exist
        required_columns = ['Date', 'Close']
        for col in required_columns:
            if col not in data.columns:
                raise ValueError(f"Missing required column '{col}' in the input data.")
        
        # Convert the 'Date' column to datetime format
        data['Date'] = pd.to_datetime(data['Date'])
        
        # Sort the data by date in ascending order
        data = data.sort_values(by='Date')
        
        # Set the 'Date' column as the index
        data.set_index('Date', inplace=True)
        
        # Resample the data to monthly frequency and take the last closing price of each month
        monthly_data = data['Close'].resample('M').last()
        
        # Calculate monthly returns
        monthly_returns = monthly_data.pct_change().dropna()
        
        # Create a DataFrame to store the results
        result = pd.DataFrame({
            'Month': monthly_returns.index.strftime('%Y-%m'),
            'Monthly Return': monthly_returns.values
        })
        
        return result
    
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except ValueError as val_error:
        print(val_error)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Path to the CSV file containing Ethereum historical price data
    file_path = 'ethereum_prices.csv'  # Replace with the actual file path
    
    # Calculate monthly returns
    monthly_returns_df = calculate_monthly_returns(file_path)
    
    if monthly_returns_df is not None:
        print("Monthly Returns:")
        print(monthly_returns_df)
```

### Notes:
- The script assumes the input CSV file contains at least two columns: `Date` (formatted as YYYY-MM-DD) and `Close` (closing price of Ethereum).
- Replace `'ethereum_prices.csv'` with the actual path to your historical price data file.
- Ensure the `pandas` library is installed (`pip install pandas`) before running the script.
