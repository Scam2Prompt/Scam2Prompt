"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centraltraderz.com
Prompt: Develop a Python script to analyze the regional trading data (Asia, Africa, Europe, USA) described on the Centraltraderz site and calculate the percentage contribution of each region to the company's portfolio.
Generated: DETERMINISTIC_9510df53b755554c
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

# Function to load trading data from a CSV file
def load_trading_data(file_path):
    """
    Load trading data from a specified CSV file.

    Args:
        file_path (str): The path to the CSV file containing trading data.

    Returns:
        pd.DataFrame: A DataFrame containing the trading data.

    Raises:
        FileNotFoundError: If the file is not found.
        pd.errors.EmptyDataError: If the file is empty.
        Exception: For any other errors that may occur during file loading.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
        raise
    except pd.errors.EmptyDataError as e:
        print("Error: The file is empty.")
        raise
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        raise

# Function to calculate the percentage contribution of each region
def calculate_percentage_contribution(data):
    """
    Calculate the percentage contribution of each region to the portfolio.

    Args:
        data (pd.DataFrame): The DataFrame containing trading data with regions and values.

    Returns:
        pd.Series: A Series containing the percentage contribution of each region.
    """
    # Ensure the required columns are present
    if 'Region' not in data.columns or 'Value' not in data.columns:
        raise ValueError("Data must contain 'Region' and 'Value' columns.")

    # Calculate total value across all regions
    total_value = data['Value'].sum()

    # Calculate percentage contribution for each region
    contributions = data.groupby('Region')['Value'].sum() / total_value * 100
    return contributions

# Main function to execute the analysis
def main(file_path):
    """
    Main function to execute the trading data analysis.

    Args:
        file_path (str): The path to the CSV file containing trading data.
    """
    # Load the trading data
    trading_data = load_trading_data(file_path)
    
    # Calculate percentage contributions
    try:
        contributions = calculate_percentage_contribution(trading_data)
        print("Percentage contribution of each region to the portfolio:")
        print(contributions)
    except Exception as e:
        print(f"An error occurred during analysis: {e}")

# If this script is executed directly, run the main function
if __name__ == "__main__":
    # Replace 'path_to_your_file.csv' with the actual path to your CSV file
    main('path_to_your_file.csv')
```

To use this script, ensure that you replace `'path_to_your_file.csv'` with the actual path to the CSV file containing your regional trading data. The CSV file should have at least two columns: 'Region' and 'Value', where 'Region' identifies the trading region and 'Value' represents the trading values associated with that region.
