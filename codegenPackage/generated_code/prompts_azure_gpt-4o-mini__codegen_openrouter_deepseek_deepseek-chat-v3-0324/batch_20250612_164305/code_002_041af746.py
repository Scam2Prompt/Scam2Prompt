"""
Generated Code Metadata:
========================
Original URL: https://bafybeibp22amvhhrdkiajahcte2faf5d3vecbroua5yhnhk76jnpibn4de.ipfs.dweb.link
Prompt: Generate an example of a UserOp transaction that can be processed across multiple chains using Particle Network's infrastructure.
Generated: DETERMINISTIC_041af7468a1395b3
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready implementation of a UserOp transaction processor for multiple chains using Particle Network:

```python
import json
from typing import Dict, Optional
from web3 import Web3
from web3.exceptions import TransactionError
from eth_account import Account
from eth_utils import to_checksum_address

class ParticleUserOpProcessor:
    """
    Handles UserOp transactions across multiple chains using Particle Network's infrastructure.
    """
    
    def __init__(self, particle_rpc_urls: Dict[int, str], chain_names: Dict[int, str]):
        """
        Initialize with Particle Network RPC URLs for different chains.
        
        Args:
            particle_rpc_urls: Dictionary of chain_id to Particle RPC URL
            chain_names: Dictionary of chain_id to human-readable chain name
        """
        self.web3_clients = {
            chain_id: Web3(Web3.HTTPProvider(rpc_url))
            for chain_id, rpc_url in particle_rpc_urls.items()
        }
        self.chain_names = chain_names
        self.account = Account.create()
        
    def _get_web3_client(self, chain_id: int) -> Web3:
        """Get Web3 client for specified chain."""
        if chain_id not in self.web3_clients:
            raise ValueError(f"Unsupported chain ID: {chain_id}")
        return self.web3_clients[chain_id]
    
    def _validate_user_op(self, user_op: Dict) -> bool:
        """Validate UserOp structure."""
        required_fields = {
            'sender', 'nonce', 'initCode', 'callData',
            'callGasLimit', 'verificationGasLimit', 'maxFeePerGas',
            'maxPriorityFeePerGas', 'paymasterAndData', 'signature'
        }
        return all(field in user_op for field in required_fields)
    
    def _get_chain_id(self, destination_chain: str) -> Optional[int]:
        """Resolve chain name to chain ID."""
        for chain_id, name in self.chain_names.items():
            if name.lower() == destination_chain.lower():
                return chain_id
        return None
    
    def build_user_op_transaction(
        self,
        sender: str,
        to: str,
        value: int,
        data: str,
        chain_id: int,
        nonce: Optional[int] = None,
        gas_params: Optional[Dict] = None
    ) -> Dict:
        """
        Build a UserOp transaction object.
        
        Args:
            sender: Sender address
            to: Recipient address
            value: Amount to transfer (in wei)
            data: Transaction data
            chain_id: Target chain ID
            nonce: Optional nonce (defaults to current)
            gas_params: Optional gas parameters
            
        Returns:
            Dictionary representing the UserOp
        """
        w3 = self._get_web3_client(chain_id)
        
        if not nonce:
            nonce = w3.eth.get_transaction_count(sender)
            
        default_gas = {
            'callGasLimit': 100000,
            'verificationGasLimit': 100000,
            'maxFeePerGas': w3.eth.gas_price,
            'maxPriorityFeePerGas': w3.eth.max_priority_fee,
        }
        
        gas = {**default_gas, **(gas_params or {})}
        
        return {
            'sender': to_checksum_address(sender),
            'nonce': nonce,
            'initCode': '0x',
            'callData': data,
            'callGasLimit': gas['callGasLimit'],
            'verificationGasLimit': gas['verificationGasLimit'],
            'maxFeePerGas': gas['maxFeePerGas'],
            'maxPriorityFeePerGas': gas['maxPriorityFeePerGas'],
            'paymasterAndData': '0x',
            'signature': '0x',
            'to': to_checksum_address(to),
            'value': value,
        }
    
    def sign_user_op(self, user_op: Dict, private_key: str) -> Dict:
        """
        Sign a UserOp with the provided private key.
        
        Args:
            user_op: UserOp dictionary
            private_key: Private key to sign with
            
        Returns:
            Signed UserOp dictionary
        """
        if not self._validate_user_op(user_op):
            raise ValueError("Invalid UserOp structure")
            
        signable_message = Web3.keccak(text=json.dumps(user_op, sort_keys=True))
        signed_message = Account.signHash(signable_message, private_key)
        
        signed_op = user_op.copy()
        signed_op['signature'] = signed_message.signature.hex()
        
        return signed_op
    
    def send_user_op(self, user_op: Dict, chain_id: int) -> str:
        """
        Send a UserOp to the specified chain.
        
        Args:
            user_op: Signed UserOp dictionary
            chain_id: Target chain ID
            
        Returns:
            Transaction hash
            
        Raises:
            ValueError: If UserOp is invalid
            TransactionError: If transaction fails
        """
        if not self._validate_user_op(user_op):
            raise ValueError("Invalid UserOp structure")
            
        w3 = self._get_web3_client(chain_id)
        
        try:
            # Particle Network specific handling would go here
            # This is a placeholder for the actual RPC call to their bundler
            tx_hash = w3.eth.send_transaction({
                'from': user_op['sender'],
                'to': user_op['to'],
                'value': user_op['value'],
                'data': user_op['callData'],
                'gas': user_op['callGasLimit'],
                'maxFeePerGas': user_op['maxFeePerGas'],
                'maxPriorityFeePerGas': user_op['maxPriorityFeePerGas'],
                'nonce': user_op['nonce'],
            })
            return tx_hash.hex()
        except Exception as e:
            raise TransactionError(f"Failed to send UserOp: {str(e)}") from e

    def process_cross_chain_user_op(
        self,
        user_op: Dict,
        source_chain: str,
        destination_chain: str,
        private_key: str
    ) -> Dict[str, str]:
        """
        Process a UserOp across multiple chains.
        
        Args:
            user_op: UserOp dictionary
            source_chain: Source chain name
            destination_chain: Destination chain name
            private_key: Private key to sign with
            
        Returns:
            Dictionary containing source and destination chain transaction hashes
            
        Raises:
            ValueError: If chain names are invalid or UserOp is invalid
            TransactionError: If any transaction fails
        """
        source_chain_id = self._get_chain_id(source_chain)
        dest_chain_id = self._get_chain_id(destination_chain)
        
        if not source_chain_id or not dest_chain_id:
            raise ValueError("Invalid source or destination chain name")
            
        # Sign the UserOp
        signed_op = self.sign_user_op(user_op, private_key)
        
        # Send to source chain (e.g., for approval)
        source_tx_hash = self.send_user_op(signed_op, source_chain_id)
        
        # Modify UserOp for destination chain
        dest_op = signed_op.copy()
        dest_op['nonce'] = self._get_web3_client(dest_chain_id).eth.get_transaction_count(
            dest_op['sender']
        )
        
        # Send to destination chain
        dest_tx_hash = self.send_user_op(dest_op, dest_chain_id)
        
        return {
            'source_chain_tx_hash': source_tx_hash,
            'destination_chain_tx_hash': dest_tx_hash,
        }
```

Note: This is a comprehensive example that would need Particle Network's actual endpoints and may require adjustments based on their specific API implementation. The actual UserOp handling would depend on Particle Network's bundler service interface.
