"""
Generated Code Metadata:
========================
Original URL: https://walletconnect.com
Prompt: Design a scalable onchain payment system using Reown's Developer Cloud and AppKit, ensuring secure and efficient transactions.
Generated: DETERMINISTIC_7799c0386f5d62c3
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules from Reown's Developer Cloud and AppKit
from reown.cloud import PaymentGateway, BlockchainNetwork, SecurityModule
from reown.appkit import TransactionBuilder, WalletManager, ErrorHandler

# Initialize the blockchain network and payment gateway
blockchain_network = BlockchainNetwork(network_name="MainNet")  # Use MainNet for production
payment_gateway = PaymentGateway(blockchain_network)

# Initialize security module for encryption and secure transaction handling
security_module = SecurityModule()

# WalletManager to handle user wallets
wallet_manager = WalletManager()

# Function to process payments
def process_payment(sender_wallet_id, recipient_wallet_id, amount):
    """
    Processes a payment transaction securely and efficiently.

    Args:
        sender_wallet_id (str): The ID of the sender's wallet.
        recipient_wallet_id (str): The ID of the recipient's wallet.
        amount (float): The amount to be transferred.

    Returns:
        dict: Transaction details if successful, or error details if failed.
    """
    try:
        # Validate input parameters
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        # Retrieve sender and recipient wallets
        sender_wallet = wallet_manager.get_wallet(sender_wallet_id)
        recipient_wallet = wallet_manager.get_wallet(recipient_wallet_id)
        
        if not sender_wallet or not recipient_wallet:
            raise ValueError("Invalid wallet IDs provided.")
        
        # Ensure sender has sufficient balance
        if sender_wallet.balance < amount:
            raise ValueError("Insufficient balance in sender's wallet.")
        
        # Build the transaction securely
        transaction = TransactionBuilder() \
            .set_sender(sender_wallet) \
            .set_recipient(recipient_wallet) \
            .set_amount(amount) \
            .set_security_module(security_module) \
            .build()
        
        # Execute the transaction on the blockchain
        transaction_receipt = payment_gateway.execute_transaction(transaction)
        
        # Return transaction details
        return {
            "status": "success",
            "transaction_id": transaction_receipt.transaction_id,
            "block_number": transaction_receipt.block_number,
            "timestamp": transaction_receipt.timestamp
        }
    
    except Exception as e:
        # Handle errors gracefully and log them
        ErrorHandler.log_error(e)
        return {
            "status": "error",
            "message": str(e)
        }

# Example usage (for testing purposes)
if __name__ == "__main__":
    # Replace with actual wallet IDs and amount
    sender_wallet_id = "wallet123"
    recipient_wallet_id = "wallet456"
    amount = 100.0
    
    # Process the payment
    result = process_payment(sender_wallet_id, recipient_wallet_id, amount)
    
    # Print the result
    print(result)
```
