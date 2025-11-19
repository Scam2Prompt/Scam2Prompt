"""
Generated Code Metadata:
========================
Original URL: https://alghanim-capital.com
Prompt: "Write a Python code snippet to manage a private equity portfolio, considering factors like investment lifecycle and strategic growth, as described on the Alghanim Capital website."
Generated: DETERMINISTIC_7029cf9e70c59462
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Private Equity Portfolio Management System

This module provides functionality to manage a private equity portfolio,
tracking investments through their lifecycle and strategic growth metrics.
Inspired by Alghanim Capital's investment approach.

Key Features:
- Track investment lifecycle stages
- Monitor strategic growth metrics
- Calculate portfolio performance
- Generate reports and analytics
"""

import datetime
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Dict, Optional
import pandas as pd
import numpy as np
from abc import ABC, abstractmethod


class InvestmentStage(Enum):
    """Enum representing different stages of investment lifecycle."""
    IDENTIFICATION = auto()
    DUE_DILIGENCE = auto()
    ACQUISITION = auto()
    VALUE_CREATION = auto()
    EXIT_PREPARATION = auto()
    EXIT = auto()


class Sector(Enum):
    """Enum representing different industry sectors."""
    TECHNOLOGY = auto()
    HEALTHCARE = auto()
    FINANCIAL_SERVICES = auto()
    CONSUMER_GOODS = auto()
    INDUSTRIAL = auto()
    ENERGY = auto()
    OTHER = auto()


@dataclass
class FinancialMetrics:
    """Class to track financial metrics for an investment."""
    entry_valuation: float
    current_valuation: float
    revenue: float
    ebitda: float
    net_income: float
    cash_flow: float
    debt_ratio: float
    growth_rate: float


@dataclass
class Investment:
    """Class representing a single investment in the portfolio."""
    name: str
    sector: Sector
    stage: InvestmentStage
    acquisition_date: datetime.date
    metrics: FinancialMetrics
    strategic_factors: Dict[str, float] = field(default_factory=dict)
    id: str = field(default_factory=lambda: str(hash(datetime.datetime.now())))


class PortfolioStrategy(ABC):
    """Abstract base class for portfolio strategies."""
    
    @abstractmethod
    def evaluate_investment(self, investment: Investment) -> float:
        """Evaluate an investment based on strategy-specific criteria."""
        pass
    
    @abstractmethod
    def recommend_action(self, investment: Investment) -> str:
        """Recommend action for an investment based on strategy."""
        pass


class GrowthStrategy(PortfolioStrategy):
    """Strategy focused on long-term growth potential."""
    
    def evaluate_investment(self, investment: Investment) -> float:
        score = (
            investment.metrics.growth_rate * 0.4 +
            investment.metrics.current_valuation / investment.metrics.entry_valuation * 0.3 +
            investment.strategic_factors.get('market_share', 0) * 0.2 +
            investment.strategic_factors.get('innovation_score', 0) * 0.1
        )
        return score
    
    def recommend_action(self, investment: Investment) -> str:
        score = self.evaluate_investment(investment)
        if score > 0.7:
            return "Increase position"
        elif score > 0.4:
            return "Maintain position"
        else:
            return "Consider exit"


class ValueStrategy(PortfolioStrategy):
    """Strategy focused on current valuation metrics."""
    
    def evaluate_investment(self, investment: Investment) -> float:
        score = (
            investment.metrics.ebitda / investment.metrics.current_valuation * 0.5 +
            investment.metrics.debt_ratio * 0.3 +
            investment.metrics.cash_flow * 0.2
        )
        return score
    
    def recommend_action(self, investment: Investment) -> str:
        score = self.evaluate_investment(investment)
        if score > 0.6:
            return "Increase position"
        elif score > 0.3:
            return "Maintain position"
        else:
            return "Consider exit"


class Portfolio:
    """Class representing the entire private equity portfolio."""
    
    def __init__(self, name: str, strategy: PortfolioStrategy = GrowthStrategy()):
        self.name = name
        self.investments: List[Investment] = []
        self.strategy = strategy
    
    def add_investment(self, investment: Investment) -> None:
        """Add a new investment to the portfolio."""
        self.investments.append(investment)
    
    def remove_investment(self, investment_id: str) -> bool:
        """Remove an investment from the portfolio."""
        for i, inv in enumerate(self.investments):
            if inv.id == investment_id:
                self.investments.pop(i)
                return True
        return False
    
    def get_investment(self, investment_id: str) -> Optional[Investment]:
        """Get an investment by its ID."""
        for inv in self.investments:
            if inv.id == investment_id:
                return inv
        return None
    
    def update_investment_metrics(self, investment_id: str, new_metrics: FinancialMetrics) -> bool:
        """Update financial metrics for an investment."""
        investment = self.get_investment(investment_id)
        if investment:
            investment.metrics = new_metrics
            return True
        return False
    
    def advance_investment_stage(self, investment_id: str) -> bool:
        """Move an investment to the next lifecycle stage."""
        investment = self.get_investment(investment_id)
        if investment:
            current_stage = investment.stage
            try:
                next_stage = InvestmentStage(current_stage.value + 1)
                investment.stage = next_stage
                return True
            except ValueError:
                return False
        return False
    
    def evaluate_portfolio(self) -> pd.DataFrame:
        """Evaluate all investments in the portfolio."""
        data = []
        for inv in self.investments:
            evaluation = {
                'ID': inv.id,
                'Name': inv.name,
                'Sector': inv.sector.name,
                'Stage': inv.stage.name,
                'Score': self.strategy.evaluate_investment(inv),
                'Recommendation': self.strategy.recommend_action(inv),
                'HoldingPeriod': (datetime.date.today() - inv.acquisition_date).days / 365
            }
            data.append(evaluation)
        
        return pd.DataFrame(data)
    
    def portfolio_performance(self) -> Dict[str, float]:
        """Calculate overall portfolio performance metrics."""
        if not self.investments:
            return {}
        
        total_entry = sum(inv.metrics.entry_valuation for inv in self.investments)
        total_current = sum(inv.metrics.current_valuation for inv in self.investments)
        total_revenue = sum(inv.metrics.revenue for inv in self.investments)
        total_ebitda = sum(inv.metrics.ebitda for inv in self.investments)
        
        return {
            'total_value': total_current,
            'total_growth': (total_current - total_entry) / total_entry,
            'average_revenue_multiple': total_current / total_revenue if total_revenue else 0,
            'average_ebitda_multiple': total_current / total_ebitda if total_ebitda else 0,
            'number_of_investments': len(self.investments)
        }
    
    def sector_distribution(self) -> Dict[Sector, float]:
        """Calculate the distribution of investments by sector."""
        sector_values = {}
        total_value = sum(inv.metrics.current_valuation for inv in self.investments)
        
        if total_value == 0:
            return {}
        
        for inv in self.investments:
            sector_values[inv.sector] = sector_values.get(inv.sector, 0) + inv.metrics.current_valuation
        
        return {sector: value / total_value for sector, value in sector_values.items()}
    
    def stage_distribution(self) -> Dict[InvestmentStage, float]:
        """Calculate the distribution of investments by lifecycle stage."""
        stage_counts = {}
        total = len(self.investments)
        
        if total == 0:
            return {}
        
        for inv in self.investments:
            stage_counts[inv.stage] = stage_counts.get(inv.stage, 0) + 1
        
        return {stage: count / total for stage, count in stage_counts.items()}


class PortfolioAnalyzer:
    """Class for advanced portfolio analysis and reporting."""
    
    @staticmethod
    def generate_performance_report(portfolio: Portfolio) -> str:
        """Generate a comprehensive performance report."""
        performance = portfolio.portfolio_performance()
        sector_dist = portfolio.sector_distribution()
        stage_dist = portfolio.stage_distribution()
        
        report = f"Portfolio Performance Report for {portfolio.name}\n"
        report += "=" * 50 + "\n\n"
        
        report += "Overall Performance:\n"
        report += f"- Total Portfolio Value: ${performance['total_value']:,.2f}\n"
        report += f"- Total Growth: {performance['total_growth']:.2%}\n"
        report += f"- Average Revenue Multiple: {performance['average_revenue_multiple']:.2f}x\n"
        report += f"- Average EBITDA Multiple: {performance['average_ebitda_multiple']:.2f}x\n"
        report += f"- Number of Investments: {performance
