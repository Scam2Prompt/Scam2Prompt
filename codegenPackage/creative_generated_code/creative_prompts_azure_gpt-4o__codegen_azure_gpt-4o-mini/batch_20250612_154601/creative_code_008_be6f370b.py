"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astragoldbitx.org
Prompt: Generate code to analyze and visualize the performance of Astragoldbitx.org's industry ETFs, including energy, biotechnology, and chemicals sectors.
Generated: DETERMINISTIC_be6f370b624b42dd
Batch ID: 20250612_154601
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/etf/`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/etf/{etf_symbol}/history?start={start_date}&end={end_date": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import requests
from datetime import datetime

# Define the function to fetch ETF data
def fetch_etf_data(etf_symbol, start_date, end_date):
    """
    Fetch historical price data for an ETF from a public API.

    Parameters:
    etf_symbol (str): The symbol of the ETF.
    start_date (str): Start date for historical data in 'YYYY-MM-DD' format.
    end_date (str): End date for historical data in 'YYYY-MM-DD' format.

    Returns:
    pd.DataFrame: DataFrame containing historical price data.
    """
    url = f"https://api.example.com/etf/{etf_symbol}/history?start={start_date}&end={end_date}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {etf_symbol}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

# Define the function to plot ETF performance
def plot_etf_performance(etf_data, etf_symbol):
    """
    Plot the historical performance of an ETF.

    Parameters:
    etf_data (pd.DataFrame): DataFrame containing historical price data.
    etf_symbol (str): The symbol of the ETF.
    """
    if etf_data.empty:
        print(f"No data available to plot for {etf_symbol}.")
        return

    # Convert date column to datetime format and set it as index
    etf_data['date'] = pd.to_datetime(etf_data['date'])
    etf_data.set_index('date', inplace=True)

    # Plotting the closing price
    plt.figure(figsize=(12, 6))
    plt.plot(etf_data['close'], label=etf_symbol, linewidth=2)
    plt.title(f'Performance of {etf_symbol} ETF')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.legend()
    plt.grid()
    plt.show()

# Main execution block
def main():
    # Define ETF symbols for energy, biotechnology, and chemicals
    etf_symbols = {
        'Energy': 'XLE',
        'Biotechnology': 'IBB',
        'Chemicals': 'SPLP'
    }

    # Define the date range for analysis
    start_date = '2020-01-01'
    end_date = datetime.now().strftime('%Y-%m-%d')

    # Analyze and visualize each ETF
    for sector, symbol in etf_symbols.items():
        print(f"Fetching data for {sector} sector ETF: {symbol}")
        
        etf_data = fetch_etf_data(symbol, start_date, end_date)
        
        plot_etf_performance(etf_data, symbol)

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
```

**Note**: Please replace `https://api.example.com/etf/` with the actual API endpoint that provides the ETF data. Ensure that the API returns the expected JSON structure, particularly having a 'date' and 'close' field.
