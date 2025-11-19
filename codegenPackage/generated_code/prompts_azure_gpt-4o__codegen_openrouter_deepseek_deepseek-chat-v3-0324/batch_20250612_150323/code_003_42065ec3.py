"""
Generated Code Metadata:
========================
Original URL: https://reown.com
Prompt: Generate code to implement multi-chain connectivity for a DeFi application using Reown's AppKit. Ensure the solution maximizes efficiency and minimizes risk exposure.
Generated: DETERMINISTIC_42065ec37c9196a1
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
from typing import Dict, List, Optional
from reown.appkit import AppKit, Chain, Wallet, Transaction
from reown.exceptions import ChainConnectionError, TransactionError
from web3 import Web3
from web3.exceptions import ContractLogicError, TransactionNotFound
from eth_utils import to_checksum_address

class MultiChainManager:
    """
    A class to manage multi-chain connectivity for DeFi applications using Reown's AppKit.
    Handles chain connections, wallet management, and cross-chain transactions.
    """
    
    def __init__(self, config: Dict[str, Dict]):
        """
        Initialize the MultiChainManager with configuration for multiple chains.
        
        Args:
            config: Dictionary containing chain configurations with chain IDs as keys.
                   Each value should be a dict with RPC URL, chain name, and other params.
        """
        self.appkit = AppKit()
        self.chains: Dict[str, Chain] = {}
        self.wallets: Dict[str, Wallet] = {}
        self._initialize_chains(config)
        
    def _initialize_chains(self, config: Dict[str, Dict]) -> None:
        """Initialize chain connections based on provided configuration."""
        for chain_id, chain_config in config.items():
            try:
                chain = self.appkit.connect_chain(
                    chain_id=chain_id,
                    rpc_url=chain_config['rpc_url'],
                    name=chain_config.get('name', f'chain_{chain_id}'),
                    **chain_config.get('options', {})
                )
                self.chains[chain_id] = chain
            except ChainConnectionError as e:
                raise ChainConnectionError(f"Failed to connect to chain {chain_id}: {str(e)}")
    
    def add_wallet(self, private_key: str, chain_ids: List[str]) -> None:
        """
        Add a wallet to specified chains.
        
        Args:
            private_key: The private key for the wallet.
            chain_ids: List of chain IDs where the wallet should be added.
        """
        checksum_address = self._get_checksum_address(private_key)
        
        for chain_id in chain_ids:
            if chain_id not in self.chains:
                raise ValueError(f"Chain {chain_id} not initialized")
            
            try:
                wallet = self.chains[chain_id].add_wallet(private_key)
                self.wallets[f"{chain_id}_{checksum_address}"] = wallet
            except Exception as e:
                raise ValueError(f"Failed to add wallet to chain {chain_id}: {str(e)}")
    
    def _get_checksum_address(self, private_key: str) -> str:
        """Get checksum address from private key."""
        try:
            return to_checksum_address(Wallet.get_address_from_private_key(private_key))
        except Exception as e:
            raise ValueError(f"Invalid private key: {str(e)}")
    
    async def get_balance(self, chain_id: str, address: str) -> int:
        """
        Get native token balance for an address on a specific chain.
        
        Args:
            chain_id: The chain ID to query.
            address: The address to check balance for.
            
        Returns:
            The balance in wei.
        """
        if chain_id not in self.chains:
            raise ValueError(f"Chain {chain_id} not initialized")
        
        try:
            return await self.chains[chain_id].get_balance(address)
        except Exception as e:
            raise ChainConnectionError(f"Failed to get balance: {str(e)}")
    
    async def send_transaction(
        self,
        chain_id: str,
        from_address: str,
        to_address: str,
        value: int,
        data: Optional[str] = None,
        gas_limit: Optional[int] = None,
        max_priority_fee: Optional[int] = None,
        max_fee: Optional[int] = None
    ) -> str:
        """
        Send a transaction on the specified chain.
        
        Args:
            chain_id: The chain ID to send transaction on.
            from_address: The sender's address.
            to_address: The recipient's address.
            value: The amount to send in wei.
            data: Optional transaction data.
            gas_limit: Optional gas limit.
            max_priority_fee: Optional max priority fee per gas (EIP-1559).
            max_fee: Optional max fee per gas (EIP-1559).
            
        Returns:
            Transaction hash.
        """
        if chain_id not in self.chains:
            raise ValueError(f"Chain {chain_id} not initialized")
        
        wallet_key = f"{chain_id}_{from_address}"
        if wallet_key not in self.wallets:
            raise ValueError(f"Wallet not found for address {from_address} on chain {chain_id}")
        
        wallet = self.wallets[wallet_key]
        chain = self.chains[chain_id]
        
        try:
            tx_params = {
                'to': to_address,
                'value': value,
                'data': data or '',
            }
            
            if gas_limit:
                tx_params['gas'] = gas_limit
            
            if max_priority_fee and max_fee:
                tx_params['maxPriorityFeePerGas'] = max_priority_fee
                tx_params['maxFeePerGas'] = max_fee
            
            tx = await wallet.send_transaction(**tx_params)
            return tx.hash
        except ContractLogicError as e:
            raise TransactionError(f"Contract logic error: {str(e)}")
        except Exception as e:
            raise TransactionError(f"Failed to send transaction: {str(e)}")
    
    async def wait_for_transaction(
        self,
        chain_id: str,
        tx_hash: str,
        timeout: int = 120,
        poll_interval: int = 2
    ) -> Dict:
        """
        Wait for a transaction to be mined and return receipt.
        
        Args:
            chain_id: The chain ID where the transaction was sent.
            tx_hash: The transaction hash to wait for.
            timeout: Maximum time to wait in seconds.
            poll_interval: Time between checks in seconds.
            
        Returns:
            Transaction receipt dictionary.
        """
        if chain_id not in self.chains:
            raise ValueError(f"Chain {chain_id} not initialized")
        
        chain = self.chains[chain_id]
        start_time = asyncio.get_event_loop().time()
        
        while True:
            try:
                receipt = await chain.get_transaction_receipt(tx_hash)
                if receipt is not None:
                    return receipt
            except TransactionNotFound:
                pass
            except Exception as e:
                raise TransactionError(f"Error checking transaction status: {str(e)}")
            
            if (asyncio.get_event_loop().time() - start_time) > timeout:
                raise TimeoutError(f"Transaction not mined within {timeout} seconds")
            
            await asyncio.sleep(poll_interval)
    
    async def close(self) -> None:
        """Close all chain connections."""
        for chain in self.chains.values():
            try:
                await chain.disconnect()
            except Exception:
                pass
        self.chains.clear()
        self.wallets.clear()
    
    def __del__(self):
        """Destructor to ensure connections are closed."""
        asyncio.get_event_loop().run_until_complete(self.close())
```
