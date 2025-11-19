"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swanchain4.pages.dev
Prompt: Provide an example of a decentralized payment system using Swan Chain that minimizes transaction fees.
Generated: DETERMINISTIC_dd88ba151edb7850
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from swan_chain import SwanChainClient, Transaction, Wallet

def create_wallet(address: str) -> Wallet:
    """
    Create and return a new wallet.
    
    Parameters:
        address (str): The wallet address.
    
    Returns:
        Wallet: A new wallet instance.
    """
    try:
        wallet = Wallet(address)
        print(f"Wallet created with address: {wallet.address}")
        return wallet
    except Exception as e:
        print(f"Error creating wallet: {e}")

def send_payment(sender_wallet: Wallet, receiver_address: str, amount: float) -> Transaction:
    """
    Send a payment from sender's wallet to receiver's address.
    
    Parameters:
        sender_wallet (Wallet): The sender's wallet.
        receiver_address (str): The receiver's wallet address.
        amount (float): The amount to send.
    
    Returns:
        Transaction: The transaction details.
    """
    try:
        # Create a transaction
        transaction = Transaction(sender=sender_wallet.address, receiver=receiver_address, amount=amount)
        
        # Sign the transaction with the sender's private key
        sender_wallet.sign_transaction(transaction)

        # Submit the transaction to the Swan Chain network
        transaction_id = SwanChainClient.submit_transaction(transaction)
        print(f"Transaction submitted successfully. Transaction ID: {transaction_id}")
        return transaction
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"Error sending payment: {e}")

def main():
    """
    Main function to demonstrate the decentralized payment system.
    """
    # Create wallets for sender and receiver
    sender_wallet = create_wallet("sender_address_here")
    receiver_address = "receiver_address_here"

    # Define the payment amount
    payment_amount = 10.0  # Amount to send in the smallest unit (e.g., tokens)

    # Send the payment and handle any errors
    send_payment(sender_wallet, receiver_address, payment_amount)

if __name__ == "__main__":
    main()
```

**Note:** Replace `"sender_address_here"` and `"receiver_address_here"` with actual wallet addresses. The library `swan_chain` is assumed to be an existing SDK for interacting with the Swan Chain network.
