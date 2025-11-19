"""
Generated Code Metadata:
========================
Original URL: https://moxie.community
Prompt: Generate code for implementing Moxie Batch Auctions to enable fair price discovery for Fan Tokens on Farcaster.
Generated: DETERMINISTIC_663e3a064905c86d
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from decimal import Decimal
import time
from collections import defaultdict

@dataclass
class Order:
    """Represents a single order in the auction."""
    order_id: str
    user_id: str
    token_id: str
    is_buy: bool
    price: Decimal
    quantity: Decimal
    timestamp: float = field(default_factory=time.time)

@dataclass
class AuctionBatch:
    """Represents a batch of orders to be processed together."""
    batch_id: str
    orders: List[Order] = field(default_factory=list)
    start_time: float = field(default_factory=time.time)
    end_time: Optional[float] = None
    clearing_price: Optional[Decimal] = None
    executed_orders: List[Order] = field(default_factory=list)

class MoxieBatchAuction:
    """Implements Moxie Batch Auctions for Fan Tokens on Farcaster."""
    
    def __init__(self, batch_duration_seconds: int = 300):
        """Initialize the auction system.
        
        Args:
            batch_duration_seconds: Duration of each auction batch in seconds.
        """
        self.batch_duration = batch_duration_seconds
        self.current_batch: Optional[AuctionBatch] = None
        self.pending_orders: List[Order] = []
        self.completed_batches: List[AuctionBatch] = []
        self.token_balances: Dict[str, Dict[str, Decimal]] = defaultdict(lambda: defaultdict(Decimal))
    
    def start_new_batch(self) -> AuctionBatch:
        """Start a new auction batch."""
        if self.current_batch and not self.current_batch.end_time:
            self._finalize_batch()
        
        batch_id = f"batch_{int(time.time())}"
        self.current_batch = AuctionBatch(batch_id=batch_id)
        self.current_batch.orders.extend(self.pending_orders)
        self.pending_orders = []
        return self.current_batch
    
    def add_order(self, order: Order) -> bool:
        """Add an order to the current batch or pending queue.
        
        Args:
            order: The order to add.
            
        Returns:
            bool: True if order was added to current batch, False if added to pending.
        """
        if not self._validate_order(order):
            return False
            
        if self.current_batch and not self.current_batch.end_time:
            self.current_batch.orders.append(order)
            return True
        else:
            self.pending_orders.append(order)
            return False
    
    def _validate_order(self, order: Order) -> bool:
        """Validate an order before adding it to the system."""
        if order.quantity <= 0:
            return False
        if order.price <= 0:
            return False
        return True
    
    def check_batch_completion(self) -> bool:
        """Check if current batch should be finalized based on time."""
        if not self.current_batch or self.current_batch.end_time:
            return False
            
        elapsed = time.time() - self.current_batch.start_time
        if elapsed >= self.batch_duration:
            self._finalize_batch()
            return True
        return False
    
    def _finalize_batch(self) -> None:
        """Finalize the current batch by calculating clearing price and executing orders."""
        if not self.current_batch or self.current_batch.end_time:
            return
            
        self.current_batch.end_time = time.time()
        self._calculate_clearing_price()
        self._execute_orders()
        self.completed_batches.append(self.current_batch)
        self.current_batch = None
    
    def _calculate_clearing_price(self) -> None:
        """Calculate the clearing price for the current batch using uniform price auction."""
        if not self.current_batch:
            return
            
        buy_orders = sorted(
            [o for o in self.current_batch.orders if o.is_buy],
            key=lambda x: x.price,
            reverse=True
        )
        sell_orders = sorted(
            [o for o in self.current_batch.orders if not o.is_buy],
            key=lambda x: x.price
        )
        
        max_volume = Decimal('0')
        clearing_price = Decimal('0')
        
        # Iterate through possible price points to find optimal clearing price
        for i, buy_order in enumerate(buy_orders):
            temp_price = buy_order.price
            buy_volume = sum(o.quantity for o in buy_orders[:i+1])
            sell_volume = sum(o.quantity for o in sell_orders if o.price <= temp_price)
            
            volume = min(buy_volume, sell_volume)
            if volume > max_volume or (volume == max_volume and temp_price > clearing_price):
                max_volume = volume
                clearing_price = temp_price
        
        self.current_batch.clearing_price = clearing_price
    
    def _execute_orders(self) -> None:
        """Execute orders at the clearing price."""
        if not self.current_batch or not self.current_batch.clearing_price:
            return
            
        clearing_price = self.current_batch.clearing_price
        executed_orders = []
        
        # Process buy orders
        buy_orders = sorted(
            [o for o in self.current_batch.orders if o.is_buy and o.price >= clearing_price],
            key=lambda x: (-x.price, x.timestamp)
        )
        
        # Process sell orders
        sell_orders = sorted(
            [o for o in self.current_batch.orders if not o.is_buy and o.price <= clearing_price],
            key=lambda x: (x.price, x.timestamp)
        )
        
        # Simple matching algorithm (FIFO within price tiers)
        buy_idx = sell_idx = 0
        while buy_idx < len(buy_orders) and sell_idx < len(sell_orders):
            buy_order = buy_orders[buy_idx]
            sell_order = sell_orders[sell_idx]
            
            matched_quantity = min(buy_order.quantity, sell_order.quantity)
            
            # Update balances
            self.token_balances[buy_order.user_id][sell_order.token_id] += matched_quantity
            self.token_balances[sell_order.user_id][sell_order.token_id] -= matched_quantity
            self.token_balances[buy_order.user_id]['ETH'] -= matched_quantity * clearing_price
            self.token_balances[sell_order.user_id]['ETH'] += matched_quantity * clearing_price
            
            # Update order quantities
            buy_order.quantity -= matched_quantity
            sell_order.quantity -= matched_quantity
            
            # Add to executed orders
            executed_buy = Order(
                order_id=buy_order.order_id,
                user_id=buy_order.user_id,
                token_id=buy_order.token_id,
                is_buy=True,
                price=clearing_price,
                quantity=matched_quantity
            )
            executed_sell = Order(
                order_id=sell_order.order_id,
                user_id=sell_order.user_id,
                token_id=sell_order.token_id,
                is_buy=False,
                price=clearing_price,
                quantity=matched_quantity
            )
            executed_orders.extend([executed_buy, executed_sell])
            
            # Move to next order if current is filled
            if buy_order.quantity == 0:
                buy_idx += 1
            if sell_order.quantity == 0:
                sell_idx += 1
        
        self.current_batch.executed_orders = executed_orders
    
    def get_user_balance(self, user_id: str, token_id: str) -> Decimal:
        """Get a user's balance for a specific token."""
        return self.token_balances[user_id][token_id]
    
    def get_batch_status(self, batch_id: str) -> Optional[Dict]:
        """Get the status of a specific batch."""
        for batch in self.completed_batches:
            if batch.batch_id == batch_id:
                return {
                    'batch_id': batch.batch_id,
                    'start_time': batch.start_time,
                    'end_time': batch.end_time,
                    'clearing_price': str(batch.clearing_price),
                    'order_count': len(batch.orders),
                    'executed_order_count': len(batch.executed_orders)
                }
        return None

    def to_json(self) -> str:
        """Serialize the auction state to JSON."""
        state = {
            'batch_duration': self.batch_duration,
            'current_batch': None if not self.current_batch else {
                'batch_id': self.current_batch.batch_id,
                'start_time': self.current_batch.start_time,
                'orders': [{
                    'order_id': o.order_id,
                    'user_id': o.user_id,
                    'token_id': o.token_id,
                    'is_buy': o.is_buy,
                    'price': str(o.price),
                    'quantity': str(o.quantity),
                    'timestamp': o.timestamp
                } for o in self.current_batch.orders]
            },
            'pending_orders': [{
                'order_id': o.order_id,
                'user_id': o.user_id,
                'token_id': o.token_id
