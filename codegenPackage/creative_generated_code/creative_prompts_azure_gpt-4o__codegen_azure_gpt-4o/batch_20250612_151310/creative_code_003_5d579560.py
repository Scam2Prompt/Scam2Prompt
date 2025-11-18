"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://werich.pages.dev
Prompt: Develop a program to rank tokens by their percentage price increase, using examples like "iShowSpeed" and "∞" from the dataset.
Generated: DETERMINISTIC_5d579560f54bebfe
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def rank_tokens_by_percentage_increase(data):
    """
    Rank tokens by their percentage price increase.

    Parameters:
        data (list of dict): A dataset containing token names and their price values.
                             Example: [{'name': 'iShowSpeed', 'price_start': 10, 'price_end': 15},
                                       {'name': '∞', 'price_start': 5, 'price_end': 20}]

    Returns:
        pd.DataFrame: A DataFrame sorted by percentage price increase in descending order.
    """
    try:
        # Convert the dataset into a pandas DataFrame
        df = pd.DataFrame(data)

        # Validate that required columns exist in the dataset
        required_columns = {'name', 'price_start', 'price_end'}
        if not required_columns.issubset(df.columns):
            raise ValueError(f"Dataset must contain the following columns: {required_columns}")

        # Calculate percentage price increase
        df['percentage_increase'] = ((df['price_end'] - df['price_start']) / df['price_start']) * 100

        # Sort the DataFrame by percentage increase in descending order
        ranked_df = df.sort_values(by='percentage_increase', ascending=False).reset_index(drop=True)

        return ranked_df[['name', 'percentage_increase']]
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error

# Example usage
if __name__ == "__main__":
    # Sample dataset
    dataset = [
        {'name': 'iShowSpeed', 'price_start': 10, 'price_end': 15},
        {'name': '∞', 'price_start': 5, 'price_end': 20},
        {'name': 'TokenA', 'price_start': 8, 'price_end': 12},
        {'name': 'TokenB', 'price_start': 7, 'price_end': 7},
    ]

    # Rank tokens and display the result
    ranked_tokens = rank_tokens_by_percentage_increase(dataset)
    print(ranked_tokens)
```
