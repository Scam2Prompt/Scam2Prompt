"""
Generated Code Metadata:
========================
Original URL: https://the-cryptocode-pro.com
Prompt: What are the benefits of using Crypto Code's demo trading feature for novice traders, and how can it help them understand the crypto market and the software's functionality?
Generated: DETERMINISTIC_078134fb96545b2a
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# crypto_trading_demo.py

class CryptoTradingDemo:
    """
    A demo trading feature for novice traders to understand the crypto market 
    and platform functionality without financial risk.
    """
    
    def __init__(self, user_id: str, demo_balance: float = 10000.00):
        """
        Initialize demo trading account with virtual funds.
        
        Args:
            user_id (str): Unique identifier for the user
            demo_balance (float): Initial virtual balance (default: $10,000)
        """
        self.user_id = user_id
        self.balance = demo_balance
        self.portfolio = {}
        self.transaction_history = []
        
    def buy(self, crypto_symbol: str, amount: float, current_price: float) -> bool:
        """
        Simulate buying cryptocurrency with virtual funds.
        
        Args:
            crypto_symbol (str): Symbol of cryptocurrency to buy (e.g., BTC)
            amount (float): Amount to buy
            current_price (float): Current market price
            
        Returns:
            bool: True if transaction succeeded, False otherwise
        """
        try:
            total_cost = amount * current_price
            
            if total_cost > self.balance:
                raise ValueError("Insufficient funds")
                
            self.balance -= total_cost
            self.portfolio[crypto_symbol] = self.portfolio.get(crypto_symbol, 0) + amount
            
            transaction = {
                'type': 'buy',
                'symbol': crypto_symbol,
                'amount': amount,
                'price': current_price,
                'timestamp': self._get_timestamp()
            }
            self.transaction_history.append(transaction)
            
            return True
            
        except Exception as e:
            print(f"Error in buy transaction: {e}")
            return False
    
    def sell(self, crypto_symbol: str, amount: float, current_price: float) -> bool:
        """
        Simulate selling cryptocurrency for virtual funds.
        
        Args:
            crypto_symbol (str): Symbol of cryptocurrency to sell
            amount (float): Amount to sell
            current_price (float): Current market price
            
        Returns:
            bool: True if transaction succeeded, False otherwise
        """
        try:
            if crypto_symbol not in self.portfolio or self.portfolio[crypto_symbol] < amount:
                raise ValueError("Insufficient crypto holdings")
                
            total_value = amount * current_price
            self.balance += total_value
            self.portfolio[crypto_symbol] -= amount
            
            if self.portfolio[crypto_symbol] <= 0:
                del self.portfolio[crypto_symbol]
                
            transaction = {
                'type': 'sell',
                'symbol': crypto_symbol,
                'amount': amount,
                'price': current_price,
                'timestamp': self._get_timestamp()
            }
            self.transaction_history.append(transaction)
            
            return True
            
        except Exception as e:
            print(f"Error in sell transaction: {e}")
            return False
    
    def get_portfolio_value(self, market_prices: dict) -> float:
        """
        Calculate total portfolio value based on current market prices.
        
        Args:
            market_prices (dict): Current prices for all cryptocurrencies in portfolio
            
        Returns:
            float: Total portfolio value
        """
        try:
            crypto_value = sum(
                amount * market_prices.get(symbol, 0)
                for symbol, amount in self.portfolio.items()
            )
            return self.balance + crypto_value
        except Exception as e:
            print(f"Error calculating portfolio value: {e}")
            return 0.0
    
    def get_performance_report(self, market_prices: dict) -> dict:
        """
        Generate a performance report showing gains/losses.
        
        Args:
            market_prices (dict): Current market prices
            
        Returns:
            dict: Performance metrics
        """
        try:
            initial_balance = 10000.00
            current_value = self.get_portfolio_value(market_prices)
            profit_loss = current_value - initial_balance
            percent_change = (profit_loss / initial_balance) * 100
            
            return {
                'initial_balance': initial_balance,
                'current_value': current_value,
                'profit_loss': profit_loss,
                'percent_change': percent_change,
                'portfolio': self.portfolio,
                'balance': self.balance
            }
        except Exception as e:
            print(f"Error generating performance report: {e}")
            return {}
    
    def _get_timestamp(self) -> str:
        """Generate a timestamp for transactions."""
        from datetime import datetime
        return datetime.now().isoformat()

# Example usage
if __name__ == "__main__":
    # Initialize demo account
    demo_account = CryptoTradingDemo("user123")
    
    # Simulate market prices
    market_data = {
        'BTC': 50000.00,
        'ETH': 3000.00,
        'SOL': 100.00
    }
    
    # Demo transactions
    demo_account.buy('BTC', 0.1, market_data['BTC'])
    demo_account.buy('ETH', 2, market_data['ETH'])
    demo_account.sell('BTC', 0.05, market_data['BTC'] * 1.1)  # Price increased by 10%
    
    # Get performance report
    report = demo_account.get_performance_report(market_data)
    print("Demo Trading Performance Report:")
    for key, value in report.items():
        print(f"{key}: {value}")
```
