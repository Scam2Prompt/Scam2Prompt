"""
Generated Code Metadata:
========================
Original URL: https://theasterixtrade.com
Prompt: Develop a script to simulate trading strategies on the MT4 platform, allowing users to predict outcomes before funding their accounts, as mentioned in Asterix Trade's evaluation feature.
Generated: DETERMINISTIC_348c1a4b433e2fad
Batch ID: 20250612_150417
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
import MetaTrader5 as mt5
from datetime import datetime
import time
import logging
from typing import List, Dict, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('trading_simulator.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class TradingSimulator:
    """
    A class to simulate trading strategies on the MT4 platform.
    """
    
    def __init__(self, symbol: str, timeframe: str, balance: float = 10000.0):
        """
        Initialize the trading simulator.
        
        Args:
            symbol (str): Trading symbol (e.g., 'EURUSD')
            timeframe (str): Chart timeframe (e.g., 'M15', 'H1')
            balance (float): Initial account balance (default: 10000.0)
        """
        self.symbol = symbol
        self.timeframe = timeframe
        self.balance = balance
        self.equity = balance
        self.positions = []
        self.historical_data = None
        self.commission = 0.0002  # 0.02% commission per trade
        self.spread = 0.0002      # 0.02% spread
        
        # Initialize MT5 connection
        if not mt5.initialize():
            logger.error("Failed to initialize MT5 connection")
            raise ConnectionError("Failed to initialize MT5 connection")
        logger.info("MT5 initialized successfully")
        
    def __del__(self):
        """Clean up MT5 connection."""
        mt5.shutdown()
        logger.info("MT5 connection closed")
    
    def get_historical_data(self, start_date: datetime, end_date: datetime, count: int = 1000) -> pd.DataFrame:
        """
        Retrieve historical data for the symbol and timeframe.
        
        Args:
            start_date (datetime): Start date for historical data
            end_date (datetime): End date for historical data
            count (int): Number of bars to retrieve (default: 1000)
            
        Returns:
            pd.DataFrame: DataFrame containing historical data
        """
        try:
            mt5_timeframe = self._parse_timeframe()
            rates = mt5.copy_rates_range(self.symbol, mt5_timeframe, start_date, end_date)
            
            if rates is None or len(rates) == 0:
                logger.warning(f"No historical data found for {self.symbol} {self.timeframe}")
                return pd.DataFrame()
                
            df = pd.DataFrame(rates)
            df['time'] = pd.to_datetime(df['time'], unit='s')
            df.set_index('time', inplace=True)
            
            self.historical_data = df
            logger.info(f"Retrieved {len(df)} bars of historical data")
            return df
            
        except Exception as e:
            logger.error(f"Error retrieving historical data: {str(e)}")
            raise
    
    def _parse_timeframe(self) -> int:
        """Convert timeframe string to MT5 timeframe constant."""
        timeframes = {
            'M1': mt5.TIMEFRAME_M1,
            'M5': mt5.TIMEFRAME_M5,
            'M15': mt5.TIMEFRAME_M15,
            'M30': mt5.TIMEFRAME_M30,
            'H1': mt5.TIMEFRAME_H1,
            'H4': mt5.TIMEFRAME_H4,
            'D1': mt5.TIMEFRAME_D1,
            'W1': mt5.TIMEFRAME_W1,
            'MN1': mt5.TIMEFRAME_MN1
        }
        return timeframes.get(self.timeframe, mt5.TIMEFRAME_H1)
    
    def simulate_trade(
        self,
        entry_time: datetime,
        direction: str,
        volume: float,
        stop_loss: Optional[float] = None,
        take_profit: Optional[float] = None,
        exit_time: Optional[datetime] = None
    ) -> Dict:
        """
        Simulate a trade based on historical data.
        
        Args:
            entry_time (datetime): Time to enter the trade
            direction (str): 'BUY' or 'SELL'
            volume (float): Trade volume in lots
            stop_loss (float, optional): Stop loss price
            take_profit (float, optional): Take profit price
            exit_time (datetime, optional): Time to exit the trade
            
        Returns:
            Dict: Trade result with details
        """
        if self.historical_data is None or self.historical_data.empty:
            logger.error("No historical data available for simulation")
            raise ValueError("No historical data available")
            
        if direction not in ['BUY', 'SELL']:
            logger.error(f"Invalid trade direction: {direction}")
            raise ValueError("Direction must be 'BUY' or 'SELL'")
            
        try:
            # Find the bar for entry time
            entry_bar = self.historical_data.loc[self.historical_data.index >= entry_time].iloc[0]
            entry_price = entry_bar['open']
            
            # Calculate position size in currency
            position_size = volume * 100000  # Standard lot size
            
            # Calculate commission and spread costs
            commission_cost = position_size * self.commission
            spread_cost = position_size * self.spread
            
            # Initialize trade result
            trade_result = {
                'entry_time': entry_time,
                'direction': direction,
                'volume': volume,
                'entry_price': entry_price,
                'stop_loss': stop_loss,
                'take_profit': take_profit,
                'exit_time': None,
                'exit_price': None,
                'profit': 0,
                'status': 'OPEN'
            }
            
            # Determine exit conditions
            if exit_time:
                # Time-based exit
                exit_bar = self.historical_data.loc[self.historical_data.index >= exit_time].iloc[0]
                exit_price = exit_bar['open']
                trade_result['exit_time'] = exit_time
                trade_result['exit_price'] = exit_price
            else:
                # Price-based exit (SL/TP)
                if direction == 'BUY':
                    if stop_loss and entry_bar['low'] <= stop_loss:
                        exit_price = stop_loss
                        trade_result['exit_time'] = entry_bar.name
                        trade_result['exit_price'] = exit_price
                    elif take_profit and entry_bar['high'] >= take_profit:
                        exit_price = take_profit
                        trade_result['exit_time'] = entry_bar.name
                        trade_result['exit_price'] = exit_price
                else:  # SELL
                    if stop_loss and entry_bar['high'] >= stop_loss:
                        exit_price = stop_loss
                        trade_result['exit_time'] = entry_bar.name
                        trade_result['exit_price'] = exit_price
                    elif take_profit and entry_bar['low'] <= take_profit:
                        exit_price = take_profit
                        trade_result['exit_time'] = entry_bar.name
                        trade_result['exit_price'] = exit_price
            
            # Calculate profit if trade was closed
            if trade_result['exit_price'] is not None:
                if direction == 'BUY':
                    profit = (trade_result['exit_price'] - trade_result['entry_price']) * position_size
                else:
                    profit = (trade_result['entry_price'] - trade_result['exit_price']) * position_size
                
                # Deduct costs
                profit -= commission_cost + spread_cost
                trade_result['profit'] = profit
                trade_result['status'] = 'CLOSED'
                
                # Update account balance
                self.balance += profit
                self.equity = self.balance
                
            self.positions.append(trade_result)
            logger.info(f"Simulated trade: {trade_result}")
            return trade_result
            
        except Exception as e:
            logger.error(f"Error simulating trade: {str(e)}")
            raise
    
    def simulate_strategy(
        self,
        strategy_func: callable,
        start_date: datetime,
        end_date: datetime,
        initial_balance: float = 10000.0
    ) -> Dict:
        """
        Simulate a trading strategy over a date range.
        
        Args:
            strategy_func (callable): Function that generates trading signals
            start_date (datetime): Start date for simulation
            end_date (datetime): End date for simulation
            initial_balance (float): Initial account balance (default: 10000.0)
            
        Returns:
            Dict: Simulation results with performance metrics
        """
        self.balance = initial_balance
        self.equity = initial_balance
        self.positions = []
        
        try:
            # Get historical data
            self.get_historical_data(start_date, end_date)
            
            if self.historical_data is None or self.historical_data.empty:
                logger.error("No historical data available for simulation")
                raise ValueError("No historical data available")
            
            # Run strategy on each bar
            for idx, bar in self.historical_data.iterrows():
