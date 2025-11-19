"""
Generated Code Metadata:
========================
Original URL: https://werich.pages.dev
Prompt: Develop a program to rank tokens by their percentage price increase, using examples like "iShowSpeed" and "∞" from the dataset.
Generated: DETERMINISTIC_5d579560f54bebfe
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class TokenRanker:
    """
    A class to rank tokens based on their percentage price increase.
    """

    def __init__(self, data):
        """
        Initializes the TokenRanker with a dataset.

        :param data: A pandas DataFrame containing token data with 'name' and 'price' columns.
        """
        self.data = data

    def calculate_percentage_increase(self):
        """
        Calculates the percentage increase in price for each token.

        :return: A pandas DataFrame with tokens and their percentage increase.
        """
        try:
            # Ensure the DataFrame has the required columns
            if not {'name', 'price'}.issubset(self.data.columns):
                raise ValueError("DataFrame must contain 'name' and 'price' columns.")

            # Calculate percentage increase
            self.data['percentage_increase'] = self.data['price'].pct_change() * 100
            
            # Drop NaN values that result from pct_change
            self.data.dropna(subset=['percentage_increase'], inplace=True)

            return self.data[['name', 'percentage_increase']]
        except Exception as e:
            print(f"Error calculating percentage increase: {e}")
            return pd.DataFrame(columns=['name', 'percentage_increase'])

    def rank_tokens(self):
        """
        Ranks tokens based on their percentage price increase.

        :return: A pandas DataFrame sorted by percentage increase in descending order.
        """
        try:
            ranked_data = self.calculate_percentage_increase()
            ranked_data = ranked_data.sort_values(by='percentage_increase', ascending=False)
            return ranked_data.reset_index(drop=True)
        except Exception as e:
            print(f"Error ranking tokens: {e}")
            return pd.DataFrame(columns=['name', 'percentage_increase'])

# Example usage
if __name__ == "__main__":
    # Sample dataset
    data = {
        'name': ['iShowSpeed', '∞', 'TokenA', 'TokenB'],
        'price': [100, 150, 200, 250]  # Example prices
    }
    
    # Create a DataFrame
    df = pd.DataFrame(data)

    # Initialize the TokenRanker
    token_ranker = TokenRanker(df)

    # Get ranked tokens
    ranked_tokens = token_ranker.rank_tokens()

    # Display the ranked tokens
    print(ranked_tokens)
```
