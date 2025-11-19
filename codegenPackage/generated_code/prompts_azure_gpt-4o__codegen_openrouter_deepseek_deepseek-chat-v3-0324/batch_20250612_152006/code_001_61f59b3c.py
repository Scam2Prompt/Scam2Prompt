"""
Generated Code Metadata:
========================
Original URL: https://axondao.gitbook.io
Prompt: Generate Python code to interact with the AXGT token contract on the Ethereum blockchain, focusing on querying token utilities and performing token burns as outlined by AxonDAO.
Generated: DETERMINISTIC_61f59b3c3879c32a
Batch ID: 20250612_152006
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_KEY": {
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
from web3.middleware import geth_poa_middleware
from typing import Optional, Dict, Any

# Configuration class to hold contract and network settings
class AXGTConfig:
    def __init__(
        self,
        rpc_url: str,
        contract_address: str,
        abi_path: str,
        chain_id: int,
        gas_limit: int = 200000,
        gas_price: Optional[int] = None,
    ):
        self.rpc_url = rpc_url
        self.contract_address = contract_address
        self.abi_path = abi_path
        self.chain_id = chain_id
        self.gas_limit = gas_limit
        self.gas_price = gas_price

# Main AXGT token interaction class
class AXGTToken:
    def __init__(self, config: AXGTConfig):
        self.config = config
        self.w3 = Web3(Web3.HTTPProvider(config.rpc_url))
        
        # Inject POA middleware if needed (for networks like Polygon, BSC, etc.)
        if 'poa' in config.rpc_url.lower():
            self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        # Load contract ABI
        with open(config.abi_path) as f:
            self.abi = json.load(f)
        
        self.contract = self.w3.eth.contract(
            address=Web3.to_checksum_address(config.contract_address),
            abi=self.abi
        )
    
    def get_token_name(self) -> str:
        """Query the token name from the contract."""
        return self.contract.functions.name().call()
    
    def get_token_symbol(self) -> str:
        """Query the token symbol from the contract."""
        return self.contract.functions.symbol().call()
    
    def get_token_decimals(self) -> int:
        """Query the token decimals from the contract."""
        return self.contract.functions.decimals().call()
    
    def get_total_supply(self) -> int:
        """Query the total token supply from the contract."""
        return self.contract.functions.totalSupply().call()
    
    def get_balance(self, address: str) -> int:
        """Query the token balance of a given address."""
        return self.contract.functions.balanceOf(
            Web3.to_checksum_address(address)
        ).call()
    
    def get_token_utilities(self) -> Dict[str, Any]:
        """Query the token utilities as defined by AxonDAO."""
        # This assumes the contract has a getUtilities() function
        # Adjust according to actual contract implementation
        try:
            utilities = self.contract.functions.getUtilities().call()
            return {
                'governance': utilities[0],
                'staking': utilities[1],
                'fee_discounts': utilities[2],
                'other_utilities': utilities[3:]
            }
        except Exception as e:
            raise Exception(f"Failed to query token utilities: {str(e)}")
    
    def burn_tokens(
        self,
        private_key: str,
        amount: int,
        gas_price: Optional[int] = None
    ) -> str:
        """
        Burn a specified amount of tokens.
        
        Args:
            private_key: The private key of the account initiating the burn
            amount: The amount of tokens to burn (in smallest unit)
            gas_price: Optional gas price to use (will use default if None)
        
        Returns:
            Transaction hash of the burn transaction
        """
        try:
            account = self.w3.eth.account.from_key(private_key)
            sender_address = account.address
            
            # Build transaction
            tx = self.contract.functions.burn(amount).build_transaction({
                'chainId': self.config.chain_id,
                'gas': self.config.gas_limit,
                'gasPrice': gas_price if gas_price else self.w3.eth.gas_price,
                'nonce': self.w3.eth.get_transaction_count(sender_address),
            })
            
            # Sign and send transaction
            signed_tx = self.w3.eth.account.sign_transaction(tx, private_key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            return tx_hash.hex()
        
        except Exception as e:
            raise Exception(f"Token burn failed: {str(e)}")
    
    def get_transaction_receipt(self, tx_hash: str) -> Dict[str, Any]:
        """Get the transaction receipt for a given transaction hash."""
        try:
            return dict(self.w3.eth.get_transaction_receipt(tx_hash))
        except Exception as e:
            raise Exception(f"Failed to get transaction receipt: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Configuration - replace with actual values
    config = AXGTConfig(
        rpc_url="https://mainnet.infura.io/v3/YOUR_INFURA_KEY",
        contract_address="0xYOUR_CONTRACT_ADDRESS",
        abi_path="path/to/axgt_abi.json",
        chain_id=1,  # Mainnet
        gas_limit=200000,
    )
    
    axgt = AXGTToken(config)
    
    # Query token info
    print(f"Token Name: {axgt.get_token_name()}")
    print(f"Token Symbol: {axgt.get_token_symbol()}")
    print(f"Total Supply: {axgt.get_total_supply()}")
    
    # Query utilities
    try:
        utilities = axgt.get_token_utilities()
        print("Token Utilities:", utilities)
    except Exception as e:
        print(f"Error querying utilities: {e}")
    
    # Example burn (commented out for safety)
    # private_key = "YOUR_PRIVATE_KEY"  # Never hardcode in production!
    # amount = 1000000000000000000  # 1 token (assuming 18 decimals)
    # try:
    #     tx_hash = axgt.burn_tokens(private_key, amount)
    #     print(f"Burn transaction sent. Hash: {tx_hash}")
    #     receipt = axgt.get_transaction_receipt(tx_hash)
    #     print("Transaction receipt:", receipt)
    # except Exception as e:
    #     print(f"Burn failed: {e}")
```
