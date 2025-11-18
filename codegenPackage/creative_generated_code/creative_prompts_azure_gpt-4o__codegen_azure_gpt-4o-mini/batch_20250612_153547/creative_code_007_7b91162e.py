"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pecinosol.com
Prompt: Create a script to verify that Pecino ($PCNO) token adheres to its "No Tax, No Bullshit" policy during transactions on the Solana blockchain.
Generated: DETERMINISTIC_7b91162e1e88d9f9
Batch ID: 20250612_153547
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json

# Constants
SOLANA_API_URL = 'https://api.mainnet-beta.solana.com'

# Function to get the transaction details for a specific signature
def get_transaction_details(signature):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getConfirmedTransaction",
        "params": [signature, 'jsonParsed']
    }
    
    try:
        response = requests.post(SOLANA_API_URL, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching transaction details: {e}")
        return None

# Function to validate transaction for Pecino ($PCNO)
def validate_pcno_transaction(signature):
    transaction_data = get_transaction_details(signature)
    
    # Check if transaction data is valid
    if not transaction_data or 'result' not in transaction_data:
        print("Invalid transaction data received.")
        return False

    transaction = transaction_data['result']
    
    # Check for specific token transfers
    for instruction in transaction['transaction']['message']['instructions']:
        # Ensure the instruction is a token transfer
        if instruction.get('parsed', {}).get('type') == 'transfer':
            token_amount = float(instruction['parsed']['info']['lamports']) / 1_000_000_000  # Convert lamports to SOL
            token_address = instruction['parsed']['info']['mint']
            
            # Check if the token is Pecino ($PCNO)
            if token_address == '<PCNO_TOKEN_ADDRESS>':
                if token_amount > 0:
                    print(f"Transaction {signature} is valid: {token_amount} $PCNO transferred.")
                else:
                    print(f"Transaction {signature}: Invalid transfer amount.")
                return True
    
    print(f"Transaction {signature}: No valid Pecino ($PCNO) transfer found.")
    return False

# Example usage
if __name__ == "__main__":
    transaction_signature = "<TRANSACTION_SIGNATURE>"  # replace with actual transaction signature
    is_valid = validate_pcno_transaction(transaction_signature)
    if is_valid:
        print("Transaction adheres to the 'No Tax, No Bullshit' policy.")
    else:
        print("Transaction does not adhere to the 'No Tax, No Bullshit' policy.")
```

Ensure to replace `<PCNO_TOKEN_ADDRESS>` with the actual token address for Pecino ($PCNO) and `<TRANSACTION_SIGNATURE>` with the actual transaction signature you want to validate.
