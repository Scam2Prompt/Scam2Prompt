"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknetvietnam.wordpress.com
Prompt: Generate a code snippet for a dApp that utilizes StarkNet's Layer 2 capabilities for enhanced scalability on Ethereum.
Generated: DETERMINISTIC_67aa3eac661911f0
Batch ID: 20250612_135528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: starknet_dapp.py

# Import necessary libraries
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.signer import KeySigner
from starknet_py.contract import Contract
from starknet_py.net.account.account import Account
from starknet_py.net.networks import MAINNET
from starknet_py.transaction_exceptions import TransactionRejectedError, TransactionFailedError

# Constants for StarkNet Configuration
STARKNET_NETWORK = MAINNET  # Use MAINNET; can be changed to TESTNET for testing
PRIVATE_KEY = "your_private_key_here"  # Replace with your private key
CONTRACT_ADDRESS = "your_contract_address_here"  # Replace with the deployed contract address
ACCOUNT_ADDRESS = "your_account_address_here"  # Replace with your StarkNet account address

class StarkNetDApp:
    """
    A Decentralized Application (dApp) leveraging StarkNet Layer 2 capabilities.
    """

    def __init__(self):
        # Initialize client for interacting with StarkNet
        self.client = GatewayClient(net=STARKNET_NETWORK)
        
        # Initialize signer for signing transactions
        self.signer = KeySigner.from_private_key(PRIVATE_KEY)
        
        # Initialize user account
        self.account = Account(
            address=ACCOUNT_ADDRESS,
            client=self.client,
            signer=self.signer
        )

    async def interact_with_contract(self, function_name: str, parameters: list):
        """
        Interact with a specified function of the deployed StarkNet contract.
        
        Args:
            function_name (str): Name of the contract function to invoke.
            parameters (list): Parameters to pass to the contract function.
        
        Returns:
            result: Result of the contract interaction.
        """
        try:
            # Fetch the contract object
            contract = await Contract.from_address(CONTRACT_ADDRESS, self.client)
            
            # Interact with the specified function
            invocation = await self.account.invoke(
                contract=contract,
                selector=function_name,
                calldata=parameters
            )
            
            # Wait for transaction to be processed
            await self.client.wait_for_tx(invocation.hash)
            
            # Return transaction hash as confirmation
            return invocation.hash
        except TransactionRejectedError as e:
            print(f"Transaction was rejected: {e}")
        except TransactionFailedError as e:
            print(f"Transaction failed: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    async def query_contract(self, function_name: str, parameters: list):
        """
        Query a specified read-only function of the deployed StarkNet contract.
        
        Args:
            function_name (str): Name of the contract function to query.
            parameters (list): Parameters to pass to the contract function.
        
        Returns:
            result: Result of the contract query.
        """
        try:
            # Fetch the contract object
            contract = await Contract.from_address(CONTRACT_ADDRESS, self.client)
            
            # Call the query function
            result = await contract.functions[function_name].call(*parameters)
            
            # Return the query results
            return result
        except Exception as e:
            print(f"An error occurred during contract query: {e}")

# Example usage of the StarkNet dApp
if __name__ == "__main__":
    import asyncio
    
    async def main():
        # Initialize the dApp
        dapp = StarkNetDApp()
        
        # Example: Interact with a contract function
        tx_hash = await dapp.interact_with_contract("example_function", [123, 456])
        print(f"Transaction hash: {tx_hash}")
        
        # Example: Query a contract function
        query_result = await dapp.query_contract("example_query_function", [789])
        print(f"Query result: {query_result}")
    
    # Run the main function
    asyncio.run(main())
```
