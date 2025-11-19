"""
Generated Code Metadata:
========================
Original URL: https://laotaigroup.com
Prompt: Write code to simulate a trading and investment planning system for Lao Tai Trading - Investment Group, incorporating financial metrics and risk analysis.
Generated: DETERMINISTIC_d40143654fb21078
Batch ID: 20250612_153224
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
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Optional
import random
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class InvestmentPortfolio:
    """Represents an investment portfolio with assets and performance metrics."""
    
    def __init__(self, name: str, initial_capital: float):
        """
        Initialize the portfolio.
        
        Args:
            name: Name of the portfolio
            initial_capital: Starting capital in USD
        """
        self.name = name
        self.initial_capital = initial_capital
        self.current_balance = initial_capital
        self.assets = {}  # {asset_name: {'quantity': qty, 'avg_price': price}}
        self.transaction_history = []
        self.performance_metrics = {
            'returns': 0.0,
            'volatility': 0.0,
            'sharpe_ratio': 0.0,
            'max_drawdown': 0.0
        }
        
    def add_asset(self, asset_name: str, quantity: float, price: float) -> bool:
        """
        Add an asset to the portfolio.
        
        Args:
            asset_name: Name of the asset
            quantity: Quantity to purchase
            price: Purchase price per unit
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            cost = quantity * price
            if cost > self.current_balance:
                logger.warning(f"Insufficient funds to purchase {asset_name}")
                return False
                
            if asset_name in self.assets:
                total_qty = self.assets[asset_name]['quantity'] + quantity
                total_cost = (self.assets[asset_name]['avg_price'] * self.assets[asset_name]['quantity']) + cost
                self.assets[asset_name]['avg_price'] = total_cost / total_qty
                self.assets[asset_name]['quantity'] = total_qty
            else:
                self.assets[asset_name] = {
                    'quantity': quantity,
                    'avg_price': price
                }
                
            self.current_balance -= cost
            self._record_transaction(
                asset_name, quantity, price, 'BUY', cost
            )
            return True
            
        except Exception as e:
            logger.error(f"Error adding asset: {e}")
            return False
    
    def remove_asset(self, asset_name: str, quantity: float, price: float) -> bool:
        """
        Sell an asset from the portfolio.
        
        Args:
            asset_name: Name of the asset
            quantity: Quantity to sell
            price: Sell price per unit
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if asset_name not in self.assets:
                logger.warning(f"Asset {asset_name} not in portfolio")
                return False
                
            if quantity > self.assets[asset_name]['quantity']:
                logger.warning(f"Not enough {asset_name} to sell")
                return False
                
            proceeds = quantity * price
            self.current_balance += proceeds
            
            # Update asset quantity
            self.assets[asset_name]['quantity'] -= quantity
            if self.assets[asset_name]['quantity'] == 0:
                del self.assets[asset_name]
                
            self._record_transaction(
                asset_name, quantity, price, 'SELL', proceeds
            )
            return True
            
        except Exception as e:
            logger.error(f"Error removing asset: {e}")
            return False
    
    def _record_transaction(self, asset: str, quantity: float, price: float, 
                          action: str, amount: float) -> None:
        """Record a transaction in the history."""
        transaction = {
            'date': datetime.now(),
            'asset': asset,
            'action': action,
            'quantity': quantity,
            'price': price,
            'amount': amount
        }
        self.transaction_history.append(transaction)
        logger.info(f"Recorded transaction: {transaction}")
    
    def calculate_performance(self, risk_free_rate: float = 0.02) -> Dict:
        """
        Calculate portfolio performance metrics.
        
        Args:
            risk_free_rate: Risk-free rate for Sharpe ratio calculation
            
        Returns:
            Dict: Performance metrics
        """
        try:
            # Simulate returns based on holdings (in a real system, this would use market data)
            portfolio_value = self.current_balance
            for asset, data in self.assets.items():
                # Simulate current price as avg_price * random fluctuation
                current_price = data['avg_price'] * (1 + random.uniform(-0.1, 0.2))
                portfolio_value += data['quantity'] * current_price
            
            # Calculate returns
            self.performance_metrics['returns'] = (
                (portfolio_value - self.initial_capital) / self.initial_capital
            )
            
            # Simulate volatility (standard deviation of returns)
            # In a real system, this would be calculated from historical data
            self.performance_metrics['volatility'] = random.uniform(0.05, 0.25)
            
            # Calculate Sharpe ratio
            self.performance_metrics['sharpe_ratio'] = (
                (self.performance_metrics['returns'] - risk_free_rate) / 
                self.performance_metrics['volatility']
            )
            
            # Simulate max drawdown
            self.performance_metrics['max_drawdown'] = random.uniform(0.0, 0.3)
            
            return self.performance_metrics
            
        except Exception as e:
            logger.error(f"Error calculating performance: {e}")
            return {}
    
    def get_portfolio_summary(self) -> Dict:
        """Return a summary of the portfolio."""
        return {
            'name': self.name,
            'initial_capital': self.initial_capital,
            'current_balance': self.current_balance,
            'asset_count': len(self.assets),
            'holdings': self.assets,
            'performance': self.performance_metrics
        }

class RiskAnalyzer:
    """Analyzes risk for investment portfolios."""
    
    @staticmethod
    def calculate_var(portfolio: InvestmentPortfolio, confidence_level: float = 0.95) -> float:
        """
        Calculate Value at Risk (VaR) for a portfolio.
        
        Args:
            portfolio: InvestmentPortfolio object
            confidence_level: Confidence level for VaR (e.g., 0.95 for 95%)
            
        Returns:
            float: VaR value
        """
        try:
            # In a real system, this would use historical data or Monte Carlo simulation
            # Here we simulate based on portfolio volatility
            volatility = portfolio.performance_metrics.get('volatility', 0.15)
            portfolio_value = portfolio.current_balance + sum(
                data['quantity'] * data['avg_price'] 
                for data in portfolio.assets.values()
            )
            
            # Using normal distribution approximation
            from scipy.stats import norm
            z_score = norm.ppf(1 - confidence_level)
            var = portfolio_value * z_score * volatility
            return abs(var)
            
        except Exception as e:
            logger.error(f"Error calculating VaR: {e}")
            return 0.0
    
    @staticmethod
    def stress_test(portfolio: InvestmentPortfolio, scenario: Dict[str, float]) -> Dict:
        """
        Perform stress testing on the portfolio.
        
        Args:
            portfolio: InvestmentPortfolio object
            scenario: Dictionary of asset classes and their stress factors
                      (e.g., {'equities': -0.3, 'bonds': -0.1})
                      
        Returns:
            Dict: Results of stress test
        """
        try:
            # In a real system, this would use more sophisticated scenario modeling
            total_value = portfolio.current_balance
            stressed_value = portfolio.current_balance
            asset_classes = {}
            
            for asset, data in portfolio.assets.items():
                # Determine asset class (simplified for demo)
                asset_class = 'equities' if random.random() > 0.5 else 'bonds'
                stress_factor = scenario.get(asset_class, 0.0)
                
                current_value = data['quantity'] * data['avg_price']
                stressed_value += current_value * (1 + stress_factor)
                total_value += current_value
                
                asset_classes[asset] = asset_class
            
            loss = total_value - stressed_value
            loss_pct = (loss / total_value) * 100 if total_value > 0 else 0.0
            
            return {
                'pre_stress_value': total_value,
                'post_stress_value': stressed_value,
                'absolute_loss': loss,
                'percentage_loss': loss_pct,
                'asset_classes': asset_classes
            }
            
        except Exception as e:
            logger.error(f"Error performing stress test: {e}")
            return {}

class TradingSystem:
    """Main trading system for Lao Tai Trading - Investment Group."""
    
    def __init__(self):
        self.portfolios = {}  #
