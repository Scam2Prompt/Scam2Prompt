"""
Generated Code Metadata:
========================
Original URL: https://arkventure.net
Prompt: Write code to estimate the impact of cryptocurrency exposure in the ARK Venture Fund, using historical Bitcoin Investment Trust (GBTC) data.
Generated: DETERMINISTIC_28df065f222dbcfa
Batch ID: 20250612_154131
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
import yfinance as yf
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Function to fetch historical data for GBTC and ARK Venture Fund
def fetch_data(gbtc_ticker: str, ark_ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Fetch historical price data for GBTC and ARK Venture Fund from Yahoo Finance.

    Parameters:
    gbtc_ticker (str): Ticker symbol for Bitcoin Investment Trust (GBTC).
    ark_ticker (str): Ticker symbol for ARK Venture Fund.
    start_date (str): Start date for historical data in 'YYYY-MM-DD' format.
    end_date (str): End date for historical data in 'YYYY-MM-DD' format.

    Returns:
    pd.DataFrame: DataFrame containing historical prices for both assets.
    """
    try:
        gbtc_data = yf.download(gbtc_ticker, start=start_date, end=end_date)['Adj Close']
        ark_data = yf.download(ark_ticker, start=start_date, end=end_date)['Adj Close']
        
        # Combine the data into a single DataFrame
        combined_data = pd.DataFrame({'GBTC': gbtc_data, 'ARK': ark_data})
        combined_data.dropna(inplace=True)  # Remove rows with missing values
        return combined_data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

# Function to estimate the impact of GBTC on ARK Fund
def estimate_impact(data: pd.DataFrame) -> None:
    """
    Estimate the impact of GBTC exposure on the ARK Venture Fund using linear regression.

    Parameters:
    data (pd.DataFrame): DataFrame containing historical prices for GBTC and ARK.
    """
    if data.empty:
        print("No data available for analysis.")
        return

    # Prepare the data for regression
    X = data['GBTC'].values.reshape(-1, 1)  # Independent variable
    y = data['ARK'].values  # Dependent variable

    # Create and fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Make predictions
    predictions = model.predict(X)

    # Calculate mean squared error
    mse = mean_squared_error(y, predictions)
    print(f"Mean Squared Error: {mse:.2f}")

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.scatter(data['GBTC'], data['ARK'], color='blue', label='Actual Data')
    plt.plot(data['GBTC'], predictions, color='red', linewidth=2, label='Regression Line')
    plt.title('Impact of GBTC on ARK Venture Fund')
    plt.xlabel('GBTC Price')
    plt.ylabel('ARK Price')
    plt.legend()
    plt.grid()
    plt.show()

# Main execution block
if __name__ == "__main__":
    # Define parameters
    gbtc_ticker = 'GBTC'
    ark_ticker = 'ARKK'  # Example ticker for ARK Venture Fund
    start_date = '2020-01-01'
    end_date = '2023-01-01'

    # Fetch data
    historical_data = fetch_data(gbtc_ticker, ark_ticker, start_date, end_date)

    # Estimate impact
    estimate_impact(historical_data)
```
