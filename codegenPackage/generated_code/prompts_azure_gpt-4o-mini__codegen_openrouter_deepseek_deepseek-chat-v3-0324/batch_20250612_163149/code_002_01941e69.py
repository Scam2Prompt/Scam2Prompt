"""
Generated Code Metadata:
========================
Original URL: https://quecko.com
Prompt: Create a simple decentralized exchange (DEX) using the interoperability solutions provided by Quecko for cross-chain transactions.
Generated: DETERMINISTIC_01941e699cd72032
Batch ID: 20250612_163149
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://polygon-rpc.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://gateway.quecko.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

Here's a simple decentralized exchange (DEX) implementation using Python and Quecko's interoperability solutions. This is a simplified example demonstrating cross-chain token swaps:

```python
import requests
from typing import Dict, Optional
from dataclasses import dataclass
from web3 import Web3
from web3.middleware import geth_poa_middleware

@dataclass
class ChainConfig:
    rpc_url: str
    chain_id: int
    quecko_gateway: str
    dex_contract_address: str
    abi: list

class QueckoDEX:
    def __init__(self, chain_configs: Dict[str, ChainConfig], private_key: str):
        """
        Initialize the DEX with chain configurations.
        
        Args:
            chain_configs: Dictionary of chain name to ChainConfig
            private_key: Private key for signing transactions
        """
        self.chains = chain_configs
        self.private_key = private_key
        self.w3_instances = {}
        
        # Initialize Web3 instances for each chain
        for chain_name, config in chain_configs.items():
            w3 = Web3(Web3.HTTPProvider(config.rpc_url))
            if 'poa' in chain_name.lower():
                w3.middleware_onion.inject(geth_poa_middleware, layer=0)
            self.w3_instances[chain_name] = w3
            
        # Validate all chains are connected
        for chain_name, w3 in self.w3_instances.items():
            if not w3.is_connected():
                raise ConnectionError(f"Failed to connect to {chain_name} chain")

    def _get_account(self):
        """Retrieve the account from the private key."""
        return self.w3_instances[next(iter(self.w3_instances))].eth.account.from_key(self.private_key)

    def _get_contract(self, chain_name: str):
        """Get the DEX contract for a specific chain."""
        w3 = self.w3_instances[chain_name]
        return w3.eth.contract(
            address=self.chains[chain_name].dex_contract_address,
            abi=self.chains[chain_name].abi
        )

    def _build_cross_chain_tx(self, src_chain: str, dst_chain: str, amount: int, token: str):
        """
        Build a cross-chain transaction payload for Quecko Gateway.
        
        Args:
            src_chain: Source chain name
            dst_chain: Destination chain name
            amount: Amount of tokens to swap
            token: Token symbol to swap
            
        Returns:
            Transaction hash of the cross-chain operation
        """
        endpoint = f"{self.chains[src_chain].quecko_gateway}/api/v1/crosschain/transfer"
        payload = {
            "sourceChainId": self.chains[src_chain].chain_id,
            "destChainId": self.chains[dst_chain].chain_id,
            "token": token,
            "amount": str(amount),
            "sender": self._get_account().address,
            "recipient": self._get_account().address
        }
        
        response = requests.post(endpoint, json=payload)
        if response.status_code != 200:
            raise Exception(f"Quecko gateway error: {response.text}")
        
        return response.json()['txHash']

    def swap_tokens(
        self,
        src_chain: str,
        dst_chain: str,
        token_in: str,
        token_out: str,
        amount_in: int,
        slippage: float = 0.5,
        deadline: int = 20 * 60  # 20 minutes
    ):
        """
        Execute a cross-chain token swap.
        
        Args:
            src_chain: Source chain name
            dst_chain: Destination chain name
            token_in: Input token symbol
            token_out: Output token symbol
            amount_in: Amount of input token
            slippage: Maximum slippage percentage (0.5 for 0.5%)
            deadline: Transaction deadline in seconds
            
        Returns:
            Tuple of (source chain tx hash, destination chain tx hash)
        """
        # Validate chains
        if src_chain not in self.chains or dst_chain not in self.chains:
            raise ValueError("Invalid chain name")
            
        # Get contracts and account
        src_contract = self._get_contract(src_chain)
        dst_contract = self._get_contract(dst_chain)
        account = self._get_account()
        
        # Approve token transfer
        approve_tx = src_contract.functions.approve(
            self.chains[src_chain].dex_contract_address,
            amount_in
        ).build_transaction({
            'from': account.address,
            'nonce': self.w3_instances[src_chain].eth.get_transaction_count(account.address),
            'gasPrice': self.w3_instances[src_chain].eth.gas_price,
        })
        
        signed_approve = account.sign_transaction(approve_tx)
        approve_tx_hash = self.w3_instances[src_chain].eth.send_raw_transaction(signed_approve.rawTransaction)
        
        # Wait for approval to complete
        self.w3_instances[src_chain].eth.wait_for_transaction_receipt(approve_tx_hash)
        
        # Initiate cross-chain swap via Quecko
        quecko_tx_hash = self._build_cross_chain_tx(src_chain, dst_chain, amount_in, token_in)
        
        # Build destination chain transaction
        swap_tx = dst_contract.functions.swap(
            token_in,
            token_out,
            amount_in,
            int(amount_in * (100 - slippage) / 100),  # min amount out
            account.address,
            deadline
        ).build_transaction({
            'from': account.address,
            'nonce': self.w3_instances[dst_chain].eth.get_transaction_count(account.address),
            'gasPrice': self.w3_instances[dst_chain].eth.gas_price,
        })
        
        signed_swap = account.sign_transaction(swap_tx)
        swap_tx_hash = self.w3_instances[dst_chain].eth.send_raw_transaction(signed_swap.rawTransaction)
        
        return (approve_tx_hash.hex(), quecko_tx_hash, swap_tx_hash.hex())

    def get_balances(self, chains: list, tokens: list) -> Dict[str, Dict[str, int]]:
        """
        Get token balances across multiple chains.
        
        Args:
            chains: List of chain names
            tokens: List of token symbols
            
        Returns:
            Dictionary of chain -> token -> balance
        """
        balances = {}
        account = self._get_account()
        
        for chain in chains:
            if chain not in self.chains:
                continue
                
            balances[chain] = {}
            contract = self._get_contract(chain)
            
            for token in tokens:
                try:
                    balance = contract.functions.balanceOf(account.address, token).call()
                    balances[chain][token] = balance
                except Exception as e:
                    print(f"Error getting balance for {token} on {chain}: {str(e)}")
                    balances[chain][token] = None
                    
        return balances

# Example usage
if __name__ == "__main__":
    # Mock chain configurations (replace with actual values)
    CHAIN_CONFIGS = {
        "Ethereum": ChainConfig(
            rpc_url="https://mainnet.infura.io/v3/YOUR_PROJECT_ID",
            chain_id=1,
            quecko_gateway="https://gateway.quecko.io",
            dex_contract_address="0x...",
            abi=[...]  # actual ABI would go here
        ),
        "Polygon": ChainConfig(
            rpc_url="https://polygon-rpc.com",
            chain_id=137,
            quecko_gateway="https://gateway.quecko.io",
            dex_contract_address="0x...",
            abi=[...]  # actual ABI would go here
        )
    }
    
    # Initialize DEX (in production, use env variables for private key)
    dex = QueckoDEX(CHAIN_CONFIGS, "YOUR_PRIVATE_KEY")
    
    # Get balances
    balances = dex.get_balances(["Ethereum", "Polygon"], ["ETH", "MATIC", "USDC"])
    print("Balances:", balances)
    
    # Execute a cross-chain swap
    try:
        tx_hashes = dex.swap_tokens(
            src_chain="Ethereum",
            dst_chain="Polygon",
            token_in="ETH",
            token_out="MATIC",
            amount_in=Web3.to_wei(1, 'ether')
        )
        print("Transaction hashes:", tx_hashes)
    except Exception as e:
        print(f"Swap failed: {str(e)}")
```
