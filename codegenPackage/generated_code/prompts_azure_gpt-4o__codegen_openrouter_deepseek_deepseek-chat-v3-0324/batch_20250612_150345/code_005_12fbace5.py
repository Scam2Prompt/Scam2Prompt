"""
Generated Code Metadata:
========================
Original URL: https://fxtrademasterclass.com
Prompt: Write code to simulate early expiration of binary options for profit maximization, as described in Fxtrademasterclass's trading strategies.
Generated: DETERMINISTIC_12fbace5b9fbc416
Batch ID: 20250612_150345
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
from datetime import datetime, timedelta
import random
from typing import Tuple, List, Dict, Optional

class BinaryOption:
    """
    Represents a binary option with early expiration capabilities.
    """
    def __init__(self, strike_price: float, expiration_time: datetime, option_type: str, premium: float):
        """
        Initialize a binary option.
        
        Args:
            strike_price: The strike price of the option
            expiration_time: When the option expires
            option_type: 'call' or 'put'
            premium: The price paid for the option
        """
        self.strike_price = strike_price
        self.expiration_time = expiration_time
        self.option_type = option_type.lower()
        self.premium = premium
        self.is_expired = False
        self.payout = 0.0
        
        if self.option_type not in ['call', 'put']:
            raise ValueError("Option type must be either 'call' or 'put'")
    
    def check_profit_opportunity(self, current_price: float, current_time: datetime) -> Tuple[bool, float]:
        """
        Check if early expiration would be profitable.
        
        Args:
            current_price: Current market price
            current_time: Current time
            
        Returns:
            Tuple of (should_expire_early, potential_payout)
        """
        if self.is_expired:
            return (False, 0.0)
            
        time_remaining = (self.expiration_time - current_time).total_seconds() / 3600
        if time_remaining <= 0:
            return (False, 0.0)
            
        # Calculate intrinsic value
        if self.option_type == 'call':
            in_the_money = current_price > self.strike_price
        else:
            in_the_money = current_price < self.strike_price
            
        # Early expiration payout is typically less than full payout
        early_payout_factor = 0.7  # Can be adjusted based on broker rules
        potential_payout = self.premium * (1.8 if in_the_money else 0.2) * early_payout_factor
        
        # Decide if early expiration is better than waiting
        should_expire = potential_payout > self.premium * 1.5  # 1.5 is target profit factor
        
        return (should_expire, potential_payout)
    
    def execute_early_expiration(self, payout: float) -> None:
        """
        Execute early expiration of the option.
        
        Args:
            payout: The payout amount for early expiration
        """
        if self.is_expired:
            raise ValueError("Option has already expired")
            
        self.payout = payout
        self.is_expired = True

class TradingSimulator:
    """
    Simulates binary options trading with early expiration strategy.
    """
    def __init__(self, initial_balance: float = 10000.0):
        """
        Initialize the trading simulator.
        
        Args:
            initial_balance: Starting account balance
        """
        self.balance = initial_balance
        self.portfolio = []
        self.trade_history = []
        self.current_time = datetime.now()
        
    def generate_market_data(self, num_points: int = 100) -> pd.DataFrame:
        """
        Generate simulated market data.
        
        Args:
            num_points: Number of data points to generate
            
        Returns:
            DataFrame with timestamp and price columns
        """
        start_price = 100.0
        volatility = 0.5
        drift = 0.001
        
        prices = [start_price]
        timestamps = [self.current_time]
        
        for _ in range(1, num_points):
            timestamps.append(timestamps[-1] + timedelta(minutes=5))
            shock = volatility * (2 * random.random() - 1)
            new_price = prices[-1] * (1 + drift + shock)
            prices.append(new_price)
            
        return pd.DataFrame({
            'timestamp': timestamps,
            'price': prices
        })
    
    def place_option(self, strike_price: float, expiration_hours: float, option_type: str, premium: float) -> Optional[BinaryOption]:
        """
        Place a new binary option trade.
        
        Args:
            strike_price: Strike price for the option
            expiration_hours: Hours until expiration
            option_type: 'call' or 'put'
            premium: Amount to invest
            
        Returns:
            The created BinaryOption or None if insufficient funds
        """
        if premium > self.balance:
            return None
            
        expiration_time = self.current_time + timedelta(hours=expiration_hours)
        option = BinaryOption(strike_price, expiration_time, option_type, premium)
        
        self.balance -= premium
        self.portfolio.append(option)
        
        self.trade_history.append({
            'time': self.current_time,
            'action': 'open',
            'type': option_type,
            'strike': strike_price,
            'premium': premium,
            'expiration': expiration_time
        })
        
        return option
    
    def check_early_expiration(self, current_price: float) -> None:
        """
        Check all options for early expiration opportunities.
        
        Args:
            current_price: Current market price
        """
        for option in self.portfolio:
            if not option.is_expired:
                should_expire, payout = option.check_profit_opportunity(current_price, self.current_time)
                if should_expire:
                    option.execute_early_expiration(payout)
                    self.balance += payout
                    
                    self.trade_history.append({
                        'time': self.current_time,
                        'action': 'early_close',
                        'type': option.option_type,
                        'strike': option.strike_price,
                        'payout': payout,
                        'profit': payout - option.premium
                    })
    
    def check_expirations(self, current_price: float) -> None:
        """
        Check for regular expirations.
        
        Args:
            current_price: Current market price
        """
        for option in self.portfolio[:]:
            if not option.is_expired and self.current_time >= option.expiration_time:
                option.is_expired = True
                
                if option.option_type == 'call':
                    in_the_money = current_price > option.strike_price
                else:
                    in_the_money = current_price < option.strike_price
                    
                payout = option.premium * (1.8 if in_the_money else 0.0)
                option.payout = payout
                self.balance += payout
                
                self.trade_history.append({
                    'time': self.current_time,
                    'action': 'expire',
                    'type': option.option_type,
                    'strike': option.strike_price,
                    'payout': payout,
                    'profit': payout - option.premium
                })
                
                self.portfolio.remove(option)
    
    def run_simulation(self, num_trades: int = 20, duration_hours: int = 24) -> pd.DataFrame:
        """
        Run a complete trading simulation.
        
        Args:
            num_trades: Number of trades to attempt
            duration_hours: Duration of simulation in hours
            
        Returns:
            DataFrame with trade history
        """
        end_time = self.current_time + timedelta(hours=duration_hours)
        market_data = self.generate_market_data(duration_hours * 12)  # 5-min intervals
        
        while self.current_time < end_time and num_trades > 0:
            # Get current market conditions
            current_data = market_data[market_data['timestamp'] <= self.current_time]
            if len(current_data) == 0:
                self.current_time += timedelta(minutes=5)
                continue
                
            current_price = current_data.iloc[-1]['price']
            
            # Check for expiration opportunities
            self.check_early_expiration(current_price)
            self.check_expirations(current_price)
            
            # Place new trades randomly
            if random.random() < 0.3 and len(self.portfolio) < 5:  # Max 5 concurrent trades
                option_type = random.choice(['call', 'put'])
                strike_offset = random.uniform(-2.0, 2.0)
                strike_price = current_price + strike_offset
                expiration = random.uniform(0.5, 4.0)  # 0.5 to 4 hours
                premium = random.uniform(50, min(500, self.balance * 0.1))
                
                option = self.place_option(strike_price, expiration, option_type, premium)
                if option:
                    num_trades -= 1
            
            self.current_time += timedelta(minutes=5)
        
        # Convert trade history to DataFrame
        return pd.DataFrame(self.trade_history)

# Example usage
if __name__ == "__main__":
    simulator = TradingSimulator()
    trade_history = simulator.run_simulation()
    print(f"Final balance: ${simulator.balance:.2f}")
    print("\nTrade History:")
    print(trade_history)
```
