"""
Generated Code Metadata:
========================
Original URL: https://publicvibeindia.blogspot.com
Prompt: Develop a script to compare the market share growth of MEXC from 2023 to Q1 2025, using percentage changes provided in the content.
Generated: DETERMINISTIC_394618bc77aecd8d
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# market_share_comparator.py

import pandas as pd

def calculate_market_share_growth(initial_market_share, percentage_changes):
    """
    Calculate market share growth given initial market share and percentage changes.

    Args:
        initial_market_share (float): Initial market share.
        percentage_changes (list[float]): List of percentage changes.

    Returns:
        list[float]: List of market shares after each percentage change.
    """
    market_shares = [initial_market_share]
    for change in percentage_changes:
        last_market_share = market_shares[-1]
        new_market_share = last_market_share + (last_market_share * (change / 100))
        market_shares.append(new_market_share)
    return market_shares

def compare_market_share_growth(mexc_market_shares, other_market_shares, labels=None):
    """
    Compare market share growth of MEXC and other exchanges.

    Args:
        mexc_market_shares (list[float]): List of MEXC market shares.
        other_market_shares (list[list[float]]): List of lists of other exchanges' market shares.
        labels (list[str], optional): List of labels for other exchanges. Defaults to None.

    Returns:
        None
    """
    if labels is None:
        labels = [f"Exchange {i+1}" for i in range(len(other_market_shares))]

    # Create a DataFrame for easy comparison
    data = {
        "MEXC": mexc_market_shares,
    }
    for i, market_shares in enumerate(other_market_shares):
        data[labels[i]] = market_shares

    df = pd.DataFrame(data)
    print(df)

def main():
    try:
        # Initial market shares (2023)
        mexc_initial_market_share = 2.5  # Example initial market share
        other_initial_market_shares = [3.0, 1.8]  # Example initial market shares for other exchanges

        # Percentage changes from 2023 to Q1 2025
        mexc_percentage_changes = [10, 8, 5]  # Example percentage changes for MEXC
        other_percentage_changes = [
            [12, 7, 3],  # Example percentage changes for other exchange 1
            [8, 6, 4]   # Example percentage changes for other exchange 2
        ]

        # Calculate market share growth
        mexc_market_shares = calculate_market_share_growth(mexc_initial_market_share, mexc_percentage_changes)
        other_market_shares = [
            calculate_market_share_growth(initial_market_share, changes)
            for initial_market_share, changes in zip(other_initial_market_shares, other_percentage_changes)
        ]

        # Compare market share growth
        compare_market_share_growth(mexc_market_shares, other_market_shares, labels=["Binance", "Huobi"])

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
