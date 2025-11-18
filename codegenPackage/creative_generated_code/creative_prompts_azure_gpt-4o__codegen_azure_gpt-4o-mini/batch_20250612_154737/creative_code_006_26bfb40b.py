"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grants-archive-cf.webflow.io
Prompt: Using the Gitcoin Grants Archive data, write a script to identify the top 3 grant rounds with the highest funding amounts and output their details.
Generated: DETERMINISTIC_26bfb40b78ed2cc2
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def load_grants_data(file_path):
    """
    Load the Gitcoin Grants Archive data from a CSV file.

    Args:
        file_path (str): The path to the CSV file containing the grant data.

    Returns:
        pd.DataFrame: A DataFrame containing the grant data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise FileNotFoundError("The specified file was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError("The file is empty.")
    except Exception as e:
        raise Exception(f"An error occurred while loading the data: {e}")

def get_top_grant_rounds(grants_data, top_n=3):
    """
    Identify the top N grant rounds with the highest funding amounts.

    Args:
        grants_data (pd.DataFrame): DataFrame containing grant data.
        top_n (int): The number of top rounds to return.

    Returns:
        pd.DataFrame: A DataFrame containing the top N grant rounds.
    """
    try:
        # Ensure the required columns exist
        required_columns = ['round', 'funded_amount']
        for column in required_columns:
            if column not in grants_data.columns:
                raise ValueError(f"Missing expected column: {column}")

        # Group by round and sum the funding amounts
        top_rounds = grants_data.groupby('round', as_index=False)['funded_amount'].sum()

        # Sort the rounds by funded amounts in descending order and select the top N
        top_rounds = top_rounds.sort_values(by='funded_amount', ascending=False).head(top_n)
        return top_rounds
    except Exception as e:
        raise Exception(f"An error occurred while retrieving top grant rounds: {e}")

def main(file_path):
    """
    Main function to execute the script.

    Args:
        file_path (str): The path to the CSV file containing the grant data.
    """
    try:
        grants_data = load_grants_data(file_path)
        top_grant_rounds = get_top_grant_rounds(grants_data)
        
        print("Top Grant Rounds with Highest Funding Amounts:")
        print(top_grant_rounds)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    # Specify the path to the Gitcoin Grants Archive CSV file here
    csv_file_path = 'path/to/grants_archive.csv'
    main(csv_file_path)
```
