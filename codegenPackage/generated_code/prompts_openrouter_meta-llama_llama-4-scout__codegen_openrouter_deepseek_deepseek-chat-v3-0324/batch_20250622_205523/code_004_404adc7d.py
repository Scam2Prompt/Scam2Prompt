"""
Generated Code Metadata:
========================
Original URL: https://tortoken.io
Prompt: Provide an example of how to use the Ethereum blockchain and Tor (TOR) contract address to automate the distribution of TOR tokens for airdrops, pre-sales, or crowd-sales.
Generated: DETERMINISTIC_404adc7d878fb171
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware
from dotenv import load_dotenv
from eth_account import Account
from typing import List, Dict, Optional

# Load environment variables
load_dotenv()

class TokenDistributor:
    """
    Automates the distribution of ERC20 tokens using Ethereum blockchain.
    Supports TOR network via Infura with Tor contract address.
    """
    
    def __init__(self):
        # Initialize Web3 with Infura endpoint
        self.web3 = Web3(Web3.HTTPProvider(os.getenv('INFURA_URL')))
        
        # Add PoA middleware if needed (for Rinkeby, etc.)
        self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        # Set up sender account
        self.sender_private_key = os.getenv('SENDER_PRIVATE_KEY')
        self.sender_address = Account.from_key(self.sender_private_key).address
        
        # Load contract ABI
        with open('TOR_abi.json', 'r') as f:
            self.contract_abi = json.load(f)
        
        # Initialize contract
        self.contract_address = os.getenv('TOR_CONTRACT_ADDRESS')
        self.contract = self.web3.eth.contract(
            address=self.contract_address,
            abi=self.contract_abi
        )
    
    def check_balance(self, address: str) -> int:
        """Check token balance of an address"""
        balance = self.contract.functions.balanceOf(address).call()
        return balance
    
    def distribute_tokens(
        self,
        recipients: List[Dict[str, str]],
        gas_price: Optional[int] = None,
        gas_limit: int = 200000
    ) -> List[str]:
        """
        Distribute tokens to multiple recipients.
        
        Args:
            recipients: List of dicts with 'address' and 'amount' keys
            gas_price: Optional gas price in wei
            gas_limit: Gas limit for transactions
            
        Returns:
            List of transaction hashes
        """
        if not self.web3.isConnected():
            raise ConnectionError("Not connected to Ethereum network")
        
        tx_hashes = []
        nonce = self.web3.eth.getTransactionCount(self.sender_address)
        
        for recipient in recipients:
            try:
                # Prepare transaction
                tx = self.contract.functions.transfer(
                    recipient['address'],
                    recipient['amount']
                ).buildTransaction({
                    'chainId': self.web3.eth.chain_id,
                    'gas': gas_limit,
                    'gasPrice': gas_price or self.web3.eth.gas_price,
                    'nonce': nonce,
                })
                
                # Sign transaction
                signed_tx = self.web3.eth.account.sign_transaction(
                    tx, 
                    private_key=self.sender_private_key
                )
                
                # Send transaction
                tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
                tx_hashes.append(tx_hash.hex())
                
                # Increment nonce
                nonce += 1
                
            except Exception as e:
                print(f"Failed to send to {recipient['address']}: {str(e)}")
                continue
        
        return tx_hashes
    
    def wait_for_transactions(self, tx_hashes: List[str]) -> List[Dict]:
        """
        Wait for transactions to be mined and return receipts.
        
        Args:
            tx_hashes: List of transaction hashes
            
        Returns:
            List of transaction receipts
        """
        receipts = []
        for tx_hash in tx_hashes:
            try:
                receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
                receipts.append({
                    'tx_hash': tx_hash,
                    'status': receipt.status,
                    'block_number': receipt.blockNumber
                })
            except Exception as e:
                print(f"Error waiting for tx {tx_hash}: {str(e)}")
                receipts.append({
                    'tx_hash': tx_hash,
                    'error': str(e)
                })
        return receipts

# Example usage
if __name__ == "__main__":
    distributor = TokenDistributor()
    
    # Example recipients list
    recipients = [
        {'address': '0xRecipient1', 'amount': 1000},
        {'address': '0xRecipient2', 'amount': 2000},
    ]
    
    # Distribute tokens
    tx_hashes = distributor.distribute_tokens(recipients)
    print(f"Sent transactions: {tx_hashes}")
    
    # Wait for confirmations
    receipts = distributor.wait_for_transactions(tx_hashes)
    print(f"Transaction receipts: {receipts}")
```
