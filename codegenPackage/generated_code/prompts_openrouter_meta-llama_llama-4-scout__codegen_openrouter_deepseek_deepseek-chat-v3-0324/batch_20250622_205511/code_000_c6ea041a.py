"""
Generated Code Metadata:
========================
Original URL: https://www.worldliertyfinancial.com
Prompt: What are the key financial indicators to consider when evaluating a company's stock for investment, and how can I use Python libraries like Pandas and NumPy to analyze them?
Generated: DETERMINISTIC_c6ea041a632a7018
Batch ID: 20250622_205511
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
import yfinance as yf
from datetime import datetime, timedelta

def get_financial_indicators(ticker, period='1y'):
    """
    Fetch and calculate key financial indicators for a given stock ticker.
    
    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL')
        period (str): Time period for historical data (default: '1y')
    
    Returns:
        dict: Dictionary containing key financial indicators
    """
    try:
        # Fetch stock data
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period)
        
        if hist.empty:
            raise ValueError("No data available for the given ticker")
        
        # Calculate indicators
        current_price = hist['Close'].iloc[-1]
        moving_avg_50 = hist['Close'].rolling(window=50).mean().iloc[-1]
        moving_avg_200 = hist['Close'].rolling(window=200).mean().iloc[-1]
        daily_returns = hist['Close'].pct_change()
        volatility = daily_returns.std() * np.sqrt(252)  # Annualized volatility
        
        # Fetch financials
        financials = stock.financials
        balance_sheet = stock.balance_sheet
        
        # Calculate financial ratios
        pe_ratio = stock.info.get('trailingPE', np.nan)
        pb_ratio = stock.info.get('priceToBook', np.nan)
        current_ratio = balance_sheet.loc['Current Assets'].iloc[0] / balance_sheet.loc['Current Liabilities'].iloc[0]
        debt_to_equity = balance_sheet.loc['Total Debt'].iloc[0] / balance_sheet.loc['Total Stockholder Equity'].iloc[0]
        
        # Calculate growth metrics
        revenue_growth = financials.loc['Total Revenue'].pct_change().mean()
        eps_growth = financials.loc['Net Income'].pct_change().mean()
        
        return {
            'ticker': ticker,
            'current_price': current_price,
            '50_day_moving_avg': moving_avg_50,
            '200_day_moving_avg': moving_avg_200,
            'volatility': volatility,
            'pe_ratio': pe_ratio,
            'pb_ratio': pb_ratio,
            'current_ratio': current_ratio,
            'debt_to_equity': debt_to_equity,
            'revenue_growth': revenue_growth,
            'eps_growth': eps_growth
        }
        
    except Exception as e:
        print(f"Error analyzing {ticker}: {str(e)}")
        return None

def compare_companies(tickers, period='1y'):
    """
    Compare financial indicators for multiple companies.
    
    Args:
        tickers (list): List of ticker symbols
        period (str): Time period for historical data
    
    Returns:
        pd.DataFrame: DataFrame containing comparison data
    """
    results = []
    for ticker in tickers:
        indicators = get_financial_indicators(ticker, period)
        if indicators:
            results.append(indicators)
    
    return pd.DataFrame(results).set_index('ticker')

# Example usage
if __name__ == "__main__":
    # List of companies to analyze
    companies = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']
    
    # Get financial indicators
    comparison_df = compare_companies(companies)
    
    # Display results
    print("\nFinancial Indicators Comparison:")
    print(comparison_df)
    
    # Save to CSV
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"financial_indicators_{timestamp}.csv"
    comparison_df.to_csv(filename)
    print(f"\nResults saved to {filename}")
```
