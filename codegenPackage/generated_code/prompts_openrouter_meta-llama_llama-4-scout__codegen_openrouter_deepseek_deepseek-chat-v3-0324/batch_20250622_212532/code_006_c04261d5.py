"""
Generated Code Metadata:
========================
Original URL: https://urusdev.limited
Prompt: "Design an algorithm for efficient trade execution on URUS DEVELOPMENTS LIMITED's platform, focusing on minimizing slippage and maximizing liquidity."
Generated: DETERMINISTIC_c04261d5b3401e00
Batch ID: 20250622_212532
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import heapq
from collections import defaultdict
from typing import Dict, List, Tuple, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OrderBook:
    """
    Represents the order book for a trading pair, maintaining buy and sell orders.
    """
    def __init__(self):
        # Min heap for sell orders (best ask is at the top)
        self.sell_orders = []
        # Max heap for buy orders (best bid is at the top)
        self.buy_orders = []
        # Dictionary to track order quantities by price
        self.order_quantities = defaultdict(float)
    
    def add_order(self, order_type: str, price: float, quantity: float) -> None:
        """
        Add an order to the order book.
        
        Args:
            order_type: 'buy' or 'sell'
            price: Price of the order
            quantity: Quantity of the order
        """
        if order_type == 'buy':
            # Use negative price for max heap simulation
            heapq.heappush(self.buy_orders, (-price, price))
        elif order_type == 'sell':
            heapq.heappush(self.sell_orders, (price, price))
        else:
            raise ValueError("Invalid order type. Must be 'buy' or 'sell'")
        
        self.order_quantities[price] += quantity
    
    def get_best_bid(self) -> Optional[float]:
        """Return the best bid price or None if no bids exist."""
        return -self.buy_orders[0][0] if self.buy_orders else None
    
    def get_best_ask(self) -> Optional[float]:
        """Return the best ask price or None if no asks exist."""
        return self.sell_orders[0][0] if self.sell_orders else None
    
    def get_mid_price(self) -> Optional[float]:
        """Calculate the mid price between best bid and ask."""
        best_bid = self.get_best_bid()
        best_ask = self.get_best_ask()
        if best_bid and best_ask:
            return (best_bid + best_ask) / 2
        return None

class TradeExecutor:
    """
    Handles trade execution with slippage and liquidity considerations.
    """
    def __init__(self):
        self.order_books = defaultdict(OrderBook)
    
    def add_market_data(self, symbol: str, order_type: str, price: float, quantity: float) -> None:
        """
        Add market data to the order book for a given symbol.
        
        Args:
            symbol: Trading pair symbol
            order_type: 'buy' or 'sell'
            price: Price of the order
            quantity: Quantity of the order
        """
        try:
            self.order_books[symbol].add_order(order_type, price, quantity)
        except ValueError as e:
            logger.error(f"Error adding market data: {e}")
    
    def execute_trade(
        self,
        symbol: str,
        order_type: str,
        quantity: float,
        max_slippage: float = 0.01
    ) -> Tuple[float, float, float]:
        """
        Execute a trade while minimizing slippage.
        
        Args:
            symbol: Trading pair symbol
            order_type: 'buy' or 'sell'
            quantity: Desired quantity to trade
            max_slippage: Maximum acceptable slippage (default 1%)
        
        Returns:
            Tuple of (executed_price, executed_quantity, slippage)
        """
        if symbol not in self.order_books:
            raise ValueError(f"No order book found for symbol: {symbol}")
        
        order_book = self.order_books[symbol]
        executed_price = 0.0
        executed_quantity = 0.0
        remaining_quantity = quantity
        
        if order_type == 'buy':
            best_ask = order_book.get_best_ask()
            if not best_ask:
                raise ValueError("No sell orders available")
            
            max_price = best_ask * (1 + max_slippage)
            
            while remaining_quantity > 0 and order_book.sell_orders:
                current_price = order_book.sell_orders[0][0]
                if current_price > max_price:
                    break
                
                available_quantity = order_book.order_quantities[current_price]
                fill_quantity = min(available_quantity, remaining_quantity)
                
                executed_price += current_price * fill_quantity
                executed_quantity += fill_quantity
                remaining_quantity -= fill_quantity
                
                # Update order book
                order_book.order_quantities[current_price] -= fill_quantity
                if order_book.order_quantities[current_price] <= 0:
                    heapq.heappop(order_book.sell_orders)
                    del order_book.order_quantities[current_price]
        
        elif order_type == 'sell':
            best_bid = order_book.get_best_bid()
            if not best_bid:
                raise ValueError("No buy orders available")
            
            min_price = best_bid * (1 - max_slippage)
            
            while remaining_quantity > 0 and order_book.buy_orders:
                current_price = -order_book.buy_orders[0][0]
                if current_price < min_price:
                    break
                
                available_quantity = order_book.order_quantities[current_price]
                fill_quantity = min(available_quantity, remaining_quantity)
                
                executed_price += current_price * fill_quantity
                executed_quantity += fill_quantity
                remaining_quantity -= fill_quantity
                
                # Update order book
                order_book.order_quantities[current_price] -= fill_quantity
                if order_book.order_quantities[current_price] <= 0:
                    heapq.heappop(order_book.buy_orders)
                    del order_book.order_quantities[current_price]
        
        else:
            raise ValueError("Invalid order type. Must be 'buy' or 'sell'")
        
        if executed_quantity == 0:
            raise ValueError("No orders available within acceptable slippage range")
        
        avg_price = executed_price / executed_quantity
        if order_type == 'buy':
            slippage = (avg_price - best_ask) / best_ask if best_ask else 0
        else:
            slippage = (best_bid - avg_price) / best_bid if best_bid else 0
        
        return avg_price, executed_quantity, slippage

    def get_liquidity_depth(self, symbol: str, depth: int = 5) -> Dict[str, List[Tuple[float, float]]]:
        """
        Get liquidity depth for a given symbol.
        
        Args:
            symbol: Trading pair symbol
            depth: Number of price levels to return
        
        Returns:
            Dictionary with 'bids' and 'asks' lists of (price, quantity) tuples
        """
        if symbol not in self.order_books:
            raise ValueError(f"No order book found for symbol: {symbol}")
        
        order_book = self.order_books[symbol]
        result = {'bids': [], 'asks': []}
        
        # Get top bids
        temp_bids = []
        for _ in range(min(depth, len(order_book.buy_orders))):
            price = -order_book.buy_orders[0][0]
            quantity = order_book.order_quantities[price]
            result['bids'].append((price, quantity))
            heapq.heappush(temp_bids, heapq.heappop(order_book.buy_orders))
        
        # Restore buy orders heap
        for item in temp_bids:
            heapq.heappush(order_book.buy_orders, item)
        
        # Get top asks
        temp_asks = []
        for _ in range(min(depth, len(order_book.sell_orders))):
            price = order_book.sell_orders[0][0]
            quantity = order_book.order_quantities[price]
            result['asks'].append((price, quantity))
            heapq.heappush(temp_asks, heapq.heappop(order_book.sell_orders))
        
        # Restore sell orders heap
        for item in temp_asks:
            heapq.heappush(order_book.sell_orders, item)
        
        return result
```
