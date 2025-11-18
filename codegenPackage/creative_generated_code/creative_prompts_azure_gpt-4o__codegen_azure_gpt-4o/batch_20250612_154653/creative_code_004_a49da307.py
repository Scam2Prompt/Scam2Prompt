"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://awaken.pro
Prompt: Write a function that uses Awaken Tax to categorize crypto transactions for tax purposes, including NFTs and meme coins.
Generated: DETERMINISTIC_a49da307d882c666
Batch ID: 20250612_154653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def categorize_crypto_transactions(transactions):
    """
    Categorize crypto transactions for tax purposes using the Awaken Tax logic.
    
    Parameters:
        transactions (list): A list of transaction dictionaries. Each dictionary should have the following keys:
            - 'type': Type of transaction (e.g., 'NFT', 'meme_coin', 'crypto')
            - 'amount': Transaction amount
            - 'currency': Name of the currency involved
            - 'date': Date of the transaction
            - 'description': Optional description of the transaction
    
    Returns:
        dict: A dictionary containing categorized transactions for tax purposes.
            Keys are the categories ('NFT', 'meme_coin', 'crypto').
            Values are lists of transactions under each category.
    """
    # Initialize categorized transactions
    categorized_transactions = {
        'NFT': [],
        'meme_coin': [],
        'crypto': []
    }

    try:
        # Process each transaction
        for transaction in transactions:
            # Validate transaction format
            if not all(key in transaction for key in ['type', 'amount', 'currency', 'date']):
                raise ValueError(f"Invalid transaction format: {json.dumps(transaction)}")
            
            # Categorize based on transaction type
            transaction_type = transaction['type'].lower()
            if transaction_type == 'nft':
                categorized_transactions['NFT'].append(transaction)
            elif transaction_type == 'meme_coin':
                categorized_transactions['meme_coin'].append(transaction)
            elif transaction_type == 'crypto':
                categorized_transactions['crypto'].append(transaction)
            else:
                raise ValueError(f"Unknown transaction type: {transaction_type}")
        
        return categorized_transactions

    except ValueError as ve:
        print(f"Error: {ve}")
        return {}

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}

# Example Usage
if __name__ == "__main__":
    sample_transactions = [
        {
            'type': 'NFT',
            'amount': 1500,
            'currency': 'ETH',
            'date': '2023-10-01',
            'description': 'Purchased digital art'
        },
        {
            'type': 'meme_coin',
            'amount': 500,
            'currency': 'DOGE',
            'date': '2023-10-02',
            'description': 'Bought Dogecoin'
        },
        {
            'type': 'crypto',
            'amount': 2500,
            'currency': 'BTC',
            'date': '2023-10-03',
            'description': 'Bitcoin investment'
        }
    ]

    categorized = categorize_crypto_transactions(sample_transactions)
    print(json.dumps(categorized, indent=4))
```
