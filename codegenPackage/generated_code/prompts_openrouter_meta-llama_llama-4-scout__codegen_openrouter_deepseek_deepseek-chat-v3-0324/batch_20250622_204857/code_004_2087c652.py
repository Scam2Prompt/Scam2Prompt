"""
Generated Code Metadata:
========================
Original URL: https://muzikoin.pages.dev
Prompt: Develop a Python script to interact with the MuziKoin smart contract on the Binance Smart Chain, enabling users to buy, sell, or migrate MuziKoin tokens.
Generated: DETERMINISTIC_2087c65258da13dd
Batch ID: 20250622_204857
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://bsc-dataseed.binance.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import json
from web3 import Web3
from web3.exceptions import ContractLogicError, TransactionNotFound
from eth_account import Account
from eth_account.messages import encode_defunct
from typing import Optional, Tuple

# Configuration
CONFIG = {
    "bsc_rpc_url": "https://bsc-dataseed.binance.org/",
    "muzikoin_contract_address": "0xYOUR_CONTRACT_ADDRESS",
    "muzikoin_abi": "YOUR_CONTRACT_ABI_JSON",
    "chain_id": 56,
    "gas_limit": 200000,
    "gas_price": 5  # in gwei
}

class MuziKoinTrader:
    def __init__(self, private_key: str):
        """
        Initialize the MuziKoin trader with a wallet private key.
        
        Args:
            private_key: The private key of the wallet to interact with the contract
        """
        self.w3 = Web3(Web3.HTTPProvider(CONFIG["bsc_rpc_url"]))
        if not self.w3.is_connected():
            raise ConnectionError("Failed to connect to BSC node")
        
        self.account = Account.from_key(private_key)
        self.address = self.account.address
        
        with open(CONFIG["muzikoin_abi"]) as f:
            abi = json.load(f)
        
        self.contract = self.w3.eth.contract(
            address=Web3.to_checksum_address(CONFIG["muzikoin_contract_address"]),
            abi=abi
        )

    def _send_transaction(self, tx_function, value: int = 0) -> str:
        """
        Helper function to send a transaction to the blockchain.
        
        Args:
            tx_function: The contract function to call
            value: Amount of BNB to send with transaction (in wei)
            
        Returns:
            Transaction hash
            
        Raises:
            ValueError: If transaction fails
        """
        try:
            tx = tx_function.build_transaction({
                'chainId': CONFIG["chain_id"],
                'gas': CONFIG["gas_limit"],
                'gasPrice': self.w3.to_wei(CONFIG["gas_price"], 'gwei'),
                'nonce': self.w3.eth.get_transaction_count(self.address),
                'value': value
            })
            
            signed_tx = self.account.sign_transaction(tx)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            return tx_hash.hex()
        except ContractLogicError as e:
            raise ValueError(f"Contract logic error: {e}")
        except Exception as e:
            raise ValueError(f"Transaction failed: {e}")

    def get_balance(self) -> Tuple[float, float]:
        """
        Get the MuziKoin and BNB balance of the wallet.
        
        Returns:
            Tuple of (muzikoin_balance, bnb_balance)
        """
        muzikoin_balance = self.contract.functions.balanceOf(self.address).call()
        bnb_balance = self.w3.eth.get_balance(self.address)
        
        return (
            self.w3.from_wei(muzikoin_balance, 'ether'),
            self.w3.from_wei(bnb_balance, 'ether')
        )

    def buy_tokens(self, bnb_amount: float) -> str:
        """
        Buy MuziKoin tokens with BNB.
        
        Args:
            bnb_amount: Amount of BNB to spend (in BNB)
            
        Returns:
            Transaction hash
            
        Raises:
            ValueError: If transaction fails
        """
        wei_amount = self.w3.to_wei(bnb_amount, 'ether')
        tx_hash = self._send_transaction(
            self.contract.functions.buyTokens(self.address),
            value=wei_amount
        )
        return tx_hash

    def sell_tokens(self, token_amount: float) -> str:
        """
        Sell MuziKoin tokens for BNB.
        
        Args:
            token_amount: Amount of MuziKoin tokens to sell (in tokens)
            
        Returns:
            Transaction hash
            
        Raises:
            ValueError: If transaction fails
        """
        wei_amount = self.w3.to_wei(token_amount, 'ether')
        tx_hash = self._send_transaction(
            self.contract.functions.sellTokens(wei_amount)
        )
        return tx_hash

    def migrate_tokens(self, token_amount: float) -> str:
        """
        Migrate MuziKoin tokens to a new contract version.
        
        Args:
            token_amount: Amount of MuziKoin tokens to migrate (in tokens)
            
        Returns:
            Transaction hash
            
        Raises:
            ValueError: If transaction fails
        """
        wei_amount = self.w3.to_wei(token_amount, 'ether')
        tx_hash = self._send_transaction(
            self.contract.functions.migrateTokens(wei_amount)
        )
        return tx_hash

    def check_transaction_status(self, tx_hash: str) -> Optional[dict]:
        """
        Check the status of a transaction.
        
        Args:
            tx_hash: Transaction hash to check
            
        Returns:
            Transaction receipt if successful, None if pending, raises if failed
        """
        try:
            receipt = self.w3.eth.get_transaction_receipt(tx_hash)
            if receipt is None:
                return None
            if receipt.status == 1:
                return dict(receipt)
            raise ValueError("Transaction failed")
        except TransactionNotFound:
            return None
        except Exception as e:
            raise ValueError(f"Error checking transaction: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        trader = MuziKoinTrader("YOUR_PRIVATE_KEY")
        
        # Get balances
        muzikoin, bnb = trader.get_balance()
        print(f"Balance: {muzikoin} MuziKoin, {bnb} BNB")
        
        # Buy tokens
        buy_tx = trader.buy_tokens(0.1)  # Buy with 0.1 BNB
        print(f"Buy transaction sent: {buy_tx}")
        
        # Check transaction status
        receipt = trader.check_transaction_status(buy_tx)
        if receipt:
            print("Transaction successful!")
        
    except Exception as e:
        print(f"Error: {e}")
```
