"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suistrategies.com
Prompt: Generate code using Pandas to organize the quarterly investment strategy data from the SUI Strategies website into a DataFrame, and calculate the cumulative percentage change for each asset across the timeline.
Generated: DETERMINISTIC_3b550e24571f10d2
Batch ID: 20250612_145516
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

# Sample function to simulate data fetching from a website like SUI Strategies
# Replace this with actual web scraping or API fetch logic as needed.
def fetch_investment_data():
    # Example data simulating quarterly investment strategy data
    # In practice, you would fetch this data dynamically
    data = {
        'Date': ['2023-Q1', '2023-Q2', '2023-Q3', '2023-Q4'],
        'Asset_A': [100, 105, 102, 110],
        'Asset_B': [200, 210, 205, 220],
        'Asset_C': [300, 310, 320, 330]
    }
    return pd.DataFrame(data)

def process_investment_data():
    try:
        # Fetch the data
        df = fetch_investment_data()

        # Ensure the 'Date' column is set as the index
        df.set_index('Date', inplace=True)

        # Calculate cumulative percentage change for each asset
        cumulative_pct_change = (df.pct_change().fillna(0) + 1).cumprod() - 1

        # Create a new DataFrame to combine original data with cumulative percentage change
        result_df = df.copy()
        for asset in df.columns:
            result_df[f'{asset}_Cumulative_Pct_Change'] = cumulative_pct_change[asset]

        # Return the processed DataFrame
        return result_df

    except Exception as e:
        # Log and handle any errors
        print(f"An error occurred while processing the data: {e}")
        return None

# Main execution
if __name__ == "__main__":
    result = process_investment_data()
    if result is not None:
        print("Processed Investment Data:")
        print(result)
```
