"""
Generated Code Metadata:
========================
Original URL: https://yethereum.com
Prompt: Generate a function that interacts with the Ethereum blockchain to deploy contracts compatible with different types of zkEVM as explained in the recent zkDay discussions.
Generated: DETERMINISTIC_cf5fb04acdcb021e
Batch ID: 20250612_135957
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from web3 import Web3
from web3.contract import Contract
from typing import Dict, Any, Optional, Tuple
from eth_typing import ChecksumAddress
from web3.exceptions import ContractLogicError, TransactionNotFound
from web3.middleware import geth_poa_middleware

class ZkEVMContractDeployer:
    """
    A class to deploy smart contracts to different zkEVM compatible chains.
    Handles deployment to multiple zkEVM implementations with proper error handling.
    """
    
    def __init__(self, rpc_url: str, private_key: str, chain_id: int):
        """
        Initialize the deployer with chain connection details.
        
        Args:
            rpc_url: The RPC endpoint URL for the zkEVM chain
            private_key: The private key for the deployer account
            chain_id: The chain ID of the target network
        """
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        
        # Add POA middleware if needed (for some zkEVMs)
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        self.private_key = private_key
        self.chain_id = chain_id
        self.account = self.w3.eth.account.from_key(private_key)
        
    def _get_nonce(self) -> int:
        """Get the current nonce for the deployer account."""
        return self.w3.eth.get_transaction_count(self.account.address)
    
    def _sign_and_send_transaction(self, tx: Dict[str, Any]) -> str:
        """
        Sign and send a transaction, returning the tx hash.
        
        Args:
            tx: The transaction dictionary
            
        Returns:
            Transaction hash as hex string
            
        Raises:
            ValueError: If transaction fails
        """
        try:
            signed_tx = self.w3.eth.account.sign_transaction(tx, self.private_key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return tx_hash.hex()
        except Exception as e:
            raise ValueError(f"Transaction failed: {str(e)}")
    
    def _wait_for_receipt(self, tx_hash: str, timeout: int = 120) -> Dict[str, Any]:
        """
        Wait for transaction receipt.
        
        Args:
            tx_hash: The transaction hash to wait for
            timeout: Timeout in seconds
            
        Returns:
            Transaction receipt
            
        Raises:
            TimeoutError: If transaction is not mined within timeout
            TransactionNotFound: If transaction is not found
        """
        try:
            return self.w3.eth.wait_for_transaction_receipt(tx_hash, timeout=timeout)
        except Exception as e:
            if "timeout" in str(e).lower():
                raise TimeoutError(f"Transaction not mined within {timeout} seconds")
            raise TransactionNotFound(f"Transaction not found: {str(e)}")
    
    def deploy_contract(
        self,
        contract_abi: str,
        contract_bytecode: str,
        constructor_args: Optional[Tuple[Any, ...]] = None,
        gas_limit: int = 2000000,
        gas_price: Optional[int] = None,
        max_priority_fee: Optional[int] = None
    ) -> Tuple[ChecksumAddress, str]:
        """
        Deploy a contract to the zkEVM chain.
        
        Args:
            contract_abi: JSON string of the contract ABI
            contract_bytecode: Compiled contract bytecode
            constructor_args: Arguments for the constructor (optional)
            gas_limit: Gas limit for deployment
            gas_price: Gas price in wei (optional)
            max_priority_fee: Max priority fee for EIP-1559 (optional)
            
        Returns:
            Tuple of (contract_address, transaction_hash)
            
        Raises:
            ContractLogicError: If contract deployment fails
            ValueError: If transaction fails
        """
        try:
            # Parse ABI
            abi = json.loads(contract_abi)
            
            # Create contract factory
            contract = self.w3.eth.contract(abi=abi, bytecode=contract_bytecode)
            
            # Build transaction
            tx_params = {
                'chainId': self.chain_id,
                'gas': gas_limit,
                'nonce': self._get_nonce(),
                'from': self.account.address
            }
            
            # Handle gas pricing (EIP-1559 or legacy)
            if gas_price is not None:
                tx_params['gasPrice'] = gas_price
            elif max_priority_fee is not None:
                base_fee = self.w3.eth.get_block('latest')['baseFeePerGas']
                tx_params['maxPriorityFeePerGas'] = max_priority_fee
                tx_params['maxFeePerGas'] = max_priority_fee + base_fee
            
            # Build constructor transaction
            if constructor_args:
                constructor_tx = contract.constructor(*constructor_args).build_transaction(tx_params)
            else:
                constructor_tx = contract.constructor().build_transaction(tx_params)
            
            # Send transaction
            tx_hash = self._sign_and_send_transaction(constructor_tx)
            
            # Wait for receipt
            receipt = self._wait_for_receipt(tx_hash)
            
            if receipt.status != 1:
                raise ContractLogicError("Contract deployment failed")
            
            contract_address = receipt['contractAddress']
            if not contract_address:
                raise ValueError("No contract address in receipt")
            
            return (contract_address, tx_hash)
            
        except json.JSONDecodeError:
            raise ValueError("Invalid contract ABI format")
        except ContractLogicError as e:
            raise ContractLogicError(f"Contract deployment failed: {str(e)}")
        except Exception as e:
            raise ValueError(f"Deployment failed: {str(e)}")
    
    def get_contract_instance(
        self,
        contract_address: ChecksumAddress,
        contract_abi: str
    ) -> Contract:
        """
        Get a contract instance for interaction.
        
        Args:
            contract_address: The deployed contract address
            contract_abi: JSON string of the contract ABI
            
        Returns:
            Web3 Contract instance
            
        Raises:
            ValueError: If ABI is invalid or address is wrong
        """
        try:
            abi = json.loads(contract_abi)
            return self.w3.eth.contract(address=contract_address, abi=abi)
        except json.JSONDecodeError:
            raise ValueError("Invalid contract ABI format")
        except Exception as e:
            raise ValueError(f"Failed to create contract instance: {str(e)}")
```
