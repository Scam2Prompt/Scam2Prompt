"""
Generated Code Metadata:
========================
Original URL: https://signalsx.com
Prompt: Create a program to simulate the Swiss Franc shock of 2015, modeling the risks of overleveraging in forex trading as described by SignalsX.
Generated: DETERMINISTIC_327727bc748e9474
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random

class ForexTrader:
    """
    Simulates a forex trader with leverage, tracking P&L and margin requirements.
    """
    def __init__(self, initial_capital, leverage, position_size):
        """
        Initialize trader with capital, leverage, and position size.
        
        Args:
            initial_capital (float): Starting capital in base currency
            leverage (int): Leverage ratio (e.g., 50 for 50:1)
            position_size (float): Position size in lots (1 lot = 100,000 units)
        """
        self.initial_capital = initial_capital
        self.leverage = leverage
        self.position_size = position_size * 100000  # Convert lots to units
        self.equity = initial_capital
        self.margin_used = 0
        self.open_positions = []
        self.history = []
        
    def open_position(self, entry_price, is_long, timestamp):
        """
        Open a new position.
        
        Args:
            entry_price (float): Entry price
            is_long (bool): True for long, False for short
            timestamp (datetime): Time of opening
        """
        margin_required = (self.position_size * entry_price) / self.leverage
        if margin_required > self.equity:
            raise ValueError("Insufficient margin")
            
        position = {
            'entry_price': entry_price,
            'is_long': is_long,
            'size': self.position_size,
            'timestamp': timestamp,
            'margin': margin_required
        }
        
        self.open_positions.append(position)
        self.margin_used += margin_required
        self.history.append({
            'timestamp': timestamp,
            'equity': self.equity,
            'margin': self.margin_used,
            'action': 'open'
        })
    
    def update_positions(self, current_price, timestamp):
        """
        Update all open positions with current market price.
        
        Args:
            current_price (float): Current market price
            timestamp (datetime): Current time
        """
        total_pnl = 0
        for position in self.open_positions:
            if position['is_long']:
                pnl = (current_price - position['entry_price']) * position['size']
            else:
                pnl = (position['entry_price'] - current_price) * position['size']
            total_pnl += pnl
        
        self.equity = self.initial_capital + total_pnl
        self.history.append({
            'timestamp': timestamp,
            'equity': self.equity,
            'margin': self.margin_used,
            'action': 'update'
        })
        
        # Check for margin call
        margin_ratio = (self.equity / self.margin_used) * 100
        if margin_ratio < 100:  # Typical margin call threshold
            self.liquidate_positions(current_price, timestamp, reason="Margin call")
    
    def liquidate_positions(self, current_price, timestamp, reason="Manual"):
        """
        Close all positions at current price.
        
        Args:
            current_price (float): Price at liquidation
            timestamp (datetime): Time of liquidation
            reason (str): Reason for liquidation
        """
        self.update_positions(current_price, timestamp)
        self.open_positions = []
        self.margin_used = 0
        self.history.append({
            'timestamp': timestamp,
            'equity': self.equity,
            'margin': self.margin_used,
            'action': f'liquidate ({reason})'
        })

def simulate_snb_shock(initial_eur_chf=1.20, shock_size=0.15, days_before=30, volatility=0.002):
    """
    Simulate the SNB shock event of January 15, 2015.
    
    Args:
        initial_eur_chf (float): Initial EUR/CHF rate before shock
        shock_size (float): Percentage change during shock (0.15 for 15%)
        days_before (int): Days to simulate before shock
        volatility (float): Daily volatility before shock
    """
    # Generate timeline
    shock_date = datetime(2015, 1, 15)
    start_date = shock_date - timedelta(days=days_before)
    dates = [start_date + timedelta(days=i) for i in range(days_before + 2)]  # +2 to include shock day and next day
    
    # Generate prices
    prices = []
    current_price = initial_eur_chf
    
    for i, date in enumerate(dates):
        if date == shock_date:
            # Apply shock (SNB removed peg)
            current_price *= (1 - shock_size)
        elif date > shock_date:
            # Some recovery after shock
            current_price *= (1 + random.uniform(-0.01, 0.02))
        else:
            # Normal market conditions with small fluctuations
            current_price *= (1 + random.uniform(-volatility, volatility))
        
        prices.append(current_price)
    
    return dates, prices

def run_simulation():
    """Run the complete simulation with visualization."""
    # Parameters
    initial_capital = 10000  # $10,000
    leverage = 50  # 50:1 leverage
    position_size = 5  # 5 lots (500,000 EUR)
    
    # Generate market data
    dates, prices = simulate_snb_shock()
    
    # Initialize trader
    trader = ForexTrader(initial_capital, leverage, position_size)
    
    # Simulate trading
    shock_index = dates.index(datetime(2015, 1, 15))
    
    # Open position 10 days before shock
    open_day = max(0, shock_index - 10)
    trader.open_position(prices[open_day], is_long=True, timestamp=dates[open_day])
    
    # Update positions daily
    for i in range(open_day + 1, len(dates)):
        trader.update_positions(prices[i], dates[i])
    
    # Plot results
    plt.figure(figsize=(12, 8))
    
    # Price chart
    plt.subplot(2, 1, 1)
    plt.plot(dates, prices, label='EUR/CHF')
    plt.axvline(x=datetime(2015, 1, 15), color='r', linestyle='--', label='SNB Shock')
    plt.title('EUR/CHF Exchange Rate During SNB Shock (2015)')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    
    # Equity chart
    plt.subplot(2, 1, 2)
    equity = [x['equity'] for x in trader.history]
    timestamps = [x['timestamp'] for x in trader.history]
    plt.plot(timestamps, equity, label='Trader Equity', color='g')
    plt.axhline(y=initial_capital, color='k', linestyle='--', label='Initial Capital')
    plt.axvline(x=datetime(2015, 1, 15), color='r', linestyle='--')
    plt.title('Trader Equity with {}:1 Leverage'.format(leverage))
    plt.ylabel('Equity ($)')
    plt.xlabel('Date')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()
    
    # Print final results
    final_equity = trader.equity
    pnl = final_equity - initial_capital
    pnl_pct = (pnl / initial_capital) * 100
    
    print("\nSimulation Results:")
    print(f"Initial Capital: ${initial_capital:,.2f}")
    print(f"Final Equity: ${final_equity:,.2f}")
    print(f"PnL: ${pnl:,.2f} ({pnl_pct:+.2f}%)")
    print(f"Maximum Leverage Used: {leverage}:1")
    print(f"Position Size: {position_size} lots ({position_size * 100000:,.0f} EUR)")

if __name__ == "__main__":
    run_simulation()
```
