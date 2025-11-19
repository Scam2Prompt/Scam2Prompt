"""
Generated Code Metadata:
========================
Original URL: https://immediate-3000-folex.com
Prompt: "Create a trading plan using Immediate 3000 Folex's strategy tester feature for optimizing performance across various asset types."
Generated: DETERMINISTIC_1e7abcd367a03432
Batch ID: 20250622_211305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import numpy as np
import pandas as pd
from datetime import datetime
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TradingPlan:
    """
    A trading plan implementation for Immediate 3000 Folex's strategy tester.
    Optimizes performance across various asset types.
    """
    
    def __init__(self, initial_capital: float = 10000.0):
        """
        Initialize the trading plan with initial capital.
        
        Args:
            initial_capital (float): Starting capital for the strategy. Defaults to 10000.0.
        """
        self.initial_capital = initial_capital
        self.current_capital = initial_capital
        self.positions = {}  # Tracks open positions: {asset: {'quantity': qty, 'entry_price': price}}
        self.trade_history = []  # Records all trades
        self.performance_metrics = {}  # Stores performance metrics
        
    def optimize_strategy(
        self,
        asset_data: Dict[str, pd.DataFrame],
        risk_per_trade: float = 0.01,
        max_position_size: float = 0.1,
        stop_loss_pct: float = 0.05,
        take_profit_pct: float = 0.1
    ) -> Dict[str, float]:
        """
        Optimize trading strategy across multiple assets.
        
        Args:
            asset_data (Dict[str, pd.DataFrame]): Dictionary of asset dataframes with OHLCV data
            risk_per_trade (float): Percentage of capital to risk per trade. Defaults to 0.01 (1%).
            max_position_size (float): Maximum percentage of capital per position. Defaults to 0.1 (10%).
            stop_loss_pct (float): Stop loss percentage. Defaults to 0.05 (5%).
            take_profit_pct (float): Take profit percentage. Defaults to 0.1 (10%).
            
        Returns:
            Dict[str, float]: Performance metrics for the strategy
        """
        try:
            if not asset_data:
                raise ValueError("Asset data cannot be empty")
                
            for asset, data in asset_data.items():
                self._process_asset(
                    asset,
                    data,
                    risk_per_trade,
                    max_position_size,
                    stop_loss_pct,
                    take_profit_pct
                )
            
            self._calculate_performance_metrics()
            return self.performance_metrics
            
        except Exception as e:
            logger.error(f"Error optimizing strategy: {str(e)}")
            raise

    def _process_asset(
        self,
        asset: str,
        data: pd.DataFrame,
        risk_per_trade: float,
        max_position_size: float,
        stop_loss_pct: float,
        take_profit_pct: float
    ) -> None:
        """
        Process trading signals for a single asset.
        
        Args:
            asset (str): Asset symbol
            data (pd.DataFrame): OHLCV data for the asset
            risk_per_trade (float): Risk per trade percentage
            max_position_size (float): Max position size percentage
            stop_loss_pct (float): Stop loss percentage
            take_profit_pct (float): Take profit percentage
        """
        try:
            # Generate trading signals (example: simple moving average crossover)
            data['sma_20'] = data['close'].rolling(window=20).mean()
            data['sma_50'] = data['close'].rolling(window=50).mean()
            data['signal'] = np.where(data['sma_20'] > data['sma_50'], 1, -1)
            
            for index, row in data.iterrows():
                if row['signal'] == 1 and asset not in self.positions:
                    self._enter_position(asset, row, risk_per_trade, max_position_size)
                elif row['signal'] == -1 and asset in self.positions:
                    self._exit_position(asset, row, take_profit_pct, stop_loss_pct)
                    
        except Exception as e:
            logger.error(f"Error processing asset {asset}: {str(e)}")
            raise

    def _enter_position(
        self,
        asset: str,
        row: pd.Series,
        risk_per_trade: float,
        max_position_size: float
    ) -> None:
        """
        Enter a new position for an asset.
        
        Args:
            asset (str): Asset symbol
            row (pd.Series): Current row of data
            risk_per_trade (float): Risk per trade percentage
            max_position_size (float): Max position size percentage
        """
        try:
            position_size = min(
                self.current_capital * max_position_size,
                self.current_capital * risk_per_trade / 0.01  # Standardize risk
            )
            
            if position_size <= 0:
                return
                
            quantity = position_size / row['close']
            self.positions[asset] = {
                'quantity': quantity,
                'entry_price': row['close'],
                'entry_time': row.name  # Assuming index is datetime
            }
            self.current_capital -= position_size
            
            # Record trade
            self.trade_history.append({
                'asset': asset,
                'action': 'BUY',
                'quantity': quantity,
                'price': row['close'],
                'timestamp': row.name,
                'capital_remaining': self.current_capital
            })
            
            logger.info(f"Entered position in {asset}: {quantity} shares at {row['close']}")
            
        except Exception as e:
            logger.error(f"Error entering position for {asset}: {str(e)}")
            raise

    def _exit_position(
        self,
        asset: str,
        row: pd.Series,
        take_profit_pct: float,
        stop_loss_pct: float
    ) -> None:
        """
        Exit an existing position for an asset.
        
        Args:
            asset (str): Asset symbol
            row (pd.Series): Current row of data
            take_profit_pct (float): Take profit percentage
            stop_loss_pct (float): Stop loss percentage
        """
        try:
            position = self.positions[asset]
            entry_price = position['entry_price']
            current_price = row['close']
            
            # Check for stop loss or take profit
            if (current_price <= entry_price * (1 - stop_loss_pct) or
                current_price >= entry_price * (1 + take_profit_pct)):
                
                profit_loss = (current_price - entry_price) * position['quantity']
                self.current_capital += position['quantity'] * current_price
                
                # Record trade
                self.trade_history.append({
                    'asset': asset,
                    'action': 'SELL',
                    'quantity': position['quantity'],
                    'price': current_price,
                    'timestamp': row.name,
                    'capital_remaining': self.current_capital,
