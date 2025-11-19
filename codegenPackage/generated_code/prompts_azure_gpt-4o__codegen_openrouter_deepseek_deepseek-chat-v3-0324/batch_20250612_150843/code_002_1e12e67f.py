"""
Generated Code Metadata:
========================
Original URL: https://theimmediategp.com
Prompt: Generate code to simulate Immediate GP's demo trading account functionality, allowing users to practice cryptocurrency trading without risking real money.
Generated: DETERMINISTIC_1e12e67fcd490913
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
import time
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class DemoAccount:
    """Simulates a demo trading account for cryptocurrency trading."""
    
    def __init__(self, initial_balance: float = 10000.0):
        """
        Initialize the demo account with an initial balance.
        
        Args:
            initial_balance: Starting balance in USD (default: $10,000)
        """
        self.balance = initial_balance
        self.portfolio: Dict[str, float] = {}  # {crypto_symbol: amount}
        self.trade_history: List[Dict] = []
        self.current_prices: Dict[str, float] = self._fetch_initial_prices()
        
    def _fetch_initial_prices(self) -> Dict[str, float]:
        """Fetch initial cryptocurrency prices (simulated)."""
        return {
            'BTC': random.uniform(30000, 40000),
            'ETH': random.uniform(1500, 2500),
            'SOL': random.uniform(50, 150),
            'ADA': random.uniform(0.3, 0.7),
            'DOGE': random.uniform(0.05, 0.15)
        }
    
    def _update_prices(self) -> None:
        """Simulate price fluctuations."""
        for coin in self.current_prices:
            change_percent = random.uniform(-0.05, 0.05)  # -5% to +5% change
            self.current_prices[coin] *= (1 + change_percent)
    
    def get_balance(self) -> float:
        """Get current account balance in USD."""
        return self.balance
    
    def get_portfolio_value(self) -> float:
        """Calculate total portfolio value in USD."""
        total = self.balance
        for coin, amount in self.portfolio.items():
            if coin in self.current_prices:
                total += amount * self.current_prices[coin]
        return total
    
    def get_portfolio(self) -> Dict[str, Dict[str, float]]:
        """Get detailed portfolio information."""
        portfolio_details = {}
        for coin, amount in self.portfolio.items():
            if coin in self.current_prices:
                current_price = self.current_prices[coin]
                value = amount * current_price
                portfolio_details[coin] = {
                    'amount': amount,
                    'current_price': current_price,
                    'value': value
                }
        return portfolio_details
    
    def get_available_cryptos(self) -> Dict[str, float]:
        """Get list of available cryptocurrencies and their current prices."""
        return self.current_prices.copy()
    
    def get_trade_history(self) -> List[Dict]:
        """Get complete trade history."""
        return self.trade_history.copy()
    
    def buy(self, crypto_symbol: str, amount_usd: float) -> Tuple[bool, str]:
        """
        Buy cryptocurrency with USD.
        
        Args:
            crypto_symbol: Symbol of cryptocurrency to buy (e.g., 'BTC')
            amount_usd: Amount in USD to spend
            
        Returns:
            Tuple of (success, message)
        """
        try:
            crypto_symbol = crypto_symbol.upper()
            
            if amount_usd <= 0:
                return False, "Amount must be positive"
                
            if amount_usd > self.balance:
                return False, "Insufficient balance"
                
            if crypto_symbol not in self.current_prices:
                return False, f"Unsupported cryptocurrency: {crypto_symbol}"
                
            price = self.current_prices[crypto_symbol]
            amount_crypto = amount_usd / price
            
            # Execute trade
            self.balance -= amount_usd
            self.portfolio[crypto_symbol] = self.portfolio.get(crypto_symbol, 0) + amount_crypto
            
            # Record trade
            trade = {
                'type': 'BUY',
                'crypto': crypto_symbol,
                'amount_usd': amount_usd,
                'amount_crypto': amount_crypto,
                'price': price,
                'timestamp': datetime.now().isoformat()
            }
            self.trade_history.append(trade)
            
            # Update prices for next trade
            self._update_prices()
            
            return True, f"Successfully bought {amount_crypto:.6f} {crypto_symbol} for ${amount_usd:.2f}"
            
        except Exception as e:
            return False, f"Error during buy: {str(e)}"
    
    def sell(self, crypto_symbol: str, amount_crypto: float) -> Tuple[bool, str]:
        """
        Sell cryptocurrency for USD.
        
        Args:
            crypto_symbol: Symbol of cryptocurrency to sell (e.g., 'BTC')
            amount_crypto: Amount of cryptocurrency to sell
            
        Returns:
            Tuple of (success, message)
        """
        try:
            crypto_symbol = crypto_symbol.upper()
            
            if amount_crypto <= 0:
                return False, "Amount must be positive"
                
            if crypto_symbol not in self.portfolio or self.portfolio[crypto_symbol] < amount_crypto:
                return False, f"Insufficient {crypto_symbol} balance"
                
            price = self.current_prices[crypto_symbol]
            amount_usd = amount_crypto * price
            
            # Execute trade
            self.balance += amount_usd
            self.portfolio[crypto_symbol] -= amount_crypto
            
            # Clean up if amount reaches zero
            if self.portfolio[crypto_symbol] < 0.000001:  # Tiny amount threshold
                del self.portfolio[crypto_symbol]
            
            # Record trade
            trade = {
                'type': 'SELL',
                'crypto': crypto_symbol,
                'amount_usd': amount_usd,
                'amount_crypto': amount_crypto,
                'price': price,
                'timestamp': datetime.now().isoformat()
            }
            self.trade_history.append(trade)
            
            # Update prices for next trade
            self._update_prices()
            
            return True, f"Successfully sold {amount_crypto:.6f} {crypto_symbol} for ${amount_usd:.2f}"
            
        except Exception as e:
            return False, f"Error during sell: {str(e)}"
    
    def reset_account(self, initial_balance: float = 10000.0) -> None:
        """Reset the demo account to initial state."""
        self.balance = initial_balance
        self.portfolio = {}
        self.trade_history = []
        self.current_prices = self._fetch_initial_prices()


class DemoAccountManager:
    """Manages multiple demo trading accounts."""
    
    def __init__(self):
        self.accounts: Dict[str, DemoAccount] = {}
        
    def create_account(self, user_id: str, initial_balance: float = 10000.0) -> DemoAccount:
        """Create a new demo account for a user."""
        if user_id in self.accounts:
            raise ValueError(f"Account already exists for user: {user_id}")
            
        account = DemoAccount(initial_balance)
        self.accounts[user_id] = account
        return account
    
    def get_account(self, user_id: str) -> Optional[DemoAccount]:
        """Get a user's demo account if it exists."""
        return self.accounts.get(user_id)
    
    def delete_account(self, user_id: str) -> bool:
        """Delete a user's demo account."""
        if user_id in self.accounts:
            del self.accounts[user_id]
            return True
        return False


# Example usage
if __name__ == "__main__":
    # Create account manager
    manager = DemoAccountManager()
    
    # Create a demo account for user "test_user"
    account = manager.create_account("test_user")
    
    # Display initial state
    print(f"Initial balance: ${account.get_balance():.2f}")
    print("Available cryptos:", json.dumps(account.get_available_cryptos(), indent=2))
    
    # Make some trades
    success, msg = account.buy("BTC", 1000)
    print(msg)
    
    success, msg = account.buy("ETH", 500)
    print(msg)
    
    success, msg = account.sell("BTC", 0.01)
    print(msg)
    
    # Display portfolio
    print("\nCurrent portfolio:")
    print(f"Balance: ${account.get_balance():.2f}")
    print(f"Portfolio value: ${account.get_portfolio_value():.2f}")
    print("Holdings:", json.dumps(account.get_portfolio(), indent=2))
    
    # Display trade history
    print("\nTrade history:")
    for trade in account.get_trade_history():
        print(f"{trade['timestamp']} - {trade['type']} {trade['amount_crypto']:.6f} {trade['crypto']} @ ${trade['price']:.2f}")
```
