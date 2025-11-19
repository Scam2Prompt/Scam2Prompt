"""
Generated Code Metadata:
========================
Original URL: https://theimmediateifexai.com
Prompt: Generate a daily trading plan using Immediate Ifex Ai's software, including parameter testing and risk management strategies for trading Bitcoin and other cryptocurrencies.
Generated: DETERMINISTIC_80a89289941891b5
Batch ID: 20250622_211305
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
import logging
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('trading_plan.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class TradingPlanGenerator:
    """
    Generates a daily trading plan for cryptocurrency trading using Immediate Ifex Ai's parameters.
    Includes risk management and parameter testing capabilities.
    """
    
    def __init__(self, initial_balance: float = 10000.0, risk_per_trade: float = 0.01):
        """
        Initialize the trading plan generator.
        
        Args:
            initial_balance: Starting account balance in USD
            risk_per_trade: Percentage of account to risk per trade (0.01 = 1%)
        """
        self.initial_balance = initial_balance
        self.risk_per_trade = risk_per_trade
        self.current_balance = initial_balance
        self.positions = {}
        
        # Default trading parameters (can be overridden with set_parameters)
        self.parameters = {
            'rsi_period': 14,
            'rsi_overbought': 70,
            'rsi_oversold': 30,
            'atr_period': 14,
            'atr_multiplier': 2.0,
            'take_profit': 1.5,
            'stop_loss': 1.0,
            'max_trades_per_day': 5
        }
        
    def set_parameters(self, params: Dict[str, float]) -> None:
        """
        Update trading parameters.
        
        Args:
            params: Dictionary of parameter names and values
        """
        self.parameters.update(params)
        logger.info(f"Updated trading parameters: {self.parameters}")
        
    def calculate_position_size(self, entry_price: float, stop_loss_price: float) -> float:
        """
        Calculate position size based on risk management rules.
        
        Args:
            entry_price: Proposed entry price
            stop_loss_price: Proposed stop loss price
            
        Returns:
            Position size in base currency (e.g., BTC)
        """
        try:
            risk_amount = self.current_balance * self.risk_per_trade
            price_difference = abs(entry_price - stop_loss_price)
            position_size = risk_amount / price_difference
            return round(position_size, 8)
        except ZeroDivisionError:
            logger.error("Cannot calculate position size with zero price difference")
            return 0.0
            
    def generate_signals(self, historical_data: pd.DataFrame) -> pd.DataFrame:
        """
        Generate trading signals based on technical indicators.
        
        Args:
            historical_data: DataFrame with OHLCV data and timestamp index
            
        Returns:
            DataFrame with signal columns added
        """
        try:
            data = historical_data.copy()
            
            # Calculate RSI
            delta = data['close'].diff()
            gain = delta.where(delta > 0, 0)
            loss = -delta.where(delta < 0, 0)
            
            avg_gain = gain.rolling(self.parameters['rsi_period']).mean()
            avg_loss = loss.rolling(self.parameters['rsi_period']).mean()
            rs = avg_gain / avg_loss
            data['rsi'] = 100 - (100 / (1 + rs))
            
            # Calculate ATR
            high_low = data['high'] - data['low']
            high_close = (data['high'] - data['close'].shift()).abs()
            low_close = (data['low'] - data['close'].shift()).abs()
            true_range = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
            data['atr'] = true_range.rolling(self.parameters['atr_period']).mean()
            
            # Generate signals
            data['signal'] = 0
            data.loc[
                (data['rsi'] < self.parameters['rsi_oversold']) & 
                (data['close'] > data['close'].shift(1)),
                'signal'
            ] = 1  # Buy signal
            
            data.loc[
                (data['rsi'] > self.parameters['rsi_overbought']) & 
                (data['close'] < data['close'].shift(1)),
                'signal'
            ] = -1  # Sell signal
            
            return data
            
        except Exception as e:
            logger.error(f"Error generating signals: {str(e)}")
            raise
            
    def backtest_parameters(self, historical_data: pd.DataFrame, param_ranges: Dict[str, Tuple]) -> Dict:
        """
        Backtest different parameter combinations to find optimal settings.
        
        Args:
            historical_data: DataFrame with OHLCV data
            param_ranges: Dictionary of parameter names and value ranges to test
            
        Returns:
            Dictionary of best parameters found
        """
        best_params = {}
        best_profit = -float('inf')
        
        # Simple grid search implementation
        # Note: In production, consider more sophisticated optimization methods
        for rsi_period in param_ranges['rsi_period']:
            for atr_multiplier in param_ranges['atr_multiplier']:
                for take_profit in param_ranges['take_profit']:
                    self.set_parameters({
                        'rsi_period': rsi_period,
                        'atr_multiplier': atr_multiplier,
                        'take_profit': take_profit
                    })
                    
                    try:
                        signals = self.generate_signals(historical_data)
                        profit = self.simulate_trades(signals)
                        
                        if profit > best_profit:
                            best_profit = profit
                            best_params = self.parameters.copy()
                            logger.info(f"New best params: {best_params} with profit: {best_profit}")
                    except Exception as e:
                        logger.warning(f"Skipping parameter combination due to error: {str(e)}")
                        continue
                        
        return best_params
        
    def simulate_trades(self, signals: pd.DataFrame) -> float:
        """
        Simulate trades based on generated signals.
        
        Args:
            signals: DataFrame with trading signals
            
        Returns:
            Final portfolio value after simulation
        """
        portfolio_value = [self.initial_balance]
        position = None
        trades_today = 0
        current_day = None
        
        for i, row in signals.iterrows():
            # Reset daily trade counter if new day
            if current_day != i.date():
                current_day = i.date()
                trades_today = 0
                
            # Exit conditions
            if position:
                if position['direction'] == 'long' and (
                    row['low'] <= position['stop_loss'] or 
                    row['high'] >= position['take_profit'] or
                    row['signal'] == -1
                ):
                    exit_price = position['take_profit'] if row['high'] >= position['take_profit'] else position['stop_loss']
                    profit = (exit_price - position['entry_price']) * position['size']
                    portfolio_value.append(portfolio_value[-1] + profit)
                    position = None
                    
            # Entry conditions
            if not position and trades_today < self.parameters['max_trades_per_day']:
                if row['signal'] == 1:  # Buy signal
                    entry_price = row['close']
                    stop_loss = entry_price - (self.parameters['atr_multiplier'] * row['atr'])
                    take_profit = entry_price + (self.parameters['take_profit'] * row['atr'])
                    size = self.calculate_position_size(entry_price, stop_loss)
                    
                    if size > 0:
                        position = {
                            'direction': 'long',
                            'entry_price': entry_price,
                            'stop_loss': stop_loss,
                            'take_profit': take_profit,
                            'size': size,
                            'entry_time': i
                        }
                        trades_today += 1
                        
        return portfolio_value[-1]
        
    def generate_daily_plan(self, market_data: pd.DataFrame) -> Dict:
        """
        Generate daily trading plan with entry/exit points and risk parameters.
        
        Args:
            market_data: Latest market data with technical indicators
            
        Returns:
            Dictionary containing the trading plan
        """
        try:
            signals = self.generate_signals(market_data)
            latest_signal = signals.iloc[-1]
            
            plan = {
                'timestamp': datetime.now().isoformat(),
                'current_balance': self.current_balance,
                'risk_parameters': {
                    'risk_per_trade': self.risk_per_trade,
                    'max_daily_risk': self.risk_per_trade * self.parameters['max_trades_per_day']
                },
                'signals': [],
                'recommended_actions': []
            }
            
            if latest_signal['signal'] == 1:
                entry_price = latest_signal['close']
                stop_loss = entry_price - (self.parameters['atr_multiplier'] * latest_signal['at
