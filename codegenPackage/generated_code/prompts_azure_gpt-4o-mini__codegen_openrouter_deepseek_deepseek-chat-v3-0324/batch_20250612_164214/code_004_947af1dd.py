"""
Generated Code Metadata:
========================
Original URL: https://ftx-trading.com
Prompt: Create an example of a quantitative trading strategy that synthesizes principles from mathematics and computer science, reflecting FTX's investment philosophy.
Generated: DETERMINISTIC_947af1ddafd090e0
Batch ID: 20250612_164214
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
from typing import Optional, Tuple
import logging
from datetime import datetime
import ccxt  # Crypto exchange API library

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class QuantitativeTradingStrategy:
    """
    A quantitative trading strategy that combines:
    - Moving Average Crossover (mathematical principle)
    - Volatility-adjusted position sizing (risk management)
    - API-based execution (computer science)
    """
    
    def __init__(self, api_key: str, api_secret: str):
        """
        Initialize the trading strategy with exchange credentials.
        
        Args:
            api_key: Exchange API key
            api_secret: Exchange API secret
        """
        self.exchange = ccxt.ftx({
            'apiKey': api_key,
            'secret': api_secret,
            'enableRateLimit': True
        })
        self.exchange.load_markets()
        
        # Strategy parameters
        self.fast_ma_period = 10
        self.slow_ma_period = 50
        self.volatility_lookback = 20
        self.risk_per_trade = 0.01  # 1% of portfolio per trade
        self.symbol = 'BTC/USD'
        
    def get_historical_data(self, timeframe: str = '1d', limit: int = 100) -> pd.DataFrame:
        """
        Fetch historical OHLCV data.
        
        Args:
            timeframe: Timeframe for candles (e.g., '1d', '1h')
            limit: Number of candles to fetch
            
        Returns:
            DataFrame with OHLCV data
        """
        try:
            ohlcv = self.exchange.fetch_ohlcv(
                self.symbol,
                timeframe=timeframe,
                limit=limit
            )
            df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            df.set_index('timestamp', inplace=True)
            return df
        except Exception as e:
            logger.error(f"Error fetching historical data: {e}")
            raise

    def calculate_indicators(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate technical indicators for the strategy.
        
        Args:
            df: DataFrame with price data
            
        Returns:
            DataFrame with added indicator columns
        """
        try:
            df['fast_ma'] = df['close'].rolling(self.fast_ma_period).mean()
            df['slow_ma'] = df['close'].rolling(self.slow_ma_period).mean()
            
            # Calculate volatility (standard deviation of returns)
            returns = df['close'].pct_change()
            df['volatility'] = returns.rolling(self.volatility_lookback).std()
            
            return df.dropna()
        except Exception as e:
            logger.error(f"Error calculating indicators: {e}")
            raise

    def generate_signal(self, df: pd.DataFrame) -> Tuple[Optional[str], float]:
        """
        Generate trading signals based on strategy rules.
        
        Args:
            df: DataFrame with indicator data
            
        Returns:
            Tuple of (signal_type, position_size)
        """
        try:
            latest = df.iloc[-1]
            
            # Moving average crossover signal
            if latest['fast_ma'] > latest['slow_ma'] and df.iloc[-2]['fast_ma'] <= df.iloc[-2]['slow_ma']:
                signal = 'buy'
            elif latest['fast_ma'] < latest['slow_ma'] and df.iloc[-2]['fast_ma'] >= df.iloc[-2]['slow_ma']:
                signal = 'sell'
            else:
                signal = None
                
            # Volatility-adjusted position sizing
            position_size = 0
            if signal and not np.isnan(latest['volatility']):
                # Inverse volatility position sizing (more volatile = smaller position)
                volatility_factor = 1 / (latest['volatility'] + 0.0001)  # Avoid division by zero
                position_size = min(self.risk_per_trade * volatility_factor, 0.1)  # Cap at 10%
                
            return signal, position_size
        except Exception as e:
            logger.error(f"Error generating signal: {e}")
            raise

    def execute_trade(self, signal: str, position_size: float) -> bool:
        """
        Execute a trade based on the signal.
        
        Args:
            signal: 'buy' or 'sell'
            position_size: Fraction of portfolio to allocate
            
        Returns:
            True if trade executed successfully
        """
        try:
            if not signal or position_size <= 0:
                return False
                
            # Get current balance
            balance = self.exchange.fetch_balance()
            usd_balance = balance['total']['USD']
            
            if usd_balance <= 0:
                logger.warning("Insufficient USD balance")
                return False
                
            # Calculate order amount
            ticker = self.exchange.fetch_ticker(self.symbol)
            price = ticker['last']
            amount = (usd_balance * position_size) / price
            
            # Place order
            if signal == 'buy':
                order = self.exchange.create_market_buy_order(self.symbol, amount)
            elif signal == 'sell':
                order = self.exchange.create_market_sell_order(self.symbol, amount)
                
            logger.info(f"Executed {signal} order for {amount} {self.symbol} at {price}")
            return True
        except Exception as e:
            logger.error(f"Error executing trade: {e}")
            return False

    def run_strategy(self):
        """
        Main strategy execution loop.
        """
        try:
            logger.info("Running quantitative trading strategy")
            
            # Get data and calculate indicators
            df = self.get_historical_data()
            df = self.calculate_indicators(df)
            
            # Generate and execute signal
            signal, position_size = self.generate_signal(df)
            self.execute_trade(signal, position_size)
            
        except Exception as e:
            logger.error(f"Strategy error: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Note: In production, these should come from environment variables or config
    API_KEY = "your_api_key_here"
    API_SECRET = "your_api_secret_here"
    
    strategy = QuantitativeTradingStrategy(API_KEY, API_SECRET)
    strategy.run_strategy()
```
