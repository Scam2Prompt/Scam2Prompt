"""
Generated Code Metadata:
========================
Original URL: https://polkadots.network
Prompt: How can I use the Polkadot library to create a decentralized application that interacts with multiple blockchains?
Generated: DETERMINISTIC_1159c523973428cc
Batch ID: 20250612_162347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MultiChainDApp:
    """
    A decentralized application that interacts with multiple blockchains using Polkadot's Substrate interface.
    """
    
    def __init__(self, chain_configs):
        """
        Initialize the DApp with configurations for multiple chains.
        
        Args:
            chain_configs (dict): Dictionary of chain configurations with chain names as keys
                                 and RPC URLs as values.
        """
        self.chain_connections = {}
        self.chain_configs = chain_configs
        self.initialize_connections()
    
    def initialize_connections(self):
        """
        Establish connections to all configured blockchains.
        """
        for chain_name, config in self.chain_configs.items():
            try:
                substrate = SubstrateInterface(
                    url=config['rpc_url'],
                    ss58_format=config.get('ss58_format', 42),
                    type_registry_preset=config.get('type_registry_preset', 'default')
                )
                self.chain_connections[chain_name] = substrate
                logger.info(f"Successfully connected to {chain_name}")
            except SubstrateRequestException as e:
                logger.error(f"Failed to connect to {chain_name}: {str(e)}")
                raise
    
    def get_account_balance(self, chain_name, address):
        """
        Query the balance of an account on a specific chain.
        
        Args:
            chain_name (str): Name of the chain to query
            address (str): SS58 address of the account
            
        Returns:
            dict: Account balance information
        """
        if chain_name not in self.chain_connections:
            raise ValueError(f"Chain {chain_name} not configured")
            
        try:
            result = self.chain_connections[chain_name].query(
                module='System',
                storage_function='Account',
                params=[address]
            )
            return {
                'free': result.value['data']['free'],
                'reserved': result.value['data']['reserved'],
                'misc_frozen': result.value['data']['misc_frozen'],
                'fee_frozen': result.value['data']['fee_frozen']
            }
        except SubstrateRequestException as e:
            logger.error(f"Error querying balance on {chain_name}: {str(e)}")
            raise
    
    def transfer_funds(self, chain_name, sender_mnemonic, recipient, amount):
        """
        Transfer funds between accounts on a specific chain.
        
        Args:
            chain_name (str): Name of the chain to perform the transfer on
            sender_mnemonic (str): Mnemonic phrase of the sender account
            recipient (str): SS58 address of the recipient
            amount (int): Amount to transfer in the smallest unit
            
        Returns:
            str: Transaction hash
        """
        if chain_name not in self.chain_connections:
            raise ValueError(f"Chain {chain_name} not configured")
            
        try:
            keypair = Keypair.create_from_mnemonic(sender_mnemonic)
            substrate = self.chain_connections[chain_name]
            
            call = substrate.compose_call(
                call_module='Balances',
                call_function='transfer',
                call_params={
                    'dest': recipient,
                    'value': amount
                }
            )
            
            extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
            receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
            
            if receipt.is_success:
                logger.info(f"Transfer successful on {chain_name}. Hash: {receipt.extrinsic_hash}")
                return receipt.extrinsic_hash
            else:
                logger.error(f"Transfer failed on {chain_name}: {receipt.error_message}")
                raise Exception(f"Transfer failed: {receipt.error_message}")
                
        except SubstrateRequestException as e:
            logger.error(f"Error during transfer on {chain_name}: {str(e)}")
            raise
    
    def query_storage(self, chain_name, module, storage_function, params=None):
        """
        Query storage from a specific chain.
        
        Args:
            chain_name (str): Name of the chain to query
            module (str): Module name
            storage_function (str): Storage function name
            params (list, optional): Parameters for the query
            
        Returns:
            The query result
        """
        if chain_name not in self.chain_connections:
            raise ValueError(f"Chain {chain_name} not configured")
            
        try:
            return self.chain_connections[chain_name].query(
                module=module,
                storage_function=storage_function,
                params=params or []
            )
        except SubstrateRequestException as e:
            logger.error(f"Error querying storage on {chain_name}: {str(e)}")
            raise
    
    def close_connections(self):
        """
        Close all active blockchain connections.
        """
        for chain_name in list(self.chain_connections.keys()):
            self.chain_connections.pop(chain_name)
            logger.info(f"Closed connection to {chain_name}")

# Example usage
if __name__ == "__main__":
    # Configuration for multiple chains
    chain_configs = {
        'polkadot': {
            'rpc_url': 'wss://rpc.polkadot.io',
            'ss58_format': 0,
            'type_registry_preset': 'polkadot'
        },
        'kusama': {
            'rpc_url': 'wss://kusama-rpc.polkadot.io',
            'ss58_format': 2,
            'type_registry_preset': 'kusama'
        }
    }
    
    try:
        # Initialize the DApp
        dapp = MultiChainDApp(chain_configs)
        
        # Example: Query balance
        balance = dapp.get_account_balance('polkadot', '14Gjs1TD93gnwEBfDMHoCgsuf1s2TVKUP6Z1qKmAZnZ8cW5q')
        print(f"Balance: {json.dumps(balance, indent=2)}")
        
        # Example: Transfer funds (commented out for safety)
        # tx_hash = dapp.transfer_funds(
        #     chain_name='kusama',
        #     sender_mnemonic='your mnemonic phrase here',
        #     recipient='FyRaMYvPqpPKx4pKc3fv3JpL9PsqJj7XU9XqF5J2R6KteXs',
        #     amount=10000000000
        # )
        # print(f"Transaction hash: {tx_hash}")
        
    except Exception as e:
        logger.error(f"Error in DApp: {str(e)}")
    finally:
        if 'dapp' in locals():
            dapp.close_connections()
```
