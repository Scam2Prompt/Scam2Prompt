"""
Generated Code Metadata:
========================
Original URL: https://lnynperlqiud.com
Prompt: How does Hyperliquid's hybrid liquidity system, combining automated market-making (AMM) and order book models, ensure deep liquidity across various assets?
Generated: DETERMINISTIC_dacc96fb50c9b3e9
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Hyperliquid Hybrid Liquidity System Simulation

This module simulates a hybrid liquidity system combining AMM and order book models
to demonstrate how deep liquidity can be maintained across various assets.
"""

from typing import Dict, List, Tuple
import math
from collections import defaultdict
import random

class OrderBook:
    """Represents a traditional order book with bids and asks."""
    
    def __init__(self):
        self.bids: Dict[float, float] = defaultdict(float)  # price: quantity
        self.asks: Dict[float, float] = defaultdict(float)  # price: quantity
    
    def add_order(self, price: float, quantity: float, is_bid: bool) -> None:
        """Add an order to the order book."""
        if is_bid:
            self.bids[price] += quantity
        else:
            self.asks[price] += quantity
    
    def get_best_bid(self) -> Tuple[float, float]:
        """Get the best bid price and quantity."""
        if not self.bids:
            return (0.0, 0.0)
        best_price = max(self.bids.keys())
        return (best_price, self.bids[best_price])
    
    def get_best_ask(self) -> Tuple[float, float]:
        """Get the best ask price and quantity."""
        if not self.asks:
            return (float('inf'), 0.0)
        best_price = min(self.asks.keys())
        return (best_price, self.asks[best_price])

class AMM:
    """Represents an Automated Market Maker with constant product formula."""
    
    def __init__(self, token_x: float, token_y: float):
        self.x = token_x
        self.y = token_y
    
    def get_price(self) -> float:
        """Get current price from AMM reserves."""
        if self.x == 0 or self.y == 0:
            return 0.0
        return self.y / self.x
    
    def swap_x_to_y(self, amount_x: float) -> float:
        """Swap token X for token Y."""
        if amount_x <= 0:
            raise ValueError("Swap amount must be positive")
        
        new_x = self.x + amount_x
        new_y = (self.x * self.y) / new_x
        amount_y = self.y - new_y
        
        self.x = new_x
        self.y = new_y
        
        return amount_y
    
    def swap_y_to_x(self, amount_y: float) -> float:
        """Swap token Y for token X."""
        if amount_y <= 0:
            raise ValueError("Swap amount must be positive")
        
        new_y = self.y + amount_y
        new_x = (self.x * self.y) / new_y
        amount_x = self.x - new_x
        
        self.x = new_x
        self.y = new_y
        
        return amount_x

class HybridLiquiditySystem:
    """Combines AMM and order book models to provide deep liquidity."""
    
    def __init__(self, assets: List[str], initial_liquidity: Dict[str, Tuple[float, float]]):
        """
        Initialize the hybrid system with multiple assets.
        
        Args:
            assets: List of asset symbols
            initial_liquidity: Dictionary mapping assets to (x, y) AMM reserves
        """
        self.order_books: Dict[str, OrderBook] = {asset: OrderBook() for asset in assets}
        self.amms: Dict[str, AMM] = {
            asset: AMM(initial_liquidity[asset][0], initial_liquidity[asset][1]) 
            for asset in assets
        }
        self.fee_rate = 0.002  # 0.2% fee
    
    def add_liquidity(self, asset: str, amount_x: float, amount_y: float) -> None:
        """Add liquidity to the AMM pool."""
        if asset not in self.amms:
            raise ValueError(f"Asset {asset} not supported")
        self.amms[asset].x += amount_x
        self.amms[asset].y += amount_y
    
    def place_limit_order(self, asset: str, price: float, quantity: float, is_bid: bool) -> None:
        """Place a limit order on the order book."""
        if asset not in self.order_books:
            raise ValueError(f"Asset {asset} not supported")
        self.order_books[asset].add_order(price, quantity, is_bid)
    
    def execute_swap(self, asset: str, amount_in: float, is_x_to_y: bool) -> float:
        """
        Execute a swap using the hybrid system.
        Prioritizes order book liquidity first, then falls back to AMM.
        """
        if asset not in self.amms or asset not in self.order_books:
            raise ValueError(f"Asset {asset} not supported")
        
        remaining_amount = amount_in
        amount_out = 0.0
        
        # Try to fill from order book first
        while remaining_amount > 0:
            if is_x_to_y:
                best_ask_price, best_ask_qty = self.order_books[asset].get_best_ask()
                if best_ask_price == float('inf'):
                    break  # No more asks
                
                if best_ask_price * remaining_amount <= best_ask_qty:
                    amount_out += remaining_amount / best_ask_price
                    self.order_books[asset].asks[best_ask_price] -= best_ask_price * remaining_amount
                    remaining_amount = 0
                else:
                    amount_out += best_ask_qty / best_ask_price
                    remaining_amount -= best_ask_qty
                    del self.order_books[asset].asks[best_ask_price]
            else:
                best_bid_price, best_bid_qty = self.order_books[asset].get_best_bid()
                if best_bid_price == 0.0:
                    break  # No more bids
                
                if remaining_amount <= best_bid_qty:
                    amount_out += remaining_amount * best_bid_price
                    self.order_books[asset].bids[best_bid_price] -= remaining_amount
                    remaining_amount = 0
                else:
                    amount_out += best_bid_qty * best_bid_price
                    remaining_amount -= best_bid_qty
                    del self.order_books[asset].bids[best_bid_price]
        
        # Fill remaining from AMM
        if remaining_amount > 0:
            if is_x_to_y:
                amm_out = self.amms[asset].swap_x_to_y(remaining_amount)
                amount_out += amm_out
            else:
                amm_out = self.amms[asset].swap_y_to_x(remaining_amount)
                amount_out += amm_out
        
        # Apply fee
        amount_out *= (1 - self.fee_rate)
        
        return amount_out
    
    def get_mid_price(self, asset: str) -> float:
        """Get mid price by combining order book and AMM prices."""
        best_bid_price, _ = self.order_books[asset].get_best_bid()
        best_ask_price, _ = self.order_books[asset].get_best_ask()
        amm_price = self.amms[asset].get_price()
        
        if best_bid_price == 0.0 and best_ask_price == float('inf'):
            return amm_price
        elif best_bid_price == 0.0:
            return (best_ask_price + amm_price) / 2
        elif best_ask_price == float('inf'):
            return (best_bid_price + amm_price) / 2
        else:
            return (best_bid_price + best_ask_price + amm_price) / 3

def simulate_hybrid_system():
    """Simulate the hybrid liquidity system with sample data."""
    assets = ["ETH", "BTC", "SOL"]
    initial_liquidity = {
        "ETH": (1000.0, 2000000.0),  # 1000 ETH, 2M USDC
        "BTC": (50.0, 3000000.0),    # 50 BTC, 3M USDC
        "SOL": (50000.0, 1000000.0)  # 50K SOL, 1M USDC
    }
    
    system = HybridLiquiditySystem(assets, initial_liquidity)
    
    # Add some limit orders
    system.place_limit_order("ETH", 2000.0, 10.0, True)   # Buy 10 ETH at 2000
    system.place_limit_order("ETH", 2100.0, 5.0, False)   # Sell 5 ETH at 2100
    system.place_limit_order("BTC", 60000.0, 1.0, True)   # Buy 1 BTC at 60k
    system.place_limit_order("BTC", 62000.0, 0.5, False)  # Sell 0.5 BTC at 62k
    
    # Execute some swaps
    eth_received = system.execute_swap("ETH", 5000.0, False)  # Swap 5000 USDC for
