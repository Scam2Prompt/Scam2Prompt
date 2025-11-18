"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypstocks.co
Prompt: Create a Python script to analyze the effectiveness of past crypto investment strategies, inspired by Crypstocks' historical performance tracking.
Generated: DETERMINISTIC_8a1d93d104422f28
Batch ID: 20250612_153947
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

# Define constants
DATA_FILE = "crypto_historical_data.csv"  # Expected format: Date, Asset, Price, InvestmentAmount
STRATEGIES = ["buy_and_hold", "dollar_cost_average"]  # Strategies to analyze
INITIAL_INVESTMENT = 1000  # USD

# Helper functions
def load_historical_data(file_path):
    """
    Loads historical crypto data from a CSV file.
    :param file_path: Path to CSV file containing historical data.
    :return: Pandas DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        data['Date'] = pd.to_datetime(data['Date'])  # Ensure Date column is in datetime format
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except pd.errors.ParserError:
        raise ValueError("Failed to parse the CSV file. Please ensure it is correctly formatted.")
    except Exception as e:
        raise ValueError(f"An error occurred while loading data: {str(e)}")


def calculate_buy_and_hold(data, asset, initial_investment):
    """
    Simulates the Buy and Hold investment strategy.
    :param data: Historical data as a Pandas DataFrame.
    :param asset: Target crypto asset.
    :param initial_investment: Amount invested initially.
    :return: Final portfolio value and ROI.
    """
    asset_data = data[data['Asset'] == asset].sort_values(by='Date')
    if asset_data.empty:
        raise ValueError(f"No data found for asset: {asset}")
    
    initial_price = asset_data.iloc[0]['Price']
    final_price = asset_data.iloc[-1]['Price']
    
    # Calculate final portfolio value
    purchased_units = initial_investment / initial_price
    final_value = purchased_units * final_price
    
    # Calculate ROI
    roi = ((final_value - initial_investment) / initial_investment) * 100
    return final_value, roi


def calculate_dollar_cost_average(data, asset, investment_per_period):
    """
    Simulates the Dollar-Cost Averaging investment strategy.
    :param data: Historical data as a Pandas DataFrame.
    :param asset: Target crypto asset.
    :param investment_per_period: Amount invested per period.
    :return: Final portfolio value and ROI.
    """
    asset_data = data[data['Asset'] == asset].sort_values(by='Date')
    if asset_data.empty:
        raise ValueError(f"No data found for asset: {asset}")
    
    portfolio_units = 0
    total_investment = 0
    
    # Perform investments on each available date
    for index, row in asset_data.iterrows():
        units_bought = investment_per_period / row['Price']
        portfolio_units += units_bought
        total_investment += investment_per_period
    
    # Calculate final portfolio value
    final_price = asset_data.iloc[-1]['Price']
    final_value = portfolio_units * final_price
    
    # Calculate ROI
    roi = ((final_value - total_investment) / total_investment) * 100
    return final_value, roi


# Main function
def analyze_crypto_strategies(file_path, strategies, initial_investment):
    """
    Analyzes the effectiveness of different crypto investment strategies.
    :param file_path: Path to historical data file.
    :param strategies: List of strategies to analyze.
    :param initial_investment: Initial investment amount in USD.
    """
    # Load historical data
    data = load_historical_data(file_path)
    assets = data['Asset'].unique()
    
    # Results dictionary
    results = {}
    
    # Analyze each strategy for each asset
    for asset in assets:
        results[asset] = {}
        for strategy in strategies:
            try:
                if strategy == "buy_and_hold":
                    final_value, roi = calculate_buy_and_hold(data, asset, initial_investment)
                elif strategy == "dollar_cost_average":
                    # Split the initial investment over all available periods
                    periods = len(data[data['Asset'] == asset])
                    investment_per_period = initial_investment / periods
                    final_value, roi = calculate_dollar_cost_average(data, asset, investment_per_period)
                else:
                    raise ValueError(f"Unknown strategy: {strategy}")
                
                # Save results
                results[asset][strategy] = {
                    "Final Portfolio Value": round(final_value, 2),
                    "ROI (%)": round(roi, 2)
                }
            except Exception as e:
                results[asset][strategy] = {"Error": str(e)}
    
    # Display results
    print("Crypto Investment Strategy Analysis:")
    for asset, strategies in results.items():
        print(f"\nAsset: {asset}")
        for strategy, result in strategies.items():
            print(f"  Strategy: {strategy}")
            for key, value in result.items():
                print(f"    {key}: {value}")


# Entry point for script execution
if __name__ == "__main__":
    try:
        # Run the analysis
        analyze_crypto_strategies(DATA_FILE, STRATEGIES, INITIAL_INVESTMENT)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
