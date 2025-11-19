"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-heist-giveaway.web.app
Prompt: Provide an example of how to handle unverified recipient transactions using Helio's payment features.
Generated: DETERMINISTIC_7be4cfd909d25b93
Batch ID: 20250612_162707
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import helio_sdk
from helio_sdk.exceptions import HelioError

# Initialize Helio's payment client
# Replace 'your_api_key' with your actual API key obtained from Helio
HELIO_API_KEY = "your_api_key"
helio_client = helio_sdk.Client(api_key=HELIO_API_KEY)

def process_transaction(amount, recipient_address, currency="SOL"):
    """
    Process a transaction to the specified recipient using Helio payment features.
    
    Parameters:
        amount (float): The transaction amount to send.
        recipient_address (str): The recipient's wallet address.
        currency (str): The currency to use for the transaction (default is SOL).
    
    Returns:
        dict: A dictionary containing transaction details, or an error message.
    """
    try:
        # Validate input parameters
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        if not recipient_address:
            raise ValueError("Recipient address cannot be empty.")
        
        # Use Helio's SDK to create and send a transaction
        transaction = helio_client.create_payment(
            amount=amount,
            recipient=recipient_address,
            currency=currency
        )
        
        # Verify transaction response
        if transaction.get("status") != "success":
            raise HelioError(f"Transaction failed: {transaction.get('message')}")
        
        # Return transaction details upon success
        return {
            "status": "success",
            "transaction_id": transaction.get("transaction_id"),
            "amount": amount,
            "currency": currency,
            "recipient_address": recipient_address
        }
    
    except ValueError as ve:
        # Handle invalid input values
        return {"status": "error", "message": str(ve)}
    
    except HelioError as he:
        # Handle errors specific to Helio's SDK
        return {"status": "error", "message": str(he)}
    
    except Exception as ex:
        # Handle any other unexpected errors
        return {"status": "error", "message": f"An unexpected error occurred: {str(ex)}"}

# Example usage
if __name__ == "__main__":
    # Replace with actual recipient address and amount
    recipient = "recipient_wallet_address"
    amount_to_send = 1.5  # Example amount in SOL
    
    transaction_result = process_transaction(amount_to_send, recipient)
    print(transaction_result)
```

Note: Ensure you have the Helio SDK installed (`pip install helio-sdk`) before running this code. Replace placeholders like `your_api_key` and `recipient_wallet_address` with actual values in your production environment.
