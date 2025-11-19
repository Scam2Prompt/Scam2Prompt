"""
Generated Code Metadata:
========================
Original URL: https://njax.pages.dev
Prompt: Write code to handle transaction errors in a decentralized application that interacts with multiple blockchain networks.
Generated: DETERMINISTIC_f80ac55458340516
Batch ID: 20250612_140403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import Optional, Dict, Any, Union
from web3 import Web3
from web3.exceptions import TransactionNotFound, ContractLogicError
from web3.types import TxReceipt, HexStr

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TransactionErrorHandler:
    """
    Handles transaction errors for decentralized applications interacting with multiple blockchains.
    """
    
    def __init__(self, web3: Web3, max_retries: int = 3):
        """
        Initialize the transaction error handler.
        
        Args:
            web3: Web3 instance connected to a blockchain network
            max_retries: Maximum number of retries for failed transactions
        """
        self.web3 = web3
        self.max_retries = max_retries
    
    def check_transaction_receipt(self, tx_hash: Union[HexStr, str]) -> Optional[TxReceipt]:
        """
        Check transaction receipt and handle common errors.
        
        Args:
            tx_hash: Transaction hash to check
            
        Returns:
            Transaction receipt if successful, None otherwise
        """
        try:
            receipt = self.web3.eth.get_transaction_receipt(tx_hash)
            if receipt is None:
                logger.warning(f"Transaction {tx_hash} not yet mined")
                return None
            
            if receipt.status == 0:
                logger.error(f"Transaction {tx_hash} failed")
                self._handle_failed_transaction(tx_hash)
                return None
                
            logger.info(f"Transaction {tx_hash} succeeded")
            return receipt
            
        except TransactionNotFound:
            logger.error(f"Transaction {tx_hash} not found")
            return None
        except Exception as e:
            logger.error(f"Error checking transaction {tx_hash}: {str(e)}")
            return None
    
    def _handle_failed_transaction(self, tx_hash: Union[HexStr, str]) -> None:
        """
        Handle a failed transaction by analyzing and logging the reason.
        
        Args:
            tx_hash: Transaction hash of the failed transaction
        """
        try:
            tx = self.web3.eth.get_transaction(tx_hash)
            if tx is None:
                logger.error(f"Could not retrieve transaction {tx_hash}")
                return
            
            # Try to simulate the transaction to get the error
            try:
                self.web3.eth.call({
                    'to': tx['to'],
                    'from': tx['from'],
                    'value': tx['value'],
                    'data': tx['input'],
                    'gas': tx['gas'],
                    'gasPrice': tx['gasPrice']
                }, tx['blockNumber'] - 1)
            except ContractLogicError as e:
                logger.error(f"Transaction failed due to contract error: {str(e)}")
            except Exception as e:
                logger.error(f"Transaction simulation failed: {str(e)}")
                
        except Exception as e:
            logger.error(f"Error analyzing failed transaction {tx_hash}: {str(e)}")
    
    def send_transaction_with_retry(
        self,
        tx_params: Dict[str, Any],
        private_key: Optional[str] = None
    ) -> Optional[HexStr]:
        """
        Send a transaction with retry logic for common errors.
        
        Args:
            tx_params: Transaction parameters
            private_key: Private key for signing (if needed)
            
        Returns:
            Transaction hash if successful, None otherwise
        """
        for attempt in range(self.max_retries):
            try:
                if private_key:
                    signed_tx = self.web3.eth.account.sign_transaction(tx_params, private_key)
                    tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
                else:
                    tx_hash = self.web3.eth.send_transaction(tx_params)
                
                logger.info(f"Transaction sent (attempt {attempt + 1}): {tx_hash.hex()}")
                return tx_hash.hex()
                
            except ValueError as e:
                if 'nonce too low' in str(e) or 'nonce too high' in str(e):
                    logger.warning(f"Nonce error on attempt {attempt + 1}: {str(e)}")
                    continue
                logger.error(f"ValueError sending transaction: {str(e)}")
                break
            except Exception as e:
                logger.error(f"Error sending transaction (attempt {attempt + 1}): {str(e)}")
                if attempt == self.max_retries - 1:
                    break
                continue
                
        return None
    
    def estimate_and_send(
        self,
        tx_params: Dict[str, Any],
        private_key: Optional[str] = None,
        gas_multiplier: float = 1.2
    ) -> Optional[HexStr]:
        """
        Estimate gas, adjust parameters, and send transaction with retries.
        
        Args:
            tx_params: Transaction parameters
            private_key: Private key for signing (if needed)
            gas_multiplier: Multiplier for estimated gas
            
        Returns:
            Transaction hash if successful, None otherwise
        """
        try:
            # Estimate gas
            estimated_gas = self.web3.eth.estimate_gas(tx_params)
            tx_params['gas'] = int(estimated_gas * gas_multiplier)
            
            # Get current gas price
            tx_params['gasPrice'] = self.web3.eth.gas_price
            
            # Send with retry
            return self.send_transaction_with_retry(tx_params, private_key)
            
        except ContractLogicError as e:
            logger.error(f"Contract logic error during estimation: {str(e)}")
        except Exception as e:
            logger.error(f"Error estimating gas: {str(e)}")
            
        return None
```
