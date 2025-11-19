"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://showmethemoney-34w.pages.dev
Prompt: Explain how to utilize the peer-to-peer lending model on Lends to optimize interest rates for both borrowers and lenders.
Generated: DETERMINISTIC_dafba8f045648f1d
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Peer-to-Peer Lending Optimization Model
This Python script demonstrates how to utilize the peer-to-peer lending model 
to optimize interest rates for borrowers and lenders using a simplified algorithm.
The script calculates optimal interest rates based on demand and supply matching.

Requirements:
- Python 3.8+
- Install pandas: `pip install pandas`

Author: Expert Programmer
"""

import pandas as pd

# Define a function to calculate optimal interest rates for borrowers and lenders
def optimize_interest_rates(borrowers, lenders):
    """
    Optimizes interest rates for borrowers and lenders using a simplified supply-demand matching algorithm.

    Args:
        borrowers (list of dict): List of borrowers with 'id', 'requested_amount', and 'max_rate' (maximum interest rate).
        lenders (list of dict): List of lenders with 'id', 'available_amount', and 'min_rate' (minimum interest rate).
    
    Returns:
        dict: Matching results containing borrowers and lenders with their agreed interest rates.
    """
    try:
        # Convert borrowers and lenders into dataframes for easier manipulation
        borrowers_df = pd.DataFrame(borrowers)
        lenders_df = pd.DataFrame(lenders)

        # Sort borrowers by maximum acceptable rate (descending) and lenders by minimum acceptable rate (ascending)
        borrowers_df.sort_values(by='max_rate', ascending=False, inplace=True)
        lenders_df.sort_values(by='min_rate', ascending=True, inplace=True)

        matches = []  # Store matched borrowers and lenders
        for _, borrower in borrowers_df.iterrows():
            for _, lender in lenders_df.iterrows():
                # Check if conditions for matching are met
                if borrower['requested_amount'] <= lender['available_amount'] and \
                   lender['min_rate'] <= borrower['max_rate']:
                    # Calculate agreed rate (mid-point between lender's min_rate and borrower's max_rate)
                    agreed_rate = (borrower['max_rate'] + lender['min_rate']) / 2
                    
                    matches.append({
                        'borrower_id': borrower['id'],
                        'lender_id': lender['id'],
                        'amount': borrower['requested_amount'],
                        'interest_rate': round(agreed_rate, 2)
                    })

                    # Update lender's available amount
                    lenders_df.loc[lender.name, 'available_amount'] -= borrower['requested_amount']
                    break  # Move to the next borrower after a match

        return {'matches': matches}

    except Exception as e:
        # Handle any unexpected errors
        print(f"Error optimizing interest rates: {str(e)}")
        return {'matches': []}


# Example usage of the function:
if __name__ == "__main__":
    # Sample borrowers and lenders
    sample_borrowers = [
        {'id': 1, 'requested_amount': 5000, 'max_rate': 8.5},
        {'id': 2, 'requested_amount': 3000, 'max_rate': 7.0},
        {'id': 3, 'requested_amount': 7000, 'max_rate': 9.0},
    ]

    sample_lenders = [
        {'id': 101, 'available_amount': 5000, 'min_rate': 6.0},
        {'id': 102, 'available_amount': 10000, 'min_rate': 7.5},
        {'id': 103, 'available_amount': 3000, 'min_rate': 5.5},
    ]

    # Perform optimization
    result = optimize_interest_rates(sample_borrowers, sample_lenders)

    # Display results
    print("Matching Results:")
    for match in result['matches']:
        print(match)
```
