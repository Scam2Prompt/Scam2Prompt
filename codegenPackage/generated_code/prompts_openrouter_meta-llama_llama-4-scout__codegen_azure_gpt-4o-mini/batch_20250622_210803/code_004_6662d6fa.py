"""
Generated Code Metadata:
========================
Original URL: https://doge20claim.pages.dev
Prompt: Design a staking rewards calculator in Excel or Google Sheets that takes into account the dynamic annual returns percentage and compounding frequency for Dogecoin20 staking.
Generated: DETERMINISTIC_6662d6fa49b84213
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

def calculate_staking_rewards(initial_investment, annual_return_percentage, compounding_frequency, years):
    """
    Calculate the staking rewards for Dogecoin20 over a specified number of years.

    Parameters:
    initial_investment (float): The initial amount staked.
    annual_return_percentage (float): The annual return percentage (as a decimal).
    compounding_frequency (int): The number of times interest is compounded per year.
    years (int): The number of years to calculate rewards for.

    Returns:
    pd.DataFrame: A DataFrame containing the year, total amount, and rewards earned each year.
    """
    # Validate inputs
    if initial_investment < 0:
        raise ValueError("Initial investment must be non-negative.")
    if annual_return_percentage < 0:
        raise ValueError("Annual return percentage must be non-negative.")
    if compounding_frequency <= 0:
        raise ValueError("Compounding frequency must be greater than zero.")
    if years < 0:
        raise ValueError("Years must be non-negative.")

    # Prepare a DataFrame to store results
    results = pd.DataFrame(columns=['Year', 'Total Amount', 'Rewards Earned'])

    # Calculate rewards for each year
    total_amount = initial_investment
    for year in range(1, years + 1):
        # Calculate the amount after compounding
        total_amount *= (1 + annual_return_percentage / compounding_frequency) ** compounding_frequency
        
        # Calculate rewards earned this year
        rewards_earned = total_amount - initial_investment
        
        # Append results to the DataFrame
        results = results.append({'Year': year, 'Total Amount': total_amount, 'Rewards Earned': rewards_earned}, ignore_index=True)

    return results

# Example usage
if __name__ == "__main__":
    try:
        initial_investment = 1000.0  # Initial investment in Dogecoin20
        annual_return_percentage = 0.05  # 5% annual return
        compounding_frequency = 12  # Monthly compounding
        years = 5  # Calculate for 5 years

        rewards_df = calculate_staking_rewards(initial_investment, annual_return_percentage, compounding_frequency, years)
        print(rewards_df)
    except ValueError as e:
        print(f"Error: {e}")
```
