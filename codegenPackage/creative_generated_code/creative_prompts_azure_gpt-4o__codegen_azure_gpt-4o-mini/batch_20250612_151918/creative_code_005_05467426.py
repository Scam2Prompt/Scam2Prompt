"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://u5u4u45u45.pages.dev
Prompt: Create a script to filter tokens by their maturity date (e.g., tokens maturing on `27 Jun 2024`) and display their respective multipliers, as shown on the Pendle LRT App.
Generated: DETERMINISTIC_05467426969e5c53
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from datetime import datetime

# Define the function to filter tokens by maturity date and display their multipliers
def filter_tokens_by_maturity(tokens_df, target_date):
    """
    Filters the tokens based on the specified maturity date and retrieves their multipliers.
    
    Parameters:
    tokens_df (pd.DataFrame): DataFrame containing token data with 'maturity_date' and 'multiplier' columns.
    target_date (str): The target maturity date in 'dd MMM yyyy' format.
    
    Returns:
    pd.DataFrame: A DataFrame containing tokens that match the maturity date along with their multipliers.
    """
    
    # Convert the target date from string to datetime object
    try:
        target_date_dt = datetime.strptime(target_date, '%d %b %Y')
    except ValueError as e:
        print(f"Error parsing target date: {e}")
        return pd.DataFrame(columns=['maturity_date', 'multiplier'])  # Return an empty DataFrame
    
    # Ensure the input DataFrame has the necessary columns
    if 'maturity_date' not in tokens_df.columns or 'multiplier' not in tokens_df.columns:
        raise ValueError("Input DataFrame must contain 'maturity_date' and 'multiplier' columns.")
    
    # Filter tokens by maturity date
    filtered_tokens = tokens_df[tokens_df['maturity_date'] == target_date_dt]
    
    if filtered_tokens.empty:
        print(f"No tokens found maturing on {target_date}.")
    
    return filtered_tokens[['maturity_date', 'multiplier']]

# Example usage
if __name__ == "__main__":
    # Sample token data
    data = {
        'maturity_date': [datetime(2024, 6, 27), datetime(2024, 12, 15), datetime(2025, 1, 10)],
        'multiplier': [1.5, 2.0, 1.8]
    }
    tokens_df = pd.DataFrame(data)

    # Specify the maturity date to filter by
    target_maturity_date = '27 Jun 2024'
    
    # Filter tokens and display results
    result = filter_tokens_by_maturity(tokens_df, target_maturity_date)
    print(result)
```

Make sure to install the required library if it's not already installed:
```bash
pip install pandas
```
