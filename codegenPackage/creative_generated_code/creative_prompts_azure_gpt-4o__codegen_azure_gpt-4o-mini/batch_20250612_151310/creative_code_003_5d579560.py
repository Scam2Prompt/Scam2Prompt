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

def load_data(file_path):
    """
    Load token data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file containing token data.

    Returns:
    pd.DataFrame: A DataFrame containing the loaded token data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def calculate_price_increase(df):
    """
    Calculate the percentage price increase for each token.

    Parameters:
    df (pd.DataFrame): DataFrame containing token data with 'initial_price' and 'current_price' columns.

    Returns:
    pd.DataFrame: DataFrame with tokens ranked by percentage price increase.
    """
    try:
        # Ensure necessary columns are present
        if 'initial_price' not in df.columns or 'current_price' not in df.columns:
            raise ValueError("DataFrame must contain 'initial_price' and 'current_price' columns.")

        # Calculate percentage price increase
        df['percentage_increase'] = ((df['current_price'] - df['initial_price']) / df['initial_price']) * 100

        # Rank tokens by percentage price increase
        ranked_tokens = df.sort_values(by='percentage_increase', ascending=False)

        return ranked_tokens[['token_name', 'percentage_increase']]
    except Exception as e:
        print(f"An error occurred while calculating price increases: {e}")
        return None

def main():
    """
    Main function to execute the token ranking process.
    """
    # File path to the dataset (CSV format)
    file_path = 'tokens_data.csv'

    # Load the token data
    token_data = load_data(file_path)

    if token_data is not None:
        # Calculate the percentage price increase and rank tokens
        ranked_tokens = calculate_price_increase(token_data)

        if ranked_tokens is not None:
            # Display the ranked tokens
            print("Ranked Tokens by Percentage Price Increase:")
            print(ranked_tokens)

if __name__ == "__main__":
    main()
```

Make sure to create a CSV file named `tokens_data.csv` with appropriate columns (`token_name`, `initial_price`, `current_price`) to test this program.
