"""
Generated Code Metadata:
========================
Original URL: https://nbnm.pages.dev
Prompt: Develop a proposal for an app that qualifies as a Sonic Native application, including the creation of a new token and use cases that drive user adoption within the Sonic network.
Generated: DETERMINISTIC_ff48a82e3cd617f8
Batch ID: 20250612_155032
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Sonic Native Application Proposal: "SonicSwap" - A Decentralized Exchange (DEX) on Sonic Network

from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, List, Dict
import hashlib
import json
from datetime import datetime

class TokenStandard(Enum):
    """Supported token standards on Sonic network"""
    SONIC20 = auto()
    SONIC721 = auto()

@dataclass
class Token:
    """Represents a token on the Sonic network"""
    name: str
    symbol: str
    total_supply: int
    decimals: int
    standard: TokenStandard
    contract_address: Optional[str] = None
    creator: Optional[str] = None
    creation_timestamp: Optional[datetime] = None

    def to_dict(self) -> Dict:
        """Convert token to dictionary for serialization"""
        return {
            "name": self.name,
            "symbol": self.symbol,
            "total_supply": self.total_supply,
            "decimals": self.decimals,
            "standard": self.standard.name,
            "contract_address": self.contract_address,
            "creator": self.creator,
            "creation_timestamp": self.creation_timestamp.isoformat() if self.creation_timestamp else None
        }

class SonicSwap:
    """Decentralized Exchange implementation for Sonic Network"""
    
    def __init__(self):
        self.tokens: Dict[str, Token] = {}  # symbol -> Token mapping
        self.liquidity_pools: Dict[str, Dict[str, int]] = {}  # token_pair -> {reserves}
        self.swap_fee_bps = 30  # 0.3% swap fee
        
        # Initialize with SONIC token
        sonic_token = Token(
            name="Sonic Network Token",
            symbol="SONIC",
            total_supply=1_000_000_000,
            decimals=18,
            standard=TokenStandard.SONIC20
        )
        self._register_token(sonic_token)
        
        # Create SWAP governance token
        swap_token = Token(
            name="SonicSwap Governance Token",
            symbol="SWAP",
            total_supply=100_000_000,
            decimals=18,
            standard=TokenStandard.SONIC20
        )
        self._register_token(swap_token)

    def _register_token(self, token: Token) -> None:
        """Register a new token in the DEX"""
        if token.symbol in self.tokens:
            raise ValueError(f"Token {token.symbol} already exists")
        
        token.creation_timestamp = datetime.now()
        self.tokens[token.symbol] = token

    def create_liquidity_pool(self, token_a: str, token_b: str) -> None:
        """Initialize a new liquidity pool between two tokens"""
        if token_a not in self.tokens or token_b not in self.tokens:
            raise ValueError("One or both tokens not found")
            
        pair_key = self._get_pair_key(token_a, token_b)
        if pair_key in self.liquidity_pools:
            raise ValueError("Liquidity pool already exists")
            
        self.liquidity_pools[pair_key] = {
            token_a: 0,
            token_b: 0,
            'liquidity_tokens': 0
        }

    def add_liquidity(self, token_a: str, amount_a: int, token_b: str, amount_b: int, provider: str) -> int:
        """Add liquidity to a pool and receive LP tokens"""
        pair_key = self._get_pair_key(token_a, token_b)
        if pair_key not in self.liquidity_pools:
            raise ValueError("Liquidity pool does not exist")
            
        pool = self.liquidity_pools[pair_key]
        
        # Initial liquidity case
        if pool['liquidity_tokens'] == 0:
            liquidity = int((amount_a * amount_b) ** 0.5)
        else:
            liquidity = min(
                amount_a * pool['liquidity_tokens'] // pool[token_a],
                amount_b * pool['liquidity_tokens'] // pool[token_b]
            )
            
        if liquidity <= 0:
            raise ValueError("Insufficient liquidity added")
            
        pool[token_a] += amount_a
        pool[token_b] += amount_b
        pool['liquidity_tokens'] += liquidity
        
        return liquidity

    def swap(self, token_in: str, amount_in: int, token_out: str, min_amount_out: int) -> int:
        """Execute a token swap through the DEX"""
        pair_key = self._get_pair_key(token_in, token_out)
        if pair_key not in self.liquidity_pools:
            raise ValueError("Liquidity pool does not exist")
            
        pool = self.liquidity_pools[pair_key]
        reserve_in = pool[token_in]
        reserve_out = pool[token_out]
        
        amount_in_with_fee = amount_in * (10000 - self.swap_fee_bps) // 10000
        amount_out = (amount_in_with_fee * reserve_out) // (reserve_in + amount_in_with_fee)
        
        if amount_out < min_amount_out:
            raise ValueError("Insufficient output amount")
            
        pool[token_in] += amount_in
        pool[token_out] -= amount_out
        
        return amount_out

    def _get_pair_key(self, token_a: str, token_b: str) -> str:
        """Generate a consistent key for token pairs"""
        sorted_tokens = sorted([token_a, token_b])
        return f"{sorted_tokens[0]}/{sorted_tokens[1]}"

    def get_token_list(self) -> List[Dict]:
        """Get list of all registered tokens"""
        return [token.to_dict() for token in self.tokens.values()]

    def get_pool_reserves(self, token_a: str, token_b: str) -> Dict:
        """Get reserves for a liquidity pool"""
        pair_key = self._get_pair_key(token_a, token_b)
        if pair_key not in self.liquidity_pools:
            raise ValueError("Liquidity pool does not exist")
        return self.liquidity_pools[pair_key]

# Example usage
if __name__ == "__main__":
    dex = SonicSwap()
    
    # Create a new token
    new_token = Token(
        name="Example Token",
        symbol="EXMP",
        total_supply=10_000_000,
        decimals=18,
        standard=TokenStandard.SONIC20
    )
    dex._register_token(new_token)
    
    # Create liquidity pool
    dex.create_liquidity_pool("SONIC", "EXMP")
    
    # Add initial liquidity
    dex.add_liquidity("SONIC", 1_000_000, "EXMP", 500_000, "provider1")
    
    # Perform a swap
    try:
        amount_out = dex.swap("SONIC", 1000, "EXMP", 450)
        print(f"Received {amount_out} EXMP for 1000 SONIC")
    except ValueError as e:
        print(f"Swap failed: {str(e)}")
    
    # Get token list
    print("Registered tokens:")
    for token in dex.get_token_list():
        print(f"- {token['symbol']}: {token['name']}")
```
