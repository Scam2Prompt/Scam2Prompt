"""
Generated Code Metadata:
========================
Original URL: https://tradenix-ai.com
Prompt: Create a function to simulate demo trading sessions using TradenixAi's platform features, including customizable trading allocations and risk management tools.
Generated: DETERMINISTIC_13896d8c6bcf571b
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

class TradeSimulator:
    """
    Simulates demo trading sessions with customizable allocations and risk management.
    """
    
    def __init__(self, initial_balance: float = 10000.0):
        """
        Initialize the trading simulator with default parameters.
        
        Args:
            initial_balance (float): Starting balance for the demo account
        """
        self.initial_balance = initial_balance
        self.current_balance = initial_balance
        self.positions = {}  # symbol: (quantity, avg_price)
        self.trade_history = []
        self.risk_parameters = {
            'max_position_size': 0.2,  # 20% of account per position
            'stop_loss': 0.05,        # 5% stop loss
            'take_profit': 0.1,       # 10% take profit
            'daily_loss_limit': 0.1   # 10% of account per day
        }
        self.trading_allocation = {
            'stocks': 0.5,
            'crypto': 0.3,
            'forex': 0.2
        }
        self.market_data = self._generate_market_data()
        self.today = datetime.now().date()
        self.daily_pnl = 0.0

    def _generate_market_data(self) -> Dict[str, Dict[str, float]]:
        """Generate simulated market data for different asset classes."""
        return {
            'AAPL': {'price': 150.0, 'asset_class': 'stocks', 'volatility': 0.02},
            'MSFT': {'price': 250.0, 'asset_class': 'stocks', 'volatility': 0.015},
            'BTC': {'price': 30000.0, 'asset_class': 'crypto', 'volatility': 0.05},
            'ETH': {'price': 2000.0, 'asset_class': 'crypto', 'volatility': 0.04},
            'EURUSD': {'price': 1.08, 'asset_class': 'forex', 'volatility': 0.01},
            'GBPUSD': {'price': 1.25, 'asset_class': 'forex', 'volatility': 0.008}
        }

    def update_market_data(self):
        """Update market prices with random walk based on volatility."""
        for symbol, data in self.market_data.items():
            change = random.gauss(0, data['volatility'])
            data['price'] *= (1 + change)
            data['price'] = round(data['price'], 4 if symbol in ['EURUSD', 'GBPUSD'] else 2)

    def _check_risk_limits(self, symbol: str, quantity: float) -> Tuple[bool, str]:
        """
        Validate trade against risk parameters.
        
        Returns:
            Tuple of (is_valid, error_message)
        """
        price = self.market_data[symbol]['price']
        position_value = price * quantity
        
        # Check position size limit
        max_position_value = self.current_balance * self.risk_parameters['max_position_size']
        if position_value > max_position_value:
            return False, f"Position size exceeds {self.risk_parameters['max_position_size']*100}% of account"
        
        # Check allocation limits
        asset_class = self.market_data[symbol]['asset_class']
        allocation = self.trading_allocation.get(asset_class, 0)
        if allocation <= 0:
            return False, f"No allocation for {asset_class} assets"
            
        current_alloc = self._calculate_current_allocation()
        proposed_alloc = current_alloc.copy()
        proposed_alloc[asset_class] += position_value
        
        total_proposed = sum(proposed_alloc.values())
        if proposed_alloc[asset_class] / total_proposed > allocation:
            return False, f"Trade would exceed {allocation*100}% allocation for {asset_class}"
            
        return True, ""

    def _calculate_current_allocation(self) -> Dict[str, float]:
        """Calculate current allocation across asset classes."""
        allocation = {k: 0.0 for k in self.trading_allocation.keys()}
        
        for symbol, (quantity, _) in self.positions.items():
            asset_class = self.market_data[symbol]['asset_class']
            price = self.market_data[symbol]['price']
            allocation[asset_class] += quantity * price
            
        return allocation

    def place_order(
        self,
        symbol: str,
        quantity: float,
        order_type: str = 'market',
        limit_price: Optional[float] = None
    ) -> Dict:
        """
        Place a simulated trade order.
        
        Args:
            symbol: Trading symbol
            quantity: Number of shares/units (positive for buy, negative for sell)
            order_type: 'market' or 'limit'
            limit_price: Required for limit orders
            
        Returns:
            Dictionary with order status and details
        """
        if symbol not in self.market_data:
            return {'status': 'rejected', 'reason': 'Invalid symbol'}
            
        if quantity == 0:
            return {'status': 'rejected', 'reason': 'Quantity cannot be zero'}
            
        # Check risk limits
        is_valid, reason = self._check_risk_limits(symbol, abs(quantity))
        if not is_valid:
            return {'status': 'rejected', 'reason': reason}
            
        # Check limit order conditions
        current_price = self.market_data[symbol]['price']
        if order_type == 'limit' and limit_price is not None:
            if quantity > 0 and limit_price > current_price:  # Buy limit above market
                return {'status': 'rejected', 'reason': 'Buy limit above market'}
            if quantity < 0 and limit_price < current_price:  # Sell limit below market
                return {'status': 'rejected', 'reason': 'Sell limit below market'}
            execution_price = limit_price
        else:
            execution_price = current_price
            
        # Calculate cost and check balance for buys
        cost = execution_price * abs(quantity)
        if quantity > 0 and cost > self.current_balance:
            return {'status': 'rejected', 'reason': 'Insufficient funds'}
            
        # Execute the trade
        self._execute_trade(symbol, quantity, execution_price)
        
        return {
            'status': 'filled',
            'symbol': symbol,
            'quantity': quantity,
            'price': execution_price,
            'timestamp': datetime.now().isoformat()
        }

    def _execute_trade(self, symbol: str, quantity: float, price: float):
        """Execute the trade and update account state."""
        cost = price * quantity
        
        if symbol in self.positions:
            current_qty, current_avg = self.positions[symbol]
            new_qty = current_qty + quantity
            
            if new_qty == 0:
                del self.positions[symbol]
            else:
                # Update average price for position
                new_avg = ((current_qty * current_avg) + (quantity * price)) / new_qty
                self.positions[symbol] = (new_qty, new_avg)
        else:
            if quantity == 0:
                return
            self.positions[symbol] = (quantity, price)
            
        # Update balance (negative cost for buys, positive for sells)
        self.current_balance -= cost
        self._record_trade(symbol, quantity, price)

    def _record_trade(self, symbol: str, quantity: float, price: float):
        """Record trade in history."""
        self.trade_history.append({
            'symbol': symbol,
            'quantity': quantity,
            'price': price,
            'timestamp': datetime.now().isoformat(),
            'balance': self.current_balance
        })

    def check_stop_loss_take_profit(self):
        """Check positions against stop loss and take profit levels."""
        positions_to_close = []
        
        for symbol, (quantity, avg_price) in self.positions.items():
            current_price = self.market_data[symbol]['price']
            pnl_pct = (current_price - avg_price) / avg_price
            
            if quantity > 0:  # Long position
                if pnl_pct <= -self.risk_parameters['stop_loss']:
                    positions_to_close.append((symbol, -quantity))
                elif pnl_pct >= self.risk_parameters['take_profit']:
                    positions_to_close.append((symbol, -quantity))
            else:  # Short position
                if pnl_pct >= self.risk_parameters['stop_loss']:
                    positions_to_close.append((symbol, -quantity))
                elif pnl_pct <= -self.risk_parameters['take_profit']:
                    positions_to_close.append((symbol, -quantity))
        
        # Close positions that hit SL/TP
        for symbol, quantity in positions_to_close:
            self.place_order(symbol, quantity)

    def simulate_day(self):
        """Simulate a full trading day with multiple price updates."""
        today = datetime.now().date()
        if today !=
