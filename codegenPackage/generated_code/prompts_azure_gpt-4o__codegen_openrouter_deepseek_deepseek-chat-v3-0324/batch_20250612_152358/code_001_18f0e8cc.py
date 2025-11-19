"""
Generated Code Metadata:
========================
Original URL: https://choccoin-dashboard.pages.dev
Prompt: Generate code to calculate a user's ranking among the top 200 buyers of $CHOC tokens during the presale based on transaction data.
Generated: DETERMINISTIC_18f0e8cc85851f12
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import List, Dict, Optional

def calculate_user_ranking(transactions: List[Dict], user_address: str) -> Optional[int]:
    """
    Calculate a user's ranking among the top 200 buyers of $CHOC tokens during the presale.

    Args:
        transactions: List of dictionaries containing transaction data with keys:
                     - 'buyer_address': str, the buyer's wallet address
                     - 'amount': float, the amount of $CHOC tokens purchased
        user_address: str, the wallet address of the user to check ranking for

    Returns:
        int: The user's ranking (1-based) if they are in top 200, None otherwise
    """
    try:
        # Convert transactions to DataFrame for easier processing
        df = pd.DataFrame(transactions)
        
        # Group by buyer_address and sum their total purchases
        grouped = df.groupby('buyer_address')['amount'].sum().reset_index()
        
        # Sort buyers by total amount in descending order
        sorted_buyers = grouped.sort_values('amount', ascending=False)
        
        # Reset index to get ranking (1-based)
        sorted_buyers.reset_index(drop=True, inplace=True)
        sorted_buyers.index += 1
        
        # Get top 200 buyers
        top_200 = sorted_buyers.head(200)
        
        # Check if user is in top 200
        user_ranking = top_200.index[top_200['buyer_address'] == user_address]
        
        if not user_ranking.empty:
            return user_ranking[0]
        return None
        
    except Exception as e:
        print(f"Error calculating user ranking: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Sample transaction data
    transactions = [
        {'buyer_address': '0x123', 'amount': 1000},
        {'buyer_address': '0x456', 'amount': 5000},
        {'buyer_address': '0x789', 'amount': 3000},
        {'buyer_address': '0x123', 'amount': 2000},
    ]
    
    user_address = '0x123'
    ranking = calculate_user_ranking(transactions, user_address)
    
    if ranking:
        print(f"User ranking: {ranking}")
    else:
        print("User is not in top 200 buyers")
```
