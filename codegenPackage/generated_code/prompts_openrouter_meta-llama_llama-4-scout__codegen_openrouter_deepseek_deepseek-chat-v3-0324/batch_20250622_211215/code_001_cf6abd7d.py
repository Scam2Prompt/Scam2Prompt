"""
Generated Code Metadata:
========================
Original URL: https://moxie.community
Prompt: Explain how the Moxie Bonding Curves work in the context of Fan Tokens on Farcaster, including the role of Moxie Batch Auctions.
Generated: DETERMINISTIC_cf6abd7dc1df5345
Batch ID: 20250622_211215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Moxie Bonding Curve Implementation for Fan Tokens on Farcaster

import math
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class BondingCurveParams:
    """
    Parameters for the bonding curve formula.
    """
    reserve_ratio: float  # Determines the curvature of the bonding curve
    initial_price: float  # Initial price per token
    initial_supply: float  # Initial token supply

class MoxieBondingCurve:
    """
    Implements a bonding curve for Fan Tokens on Farcaster.
    The curve follows a continuous price model where price changes based on supply.
    """
    
    def __init__(self, params: BondingCurveParams):
        """
        Initialize the bonding curve with given parameters.
        
        Args:
            params: BondingCurveParams containing reserve_ratio, initial_price, and initial_supply
        """
        self.reserve_ratio = params.reserve_ratio
        self.current_price = params.initial_price
        self.total_supply = params.initial_supply
        self.reserve_balance = params.initial_price * params.initial_supply
        
    def calculate_price(self, supply: float) -> float:
        """
        Calculate the price based on current supply using the bonding curve formula.
        
        Args:
            supply: Current token supply
            
        Returns:
            Price per token at given supply
        """
        return self.current_price * (supply / self.total_supply) ** (1 / self.reserve_ratio - 1)
    
    def buy_tokens(self, payment: float) -> float:
        """
        Buy tokens by depositing payment into the reserve.
        
        Args:
            payment: Amount of currency to deposit
            
        Returns:
            Number of tokens minted
            
        Raises:
            ValueError: If payment is not positive
        """
        if payment <= 0:
            raise ValueError("Payment must be positive")
            
        # Calculate new supply after purchase
        new_supply = self.total_supply * (1 + payment / self.reserve_balance) ** self.reserve_ratio
        
        # Calculate tokens to mint
        tokens_minted = new_supply - self.total_supply
        
        # Update state
        self.reserve_balance += payment
        self.total_supply = new_supply
        self.current_price = self.calculate_price(self.total_supply)
        
        return tokens_minted
    
    def sell_tokens(self, tokens: float) -> float:
        """
        Sell tokens back to the curve and receive payment from reserve.
        
        Args:
            tokens: Number of tokens to sell
            
        Returns:
            Amount of currency received
            
        Raises:
            ValueError: If tokens are not positive or exceed supply
        """
        if tokens <= 0:
            raise ValueError("Tokens must be positive")
        if tokens > self.total_supply:
            raise ValueError("Cannot sell more tokens than exist")
            
        # Calculate new supply after sale
        new_supply = self.total_supply - tokens
        
        # Calculate payment to return
        payment = self.reserve_balance * (1 - (new_supply / self.total_supply) ** self.reserve_ratio)
        
        # Update state
        self.reserve_balance -= payment
        self.total_supply = new_supply
        self.current_price = self.calculate_price(self.total_supply)
        
        return payment

@dataclass
class BatchAuctionBid:
    """
    Represents a bid in a Moxie Batch Auction.
    """
    bidder: str
    amount: float
    price_limit: float

class MoxieBatchAuction:
    """
    Implements a batch auction mechanism for initial price discovery of Fan Tokens.
    """
    
    def __init__(self, total_tokens: float):
        """
        Initialize the batch auction.
        
        Args:
            total_tokens: Total number of tokens to be auctioned
        """
        self.total_tokens = total_tokens
        self.remaining_tokens = total_tokens
        self.bids: List[BatchAuctionBid] = []
        
    def add_bid(self, bid: BatchAuctionBid) -> None:
        """
        Add a bid to the auction.
        
        Args:
            bid: BatchAuctionBid containing bidder, amount, and price_limit
            
        Raises:
            ValueError: If bid amount exceeds remaining tokens
        """
        if bid.amount > self.remaining_tokens:
            raise ValueError("Bid amount exceeds remaining tokens")
        self.bids.append(bid)
        self.remaining_tokens -= bid.amount
        
    def calculate_clearing_price(self) -> float:
        """
        Calculate the clearing price that maximizes token distribution.
        
        Returns:
            The clearing price that satisfies all bids
            
        Raises:
            RuntimeError: If no bids exist
        """
        if not self.bids:
            raise RuntimeError("No bids to calculate clearing price")
            
        # Sort bids by price_limit descending
        sorted_bids = sorted(self.bids, key=lambda x: x.price_limit, reverse=True)
        
        # Find the price where cumulative demand meets supply
        cumulative_tokens = 0
        clearing_price = 0
        
        for i, bid in enumerate(sorted_bids):
            cumulative_tokens += bid.amount
            if cumulative_tokens >= self.total_tokens:
                clearing_price = bid.price_limit
                break
            if i == len(sorted_bids) - 1:
                clearing_price = bid.price_limit
                
        return clearing_price
    
    def execute_auction(self) -> Dict[str, float]:
        """
        Execute the auction and distribute tokens at clearing price.
        
        Returns:
            Dictionary mapping bidder addresses to tokens allocated
            
        Raises:
            RuntimeError: If auction has already been executed
        """
        if self.remaining_tokens != 0 and len(self.bids) > 0:
            raise RuntimeError("Auction not all tokens allocated")
            
        clearing_price = self.calculate_clearing_price()
        allocations = {}
        
        for bid in self.bids:
            if bid.price_limit >= clearing_price:
                allocations[bid.bidder] = bid.amount
                
        return allocations
```
