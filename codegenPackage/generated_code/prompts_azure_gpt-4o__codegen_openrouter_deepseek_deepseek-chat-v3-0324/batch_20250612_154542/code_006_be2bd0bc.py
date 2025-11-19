"""
Generated Code Metadata:
========================
Original URL: https://mcoinners.com
Prompt: Write a Python program that uses trading bot algorithms to simulate cryptocurrency trading on digital currency stock markets, inspired by the trading bot usage described on mcoinners.com.
Generated: DETERMINISTIC_be2bd0bc4696f0b5
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import ccxt
import pandas as pd
import numpy as np
from time import sleep
from datetime import datetime
import logging
from typing import Dict, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('trading_bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class TradingBot:
    def __init__(self, exchange_id: str, api_key: str, secret: str, symbol: str):
        """
        Initialize the trading bot with exchange credentials and trading pair.
        
        Args:
            exchange_id: Exchange identifier (e.g., 'binance')
            api_key: Exchange API key
            secret: Exchange API secret
            symbol: Trading pair (e.g., 'BTC/USDT')
        """
        self.exchange_id = exchange_id
        self.symbol = symbol
        self.api_key = api_key
        self.secret = secret
        
        try:
            # Initialize exchange connection
            exchange_class = getattr(ccxt, exchange_id)
            self.exchange = exchange_class({
                'apiKey': api_key,
                'secret': secret,
                'enableRateLimit': True,
            })
            logger.info(f"Connected to {exchange_id} exchange")
        except Exception as e:
            logger.error(f"Error initializing exchange: {e}")
            raise

    def get_historical_data(self, timeframe: str = '1h', limit: int = 100) -> pd.DataFrame:
        """
        Fetch historical OHLCV data from the exchange.
        
        Args:
            timeframe: Timeframe for candles (e.g., '1h', '4h', '1d')
            limit: Number of candles to fetch
            
        Returns:
            DataFrame containing OHLCV data
        """
        try:
            ohlcv = self.exchange.fetch_ohlcv(self.symbol, timeframe, limit=limit)
            df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            df.set_index('timestamp', inplace=True)
            return df
        except Exception as e:
            logger.error(f"Error fetching historical data: {e}")
            raise

    def calculate_indicators(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate technical indicators for trading strategy.
        
        Args:
            df: DataFrame with OHLCV data
            
        Returns:
            DataFrame with added indicator columns
        """
        try:
            # Simple Moving Averages
            df['sma_20'] = df['close'].rolling(window=20).mean()
            df['sma_50'] = df['close'].rolling(window=50).mean()
            
            # Relative Strength Index
            delta = df['close'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
            rs = gain / loss
            df['rsi'] = 100 - (100 / (1 + rs))
            
            # Bollinger Bands
            df['bb_upper'] = df['sma_20'] + (2 * df['close'].rolling(window=20).std())
            df['bb_lower'] = df['sma_20'] - (2 * df['close'].rolling(window=20).std())
            
            return df
        except Exception as e:
            logger.error(f"Error calculating indicators: {e}")
            raise

    def get_current_price(self) -> float:
        """
        Get the current price of the trading pair.
        
        Returns:
            Current price as float
        """
        try:
            ticker = self.exchange.fetch_ticker(self.symbol)
            return ticker['last']
        except Exception as e:
            logger.error(f"Error fetching current price: {e}")
            raise

    def get_balance(self, currency: str) -> float:
        """
        Get available balance for a specific currency.
        
        Args:
            currency: Currency symbol (e.g., 'BTC', 'USDT')
            
        Returns:
            Available balance as float
        """
        try:
            balance = self.exchange.fetch_balance()
            return balance['free'].get(currency, 0.0)
        except Exception as e:
            logger.error(f"Error fetching balance: {e}")
            raise

    def create_order(self, side: str, amount: float, price: Optional[float] = None) -> Dict:
        """
        Create a market or limit order.
        
        Args:
            side: 'buy' or 'sell'
            amount: Amount to trade
            price: Price for limit order (None for market order)
            
        Returns:
            Order information dictionary
        """
        try:
            order_type = 'limit' if price else 'market'
            order = self.exchange.create_order(
                symbol=self.symbol,
                type=order_type,
                side=side,
                amount=amount,
                price=price
            )
            logger.info(f"Created {order_type} {side} order: {order}")
            return order
        except Exception as e:
            logger.error(f"Error creating {side} order: {e}")
            raise

    def check_order_status(self, order_id: str) -> Dict:
        """
        Check the status of an order.
        
        Args:
            order_id: Order ID to check
            
        Returns:
            Order status dictionary
        """
        try:
            return self.exchange.fetch_order(order_id, self.symbol)
        except Exception as e:
            logger.error(f"Error checking order status: {e}")
            raise

    def trading_strategy(self, df: pd.DataFrame) -> Tuple[Optional[str], Optional[float]]:
        """
        Implement a simple moving average crossover strategy.
        
        Args:
            df: DataFrame with OHLCV and indicator data
            
        Returns:
            Tuple of (action, price) where action is 'buy', 'sell', or None
        """
        try:
            last_row = df.iloc[-1]
            prev_row = df.iloc[-2]
            
            # SMA Crossover strategy
            if prev_row['sma_20'] <= prev_row['sma_50'] and last_row['sma_20'] > last_row['sma_50']:
                return 'buy', None  # Market buy
            elif prev_row['sma_20'] >= prev_row['sma_50'] and last_row['sma_20'] < last_row['sma_50']:
                return 'sell', None  # Market sell
                
            # RSI overbought/oversold
            elif last_row['rsi'] > 70:
                return 'sell', last_row['bb_upper']  # Limit sell at upper BB
            elif last_row['rsi'] < 30:
                return 'buy', last_row['bb_lower']  # Limit buy at lower BB
                
            return None, None
        except Exception as e:
            logger.error(f"Error in trading strategy: {e}")
            return None, None

    def run(self, timeframe: str = '1h', trade_amount: float = 0.01):
        """
        Main trading bot execution loop.
        
        Args:
            timeframe: Timeframe for analysis
            trade_amount: Base amount to trade (in quote currency)
        """
        logger.info(f"Starting trading bot for {self.symbol} on {self.exchange_id}")
        
        while True:
            try:
                # Get market data
                df = self.get_historical_data(timeframe)
                df = self.calculate_indicators(df)
                
                # Get current price and balances
                current_price = self.get_current_price()
                base_currency, quote_currency = self.symbol.split('/')
                base_balance = self.get_balance(base_currency)
                quote_balance = self.get_balance(quote_currency)
                
                logger.info(f"Current price: {current_price:.2f} | {base_currency} balance: {base_balance:.6f} | {quote_currency} balance: {quote_balance:.2f}")
                
                # Determine trading action
                action, price = self.trading_strategy(df)
                
                if action == 'buy' and quote_balance >= trade_amount:
                    amount = trade_amount / (price if price else current_price)
                    self.create_order('buy', amount, price)
                    
                elif action == 'sell' and base_balance >= trade_amount:
                    amount = trade_amount if base_currency == quote_currency else base_balance
                    self.create_order('sell', amount, price)
                
                # Wait for next candle
                sleep(self.exchange.rateLimit / 1000)
                
            except KeyboardInterrupt:
                logger.info("Shutting down trading bot...")
                break
            except Exception as e:
                logger.error(f"Error in main loop: {e}")
                sleep(60)  # Wait before retrying

if __name__ == "__main__":
    # Configuration - replace with your actual API keys
    CONFIG = {
        'exchange_id': 'binance',
        '
