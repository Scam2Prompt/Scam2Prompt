"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fairmints.fun
Prompt: Generate code to calculate the holder distribution percentages for the $FAIR token using wallet addresses and balances provided by the FairMint Mint Market.
Generated: DETERMINISTIC_5ce8dbb8dc39a43a
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def calculate_holder_distribution(wallet_data):
    """
    Calculate the holder distribution percentages for the $FAIR token.

    Args:
        wallet_data (list): A list of dictionaries containing wallet addresses 
                            and their respective balances. Example:
                            [
                                {"address": "0x123", "balance": 1000},
                                {"address": "0x456", "balance": 2000},
                                {"address": "0x789", "balance": 500}
                            ]

    Returns:
        dict: A dictionary mapping wallet addresses to their percentage holdings 
              of the total token supply.
              Example:
              {
                  "0x123": 25.0,
                  "0x456": 50.0,
                  "0x789": 12.5
              }
    """
    try:
        # Validate input
        if not isinstance(wallet_data, list):
            raise ValueError("Input data must be a list of wallet dictionaries.")
        
        # Calculate total balance
        total_balance = sum(wallet["balance"] for wallet in wallet_data)
        
        if total_balance == 0:
            raise ValueError("Total balance of all wallets cannot be zero.")
        
        # Calculate percentage holdings for each wallet
        distribution = {
            wallet["address"]: (wallet["balance"] / total_balance) * 100
            for wallet in wallet_data
        }
        
        return distribution

    except KeyError as e:
        raise ValueError(f"Missing expected key in wallet data: {e}")
    except TypeError as e:
        raise ValueError(f"Invalid data type encountered: {e}")


if __name__ == "__main__":
    # Example input data
    wallet_data = [
        {"address": "0x123", "balance": 1000},
        {"address": "0x456", "balance": 2000},
        {"address": "0x789", "balance": 500}
    ]
    
    try:
        # Calculate distribution
        distribution = calculate_holder_distribution(wallet_data)
        
        # Print the result in a readable format (JSON)
        print("Holder Distribution Percentages:")
        print(json.dumps(distribution, indent=4))
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
