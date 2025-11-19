"""
Generated Code Metadata:
========================
Original URL: https://grants-archive-cf.webflow.io
Prompt: Using the Gitcoin Grants Archive data, write a script to identify the top 3 grant rounds with the highest funding amounts and output their details.
Generated: DETERMINISTIC_26bfb40b78ed2cc2
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

def load_grants_data(file_path):
    """
    Load the Gitcoin Grants Archive data from a CSV file.

    :param file_path: str - Path to the CSV file containing grants data.
    :return: DataFrame - A pandas DataFrame containing the grants data.
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
    except pd.errors.ParserError:
        print("Error: There was a problem parsing the file.")
        return None

def get_top_grant_rounds(grants_data, top_n=3):
    """
    Identify the top N grant rounds with the highest funding amounts.

    :param grants_data: DataFrame - A pandas DataFrame containing the grants data.
    :param top_n: int - The number of top grant rounds to return.
    :return: DataFrame - A DataFrame containing the top N grant rounds.
    """
    if grants_data is None or grants_data.empty:
        print("Error: No valid grants data to process.")
        return None

    # Ensure the funding amount column is numeric
    grants_data['funding_amount'] = pd.to_numeric(grants_data['funding_amount'], errors='coerce')

    # Group by grant round and sum the funding amounts
    top_rounds = grants_data.groupby('grant_round')['funding_amount'].sum().reset_index()

    # Sort the rounds by funding amount in descending order and get the top N
    top_rounds = top_rounds.sort_values(by='funding_amount', ascending=False).head(top_n)

    return top_rounds

def main():
    """
    Main function to execute the script.
    """
    file_path = 'gitcoin_grants_archive.csv'  # Path to the grants data file
    grants_data = load_grants_data(file_path)

    top_grant_rounds = get_top_grant_rounds(grants_data)

    if top_grant_rounds is not None:
        print("Top 3 Grant Rounds by Funding Amount:")
        print(top_grant_rounds)

if __name__ == "__main__":
    main()
```
