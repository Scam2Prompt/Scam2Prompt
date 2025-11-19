"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://federalfirstcapitalunion.com
Prompt: Create a function that calculates the best personal checking account options based on the features listed by Federal First Capital Union.
Generated: DETERMINISTIC_94b136796cc29f8f
Batch ID: 20250612_164319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd

def calculate_best_checking_account(features):
    """
    Calculates and ranks the best personal checking account options 
    based on provided features.

    Args:
        features (dict): A dictionary containing key features to prioritize. 
                         Example: {'low_fees': 1, 'high_interest': 0.8, 'online_access': 0.5}

    Returns:
        pd.DataFrame: A sorted DataFrame with the best checking account options ranked.
    """

    # Error Handling: Validate input
    if not isinstance(features, dict):
        raise ValueError("Features must be provided as a dictionary with weights.")

    # Example checking account data (this would normally come from a database or API)
    checking_accounts = [
        {'account_name': 'Basic Checking', 'low_fees': 1, 'high_interest': 0, 'online_access': 1, 'monthly_fee': 5},
        {'account_name': 'Premium Checking', 'low_fees': 0.7, 'high_interest': 1, 'online_access': 1, 'monthly_fee': 15},
        {'account_name': 'Student Checking', 'low_fees': 1, 'high_interest': 0.3, 'online_access': 0.8, 'monthly_fee': 0},
        {'account_name': 'Business Checking', 'low_fees': 0.5, 'high_interest': 0.5, 'online_access': 0.9, 'monthly_fee': 25}
    ]

    # Convert data to a DataFrame for processing
    accounts_df = pd.DataFrame(checking_accounts)

    # Normalize weights to ensure they sum to 1
    total_weight = sum(features.values())
    normalized_weights = {k: v / total_weight for k, v in features.items()}

    # Calculate a composite score for each account based on supplied weights
    def calculate_score(row):
        score = 0
        for feature, weight in normalized_weights.items():
            if feature in row:
                score += row[feature] * weight
        return score

    # Apply scoring function to all rows in the DataFrame
    accounts_df['score'] = accounts_df.apply(calculate_score, axis=1)

    # Sort accounts by score in descending order (best account first)
    sorted_accounts = accounts_df.sort_values(by='score', ascending=False)

    # Return sorted DataFrame
    return sorted_accounts[['account_name', 'score', 'monthly_fee']]

# Example usage:
if __name__ == "__main__":
    # User-defined feature preferences
    user_features = {'low_fees': 1, 'high_interest': 0.8, 'online_access': 0.5}

    try:
        # Calculate and display the best checking accounts
        best_accounts = calculate_best_checking_account(user_features)
        print(best_accounts)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
