"""
Generated Code Metadata:
========================
Original URL: https://propsfundedtrader.com
Prompt: Generate a sample trading plan that aims for a 10% return per month, considering the parameters set by Props Funded Traders for their funded accounts.
Generated: DETERMINISTIC_13bbd65696eb51ff
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from typing import Dict, List, Tuple, Optional

class TradingPlan:
    """
    A trading plan designed to achieve a 10% monthly return while adhering to Props Funded Traders' rules.
    This includes risk management, position sizing, and trade execution logic.
    """
    
    def __init__(self, initial_capital: float, max_daily_loss_pct: float = 5.0, max_monthly_loss_pct: float = 10.0):
        """
        Initialize the trading plan with account parameters.
        
        Args:
            initial_capital (float): Starting account balance
            max_daily_loss_pct (float): Max daily loss percentage (default: 5%)
            max_monthly_loss_pct (float): Max monthly loss percentage (default: 10%)
        """
        self.initial_capital = initial_capital
        self.current_balance = initial_capital
        self.max_daily_loss = max_daily_loss_pct / 100 * initial_capital
        self.max_monthly_loss = max_monthly_loss_pct / 100 * initial_capital
        self.daily_pnl = 0.0
        self.monthly_pnl = 0.0
        self.trades = []
        self.trade_id = 1
        self.monthly_target = 0.10 * initial_capital
        self.daily_target = self.monthly_target / 20  # Assuming 20 trading days/month
        
        # Risk parameters
        self.max_risk_per_trade = 0.01 * initial_capital  # 1% risk per trade
        self.max_position_size_pct = 0.1  # Max 10% of account per position
        
        # Trading parameters
        self.entry_slippage_pct = 0.05  # 0.05% slippage on entry
        self.exit_slippage_pct = 0.05   # 0.05% slippage on exit
        self.commission_per_trade = 1.0  # $1 per trade
        
        # Market data
        self.instruments = ['ES', 'NQ', 'RTY', 'CL', 'GC']
        self.volatility = {inst: 1.0 for inst in self.instruments}  # Placeholder for volatility
        
    def calculate_position_size(self, instrument: str, stop_loss_pips: float) -> Tuple[float, int]:
        """
        Calculate position size based on risk parameters.
        
        Args:
            instrument (str): Trading instrument
            stop_loss_pips (float): Stop loss in pips
            
        Returns:
            Tuple[float, int]: Position size in dollars and contract size
        """
        if stop_loss_pips <= 0:
            raise ValueError("Stop loss must be positive")
            
        # Get pip value (simplified - in reality this would be instrument-specific)
        pip_value = 5.0 if instrument in ['ES', 'NQ', 'RTY'] else 10.0
        
        # Calculate max position size based on risk
        max_risk_units = self.max_risk_per_trade / (stop_loss_pips * pip_value)
        max_position_units = (self.max_position_size_pct * self.current_balance) / pip_value
        
        # Use the smaller of the two
        position_units = min(max_risk_units, max_position_units)
        position_size = position_units * pip_value
        
        # Round to nearest contract
        contracts = max(1, int(round(position_units)))
        
        return position_size, contracts
    
    def execute_trade(self, instrument: str, direction: str, entry_price: float, stop_loss: float, take_profit: float) -> Dict:
        """
        Execute a trade with proper risk management.
        
        Args:
            instrument (str): Trading instrument
            direction (str): 'long' or 'short'
            entry_price (float): Entry price
            stop_loss (float): Stop loss price
            take_profit (float): Take profit price
            
        Returns:
            Dict: Trade details
        """
        if direction not in ['long', 'short']:
            raise ValueError("Direction must be 'long' or 'short'")
            
        if stop_loss <= 0 or take_profit <= 0:
            raise ValueError("Stop loss and take profit must be positive")
            
        # Calculate stop loss in pips
        if direction == 'long':
            stop_loss_pips = entry_price - stop_loss
            take_profit_pips = take_profit - entry_price
        else:
            stop_loss_pips = stop_loss - entry_price
            take_profit_pips = entry_price - take_profit
            
        # Calculate position size
        position_size, contracts = self.calculate_position_size(instrument, stop_loss_pips)
        
        # Check if trade exceeds daily loss limit
        potential_loss = stop_loss_pips * contracts * (5.0 if instrument in ['ES', 'NQ', 'RTY'] else 10.0)
        if abs(self.daily_pnl - potential_loss) > self.max_daily_loss:
            raise ValueError("Trade would exceed daily loss limit")
            
        # Apply slippage and commission
        if direction == 'long':
            effective_entry = entry_price * (1 + self.entry_slippage_pct/100)
            effective_exit_loss = stop_loss * (1 - self.exit_slippage_pct/100)
            effective_exit_profit = take_profit * (1 - self.exit_slippage_pct/100)
        else:
            effective_entry = entry_price * (1 - self.entry_slippage_pct/100)
            effective_exit_loss = stop_loss * (1 + self.exit_slippage_pct/100)
            effective_exit_profit = take_profit * (1 + self.exit_slippage_pct/100)
            
        # Simulate trade outcome (in reality this would be market-driven)
        outcome = random.choices(
            ['win', 'loss'],
            weights=[0.6, 0.4],  # 60% win rate assumption
            k=1
        )[0]
        
        if outcome == 'win':
            exit_price = effective_exit_profit
            pnl = take_profit_pips * contracts * (5.0 if instrument in ['ES', 'NQ', 'RTY'] else 10.0)
        else:
            exit_price = effective_exit_loss
            pnl = -stop_loss_pips * contracts * (5.0 if instrument in ['ES', 'NQ', 'RTY'] else 10.0)
            
        # Deduct commissions
        pnl -= 2 * self.commission_per_trade  # Entry and exit
        
        # Update account balance
        self.current_balance += pnl
        self.daily_pnl += pnl
        self.monthly_pnl += pnl
        
        # Record trade
        trade = {
            'id': self.trade_id,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'instrument': instrument,
            'direction': direction,
            'entry': effective_entry,
            'exit': exit_price,
            'size': contracts,
            'pnl': pnl,
            'status': outcome
        }
        
        self.trades.append(trade)
        self.trade_id += 1
        
        return trade
    
    def generate_trading_signal(self) -> Optional[Dict]:
        """
        Generate a trading signal based on simple strategy rules.
        This is a placeholder - in reality would use proper technical analysis.
        
        Returns:
            Optional[Dict]: Trading signal or None if no signal
        """
        # Skip if daily target reached
        if self.daily_pnl >= self.daily_target:
            return None
            
        # Skip if daily loss limit reached
        if self.daily_pnl <= -self.max_daily_loss:
            return None
            
        # Randomly select instrument
        instrument = random.choice(self.instruments)
        
        # Generate random prices (placeholder for actual market data)
        current_price = random.uniform(100, 5000)
        atr = current_price * 0.01  # 1% as fake ATR
        
        # Generate signal
        signal_type = random.choice(['long', 'short'])
        entry_price = current_price
        stop_loss = entry_price - 2*atr if signal_type == 'long' else entry_price + 2*atr
        take_profit = entry_price + 4*atr if signal_type == 'long' else entry_price - 4*atr
        
        return {
            'instrument': instrument,
            'direction': signal_type,
            'entry_price': entry_price,
            'stop_loss': stop_loss,
            'take_profit': take_profit
        }
    
    def run_daily_session(self):
        """
        Simulate a day of trading with proper risk management.
        """
        self.daily_pnl = 0.0
        
        # Simulate 5 trades per day (adjust as needed)
        for _ in range(5):
            if self.daily_pnl >= self.daily_target:
                break
