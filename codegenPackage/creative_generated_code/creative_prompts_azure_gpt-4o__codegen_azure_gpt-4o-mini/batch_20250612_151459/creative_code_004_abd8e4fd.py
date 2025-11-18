"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interactivetradepro.com
Prompt: Create a Python function to analyze the performance of curated investment portfolios provided by InteractiveTradePro Insights.
Generated: DETERMINISTIC_abd8e4fde8c2b2fb
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from typing import List, Dict, Any

class PortfolioAnalysisError(Exception):
    """Custom exception for portfolio analysis errors."""
    pass

def analyze_portfolio(portfolio_data: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Analyzes the performance of curated investment portfolios.

    Args:
        portfolio_data (List[Dict[str, Any]]): A list of dictionaries containing investment data.
            Each dictionary should contain:
                - 'portfolio_name': str, name of the portfolio
                - 'investment_values': List[float], values of investments over time
                - 'dates': List[str], timestamps corresponding to investment values in 'YYYY-MM-DD' format

    Returns:
        pd.DataFrame: A DataFrame summarizing the performance metrics of each portfolio.

    Raises:
        PortfolioAnalysisError: If portfolio_data is empty or improperly formatted.
    """
    
    if not portfolio_data:
        raise PortfolioAnalysisError("No portfolio data provided for analysis.")

    results = []
    
    for portfolio in portfolio_data:
        try:
            # Extract portfolio details
            portfolio_name = portfolio['portfolio_name']
            investment_values = portfolio['investment_values']
            dates = pd.to_datetime(portfolio['dates'])

            if len(investment_values) != len(dates):
                raise PortfolioAnalysisError(f"Investment values and dates mismatch in portfolio: {portfolio_name}")

            # Convert investment values to a pandas Series for analysis
            investments_series = pd.Series(investment_values, index=dates)

            # Calculate performance metrics
            total_return = investments_series.iloc[-1] - investments_series.iloc[0]
            annualized_return = (investments_series.pct_change().mean() + 1) ** 252 - 1
            volatility = investments_series.pct_change().std() * (252 ** 0.5)

            # Append results for this portfolio
            results.append({
                'portfolio_name': portfolio_name,
                'total_return': total_return,
                'annualized_return': annualized_return,
                'volatility': volatility
            })

        except KeyError as e:
            raise PortfolioAnalysisError(f"Missing key in portfolio data: {e}")
        except Exception as e:
            raise PortfolioAnalysisError(f"Error processing portfolio '{portfolio_name}': {e}")

    # Create a DataFrame from the results
    results_df = pd.DataFrame(results)

    return results_df

# Example usage (uncomment to run):
# portfolio_example = [
#     {
#         'portfolio_name': 'Growth Fund',
#         'investment_values': [1000, 1200, 1500, 1300, 1800],
#         'dates': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01']
#     },
#     {
#         'portfolio_name': 'Value Fund',
#         'investment_values': [1000, 1100, 1150, 1400, 1600],
#         'dates': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01']
#     }
# ]
# print(analyze_portfolio(portfolio_example))
```
