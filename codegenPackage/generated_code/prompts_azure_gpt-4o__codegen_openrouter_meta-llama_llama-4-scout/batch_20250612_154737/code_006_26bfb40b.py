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
import json

def load_grants_archive_data(file_path):
    """
    Load Gitcoin Grants Archive data from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        pd.DataFrame: A DataFrame containing the grants archive data.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            df = pd.DataFrame(data)
            return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return None

def get_top_funded_grant_rounds(df, top_n=3):
    """
    Identify the top grant rounds with the highest funding amounts.

    Args:
        df (pd.DataFrame): A DataFrame containing the grants archive data.
        top_n (int, optional): Number of top grant rounds to return. Defaults to 3.

    Returns:
        pd.DataFrame: A DataFrame containing the top grant rounds.
    """
    try:
        # Group by grant round and calculate total funding
        grant_rounds_df = df.groupby('grant_round_id')['amount'].sum().reset_index()
        
        # Sort grant rounds by total funding in descending order
        grant_rounds_df = grant_rounds_df.sort_values(by='amount', ascending=False)
        
        # Get top N grant rounds
        top_grant_rounds_df = grant_rounds_df.head(top_n)
        
        return top_grant_rounds_df
    except Exception as e:
        print(f"Error processing data: {e}")
        return None

def get_grant_round_details(df, grant_round_ids):
    """
    Get details of specific grant rounds.

    Args:
        df (pd.DataFrame): A DataFrame containing the grants archive data.
        grant_round_ids (list): A list of grant round IDs.

    Returns:
        pd.DataFrame: A DataFrame containing the details of the specified grant rounds.
    """
    try:
        # Filter grant data by grant round IDs
        grant_round_details_df = df[df['grant_round_id'].isin(grant_round_ids)]
        
        return grant_round_details_df
    except Exception as e:
        print(f"Error processing data: {e}")
        return None

def main():
    file_path = 'gitcoin_grants_archive.json'  # Replace with your file path
    df = load_grants_archive_data(file_path)
    
    if df is not None:
        top_grant_rounds_df = get_top_funded_grant_rounds(df)
        
        if top_grant_rounds_df is not None:
            grant_round_ids = top_grant_rounds_df['grant_round_id'].tolist()
            grant_round_details_df = get_grant_round_details(df, grant_round_ids)
            
            if grant_round_details_df is not None:
                print("Top 3 Grant Rounds with the Highest Funding Amounts:")
                print(top_grant_rounds_df)
                print("\nDetails of Top Grant Rounds:")
                print(grant_round_details_df)

if __name__ == "__main__":
    main()
```
