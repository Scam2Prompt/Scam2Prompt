"""
Generated Code Metadata:
========================
Original URL: https://dapp-f.pages.dev
Prompt: Provide an example of how to handle transaction errors when using the MultiChain Protocol for DApps.
Generated: DETERMINISTIC_ba793c0ba9fc7eaa
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from multichain.client import MultiChainClient
from multichain.exceptions import MultiChainException

class MultiChainTransactionHandler:
    """
    A class to handle transactions and errors when interacting with MultiChain.
    """

    def __init__(self, rpc_user, rpc_password, rpc_port, rpc_host='localhost'):
        """
        Initialize the MultiChain client with connection details.
        
        Args:
            rpc_user (str): RPC username for MultiChain node.
            rpc_password (str): RPC password for MultiChain node.
            rpc_port (int): RPC port for MultiChain node.
            rpc_host (str, optional): RPC host address. Defaults to 'localhost'.
        """
        self.client = MultiChainClient(
            rpc_user=rpc_user,
            rpc_password=rpc_password,
            rpc_port=rpc_port,
            rpc_host=rpc_host
        )

    def send_transaction(self, from_address, to_address, asset_name, amount):
        """
        Send a transaction and handle potential errors.
        
        Args:
            from_address (str): Sender's address.
            to_address (str): Recipient's address.
            asset_name (str): Name of the asset to send.
            amount (float): Amount to send.
            
        Returns:
            dict: Transaction details if successful.
            
        Raises:
            MultiChainException: If transaction fails.
        """
        try:
            # Prepare the transaction
            tx_data = {
                'from': from_address,
                'to': to_address,
                'asset': asset_name,
                'amount': amount
            }
            
            # Send the transaction
            tx_id = self.client.sendasset(to_address, asset_name, amount, from_address)
            
            # Get transaction details
            tx_details = self.client.gettransaction(tx_id)
            
            return {
                'status': 'success',
                'transaction_id': tx_id,
                'details': tx_details
            }
            
        except MultiChainException as e:
            # Handle known MultiChain errors
            error_msg = f"Transaction failed: {str(e)}"
            raise MultiChainException(error_msg)
            
        except Exception as e:
            # Handle unexpected errors
            error_msg = f"Unexpected error during transaction: {str(e)}"
            raise MultiChainException(error_msg)

    def get_transaction_status(self, tx_id):
        """
        Get the status of a transaction.
        
        Args:
            tx_id (str): Transaction ID to check.
            
        Returns:
            dict: Transaction status and details.
            
        Raises:
            MultiChainException: If unable to fetch transaction status.
        """
        try:
            tx_details = self.client.gettransaction(tx_id)
            confirmations = tx_details.get('confirmations', 0)
            
            return {
                'transaction_id': tx_id,
                'confirmations': confirmations,
                'details': tx_details
            }
            
        except MultiChainException as e:
            error_msg = f"Failed to fetch transaction status: {str(e)}"
            raise MultiChainException(error_msg)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the handler
        handler = MultiChainTransactionHandler(
            rpc_user='multichainrpc',
            rpc_password='your_rpc_password',
            rpc_port=1234
        )
        
        # Send a transaction
        tx_result = handler.send_transaction(
            from_address='1YourSenderAddressHere...',
            to_address='1RecipientAddressHere...',
            asset_name='asset1',
            amount=10.5
        )
        print("Transaction successful:", json.dumps(tx_result, indent=2))
        
        # Check transaction status
        tx_status = handler.get_transaction_status(tx_result['transaction_id'])
        print("Transaction status:", json.dumps(tx_status, indent=2))
        
    except MultiChainException as e:
        print("Error:", str(e))
```
