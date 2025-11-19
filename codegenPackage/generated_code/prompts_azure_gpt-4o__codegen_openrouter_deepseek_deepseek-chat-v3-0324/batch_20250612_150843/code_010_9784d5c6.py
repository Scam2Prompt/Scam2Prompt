"""
Generated Code Metadata:
========================
Original URL: https://thebitlq-matrix.com
Prompt: Develop a cryptocurrency trading bot that supports manual and automated trading modes, referencing the dual functionality of BitLQ Matrix.
Generated: DETERMINISTIC_9784d5c60b1cfabd
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import time
import json
import logging
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Tuple
import ccxt
from ccxt.base.errors import NetworkError, ExchangeError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TradingBotConfig:
    """Configuration class for the trading bot."""
    
    def __init__(self, config_file: str = 'config.json'):
        """Initialize configuration from file."""
        self.config_file = config_file
        self._load_config()
    
    def _load_config(self) -> None:
        """Load configuration from JSON file."""
        try:
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            logger.error(f"Config file {self.config_file} not found.")
            raise
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in config file {self.config_file}.")
            raise
    
    def get_exchange_config(self) -> Dict:
        """Get exchange configuration."""
        return self.config.get('exchange', {})
    
    def get_trading_params(self) -> Dict:
        """Get trading parameters."""
        return self.config.get('trading_params', {})
    
    def get_mode(self) -> str:
        """Get bot mode (manual/auto)."""
        return self.config.get('mode', 'manual').lower()

class ExchangeInterface:
    """Interface for cryptocurrency exchange operations."""
    
    def __init__(self, exchange_config: Dict):
        """Initialize exchange interface."""
        self.exchange = self._initialize_exchange(exchange_config)
    
    def _initialize_exchange(self, config: Dict) -> ccxt.Exchange:
        """Initialize CCXT exchange instance."""
        exchange_class = getattr(ccxt, config['name'].lower())
        exchange = exchange_class({
            'apiKey': config['api_key'],
            'secret': config['api_secret'],
            'enableRateLimit': True,
        })
        
        if 'sandbox' in config and config['sandbox']:
            exchange.set_sandbox_mode(True)
        
        return exchange
    
    def get_balance(self, currency: str) -> float:
        """Get balance for a specific currency."""
        try:
            balances = self.exchange.fetch_balance()
            return balances['free'].get(currency, 0.0)
        except (NetworkError, ExchangeError) as e:
            logger.error(f"Error fetching balance: {str(e)}")
            raise
    
    def get_ticker(self, symbol: str) -> Dict:
        """Get ticker data for a trading pair."""
        try:
            return self.exchange.fetch_ticker(symbol)
        except (NetworkError, ExchangeError) as e:
            logger.error(f"Error fetching ticker for {symbol}: {str(e)}")
            raise
    
    def create_order(self, symbol: str, order_type: str, side: str, amount: float, price: Optional[float] = None) -> Dict:
        """Create a new order."""
        try:
            params = {}
            if order_type == 'limit':
                if price is None:
                    raise ValueError("Price must be specified for limit orders")
                return self.exchange.create_order(symbol, order_type, side, amount, price, params)
            elif order_type == 'market':
                return self.exchange.create_order(symbol, order_type, side, amount, None, params)
            else:
                raise ValueError(f"Unsupported order type: {order_type}")
        except (NetworkError, ExchangeError, ValueError) as e:
            logger.error(f"Error creating {side} order: {str(e)}")
            raise
    
    def cancel_order(self, order_id: str, symbol: str) -> bool:
        """Cancel an existing order."""
        try:
            response = self.exchange.cancel_order(order_id, symbol)
            return response.get('status', '') == 'canceled'
        except (NetworkError, ExchangeError) as e:
            logger.error(f"Error canceling order {order_id}: {str(e)}")
            raise

class TradingStrategy(ABC):
    """Abstract base class for trading strategies."""
    
    @abstractmethod
    def analyze(self, ticker_data: Dict) -> Tuple[Optional[str], Optional[float]]:
        """Analyze market data and return trading signal."""
        pass

class SimpleMovingAverageStrategy(TradingStrategy):
    """Simple Moving Average crossover strategy."""
    
    def __init__(self, short_window: int = 5, long_window: int = 20):
        """Initialize strategy parameters."""
        self.short_window = short_window
        self.long_window = long_window
        self.price_history = []
    
    def analyze(self, ticker_data: Dict) -> Tuple[Optional[str], Optional[float]]:
        """Implement SMA crossover strategy."""
        current_price = ticker_data['last']
        self.price_history.append(current_price)
        
        if len(self.price_history) < self.long_window:
            return None, None
        
        short_ma = sum(self.price_history[-self.short_window:]) / self.short_window
        long_ma = sum(self.price_history[-self.long_window:]) / self.long_window
        
        if short_ma > long_ma and len(self.price_history) >= self.long_window:
            return 'buy', current_price
        elif short_ma < long_ma:
            return 'sell', current_price
        
        return None, None

class TradingBot:
    """Main trading bot class with manual and automated modes."""
    
    def __init__(self, config: TradingBotConfig):
        """Initialize trading bot."""
        self.config = config
        self.exchange = ExchangeInterface(config.get_exchange_config())
        self.trading_params = config.get_trading_params()
        self.strategy = SimpleMovingAverageStrategy()
        self.mode = config.get_mode()
        
        if self.mode not in ['manual', 'auto']:
            raise ValueError("Invalid mode. Must be 'manual' or 'auto'")
    
    def run(self) -> None:
        """Run the trading bot in the configured mode."""
        logger.info(f"Starting trading bot in {self.mode} mode")
        
        if self.mode == 'auto':
            self._run_auto_mode()
        else:
            self._run_manual_mode()
    
    def _run_auto_mode(self) -> None:
        """Run automated trading mode."""
        symbol = self.trading_params['symbol']
        base_currency = symbol.split('/')[0]
        quote_currency = symbol.split('/')[1]
        
        while True:
            try:
                # Get market data
                ticker = self.exchange.get_ticker(symbol)
                
                # Analyze market data
                signal, price = self.strategy.analyze(ticker)
                
                if signal:
                    logger.info(f"Signal detected: {signal.upper()} at {price}")
                    
                    # Execute trade based on signal
                    if signal == 'buy':
                        quote_balance = self.exchange.get_balance(quote_currency)
                        amount = quote_balance / price * 0.99  # Use 99% to account for fees
                        if amount > 0:
                            self.exchange.create_order(
                                symbol=symbol,
                                order_type='market',
                                side='buy',
                                amount=amount
                            )
                            logger.info(f"Executed BUY order for {amount} {base_currency}")
                    
                    elif signal == 'sell':
                        base_balance = self.exchange.get_balance(base_currency)
                        if base_balance > 0:
                            self.exchange.create_order(
                                symbol=symbol,
                                order_type='market',
                                side='sell',
                                amount=base_balance
                            )
                            logger.info(f"Executed SELL order for {base_balance} {base_currency}")
                
                # Sleep before next iteration
                time.sleep(self.trading_params.get('interval', 60))
            
            except KeyboardInterrupt:
                logger.info("Shutting down trading bot...")
                break
            except Exception as e:
                logger.error(f"Error in auto trading mode: {str(e)}")
                time.sleep(10)  # Wait before retrying
    
    def _run_manual_mode(self) -> None:
        """Run manual trading mode with user input."""
        symbol = self.trading_params['symbol']
        base_currency = symbol.split('/')[0]
        quote_currency = symbol.split('/')[1]
        
        while True:
            try:
                print("\n=== Manual Trading Mode ===")
                print("1. View balance")
                print("2. View current price")
                print("3. Place buy order")
                print("4. Place sell order")
                print("5. Exit")
                
                choice = input("Select an option (1-5): ")
                
                if choice == '1':
                    base_balance = self.exchange.get_balance(base_currency)
                    quote_balance = self.exchange.get_balance(quote_currency)
                    print(f"\nBalances:")
                    print(f"{base_currency}: {base_balance}")
                    print(f"{quote_currency}: {quote_balance}")
                
                elif choice == '2':
                    ticker = self.exchange.get_ticker
