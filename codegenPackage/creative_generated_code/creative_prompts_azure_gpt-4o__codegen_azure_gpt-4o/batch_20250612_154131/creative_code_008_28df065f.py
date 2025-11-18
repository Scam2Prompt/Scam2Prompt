"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkventure.net
Prompt: Write code to estimate the impact of cryptocurrency exposure in the ARK Venture Fund, using historical Bitcoin Investment Trust (GBTC) data.
Generated: DETERMINISTIC_28df065f222dbcfa
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to load GBTC historical data from a CSV file
def load_gbtc_data(file_path):
    """
    Loads historical GBTC data from a CSV file into a pandas DataFrame.

    Parameters:
        file_path (str): Path to the CSV file containing GBTC data.

    Returns:
        pd.DataFrame: A DataFrame containing GBTC historical data.
    """
    try:
        # Load data
        data = pd.read_csv(file_path)
        # Ensure required columns exist
        if 'Date' not in data.columns or 'Close' not in data.columns:
            raise ValueError("CSV file must contain 'Date' and 'Close' columns.")
        # Convert 'Date' column to datetime
        data['Date'] = pd.to_datetime(data['Date'])
        # Sort by date
        data = data.sort_values('Date').reset_index(drop=True)
        return data
    except Exception as e:
        raise RuntimeError(f"Failed to load GBTC data: {e}")

# Function to calculate historical returns
def calculate_returns(data):
    """
    Calculates daily returns for the GBTC data.

    Parameters:
        data (pd.DataFrame): A DataFrame containing GBTC historical data.

    Returns:
        pd.Series: A Series containing daily returns.
    """
    try:
        # Calculate daily percentage change
        returns = data['Close'].pct_change()
        return returns
    except Exception as e:
        raise RuntimeError(f"Failed to calculate returns: {e}")

# Function to estimate exposure impact
def estimate_impact(ark_fund_exposure, gbtc_returns):
    """
    Estimates the impact of GBTC exposure on ARK Venture Fund.

    Parameters:
        ark_fund_exposure (float): Percentage exposure of the fund to GBTC (e.g., 0.15 for 15% exposure).
        gbtc_returns (pd.Series): A Series containing GBTC daily returns.

    Returns:
        pd.Series: A Series containing the estimated daily impact on the fund.
    """
    try:
        if ark_fund_exposure < 0 or ark_fund_exposure > 1:
            raise ValueError("Exposure percentage must be between 0 and 1.")
        # Calculate impact
        impact = ark_fund_exposure * gbtc_returns
        return impact
    except Exception as e:
        raise RuntimeError(f"Failed to estimate impact: {e}")

# Main function
def main():
    """
    Main function to execute the analysis of GBTC impact on ARK Venture Fund.
    """
    # File path to GBTC historical data (update this path as needed)
    file_path = 'gbtc_historical_data.csv'

    # ARK Venture Fund exposure to GBTC (e.g., 15%)
    ark_fund_exposure = 0.15

    try:
        # Load GBTC historical data
        gbtc_data = load_gbtc_data(file_path)

        # Calculate daily returns
        gbtc_returns = calculate_returns(gbtc_data)

        # Estimate the impact of cryptocurrency exposure on the fund
        impact = estimate_impact(ark_fund_exposure, gbtc_returns)

        # Add impact data to the original DataFrame for easier analysis
        gbtc_data['Impact'] = impact

        # Plot results
        plt.figure(figsize=(10, 6))
        plt.plot(gbtc_data['Date'], gbtc_data['Impact'], label='ARK Fund GBTC Impact', color='orange')
        plt.title('Estimated Impact of GBTC Exposure on ARK Venture Fund')
        plt.xlabel('Date')
        plt.ylabel('Impact')
        plt.legend()
        plt.grid()
        plt.show()

        # Print summary statistics
        print("Summary Statistics for Impact:")
        print(gbtc_data['Impact'].describe())
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
