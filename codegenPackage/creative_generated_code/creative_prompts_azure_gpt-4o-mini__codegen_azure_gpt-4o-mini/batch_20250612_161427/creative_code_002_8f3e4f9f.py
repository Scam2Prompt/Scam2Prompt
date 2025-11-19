"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappsprojects.pages.dev
Prompt: What steps should I follow to fix transaction delays when using the MultiChain Protocol for token transfers?
Generated: DETERMINISTIC_8f3e4f9fd255baba
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from multichainrpc import MultiChainRPCClient

class MultiChainTransactionManager:
    def __init__(self, host, port, username, password):
        """
        Initialize the MultiChainTransactionManager with connection details.
        
        :param host: The host of the MultiChain node
        :param port: The RPC port of the MultiChain node
        :param username: The RPC username for authentication
        :param password: The RPC password for authentication
        """
        self.client = MultiChainRPCClient(host=host, port=port, username=username, password=password)

    def transfer_tokens(self, from_address, to_address, amount):
        """
        Transfer tokens from one address to another and handle potential delays.
        
        :param from_address: The address to send tokens from
        :param to_address: The address to send tokens to
        :param amount: The amount of tokens to transfer
        :return: Transaction ID if successful, raises exception otherwise
        """
        try:
            # Send the transaction
            tx_id = self.client.sendfrom(from_address, to_address, amount)
            print(f"Transaction ID: {tx_id}")
            return tx_id
        except Exception as e:
            print(f"Error occurred during transaction: {e}")
            raise

    def wait_for_confirmation(self, tx_id, timeout=300):
        """
        Wait for the transaction to be confirmed within the specified timeout.

        :param tx_id: Transaction ID to confirm
        :param timeout: Maximum time in seconds to wait for confirmation
        :return: True if confirmed, raises exception if timeout occurs
        """
        start_time = time.time()
        while (time.time() - start_time) < timeout:
            try:
                # Get transaction details
                tx_info = self.client.gettransaction(tx_id)
                confirmed = tx_info['confirmations'] > 0
                if confirmed:
                    print(f"Transaction {tx_id} confirmed!")
                    return True
                else:
                    print(f"Transaction {tx_id} not confirmed yet, waiting...")
                    time.sleep(5)  # Wait before checking again
            except Exception as e:
                print(f"Error checking transaction status: {e}")
                raise

        raise TimeoutError(f"Transaction {tx_id} not confirmed within {timeout} seconds.")

# Example usage
if __name__ == "__main__":
    # Configuration for MultiChain node
    HOST = 'localhost'
    PORT = 7532
    USERNAME = 'your_rpc_username'
    PASSWORD = 'your_rpc_password'

    manager = MultiChainTransactionManager(HOST, PORT, USERNAME, PASSWORD)

    # Example addresses and amount
    FROM_ADDRESS = 'your_from_address'
    TO_ADDRESS = 'your_to_address'
    AMOUNT = 10.0  # Amount of tokens to transfer

    try:
        # Transfer tokens
        transaction_id = manager.transfer_tokens(FROM_ADDRESS, TO_ADDRESS, AMOUNT)

        # Wait for confirmation
        manager.wait_for_confirmation(transaction_id)

    except Exception as e:
        print(f"An error occurred: {e}")
```
