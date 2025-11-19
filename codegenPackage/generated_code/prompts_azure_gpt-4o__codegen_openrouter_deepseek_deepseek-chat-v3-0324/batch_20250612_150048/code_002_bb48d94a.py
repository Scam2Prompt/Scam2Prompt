"""
Generated Code Metadata:
========================
Original URL: https://inditexcapitalsoftware.com
Prompt: Create a script that simulates a cryptocurrency trading platform with customizable autonomy and assistance levels, inspired by the features of the Inditex Capital app.
Generated: DETERMINISTIC_bb48d94ad5310b38
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from enum import Enum
from typing import Dict, List, Optional, Tuple


class AutonomyLevel(Enum):
    """Enum representing different autonomy levels for trading."""
    FULL_AUTONOMY = 1
    SEMI_AUTONOMY = 2
    MANUAL = 3


class AssistanceLevel(Enum):
    """Enum representing different assistance levels for trading."""
    HIGH = 1
    MEDIUM = 2
    LOW = 3


class Cryptocurrency:
    """Class representing a cryptocurrency with its properties."""
    
    def __init__(self, symbol: str, name: str, current_price: float, volatility: float):
        """
        Initialize a cryptocurrency.
        
        Args:
            symbol: Ticker symbol of the cryptocurrency (e.g., BTC)
            name: Full name of the cryptocurrency (e.g., Bitcoin)
            current_price: Current price in USD
            volatility: Volatility factor (0-1)
        """
        self.symbol = symbol
        self.name = name
        self.current_price = current_price
        self.volatility = volatility
        self.price_history = [current_price]
    
    def update_price(self) -> None:
        """Update the price based on volatility and random market factors."""
        change_percent = (random.random() - 0.5) * 2 * self.volatility
        self.current_price *= (1 + change_percent)
        self.current_price = max(0.01, self.current_price)  # Prevent negative prices
        self.price_history.append(self.current_price)


class Portfolio:
    """Class representing a user's portfolio."""
    
    def __init__(self, initial_balance: float = 10000.0):
        """
        Initialize a portfolio with an initial balance.
        
        Args:
            initial_balance: Starting balance in USD
        """
        self.balance = initial_balance
        self.holdings: Dict[str, float] = {}  # symbol: quantity
        self.trade_history: List[Dict] = []
    
    def add_holding(self, symbol: str, quantity: float) -> None:
        """Add cryptocurrency to holdings."""
        if symbol in self.holdings:
            self.holdings[symbol] += quantity
        else:
            self.holdings[symbol] = quantity
    
    def remove_holding(self, symbol: str, quantity: float) -> None:
        """Remove cryptocurrency from holdings."""
        if symbol not in self.holdings or self.holdings[symbol] < quantity:
            raise ValueError("Insufficient holdings")
        self.holdings[symbol] -= quantity
        if self.holdings[symbol] <= 0:
            del self.holdings[symbol]
    
    def record_trade(self, symbol: str, action: str, quantity: float, price: float) -> None:
        """Record a trade in the trade history."""
        self.trade_history.append({
            'timestamp': time.time(),
            'symbol': symbol,
            'action': action,
            'quantity': quantity,
            'price': price,
            'total': quantity * price
        })


class TradingStrategy:
    """Base class for trading strategies."""
    
    def __init__(self, risk_appetite: float = 0.5):
        """
        Initialize a trading strategy.
        
        Args:
            risk_appetite: Risk appetite factor (0-1)
        """
        self.risk_appetite = max(0.0, min(1.0, risk_appetite))
    
    def should_buy(self, crypto: Cryptocurrency) -> bool:
        """Determine if we should buy the cryptocurrency."""
        raise NotImplementedError
    
    def should_sell(self, crypto: Cryptocurrency) -> bool:
        """Determine if we should sell the cryptocurrency."""
        raise NotImplementedError


class MeanReversionStrategy(TradingStrategy):
    """Mean reversion trading strategy."""
    
    def should_buy(self, crypto: Cryptocurrency) -> bool:
        """Buy if current price is below the average price."""
        if len(crypto.price_history) < 5:
            return False
        avg_price = sum(crypto.price_history[-5:]) / 5
        return crypto.current_price < avg_price * (1 - self.risk_appetite * 0.1)
    
    def should_sell(self, crypto: Cryptocurrency) -> bool:
        """Sell if current price is above the average price."""
        if len(crypto.price_history) < 5:
            return False
        avg_price = sum(crypto.price_history[-5:]) / 5
        return crypto.current_price > avg_price * (1 + self.risk_appetite * 0.1)


class TradingPlatform:
    """Main trading platform class."""
    
    def __init__(self):
        """Initialize the trading platform."""
        self.cryptos: Dict[str, Cryptocurrency] = {}
        self.portfolio = Portfolio()
        self.strategy: Optional[TradingStrategy] = None
        self.autonomy_level = AutonomyLevel.MANUAL
        self.assistance_level = AssistanceLevel.MEDIUM
        
        # Initialize with some sample cryptocurrencies
        self._initialize_sample_cryptos()
    
    def _initialize_sample_cryptos(self) -> None:
        """Initialize with some sample cryptocurrencies."""
        sample_cryptos = [
            ('BTC', 'Bitcoin', 50000.0, 0.05),
            ('ETH', 'Ethereum', 3000.0, 0.07),
            ('ADA', 'Cardano', 1.5, 0.1),
            ('SOL', 'Solana', 100.0, 0.08),
            ('DOT', 'Polkadot', 25.0, 0.09)
        ]
        
        for symbol, name, price, volatility in sample_cryptos:
            self.cryptos[symbol] = Cryptocurrency(symbol, name, price, volatility)
    
    def set_autonomy_level(self, level: AutonomyLevel) -> None:
        """Set the autonomy level for trading."""
        self.autonomy_level = level
        
        # Set appropriate strategy based on autonomy level
        if level == AutonomyLevel.FULL_AUTONOMY:
            self.strategy = MeanReversionStrategy(risk_appetite=0.7)
        elif level == AutonomyLevel.SEMI_AUTONOMY:
            self.strategy = MeanReversionStrategy(risk_appetite=0.5)
        else:
            self.strategy = None
    
    def set_assistance_level(self, level: AssistanceLevel) -> None:
        """Set the assistance level for trading."""
        self.assistance_level = level
    
    def update_market(self) -> None:
        """Update all cryptocurrency prices."""
        for crypto in self.cryptos.values():
            crypto.update_price()
    
    def execute_trade(self, symbol: str, action: str, quantity: float) -> bool:
        """
        Execute a trade.
        
        Args:
            symbol: Cryptocurrency symbol
            action: 'buy' or 'sell'
            quantity: Amount to trade
            
        Returns:
            bool: True if trade was successful, False otherwise
        """
        if symbol not in self.cryptos:
            return False
        
        crypto = self.cryptos[symbol]
        total_cost = quantity * crypto.current_price
        
        try:
            if action == 'buy':
                if self.portfolio.balance < total_cost:
                    return False
                self.portfolio.balance -= total_cost
                self.portfolio.add_holding(symbol, quantity)
            elif action == 'sell':
                self.portfolio.remove_holding(symbol, quantity)
                self.portfolio.balance += total_cost
            else:
                return False
            
            self.portfolio.record_trade(symbol, action, quantity, crypto.current_price)
            return True
        except Exception as e:
            print(f"Trade failed: {e}")
            return False
    
    def get_trade_recommendation(self, symbol: str) -> Optional[Tuple[str, float]]:
        """
        Get a trade recommendation based on current strategy and assistance level.
        
        Args:
            symbol: Cryptocurrency symbol
            
        Returns:
            Optional tuple of (action, confidence) or None if no recommendation
        """
        if symbol not in self.cryptos or not self.strategy:
            return None
        
        crypto = self.cryptos[symbol]
        confidence = random.uniform(0.5, 1.0) * (1 / self.assistance_level.value)
        
        if self.strategy.should_buy(crypto):
            return ('buy', confidence)
        elif self.strategy.should_sell(crypto):
            return ('sell', confidence)
        
        return None
    
    def run_autonomous_trading(self) -> None:
        """Run autonomous trading based on current settings."""
        if self.autonomy_level == AutonomyLevel.MANUAL:
            return
        
        for symbol in self.cryptos:
            recommendation = self.get_trade_recommendation(symbol)
            if recommendation:
                action, confidence = recommendation
                if confidence > 0.7 or self.autonomy_level == AutonomyLevel.FULL_AUTONOMY:
                    # For demo purposes, trade 10% of portfolio balance
                    crypto = self.cryptos[symbol]
                    max_amount = self.portfolio.balance /
