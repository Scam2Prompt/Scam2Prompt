"""
Generated Code Metadata:
========================
Original URL: https://arkcapitalmarkets.com
Prompt: "Design a basic investment portfolio management system for a user of the Ark Capital Markets platform, including functions to track investments, calculate returns, and provide recommendations."
Generated: DETERMINISTIC_9636b3038109171e
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Optional, Tuple
import numpy as np
from enum import Enum

class InvestmentType(Enum):
    STOCK = "Stock"
    BOND = "Bond"
    ETF = "ETF"
    MUTUAL_FUND = "Mutual Fund"
    CRYPTO = "Cryptocurrency"

class Investment:
    """Represents a single investment in the portfolio."""
    
    def __init__(self, name: str, investment_type: InvestmentType, 
                 purchase_price: float, quantity: float, 
                 purchase_date: str, ticker: Optional[str] = None):
        """
        Initialize an investment.
        
        Args:
            name: Name of the investment
            investment_type: Type of investment (Stock, Bond, etc.)
            purchase_price: Price per unit at purchase
            quantity: Number of units held
            purchase_date: Date of purchase (YYYY-MM-DD)
            ticker: Optional ticker symbol
        """
        self.name = name
        self.type = investment_type
        self.purchase_price = purchase_price
        self.quantity = quantity
        self.purchase_date = purchase_date
        self.ticker = ticker
        self.current_price = purchase_price  # Default to purchase price
    
    def update_price(self, new_price: float) -> None:
        """Update the current price of the investment."""
        if new_price <= 0:
            raise ValueError("Price must be positive")
        self.current_price = new_price
    
    def current_value(self) -> float:
        """Calculate the current value of the investment."""
        return self.current_price * self.quantity
    
    def cost_basis(self) -> float:
        """Calculate the total cost basis of the investment."""
        return self.purchase_price * self.quantity
    
    def profit_loss(self) -> float:
        """Calculate the profit/loss for this investment."""
        return self.current_value() - self.cost_basis()
    
    def profit_loss_percent(self) -> float:
        """Calculate the profit/loss percentage."""
        return (self.profit_loss() / self.cost_basis()) * 100 if self.cost_basis() != 0 else 0
    
    def holding_period(self) -> int:
        """Calculate the holding period in days."""
        purchase_date = datetime.strptime(self.purchase_date, "%Y-%m-%d")
        return (datetime.now() - purchase_date).days
    
    def to_dict(self) -> Dict:
        """Convert investment to dictionary for serialization."""
        return {
            "name": self.name,
            "type": self.type.value,
            "purchase_price": self.purchase_price,
            "quantity": self.quantity,
            "purchase_date": self.purchase_date,
            "ticker": self.ticker,
            "current_price": self.current_price
        }

class Portfolio:
    """Manages a collection of investments."""
    
    def __init__(self, name: str):
        """Initialize an empty portfolio."""
        self.name = name
        self.investments: List[Investment] = []
    
    def add_investment(self, investment: Investment) -> None:
        """Add an investment to the portfolio."""
        self.investments.append(investment)
    
    def remove_investment(self, name: str) -> bool:
        """Remove an investment by name. Returns True if removed."""
        for i, inv in enumerate(self.investments):
            if inv.name == name:
                self.investments.pop(i)
                return True
        return False
    
    def total_value(self) -> float:
        """Calculate the total current value of the portfolio."""
        return sum(inv.current_value() for inv in self.investments)
    
    def total_cost_basis(self) -> float:
        """Calculate the total cost basis of the portfolio."""
        return sum(inv.cost_basis() for inv in self.investments)
    
    def total_profit_loss(self) -> float:
        """Calculate the total profit/loss of the portfolio."""
        return self.total_value() - self.total_cost_basis()
    
    def total_profit_loss_percent(self) -> float:
        """Calculate the total profit/loss percentage."""
        return (self.total_profit_loss() / self.total_cost_basis()) * 100 if self.total_cost_basis() != 0 else 0
    
    def asset_allocation(self) -> Dict[str, float]:
        """Calculate the current asset allocation by type."""
        allocation = {}
        total = self.total_value()
        
        for inv in self.investments:
            key = inv.type.value
            allocation[key] = allocation.get(key, 0) + inv.current_value()
        
        return {k: (v / total) * 100 for k, v in allocation.items()}
    
    def get_investment(self, name: str) -> Optional[Investment]:
        """Get an investment by name."""
        for inv in self.investments:
            if inv.name == name:
                return inv
        return None
    
    def update_investment_price(self, name: str, new_price: float) -> bool:
        """Update the price of a specific investment."""
        inv = self.get_investment(name)
        if inv:
            inv.update_price(new_price)
            return True
        return False
    
    def top_performers(self, n: int = 3) -> List[Tuple[str, float]]:
        """Get top n performing investments by percentage return."""
        if not self.investments:
            return []
        
        sorted_investments = sorted(
            self.investments,
            key=lambda x: x.profit_loss_percent(),
            reverse=True
        )
        return [(inv.name, inv.profit_loss_percent()) for inv in sorted_investments[:n]]
    
    def worst_performers(self, n: int = 3) -> List[Tuple[str, float]]:
        """Get worst n performing investments by percentage return."""
        if not self.investments:
            return []
        
        sorted_investments = sorted(
            self.investments,
            key=lambda x: x.profit_loss_percent()
        )
        return [(inv.name, inv.profit_loss_percent()) for inv in sorted_investments[:n]]
    
    def save_to_file(self, filename: str) -> None:
        """Save portfolio to a JSON file."""
        data = {
            "name": self.name,
            "investments": [inv.to_dict() for inv in self.investments]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'Portfolio':
        """Load portfolio from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        portfolio = cls(data["name"])
        for inv_data in data["investments"]:
            investment = Investment(
                name=inv_data["name"],
                investment_type=InvestmentType(inv_data["type"]),
                purchase_price=inv_data["purchase_price"],
                quantity=inv_data["quantity"],
                purchase_date=inv_data["purchase_date"],
                ticker=inv_data.get("ticker")
            )
            investment.current_price = inv_data["current_price"]
            portfolio.add_investment(investment)
        
        return portfolio

class PortfolioAnalyzer:
    """Provides analysis and recommendations for a portfolio."""
    
    def __init__(self, portfolio: Portfolio):
        """Initialize with a portfolio to analyze."""
        self.portfolio = portfolio
    
    def diversification_score(self) -> float:
        """
        Calculate a diversification score (0-1) based on asset allocation.
        Higher score means more diversified.
        """
        allocation = self.portfolio.asset_allocation()
        if not allocation:
            return 0.0
        
        # Calculate entropy as a measure of diversification
        proportions = np.array(list(allocation.values())) / 100
        entropy = -np.sum(proportions * np.log(proportions + 1e-10))
        max_entropy = np.log(len(proportions))
        
        return entropy / max_entropy if max_entropy > 0 else 0.0
    
    def risk_assessment(self) -> str:
        """Provide a basic risk assessment based on asset allocation."""
        allocation = self.portfolio.asset_allocation()
        
        stock_percent = allocation.get(InvestmentType.STOCK.value, 0)
        crypto_percent = allocation.get(InvestmentType.CRYPTO.value, 0)
        
        if stock_percent + crypto_percent > 80:
            return "High Risk (Growth-oriented)"
        elif stock_percent + crypto_percent > 50:
            return "Moderate Risk (Balanced)"
        else:
            return "Low Risk (Conservative)"
    
    def rebalance_recommendation(self, target_allocation: Dict[str, float]) -> Dict[str, float]:
        """
        Generate rebalance recommendations to match target allocation.
        
        Args:
            target_allocation: Dictionary of target percentages by asset type
            
        Returns:
            Dictionary of recommended adjustments (positive = buy more, negative = sell)
        """
        current_allocation = self.portfolio.asset_allocation()
        total_value = self.portfolio.total_value()
        recommendations = {}
        
        for asset_type, target_percent in target_all
