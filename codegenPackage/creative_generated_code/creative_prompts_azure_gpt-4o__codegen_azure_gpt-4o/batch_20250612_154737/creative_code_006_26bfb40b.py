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
import json

def load_data(file_path):
    """
    Load Gitcoin Grants Archive data from a JSON file.

    Args:
        file_path (str): Path to the JSON file containing grant data.

    Returns:
        list: List of grant round dictionaries.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data.get("grantRounds", [])
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Error decoding JSON from file: {file_path}")

def get_top_funded_rounds(grant_rounds, top_n=3):
    """
    Identify the top N grant rounds with the highest funding amounts.

    Args:
        grant_rounds (list): List of grant round dictionaries.
        top_n (int): Number of top rounds to return.

    Returns:
        list: List of top N grant rounds sorted by funding amount.
    """
    if not grant_rounds:
        raise ValueError("The grant rounds list is empty.")

    # Ensure fundingAmount is available and sort by fundingAmount in descending order
    sorted_rounds = sorted(
        grant_rounds,
        key=lambda round: round.get("fundingAmount", 0),
        reverse=True
    )
    return sorted_rounds[:top_n]

def main():
    """
    Main function to load data, identify top funded grant rounds, and output their details.
    """
    # Path to the Gitcoin Grants Archive JSON file
    file_path = "gitcoin_grants_archive.json"

    try:
        # Load grant rounds data from file
        grant_rounds = load_data(file_path)

        # Get top 3 grant rounds with highest funding amounts
        top_rounds = get_top_funded_rounds(grant_rounds, top_n=3)

        # Output the details of the top grant rounds
        print("Top 3 Grant Rounds by Funding Amount:")
        for idx, round in enumerate(top_rounds, start=1):
            print(f"\nRank {idx}:")
            print(f"  Round Name: {round.get('name', 'N/A')}")
            print(f"  Funding Amount: ${round.get('fundingAmount', 0):,.2f}")
            print(f"  Description: {round.get('description', 'N/A')}")
            print(f"  Start Date: {round.get('startDate', 'N/A')}")
            print(f"  End Date: {round.get('endDate', 'N/A')}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
