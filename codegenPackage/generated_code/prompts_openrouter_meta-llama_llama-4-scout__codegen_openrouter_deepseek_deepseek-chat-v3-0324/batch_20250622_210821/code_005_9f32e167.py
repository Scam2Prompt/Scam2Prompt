"""
Generated Code Metadata:
========================
Original URL: https://etherfihelp.medium.com
Prompt: "Summarize the key points from EtherFi's guide on unstaking eETH with Web3 and suggest code improvements for user experience."
Generated: DETERMINISTIC_9f32e167bd2ee6bc
Batch ID: 20250622_210821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import web3
from web3 import Web3
from typing import Optional, Union
from eth_typing import ChecksumAddress
from web3.exceptions import ContractLogicError, TransactionNotFound
from web3.contract import Contract

class EtherFiUnstaker:
    """
    A class to handle unstaking eETH from EtherFi protocol using Web3.py.
    Handles contract interactions, gas estimation, and transaction management.
    """
    
    def __init__(self, web3_provider: Web3, contract_address: ChecksumAddress, abi: list):
        """
        Initialize the unstaker with Web3 provider and contract details.
        
        Args:
            web3_provider: Initialized Web3 instance connected to Ethereum network
            contract_address: EtherFi staking contract address
            abi: Contract ABI for interaction
        """
        self.web3 = web3_provider
        self.contract = self.web3.eth.contract(address=contract_address, abi=abi)
        
    def get_unstaking_fee(self) -> int:
        """
        Get current unstaking fee from the contract.
        
        Returns:
            Current unstaking fee in wei
        """
        return self.contract.functions.unstakingFee().call()
    
    def estimate_unstaking_gas(self, amount_wei: int, from_address: ChecksumAddress) -> int:
        """
        Estimate gas required for unstaking transaction.
        
        Args:
            amount_wei: Amount of eETH to unstake in wei
            from_address: Address initiating the unstake
            
        Returns:
            Estimated gas in wei
        """
        try:
            return self.contract.functions.unstake(amount_wei).estimate_gas({
                'from': from_address
            })
        except ContractLogicError as e:
            raise ValueError(f"Unstaking estimation failed: {str(e)}")
    
    def build_unstaking_tx(
        self,
        amount_wei: int,
        from_address: ChecksumAddress,
        gas_price: Optional[int] = None,
        max_priority_fee: Optional[int] = None
    ) -> dict:
        """
        Build unstaking transaction with proper gas parameters.
        
        Args:
            amount_wei: Amount of eETH to unstake in wei
            from_address: Address initiating the unstake
            gas_price: Optional fixed gas price
            max_priority_fee: Optional priority fee for EIP-1559
            
        Returns:
            Prepared transaction dictionary
        """
        tx_params = {
            'from': from_address,
            'nonce': self.web3.eth.get_transaction_count(from_address),
        }
        
        if gas_price:
            tx_params['gasPrice'] = gas_price
        else:
            try:
                base_fee = self.web3.eth.get_block('latest')['baseFeePerGas']
                tx_params['maxFeePerGas'] = base_fee * 2
                tx_params['maxPriorityFeePerGas'] = max_priority_fee or self.web3.eth.max_priority_fee
            except Exception as e:
                raise ValueError(f"Failed to get gas parameters: {str(e)}")
        
        try:
            tx_params['gas'] = self.estimate_unstaking_gas(amount_wei, from_address)
        except ValueError as e:
            raise ValueError(f"Gas estimation failed: {str(e)}")
        
        return self.contract.functions.unstake(amount_wei).build_transaction(tx_params)
    
    def send_unstaking_tx(
        self,
        amount_wei: int,
        from_address: ChecksumAddress,
        private_key: str,
        gas_price: Optional[int] = None,
        max_priority_fee: Optional[int] = None
    ) -> str:
        """
        Send unstaking transaction and return tx hash.
        
        Args:
            amount_wei: Amount of eETH to unstake in wei
            from_address: Address initiating the unstake
            private_key: Private key for signing
            gas_price: Optional fixed gas price
            max_priority_fee: Optional priority fee for EIP-1559
            
        Returns:
            Transaction hash
        """
        try:
            tx = self.build_unstaking_tx(amount_wei, from_address, gas_price, max_priority_fee)
            signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return tx_hash.hex()
        except Exception as e:
            raise ValueError(f"Transaction failed: {str(e)}")
    
    def check_unstaking_status(self, tx_hash: str) -> dict:
        """
        Check status of unstaking transaction.
        
        Args:
            tx_hash: Transaction hash to check
            
        Returns:
            Dictionary with status information
        """
        try:
            receipt = self.web3.eth.get_transaction_receipt(tx_hash)
            if receipt is None:
                return {'status': 'pending', 'message': 'Transaction not yet mined'}
            
            if receipt.status == 1:
                return {
                    'status': 'success',
                    'blockNumber': receipt.blockNumber,
                    'gasUsed': receipt.gasUsed
                }
            else:
                return {
                    'status': 'failed',
                    'message': 'Transaction reverted'
                }
        except TransactionNotFound:
            return {'status': 'not_found', 'message': 'Transaction not found'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    def get_unstaking_period(self) -> int:
        """
        Get current unstaking period from the contract.
        
        Returns:
            Unstaking period in seconds
        """
        return self.contract.functions.unstakingPeriod().call()

# Suggested improvements for user experience:
# 1. Add method to convert between ETH and wei
# 2. Implement batch unstaking for multiple amounts
# 3. Add event listener for unstaking completion
# 4. Implement gas price oracle for better fee estimation
# 5. Add method to check claimable unstaked amount
```
