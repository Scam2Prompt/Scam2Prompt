"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spaceprocurator.pages.dev
Prompt: Provide an example of how to use the Multichain MPC (Multi-Party Computation) for secure and non-custodial cross-chain bridging in a blockchain application.
Generated: DETERMINISTIC_31757f28e616183b
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from multichain import Multichain

# Configure logging
logging.basicConfig(level=logging.INFO)

class CrossChainBridge:
    def __init__(self, multichain_config):
        """
        Initialize the CrossChainBridge with Multichain configuration.
        
        :param multichain_config: Dictionary containing Multichain connection parameters.
        """
        self.multichain = Multichain(multichain_config)
        self.setup()

    def setup(self):
        """Setup initial configurations, create necessary addresses, and ensure chains are connected."""
        try:
            # Ensure the Multichain node is properly connected
            self.multichain.test_connection()
            logging.info("Multichain connection established.")
        except Exception as e:
            logging.error(f"Failed to connect to Multichain: {e}")
            raise

    def create_bridge_transaction(self, from_address, to_address, amount, asset):
        """
        Create a bridge transaction to transfer assets between chains.
        
        :param from_address: Wallet address to send from.
        :param to_address: Wallet address to send to.
        :param amount: Amount of asset to transfer.
        :param asset: The asset type to transfer.
        :return: Transaction ID of the created transaction.
        """
        try:
            # Validate inputs
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            if not asset:
                raise ValueError("Asset type must be specified.")
            
            # Create the transaction
            tx_id = self.multichain.send_from(from_address, to_address, amount, asset)
            logging.info(f"Transaction created with ID: {tx_id}")
            return tx_id
        
        except Exception as e:
            logging.error(f"Error creating bridge transaction: {e}")
            raise

    def monitor_transaction(self, tx_id):
        """
        Monitor the status of a transaction until confirmation.
        
        :param tx_id: The transaction ID to monitor.
        """
        try:
            while True:
                tx_info = self.multichain.get_transaction(tx_id)
                
                if tx_info['confirmations'] > 0:
                    logging.info(f"Transaction {tx_id} confirmed.")
                    break
                
                logging.info(f"Transaction {tx_id} is pending...")
        
        except Exception as e:
            logging.error(f"Error monitoring transaction {tx_id}: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Example Multichain configuration
    multichain_config = {
        'host': 'localhost',
        'port': 7200,
        'user': 'your_rpc_user',
        'password': 'your_rpc_password',
        'chain_name': 'your_chain'
    }

    # Instantiate the CrossChainBridge
    bridge = CrossChainBridge(multichain_config)

    # Create a bridge transaction
    from_address = 'source_wallet_address'
    to_address = 'destination_wallet_address'
    amount = 10.0
    asset = 'your_asset'

    try:
        transaction_id = bridge.create_bridge_transaction(from_address, to_address, amount, asset)
        bridge.monitor_transaction(transaction_id)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
