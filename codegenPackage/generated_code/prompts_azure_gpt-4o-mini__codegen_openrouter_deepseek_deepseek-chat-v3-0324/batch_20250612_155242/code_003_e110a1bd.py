"""
Generated Code Metadata:
========================
Original URL: https://initia.co
Prompt: Describe the process of integrating a multichain application with Initia's ecosystem.
Generated: DETERMINISTIC_e110a1bdf5365e46
Batch ID: 20250612_155242
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import requests
from typing import Dict, Any, Optional
from web3 import Web3
from web3.middleware import geth_poa_middleware

class InitiaMultichainIntegration:
    """
    A class to handle integration between a multichain application and Initia's ecosystem.
    """
    
    def __init__(self, initia_rpc_url: str, private_key: str, chain_id: int):
        """
        Initialize the integration with Initia's RPC URL and private key.
        
        Args:
            initia_rpc_url (str): The RPC URL for the Initia blockchain.
            private_key (str): The private key for the wallet.
            chain_id (int): The chain ID of the Initia network.
        """
        self.initia_rpc_url = initia_rpc_url
        self.private_key = private_key
        self.chain_id = chain_id
        
        # Initialize Web3 connection
        self.w3 = Web3(Web3.HTTPProvider(initia_rpc_url))
        
        # Add POA middleware if needed (for some testnets)
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        # Set the default account
        self.account = self.w3.eth.account.from_key(private_key)
        self.w3.eth.default_account = self.account.address
    
    def get_contract(self, contract_address: str, abi: str) -> Any:
        """
        Get a contract instance from its address and ABI.
        
        Args:
            contract_address (str): The address of the contract.
            abi (str): The ABI of the contract as a JSON string.
            
        Returns:
            Any: The contract instance.
        """
        contract_abi = json.loads(abi)
        contract = self.w3.eth.contract(address=contract_address, abi=contract_abi)
        return contract
    
    def send_transaction(self, contract_function, value: int = 0, gas: int = 200000) -> str:
        """
        Send a transaction to the Initia blockchain.
        
        Args:
            contract_function: The contract function to call.
            value (int): The value to send with the transaction (in wei).
            gas (int): The gas limit for the transaction.
            
        Returns:
            str: The transaction hash.
            
        Raises:
            Exception: If the transaction fails.
        """
        try:
            # Build the transaction
            tx = contract_function.build_transaction({
                'chainId': self.chain_id,
                'gas': gas,
                'value': value,
                'nonce': self.w3.eth.get_transaction_count(self.account.address),
            })
            
            # Sign the transaction
            signed_tx = self.w3.eth.account.sign_transaction(tx, self.private_key)
            
            # Send the transaction
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            # Wait for the transaction to be mined
            tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
            
            if tx_receipt.status == 0:
                raise Exception("Transaction failed")
                
            return tx_hash.hex()
        except Exception as e:
            raise Exception(f"Transaction failed: {str(e)}")
    
    def query_contract(self, contract_function) -> Any:
        """
        Query a contract function (read-only).
        
        Args:
            contract_function: The contract function to call.
            
        Returns:
            Any: The result of the function call.
        """
        return contract_function.call()
    
    def get_balance(self, address: Optional[str] = None) -> int:
        """
        Get the balance of an address (or the default account if None).
        
        Args:
            address (Optional[str]): The address to query. Defaults to None.
            
        Returns:
            int: The balance in wei.
        """
        if address is None:
            address = self.account.address
        return self.w3.eth.get_balance(address)
    
    def get_transaction_status(self, tx_hash: str) -> Dict[str, Any]:
        """
        Get the status of a transaction.
        
        Args:
            tx_hash (str): The transaction hash.
            
        Returns:
            Dict[str, Any]: The transaction receipt.
        """
        return dict(self.w3.eth.get_transaction_receipt(tx_hash))
    
    def bridge_asset(
        self,
        target_chain_rpc: str,
        bridge_contract_address: str,
        bridge_abi: str,
        token_address: str,
        token_abi: str,
        amount: int,
        recipient: str
    ) -> str:
        """
        Bridge an asset from Initia to another chain.
        
        Args:
            target_chain_rpc (str): The RPC URL of the target chain.
            bridge_contract_address (str): The address of the bridge contract.
            bridge_abi (str): The ABI of the bridge contract.
            token_address (str): The address of the token to bridge.
            token_abi (str): The ABI of the token contract.
            amount (int): The amount to bridge (in wei).
            recipient (str): The recipient address on the target chain.
            
        Returns:
            str: The transaction hash of the bridge operation.
            
        Raises:
            Exception: If the bridge operation fails.
        """
        try:
            # Approve the bridge contract to spend the tokens
            token_contract = self.get_contract(token_address, token_abi)
            approve_tx = token_contract.functions.approve(
                bridge_contract_address,
                amount
            )
            approve_tx_hash = self.send_transaction(approve_tx)
            
            # Call the bridge contract to initiate the transfer
            bridge_contract = self.get_contract(bridge_contract_address, bridge_abi)
            bridge_tx = bridge_contract.functions.transferToChain(
                token_address,
                amount,
                recipient,
                target_chain_rpc
            )
            bridge_tx_hash = self.send_transaction(bridge_tx)
            
            return bridge_tx_hash
        except Exception as e:
            raise Exception(f"Bridge operation failed: {str(e)}")
```
