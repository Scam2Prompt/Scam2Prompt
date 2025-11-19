"""
Generated Code Metadata:
========================
Original URL: https://sheesh.vc
Prompt: What are some best practices for venture capital firms like Sheesh Venture Club in managing their investment portfolios?
Generated: DETERMINISTIC_e47d1394f45f59b6
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# portfolio_management.py
"""
This module provides a set of tools and best practices for venture capital firms
to manage their investment portfolios effectively.
"""

from typing import List, Dict, Optional
from datetime import datetime
import logging
from enum import Enum

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class InvestmentStage(Enum):
    """Enum representing different stages of investment."""
    SEED = "Seed"
    SERIES_A = "Series A"
    SERIES_B = "Series B"
    SERIES_C = "Series C"
    GROWTH = "Growth"
    LATE_STAGE = "Late Stage"

class Investment:
    """Class representing a single investment in the portfolio."""
    
    def __init__(
        self,
        company_name: str,
        stage: InvestmentStage,
        investment_date: datetime,
        amount: float,
        ownership_percentage: float,
        sector: str,
        notes: Optional[str] = None
    ):
        self.company_name = company_name
        self.stage = stage
        self.investment_date = investment_date
        self.amount = amount
        self.ownership_percentage = ownership_percentage
        self.sector = sector
        self.notes = notes
        self.valuation_updates: List[Dict] = []
        self.follow_up_dates: List[datetime] = []
        
    def add_valuation_update(self, date: datetime, valuation: float, notes: str) -> None:
        """Add a new valuation update for the investment."""
        if valuation <= 0:
            raise ValueError("Valuation must be positive")
        self.valuation_updates.append({
            'date': date,
            'valuation': valuation,
            'notes': notes
        })
        logger.info(f"Added valuation update for {self.company_name}")
        
    def add_follow_up_date(self, date: datetime) -> None:
        """Add a follow-up date for the investment."""
        if date < datetime.now():
            raise ValueError("Follow-up date cannot be in the past")
        self.follow_up_dates.append(date)
        logger.info(f"Added follow-up date for {self.company_name}")

class Portfolio:
    """Class representing the entire investment portfolio."""
    
    def __init__(self):
        self.investments: List[Investment] = []
        
    def add_investment(self, investment: Investment) -> None:
        """Add a new investment to the portfolio."""
        self.investments.append(investment)
        logger.info(f"Added new investment: {investment.company_name}")
        
    def remove_investment(self, company_name: str) -> bool:
        """Remove an investment from the portfolio."""
        for i, investment in enumerate(self.investments):
            if investment.company_name == company_name:
                del self.investments[i]
                logger.info(f"Removed investment: {company_name}")
                return True
        logger.warning(f"Investment not found: {company_name}")
        return False
    
    def get_investment_by_name(self, company_name: str) -> Optional[Investment]:
        """Get an investment by company name."""
        for investment in self.investments:
            if investment.company_name == company_name:
                return investment
        return None
    
    def get_investments_by_stage(self, stage: InvestmentStage) -> List[Investment]:
        """Get all investments in a specific stage."""
        return [inv for inv in self.investments if inv.stage == stage]
    
    def get_investments_by_sector(self, sector: str) -> List[Investment]:
        """Get all investments in a specific sector."""
        return [inv for inv in self.investments if inv.sector.lower() == sector.lower()]
    
    def calculate_portfolio_value(self) -> float:
        """Calculate the total current value of the portfolio."""
        total = 0.0
        for investment in self.investments:
            if investment.valuation_updates:
                latest_valuation = investment.valuation_updates[-1]['valuation']
                total += latest_valuation * (investment.ownership_percentage / 100)
        return total
    
    def calculate_diversification(self) -> Dict[str, float]:
        """Calculate sector diversification percentages."""
        sector_totals = {}
        total_value = self.calculate_portfolio_value()
        
        if total_value == 0:
            return {}
            
        for investment in self.investments:
            if investment.valuation_updates:
                latest_valuation = investment.valuation_updates[-1]['valuation']
                value = latest_valuation * (investment.ownership_percentage / 100)
                sector_totals[investment.sector] = sector_totals.get(investment.sector, 0) + value
        
        return {sector: (value/total_value)*100 for sector, value in sector_totals.items()}
    
    def get_upcoming_follow_ups(self, days_ahead: int = 30) -> List[Dict]:
        """Get all follow-ups due in the next specified days."""
        cutoff_date = datetime.now() + timedelta(days=days_ahead)
        upcoming = []
        
        for investment in self.investments:
            for date in investment.follow_up_dates:
                if datetime.now() <= date <= cutoff_date:
                    upcoming.append({
                        'company': investment.company_name,
                        'date': date,
                        'stage': investment.stage.value
                    })
        
        return sorted(upcoming, key=lambda x: x['date'])

class PortfolioAnalyzer:
    """Class for analyzing portfolio performance and metrics."""
    
    @staticmethod
    def calculate_irr(investments: List[Investment], current_value: float) -> float:
        """
        Calculate Internal Rate of Return (IRR) for the portfolio.
        Simplified calculation - in practice would use more sophisticated methods.
        """
        if not investments:
            return 0.0
            
        total_invested = sum(inv.amount for inv in investments)
        time_period = (datetime.now() - min(inv.investment_date for inv in investments)).days / 365
        
        if time_period == 0 or total_invested == 0:
            return 0.0
            
        return ((current_value / total_invested) ** (1 / time_period) - 1) * 100
    
    @staticmethod
    def calculate_tvpi(investments: List[Investment], current_value: float) -> float:
        """Calculate Total Value to Paid-In ratio."""
        total_invested = sum(inv.amount for inv in investments)
        return current_value / total_invested if total_invested != 0 else 0.0
    
    @staticmethod
    def generate_performance_report(portfolio: Portfolio) -> Dict:
        """Generate a comprehensive performance report for the portfolio."""
        current_value = portfolio.calculate_portfolio_value()
        diversification = portfolio.calculate_diversification()
        
        return {
            'total_portfolio_value': current_value,
            'total_invested': sum(inv.amount for inv in portfolio.investments),
            'irr': PortfolioAnalyzer.calculate_irr(portfolio.investments, current_value),
            'tvpi': PortfolioAnalyzer.calculate_tvpi(portfolio.investments, current_value),
            'diversification': diversification,
            'investment_count': len(portfolio.investments),
            'by_stage': {
                stage.value: len(portfolio.get_investments_by_stage(stage))
                for stage in InvestmentStage
            }
        }

class PortfolioOptimizer:
    """Class for optimizing portfolio allocation and strategy."""
    
    @staticmethod
    def suggest_rebalancing(portfolio: Portfolio, target_allocation: Dict[str, float]) -> Dict[str, float]:
        """
        Suggest rebalancing actions based on target sector allocation.
        Returns the difference between current and target allocation.
        """
        current_allocation = portfolio.calculate_diversification()
        suggestions = {}
        
        for sector, target in target_allocation.items():
            current = current_allocation.get(sector, 0)
            suggestions[sector] = target - current
            
        return suggestions
    
    @staticmethod
    def check_concentration_risk(portfolio: Portfolio, threshold: float = 20.0) -> List[str]:
        """Identify investments that exceed concentration risk threshold."""
        warnings = []
        total_value = portfolio.calculate_portfolio_value()
        
        if total_value == 0:
            return warnings
            
        for investment in portfolio.investments:
            if investment.valuation_updates:
                investment_value = investment.valuation_updates[-1]['valuation'] * (investment.ownership_percentage / 100)
                percentage = (investment_value / total_value) * 100
                if percentage > threshold:
                    warnings.append(
                        f"Concentration warning: {investment.company_name} "
                        f"({percentage:.2f}% of portfolio)"
                    )
        
        return warnings
```
