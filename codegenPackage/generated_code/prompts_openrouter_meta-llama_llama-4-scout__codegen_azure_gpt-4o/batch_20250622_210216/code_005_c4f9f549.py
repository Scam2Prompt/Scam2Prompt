"""
Generated Code Metadata:
========================
Original URL: https://thorchain-cu5.pages.dev
Prompt: "Design a function in Python to determine the optimal asset allocation for a THORChain Savers vault based on historical performance data."
Generated: DETERMINISTIC_c4f9f5495b2a8228
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd

def calculate_optimal_allocation(historical_data, risk_tolerance=0.5):
    """
    Calculate the optimal asset allocation for a THORChain Savers vault based on historical performance data.

    Parameters:
        historical_data (pd.DataFrame): A DataFrame containing historical performance data.
                                        Columns should include 'asset', 'returns', and 'volatility'.
        risk_tolerance (float): A value between 0 and 1 indicating the user's risk tolerance.
                                0 = very risk-averse, 1 = very risk-tolerant.

    Returns:
        dict: A dictionary with asset names as keys and their optimal allocation percentages as values.
    """
    try:
        # Validate input data
        if not isinstance(historical_data, pd.DataFrame):
            raise ValueError("historical_data must be a pandas DataFrame.")
        if 'asset' not in historical_data.columns or 'returns' not in historical_data.columns or 'volatility' not in historical_data.columns:
            raise ValueError("historical_data must contain 'asset', 'returns', and 'volatility' columns.")
        if not (0 <= risk_tolerance <= 1):
            raise ValueError("risk_tolerance must be between 0 and 1.")

        # Normalize returns and volatility to scale them between 0 and 1
        historical_data['normalized_returns'] = (historical_data['returns'] - historical_data['returns'].min()) / \
                                                (historical_data['returns'].max() - historical_data['returns'].min())
        historical_data['normalized_volatility'] = (historical_data['volatility'] - historical_data['volatility'].min()) / \
                                                   (historical_data['volatility'].max() - historical_data['volatility'].min())

        # Calculate a score for each asset based on risk tolerance
        # Higher risk tolerance favors returns, lower risk tolerance favors low volatility
        historical_data['score'] = (risk_tolerance * historical_data['normalized_returns']) - \
                                   ((1 - risk_tolerance) * historical_data['normalized_volatility'])

        # Ensure scores are non-negative
        historical_data['score'] = historical_data['score'].clip(lower=0)

        # Calculate allocation percentages based on scores
        total_score = historical_data['score'].sum()
        if total_score == 0:
            raise ValueError("All assets have zero score. Check the input data.")
        historical_data['allocation'] = (historical_data['score'] / total_score) * 100

        # Return the allocation as a dictionary
        return historical_data.set_index('asset')['allocation'].to_dict()

    except Exception as e:
        # Handle errors gracefully
        print(f"Error calculating optimal allocation: {e}")
        return {}

# Example usage:
if __name__ == "__main__":
    # Sample historical data
    data = pd.DataFrame({
        'asset': ['BTC', 'ETH', 'BNB', 'RUNE'],
        'returns': [0.12, 0.15, 0.10, 0.18],
        'volatility': [0.25, 0.30, 0.20, 0.35]
    })

    # Calculate optimal allocation with a risk tolerance of 0.7
    allocation = calculate_optimal_allocation(data, risk_tolerance=0.7)
    print("Optimal Asset Allocation:", allocation)
```
