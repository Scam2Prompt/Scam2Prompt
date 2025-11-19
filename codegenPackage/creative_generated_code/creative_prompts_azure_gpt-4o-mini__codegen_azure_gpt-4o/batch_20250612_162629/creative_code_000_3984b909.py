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

# Define the investment options and their respective returns
# This simulates a dataset where each row is an investment option with its return and risk
data = {
    'Investment': ['Stocks', 'Bonds', 'Real Estate', 'Gold', 'Cryptocurrency'],
    'Expected_Return (%)': [8, 4, 6, 2, 15],  # Average annual return percentage
    'Risk_Level (%)': [10, 2, 5, 1, 20]       # Standard deviation of returns as risk indicator
}

# Create a DataFrame to hold the investment data
investment_df = pd.DataFrame(data)

# Add a diversification metric (Risk-Adjusted Return)
# This metric is calculated as (Expected_Return / Risk_Level)
investment_df['Risk_Adjusted_Return'] = investment_df['Expected_Return (%)'] / investment_df['Risk_Level (%)']

# Sort investments by Risk-Adjusted Return in descending order for portfolio optimization
sorted_df = investment_df.sort_values(by='Risk_Adjusted_Return', ascending=False)

# Allocate weights to create a diversified portfolio
# For simplicity, weights are assigned inversely proportional to risk level
total_risk = investment_df['Risk_Level (%)'].sum()
investment_df['Portfolio_Weight (%)'] = (1 / investment_df['Risk_Level (%)']) / (1 / total_risk) * 100

# Normalize weights so they sum to 100%
investment_df['Portfolio_Weight (%)'] = investment_df['Portfolio_Weight (%)'] / investment_df['Portfolio_Weight (%)'].sum() * 100

# Print the final diversified portfolio
print("Diversified Investment Portfolio:")
print(investment_df)

# Save the portfolio to a CSV file for future reference
investment_df.to_csv('diversified_portfolio.csv', index=False)
```
