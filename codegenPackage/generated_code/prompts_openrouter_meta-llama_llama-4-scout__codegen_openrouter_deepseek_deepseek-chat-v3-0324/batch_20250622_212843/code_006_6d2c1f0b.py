"""
Generated Code Metadata:
========================
Original URL: https://www.apps-axiomtrade.com
Prompt: Write a trading simulator using Python, incorporating technical indicators such as Moving Averages, RSI, and Bollinger Bands, to help beginners practice trading strategies.
Generated: DETERMINISTIC_6d2c1f0bd1c59bc7
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random
from enum import Enum

class TradeAction(Enum):
    BUY = 1
    SELL = 2
    HOLD = 3

class TradingSimulator:
    """
    A trading simulator that allows users to practice trading strategies using technical indicators.
    """
    
    def __init__(self, initial_balance=10000, commission=0.001):
        """
        Initialize the trading simulator.
        
        Args:
            initial_balance (float): Starting balance in USD
            commission (float): Trading commission per trade (percentage)
        """
        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.commission = commission
        self.portfolio = {}
        self.trade_history = []
        self.data = None
        
    def generate_random_data(self, days=365, start_price=100, volatility=0.02):
        """
        Generate random price data for simulation.
        
        Args:
            days (int): Number of days to generate data for
            start_price (float): Starting price of the asset
            volatility (float): Daily price volatility
            
        Returns:
            pd.DataFrame: Generated price data with dates
        """
        dates = [datetime.now() - timedelta(days=x) for x in range(days, 0, -1)]
        prices = [start_price]
        
        for _ in range(1, days):
            change = random.uniform(-volatility, volatility)
            prices.append(prices[-1] * (1 + change))
            
        self.data = pd.DataFrame({
            'Date': dates,
            'Price': prices,
            'Open': [p * random.uniform(0.99, 1.01) for p in prices],
            'High': [p * random.uniform(1.0, 1.02) for p in prices],
            'Low': [p * random.uniform(0.98, 1.0) for p in prices],
            'Close': prices
        })
        
        self._calculate_indicators()
        return self.data
    
    def _calculate_indicators(self):
        """Calculate technical indicators for the generated data."""
        if self.data is None:
            raise ValueError("No data available. Generate or load data first.")
            
        # Simple Moving Averages
        self.data['SMA_20'] = self.data['Close'].rolling(window=20).mean()
        self.data['SMA_50'] = self.data['Close'].rolling(window=50).mean()
        
        # Relative Strength Index (RSI)
        delta = self.data['Close'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        
        avg_gain = gain.rolling(window=14).mean()
        avg_loss = loss.rolling(window=14).mean()
        
        rs = avg_gain / avg_loss
        self.data['RSI'] = 100 - (100 / (1 + rs))
        
        # Bollinger Bands
        rolling_mean = self.data['Close'].rolling(window=20).mean()
        rolling_std = self.data['Close'].rolling(window=20).std()
        
        self.data['BB_upper'] = rolling_mean + (rolling_std * 2)
        self.data['BB_lower'] = rolling_mean - (rolling_std * 2)
        
    def load_data(self, file_path):
        """
        Load trading data from a CSV file.
        
        Args:
            file_path (str): Path to the CSV file containing trading data
        """
        try:
            self.data = pd.read_csv(file_path)
            if 'Date' in self.data.columns:
                self.data['Date'] = pd.to_datetime(self.data['Date'])
            self._calculate_indicators()
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")
    
    def execute_trade(self, action, symbol, quantity, price):
        """
        Execute a trade based on the given action.
        
        Args:
            action (TradeAction): BUY, SELL, or HOLD
            symbol (str): Asset symbol
            quantity (float): Amount to trade
            price (float): Current price of the asset
            
        Returns:
            bool: True if trade was successful, False otherwise
        """
        if action == TradeAction.HOLD:
            return True
            
        total_cost = quantity * price
        commission_cost = total_cost * self.commission
        
        if action == TradeAction.BUY:
            if self.balance < (total_cost + commission_cost):
                return False
                
            self.balance -= (total_cost + commission_cost)
            if symbol in self.portfolio:
                self.portfolio[symbol] += quantity
            else:
                self.portfolio[symbol] = quantity
                
        elif action == TradeAction.SELL:
            if symbol not in self.portfolio or self.portfolio[symbol] < quantity:
                return False
                
            self.balance += (total_cost - commission_cost)
            self.portfolio[symbol] -= quantity
            if self.portfolio[symbol] == 0:
                del self.portfolio[symbol]
                
        self.trade_history.append({
            'date': datetime.now(),
            'action': action,
            'symbol': symbol,
            'quantity': quantity,
            'price': price,
            'commission': commission_cost,
            'balance': self.balance
        })
        
        return True
    
    def moving_average_crossover(self, symbol, current_price, current_date):
        """
        Simple moving average crossover strategy.
        
        Args:
            symbol (str): Asset symbol
            current_price (float): Current price of the asset
            current_date (datetime): Current date
            
        Returns:
            TradeAction: Suggested trade action
        """
        if self.data is None:
            return TradeAction.HOLD
            
        current_data = self.data[self.data['Date'] <= current_date].tail(50)
        if len(current_data) < 50:
            return TradeAction.HOLD
            
        sma_20 = current_data['SMA_20'].iloc[-1]
        sma_50 = current_data['SMA_50'].iloc[-1]
        
        # Buy when short-term MA crosses above long-term MA
        if sma_20 > sma_50 and current_data['SMA_20'].iloc[-2] <= current_data['SMA_50'].iloc[-2]:
            return TradeAction.BUY
        # Sell when short-term MA crosses below long-term MA
        elif sma_20 < sma_50 and current_data['SMA_20'].iloc[-2] >= current_data['SMA_50'].iloc[-2]:
            return TradeAction.SELL
            
        return TradeAction.HOLD
    
    def rsi_strategy(self, symbol, current_price, current_date):
        """
        RSI-based trading strategy.
        
        Args:
            symbol (str): Asset symbol
            current_price (float): Current price of the asset
            current_date (datetime): Current date
            
        Returns:
            TradeAction: Suggested trade action
        """
        if self.data is None:
            return TradeAction.HOLD
            
        current_data = self.data[self.data['Date'] <= current_date].tail(15)
        if len(current_data) < 15:
            return TradeAction.HOLD
            
        rsi = current_data['RSI'].iloc[-1]
        
        # Buy when RSI is below 30 (oversold)
        if rsi < 30:
            return TradeAction.BUY
        # Sell when RSI is above 70 (overbought)
        elif rsi > 70:
            return TradeAction.SELL
            
        return TradeAction.HOLD
    
    def bollinger_bands_strategy(self, symbol, current_price, current_date):
        """
        Bollinger Bands trading strategy.
        
        Args:
            symbol (str): Asset symbol
            current_price (float): Current price of the asset
            current_date (datetime): Current date
            
        Returns:
            TradeAction: Suggested trade action
        """
        if self.data is None:
            return TradeAction.HOLD
            
        current_data = self.data[self.data['Date'] <= current_date].tail(20)
        if len(current_data) < 20:
            return TradeAction.HOLD
            
        bb_lower = current_data['BB_lower'].iloc[-1]
        bb_upper = current_data['BB_upper'].iloc[-1]
        
        # Buy when price is below lower band
        if current_price < bb_lower:
            return TradeAction.BUY
        # Sell when price is above upper band
        elif current_price > bb_upper:
            return TradeAction.SELL
            
        return TradeAction.HOLD
    
    def run_simulation(self, symbol='STOCK', strategy='moving_average', days=None):
        """
        Run a trading simulation using the selected strategy.
        
        Args:
            symbol (str): Asset symbol to trade
            strategy (str): Trading strategy to use
            days (int): Number of days to simulate (None for all data)
            
        Returns:
            dict: Simulation results including final balance and performance metrics
        """
        if self.data is None:
            self.generate_random
