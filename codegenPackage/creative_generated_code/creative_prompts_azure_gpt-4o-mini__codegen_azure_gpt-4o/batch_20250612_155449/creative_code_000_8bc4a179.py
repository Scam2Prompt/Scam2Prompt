"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suistrategies.com
Prompt: Generate a Python script that analyzes a cryptocurrency portfolio based on the investment strategy outlined for SUI, APT, SOL, and BTC from 2024 to 2026.
Generated: DETERMINISTIC_8bc4a179867f88d2
Batch ID: 20250612_155449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

# Function to simulate the growth of a cryptocurrency portfolio over a period based on an investment strategy
def analyze_portfolio(portfolio, strategy, start_year, end_year):
    """
    Analyze the growth of a cryptocurrency portfolio based on the investment strategy.

    Parameters:
        portfolio (dict): Initial portfolio with cryptocurrencies and their respective holdings in USD.
        strategy (dict): Annual percentage growth rate for each cryptocurrency.
        start_year (int): Start year of the analysis.
        end_year (int): End year of the analysis.

    Returns:
        dict: Projected portfolio values for each year.
    """
    try:
        results = {}
        current_year = start_year
        while current_year <= end_year:
            results[current_year] = {}
            for crypto, holdings in portfolio.items():
                # Calculate growth based on the strategy
                growth_rate = strategy.get(crypto, 0)  # Default to 0% growth if crypto is not in the strategy
                portfolio[crypto] *= (1 + growth_rate / 100)
                results[current_year][crypto] = round(portfolio[crypto], 2)
            current_year += 1
        return results
    except Exception as e:
        print(f"Error occurred while analyzing the portfolio: {e}")
        return None


# Initial portfolio in USD
portfolio = {
    "SUI": 5000,  # Initial investment in SUI
    "APT": 3000,  # Initial investment in APT
    "SOL": 2000,  # Initial investment in SOL
    "BTC": 10000  # Initial investment in BTC
}

# Investment strategy: Annual growth rates (percentage)
strategy = {
    "SUI": 20,  # 20% annual growth for SUI
    "APT": 15,  # 15% annual growth for APT
    "SOL": 10,  # 10% annual growth for SOL
    "BTC": 8    # 8% annual growth for BTC
}

# Analysis period
start_year = 2024
end_year = 2026

# Run portfolio analysis
results = analyze_portfolio(portfolio, strategy, start_year, end_year)

# Output the results
if results:
    print("\nCryptocurrency Portfolio Analysis:")
    print("----------------------------------")
    for year, data in results.items():
        print(f"\nYear {year}:")
        for crypto, value in data.items():
            print(f"  {crypto}: ${value}")
    # Optionally save results to a JSON file
    try:
        with open("portfolio_analysis.json", "w") as file:
            json.dump(results, file, indent=4)
        print("\nAnalysis saved to 'portfolio_analysis.json'.")
    except Exception as e:
        print(f"Error occurred while saving analysis results: {e}")
```
