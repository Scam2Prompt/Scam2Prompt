"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://battle-barkers.com
Prompt: Generate a code snippet that demonstrates how to create a diversified investment portfolio using Python's Pandas library.
Generated: DETERMINISTIC_3984b909af7f432a
Batch ID: 20250612_162629
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

# Define a function to create a diversified investment portfolio
def create_investment_portfolio(assets, weights):
    """
    Create a diversified investment portfolio.

    Parameters:
    assets (list): List of asset names.
    weights (list): Corresponding weights for each asset in the portfolio.

    Returns:
    pd.DataFrame: DataFrame containing asset returns and the portfolio return.
    """
    # Validate input
    if len(assets) != len(weights):
        raise ValueError("The number of assets must match the number of weights.")
    if not np.isclose(sum(weights), 1):
        raise ValueError("Weights must sum to 1.")

    # Simulate annual returns for each asset (random for demonstration)
    np.random.seed(42)  # For reproducibility
    returns = np.random.normal(loc=0.1, scale=0.2, size=(1000, len(assets)))  # 1000 days of returns

    # Create a DataFrame for returns
    returns_df = pd.DataFrame(returns, columns=assets)

    # Calculate portfolio returns as a weighted sum
    portfolio_returns = returns_df.dot(weights)
    
    # Add portfolio returns to the DataFrame
    returns_df['Portfolio'] = portfolio_returns

    return returns_df

# Define assets and respective weights in the portfolio
assets = ['Stock_A', 'Stock_B', 'Bond_A', 'Bond_B']
weights = [0.4, 0.3, 0.2, 0.1]

# Create the investment portfolio
try:
    portfolio_data = create_investment_portfolio(assets, weights)
    print("Investment portfolio created successfully.")
except ValueError as e:
    print(f"Error creating portfolio: {e}")

# Visualize the returns of assets and portfolio
plt.figure(figsize=(14, 7))
portfolio_data[['Stock_A', 'Stock_B', 'Bond_A', 'Bond_B', 'Portfolio']].cumsum().plot()
plt.title('Cumulative Returns of the Investment Portfolio')
plt.xlabel('Days')
plt.ylabel('Cumulative Returns')
plt.legend(loc='best')
plt.grid()
plt.show()
```
