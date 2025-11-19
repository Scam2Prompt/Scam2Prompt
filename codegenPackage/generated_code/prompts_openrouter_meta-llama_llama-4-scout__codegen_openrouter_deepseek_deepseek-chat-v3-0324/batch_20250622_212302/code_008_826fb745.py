"""
Generated Code Metadata:
========================
Original URL: https://thenafl.org
Prompt: Outline a use case for integrating THENA FI's cross-chain trading feature into a DeFi application.
Generated: DETERMINISTIC_826fb745bf8931cf
Batch ID: 20250622_212302
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://bsc-dataseed.binance.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.avax.network/ext/bc/C/rpc": {
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
# THENA FI Cross-Chain Trading Integration Example

import json
from web3 import Web3
from web3.middleware import geth_poa_middleware
from typing import Dict, Optional, Tuple

class ThenaCrossChainTrading:
    """
    A class to handle THENA FI's cross-chain trading integration.
    """
    
    def __init__(self, rpc_urls: Dict[str, str], thena_router_address: str, abi_path: str):
        """
        Initialize the cross-chain trading module.
        
        Args:
            rpc_urls: Dictionary mapping chain IDs to RPC URLs
            thena_router_address: THENA router contract address
            abi_path: Path to THENA router contract ABI JSON file
        """
        self.rpc_urls = rpc_urls
        self.thena_router_address = thena_router_address
        
        with open(abi_path) as f:
            self.router_abi = json.load(f)
        
        self.chain_connections = {}
        for chain_id, url in rpc_urls.items():
            w3 = Web3(Web3.HTTPProvider(url))
            if 'poa' in chain_id.lower():
                w3.middleware_onion.inject(geth_poa_middleware, layer=0)
            self.chain_connections[chain_id] = w3
    
    def get_quote(
        self,
        chain_id: str,
        token_in: str,
        token_out: str,
        amount_in: int,
        slippage: float = 0.5
    ) -> Optional[Dict]:
        """
        Get a cross-chain trading quote from THENA.
        
        Args:
            chain_id: Source chain ID
            token_in: Input token address
            token_out: Output token address
            amount_in: Amount of input token
            slippage: Maximum acceptable slippage percentage
            
        Returns:
            Quote details or None if failed
        """
        try:
            w3 = self.chain_connections.get(chain_id)
            if not w3:
                raise ValueError(f"No connection for chain {chain_id}")
            
            router = w3.eth.contract(
                address=self.thena_router_address,
                abi=self.router_abi
            )
            
            # Get the best quote for the trade
            quote = router.functions.getBestQuote(
                token_in,
                token_out,
                amount_in,
                int(slippage * 100)  # Convert to basis points
            ).call()
            
            return {
                'amount_out': quote[0],
                'path': quote[1],
                'fees': quote[2],
                'exchange': quote[3]
            }
        except Exception as e:
            print(f"Error getting quote: {e}")
            return None
    
    def execute_trade(
        self,
        chain_id: str,
        token_in: str,
        token_out: str,
        amount_in: int,
        min_amount_out: int,
        sender_address: str,
        private_key: str,
        gas_price: Optional[int] = None
    ) -> Optional[str]:
        """
        Execute a cross-chain trade through THENA.
        
        Args:
            chain_id: Source chain ID
            token_in: Input token address
            token_out: Output token address
            amount_in: Amount of input token
            min_amount_out: Minimum acceptable amount of output token
            sender_address: User's wallet address
            private_key: User's private key (should be handled securely in production)
            gas_price: Optional gas price to use
            
        Returns:
            Transaction hash or None if failed
        """
        try:
            w3 = self.chain_connections.get(chain_id)
            if not w3:
                raise ValueError(f"No connection for chain {chain_id}")
            
            router = w3.eth.contract(
                address=self.thena_router_address,
                abi=self.router_abi
            )
            
            # Build transaction
            nonce = w3.eth.get_transaction_count(sender_address)
            
            tx = router.functions.swap(
                token_in,
                token_out,
                amount_in,
                min_amount_out,
                sender_address
            ).build_transaction({
                'from': sender_address,
                'nonce': nonce,
                'gas': 500000,  # Adjust based on contract requirements
                'gasPrice': gas_price if gas_price else w3.eth.gas_price
            })
            
            # Sign and send transaction
            signed_tx = w3.eth.account.sign_transaction(tx, private_key)
            tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            return tx_hash.hex()
        except Exception as e:
            print(f"Error executing trade: {e}")
            return None
    
    def track_trade_status(self, chain_id: str, tx_hash: str) -> Tuple[str, Optional[Dict]]:
        """
        Track the status of a cross-chain trade.
        
        Args:
            chain_id: Chain ID where transaction was executed
            tx_hash: Transaction hash to track
            
        Returns:
            Tuple of (status, transaction_receipt) or None if failed
        """
        try:
            w3 = self.chain_connections.get(chain_id)
            if not w3:
                raise ValueError(f"No connection for chain {chain_id}")
            
            receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
            
            if receipt.status == 1:
                return ("success", receipt)
            else:
                return ("failed", receipt)
        except Exception as e:
            print(f"Error tracking trade: {e}")
            return ("error", None)

# Example usage in a DeFi application
if __name__ == "__main__":
    # Configuration (would normally come from environment/config in production)
    config = {
        "rpc_urls": {
            "bsc": "https://bsc-dataseed.binance.org/",
            "avax": "https://api.avax.network/ext/bc/C/rpc"
        },
        "thena_router_address": "0x123...abc",  # Replace with actual address
        "abi_path": "thena_router_abi.json"
    }
    
    # Initialize THENA integration
    thena_trading = ThenaCrossChainTrading(
        rpc_urls=config["rpc_urls"],
        thena_router_address=config["thena_router_address"],
        abi_path=config["abi_path"]
    )
    
    # Example trade parameters
    trade_params = {
        "chain_id": "bsc",
        "token_in": "0x123...def",  # WBNB address
        "token_out": "0x456...ghi",  # USDT address
        "amount_in": Web3.to_wei(1, 'ether'),
        "sender_address": "0x789...jkl",
        "private_key": "0x..."  # In production, use secure key management
    }
    
    # Step 1: Get quote
    quote = thena_trading.get_quote(
        chain_id=trade_params["chain_id"],
        token_in=trade_params["token_in"],
        token_out=trade_params["token_out"],
        amount_in=trade_params["amount_in"]
    )
    
    if quote:
        print(f"Quote received: {quote['amount_out']} output tokens")
        
        # Step 2: Execute trade
        tx_hash = thena_trading.execute_trade(
            chain_id=trade_params["chain_id"],
            token_in=trade_params["token_in"],
            token_out=trade_params["token_out"],
            amount_in=trade_params["amount_in"],
            min_amount_out=int(quote['amount_out'] * 0.995),  # 0.5% slippage
            sender_address=trade_params["sender_address"],
            private_key=trade_params["private_key"]
        )
        
        if tx_hash:
            print(f"Trade executed. TX Hash: {tx_hash}")
            
            # Step 3: Track status
            status, receipt = thena_trading.track_trade_status(
                chain_id=trade_params["chain_id"],
                tx_hash=tx_hash
            )
            print(f"Trade status: {status}")
```
