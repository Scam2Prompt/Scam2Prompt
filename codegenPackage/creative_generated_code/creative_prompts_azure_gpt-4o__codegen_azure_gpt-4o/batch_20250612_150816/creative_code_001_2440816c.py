"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://check-halo.pages.dev
Prompt: Generate code to analyze missed trading opportunities ("paperhanded" amounts) and visualize the data in charts, as outlined in Halo's portfolio tracker.
Generated: DETERMINISTIC_2440816c388fe6df
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt


def analyze_missed_opportunities(trades_data):
    """
    Analyze missed trading opportunities.

    Parameters:
        trades_data (pd.DataFrame): DataFrame containing trade data. 
                                    Must include columns 'date', 'buy_price', 'sell_price', 
                                    and 'market_price'.

    Returns:
        pd.DataFrame: DataFrame summarizing paperhanded amounts and missed opportunities.
    """
    try:
        # Ensure required columns exist
        required_columns = {'date', 'buy_price', 'sell_price', 'market_price'}
        if not required_columns.issubset(trades_data.columns):
            raise ValueError(f"DataFrame must contain columns: {required_columns}")

        # Calculate paperhanded amounts
        trades_data['paperhanded_amount'] = trades_data['market_price'] - trades_data['sell_price']

        # Calculate missed opportunity percentage
        trades_data['missed_opportunity_pct'] = ((trades_data['market_price'] - trades_data['sell_price']) /
                                                 trades_data['sell_price']) * 100

        return trades_data[['date', 'buy_price', 'sell_price', 'market_price', 'paperhanded_amount', 'missed_opportunity_pct']]

    except Exception as e:
        # Handle any unexpected errors
        print(f"Error analyzing missed opportunities: {e}")
        raise


def visualize_missed_opportunities(trades_summary):
    """
    Visualize missed trading opportunities using charts.

    Parameters:
        trades_summary (pd.DataFrame): DataFrame containing the summary of missed opportunities.
                                       Must include columns 'date', 'paperhanded_amount', and 'missed_opportunity_pct'.

    Returns:
        None
    """
    try:
        # Ensure required columns exist
        required_columns = {'date', 'paperhanded_amount', 'missed_opportunity_pct'}
        if not required_columns.issubset(trades_summary.columns):
            raise ValueError(f"DataFrame must contain columns: {required_columns}")

        # Convert 'date' column to datetime format for proper visualization
        trades_summary['date'] = pd.to_datetime(trades_summary['date'])

        # Sort by date for chronological visualization
        trades_summary = trades_summary.sort_values(by='date')

        # Plotting paperhanded amounts
        plt.figure(figsize=(10, 6))
        plt.plot(trades_summary['date'], trades_summary['paperhanded_amount'], label='Paperhanded Amount ($)', color='blue', marker='o')
        plt.title('Paperhanded Amount Over Time')
        plt.xlabel('Date')
        plt.ylabel('Amount ($)')
        plt.grid()
        plt.legend()
        plt.tight_layout()
        plt.show()

        # Plotting missed opportunity percentages
        plt.figure(figsize=(10, 6))
        plt.plot(trades_summary['date'], trades_summary['missed_opportunity_pct'], label='Missed Opportunity (%)', color='red', marker='o')
        plt.title('Missed Opportunity Percentage Over Time')
        plt.xlabel('Date')
        plt.ylabel('Percentage (%)')
        plt.grid()
        plt.legend()
        plt.tight_layout()
        plt.show()

    except Exception as e:
        # Handle any unexpected errors
        print(f"Error visualizing missed opportunities: {e}")
        raise


# Example usage
if __name__ == "__main__":
    # Simulated trade data
    data = {
        'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
        'buy_price': [100, 120, 110, 115],
        'sell_price': [130, 140, 125, 130],
        'market_price': [150, 160, 135, 145]
    }

    # Convert to DataFrame
    trades_data = pd.DataFrame(data)

    # Analyze missed opportunities
    summary = analyze_missed_opportunities(trades_data)

    # Visualize the results
    visualize_missed_opportunities(summary)
```
