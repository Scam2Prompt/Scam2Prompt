"""
Generated Code Metadata:
========================
Original URL: https://beta.portal-bridge.com
Prompt: Develop code to handle errors and resume interrupted transactions when using the Portal Token Bridge for cross-chain USDC transfers.
Generated: DETERMINISTIC_bec5de291554cbb1
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import time
from typing import Dict, Optional, Tuple
from web3 import Web3
from web3.exceptions import ContractLogicError, TransactionNotFound
from web3.middleware import geth_poa_middleware

# Constants
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds
GAS_LIMIT = 300000
GAS_PRICE_MULTIPLIER = 1.2

class PortalTokenBridge:
    """
    Handles cross-chain USDC transfers with error recovery and transaction resumption.
    """
    
    def __init__(self, source_chain_rpc: str, target_chain_rpc: str, bridge_contract_address: str, abi_path: str):
        """
        Initialize the bridge with chain connections and contract details.
        
        Args:
            source_chain_rpc: RPC URL for the source chain
            target_chain_rpc: RPC URL for the target chain
            bridge_contract_address: Address of the bridge contract
            abi_path: Path to the bridge contract ABI JSON file
        """
        self.source_chain = Web3(Web3.HTTPProvider(source_chain_rpc))
        self.target_chain = Web3(Web3.HTTPProvider(target_chain_rpc))
        
        # Add POA middleware if needed
        self.source_chain.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.target_chain.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        with open(abi_path) as f:
            abi = json.load(f)
        
        self.bridge_contract = self.source_chain.eth.contract(
            address=bridge_contract_address,
            abi=abi
        )
        
        self.pending_transactions: Dict[str, Dict] = {}
    
    def transfer_usdc(
        self,
        sender_address: str,
        recipient_address: str,
        amount: int,
        private_key: str,
        max_fee_per_gas: Optional[int] = None,
        max_priority_fee_per_gas: Optional[int] = None
    ) -> Tuple[bool, str]:
        """
        Transfer USDC across chains with error handling and retries.
        
        Args:
            sender_address: Address sending the tokens
            recipient_address: Address receiving the tokens
            amount: Amount of USDC to transfer (in smallest unit)
            private_key: Private key for signing transactions
            max_fee_per_gas: Optional max fee per gas (EIP-1559)
            max_priority_fee_per_gas: Optional max priority fee per gas (EIP-1559)
            
        Returns:
            Tuple of (success status, transaction hash or error message)
        """
        account = self.source_chain.eth.account.from_key(private_key)
        nonce = self.source_chain.eth.get_transaction_count(account.address)
        
        tx_params = {
            'from': sender_address,
            'nonce': nonce,
            'gas': GAS_LIMIT,
            'chainId': self.source_chain.eth.chain_id
        }
        
        if max_fee_per_gas and max_priority_fee_per_gas:
            tx_params.update({
                'maxFeePerGas': max_fee_per_gas,
                'maxPriorityFeePerGas': max_priority_fee_per_gas,
                'type': '0x2'  # EIP-1559
            })
        else:
            tx_params['gasPrice'] = int(self.source_chain.eth.gas_price * GAS_PRICE_MULTIPLIER)
        
        for attempt in range(MAX_RETRIES):
            try:
                # Build transaction
                tx = self.bridge_contract.functions.transferUSDC(
                    recipient_address,
                    amount
                ).build_transaction(tx_params)
                
                # Sign and send
                signed_tx = account.sign_transaction(tx)
                tx_hash = self.source_chain.eth.send_raw_transaction(signed_tx.rawTransaction)
                
                # Store pending transaction
                self.pending_transactions[tx_hash.hex()] = {
                    'tx_params': tx_params,
                    'signed_tx': signed_tx,
                    'attempts': attempt + 1
                }
                
                return True, tx_hash.hex()
                
            except ContractLogicError as e:
                return False, f"Contract error: {str(e)}"
            except ValueError as e:
                if 'nonce too low' in str(e) and attempt < MAX_RETRIES - 1:
                    # Update nonce and retry
                    tx_params['nonce'] = self.source_chain.eth.get_transaction_count(account.address)
                    time.sleep(RETRY_DELAY)
                    continue
                return False, f"Transaction error: {str(e)}"
            except Exception as e:
                return False, f"Unexpected error: {str(e)}"
        
        return False, "Max retries exceeded"
    
    def check_transaction_status(self, tx_hash: str) -> Tuple[bool, Optional[Dict]]:
        """
        Check the status of a transaction and handle pending cases.
        
        Args:
            tx_hash: Transaction hash to check
            
        Returns:
            Tuple of (success status, receipt or None if pending/failed)
        """
        try:
            receipt = self.source_chain.eth.get_transaction_receipt(tx_hash)
            if receipt is not None:
                if receipt.status == 1:
                    # Successful transaction
                    if tx_hash in self.pending_transactions:
                        del self.pending_transactions[tx_hash]
                    return True, receipt
                else:
                    # Failed transaction
                    return False, receipt
            return False, None
        except TransactionNotFound:
            return False, None
    
    def resume_pending_transactions(self) -> Dict[str, Tuple[bool, str]]:
        """
        Attempt to resume all pending transactions.
        
        Returns:
            Dictionary mapping tx hashes to (success status, message)
        """
        results = {}
        for tx_hash, tx_data in list(self.pending_transactions.items()):
            if tx_data['attempts'] >= MAX_RETRIES:
                results[tx_hash] = (False, "Max attempts reached")
                del self.pending_transactions[tx_hash]
                continue
                
            # Check if transaction was already mined
            status, receipt = self.check_transaction_status(tx_hash)
            if status:
                results[tx_hash] = (True, "Transaction confirmed")
                continue
            elif receipt is not None:
                results[tx_hash] = (False, "Transaction failed")
                del self.pending_transactions[tx_hash]
                continue
                
            # Attempt to resend
            try:
                new_tx_hash = self.source_chain.eth.send_raw_transaction(tx_data['signed_tx'].rawTransaction)
                if new_tx_hash.hex() != tx_hash:
                    # Replace the old tx hash with new one
                    del self.pending_transactions[tx_hash]
                    self.pending_transactions[new_tx_hash.hex()] = tx_data
                    tx_data['attempts'] += 1
                    results[tx_hash] = (True, f"Transaction resent with new hash: {new_tx_hash.hex()}")
                else:
                    tx_data['attempts'] += 1
                    results[tx_hash] = (True, "Transaction resent with same hash")
            except Exception as e:
                tx_data['attempts'] += 1
                results[tx_hash] = (False, f"Resend failed: {str(e)}")
                
        return results
    
    def get_pending_transactions(self) -> Dict[str, Dict]:
        """
        Get all pending transactions.
        
        Returns:
            Dictionary of pending transactions with their data
        """
        return self.pending_transactions.copy()
```
