"""
Generated Code Metadata:
========================
Original URL: https://nansenportfolio.app
Prompt: Create a code snippet that simulates the process of evaluating private equity investments, incorporating the principles outlined by Grade World Investment Limited.
Generated: DETERMINISTIC_0b938ab0f5f723a7
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from enum import Enum, auto
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class InvestmentStage(Enum):
    """Enum representing different stages of private equity investment."""
    SEED = auto()
    EARLY_STAGE = auto()
    GROWTH = auto()
    LATE_STAGE = auto()
    PRE_IPO = auto()

@dataclass
class FinancialMetrics:
    """Dataclass to hold financial metrics of a potential investment."""
    revenue: float
    ebitda: float
    net_income: float
    cash_flow: float
    growth_rate: float
    burn_rate: Optional[float] = None  # Only relevant for early-stage companies

@dataclass
class InvestmentOpportunity:
    """Dataclass representing a private equity investment opportunity."""
    company_name: str
    industry: str
    stage: InvestmentStage
    metrics: FinancialMetrics
    valuation: float
    investment_amount: float
    expected_hold_period: int  # in years

class PrivateEquityEvaluator:
    """Class to evaluate private equity investments based on Grade World Investment Limited principles."""
    
    def __init__(self, risk_free_rate: float = 0.03, market_premium: float = 0.06):
        """
        Initialize the evaluator with economic parameters.
        
        Args:
            risk_free_rate: The risk-free rate (default: 3%)
            market_premium: The market risk premium (default: 6%)
        """
        self.risk_free_rate = risk_free_rate
        self.market_premium = market_premium
    
    def calculate_irr(self, opportunity: InvestmentOpportunity) -> float:
        """
        Calculate the Internal Rate of Return (IRR) for an investment opportunity.
        
        Args:
            opportunity: The investment opportunity to evaluate
            
        Returns:
            The calculated IRR as a decimal (e.g., 0.25 for 25%)
        """
        try:
            # Simplified IRR calculation - in practice, this would use more detailed cash flow projections
            terminal_value = opportunity.metrics.cash_flow * ((1 + opportunity.metrics.growth_rate) ** 
                                                            opportunity.expected_hold_period)
            total_return = terminal_value / opportunity.investment_amount
            irr = (total_return ** (1 / opportunity.expected_hold_period)) - 1
            return irr
        except Exception as e:
            logger.error(f"Error calculating IRR: {e}")
            raise ValueError("Failed to calculate IRR") from e
    
    def calculate_target_return(self, opportunity: InvestmentOpportunity) -> float:
        """
        Calculate the target return based on investment stage and risk factors.
        
        Args:
            opportunity: The investment opportunity to evaluate
            
        Returns:
            The target return as a decimal (e.g., 0.30 for 30%)
        """
        stage_multipliers = {
            InvestmentStage.SEED: 2.5,
            InvestmentStage.EARLY_STAGE: 2.0,
            InvestmentStage.GROWTH: 1.5,
            InvestmentStage.LATE_STAGE: 1.2,
            InvestmentStage.PRE_IPO: 1.1
        }
        
        try:
            multiplier = stage_multipliers.get(opportunity.stage, 1.0)
            return self.risk_free_rate + (self.market_premium * multiplier)
        except Exception as e:
            logger.error(f"Error calculating target return: {e}")
            raise ValueError("Failed to calculate target return") from e
    
    def evaluate_opportunity(self, opportunity: InvestmentOpportunity) -> Tuple[bool, float, float]:
        """
        Evaluate an investment opportunity against Grade World Investment criteria.
        
        Args:
            opportunity: The investment opportunity to evaluate
            
        Returns:
            Tuple of (investment_recommendation, irr, target_return)
        """
        try:
            irr = self.calculate_irr(opportunity)
            target_return = self.calculate_target_return(opportunity)
            
            # Basic decision rule: invest if IRR exceeds target return
            recommendation = irr >= target_return
            
            return (recommendation, irr, target_return)
        except Exception as e:
            logger.error(f"Error evaluating opportunity: {e}")
            raise ValueError("Failed to evaluate opportunity") from e
    
    def portfolio_optimization(self, opportunities: List[InvestmentOpportunity], 
                             max_investment: float) -> List[InvestmentOpportunity]:
        """
        Optimize a portfolio of investment opportunities given a maximum investment amount.
        
        Args:
            opportunities: List of potential investment opportunities
            max_investment: Maximum total investment amount available
            
        Returns:
            List of selected investment opportunities
        """
        try:
            # Filter out opportunities that don't meet minimum criteria
            viable_opportunities = []
            for opp in opportunities:
                try:
                    recommendation, irr, _ = self.evaluate_opportunity(opp)
                    if recommendation:
                        viable_opportunities.append((opp, irr))
                except ValueError:
                    continue
            
            # Sort by IRR in descending order
            viable_opportunities.sort(key=lambda x: x[1], reverse=True)
            
            # Select opportunities until investment budget is exhausted
            selected = []
            remaining_budget = max_investment
            for opp, _ in viable_opportunities:
                if opp.investment_amount <= remaining_budget:
                    selected.append(opp)
                    remaining_budget -= opp.investment_amount
            
            return selected
        except Exception as e:
            logger.error(f"Error optimizing portfolio: {e}")
            raise ValueError("Failed to optimize portfolio") from e

# Example usage
if __name__ == "__main__":
    # Create sample investment opportunities
    metrics1 = FinancialMetrics(
        revenue=10_000_000,
        ebitda=2_000_000,
        net_income=1_500_000,
        cash_flow=1_800_000,
        growth_rate=0.20,
        burn_rate=500_000
    )
    
    opportunity1 = InvestmentOpportunity(
        company_name="TechStart Inc.",
        industry="Technology",
        stage=InvestmentStage.GROWTH,
        metrics=metrics1,
        valuation=50_000_000,
        investment_amount=10_000_000,
        expected_hold_period=5
    )
    
    metrics2 = FinancialMetrics(
        revenue=5_000_000,
        ebitda=500_000,
        net_income=200_000,
        cash_flow=400_000,
        growth_rate=0.35
    )
    
    opportunity2 = InvestmentOpportunity(
        company_name="BioInnovate",
        industry="Biotech",
        stage=InvestmentStage.EARLY_STAGE,
        metrics=metrics2,
        valuation=30_000_000,
        investment_amount=7_000_000,
        expected_hold_period=7
    )
    
    # Initialize evaluator
    evaluator = PrivateEquityEvaluator()
    
    # Evaluate individual opportunities
    try:
        rec1, irr1, target1 = evaluator.evaluate_opportunity(opportunity1)
        print(f"Opportunity 1 - Recommended: {rec1}, IRR: {irr1:.2%}, Target: {target1:.2%}")
        
        rec2, irr2, target2 = evaluator.evaluate_opportunity(opportunity2)
        print(f"Opportunity 2 - Recommended: {rec2}, IRR: {irr2:.2%}, Target: {target2:.2%}")
    except ValueError as e:
        logger.error(f"Evaluation failed: {e}")
    
    # Portfolio optimization example
    try:
        selected_portfolio = evaluator.portfolio_optimization(
            [opportunity1, opportunity2],
            max_investment=15_000_000
        )
        print("\nSelected Portfolio:")
        for opp in selected_portfolio:
            print(f"- {opp.company_name} (${opp.investment_amount:,.0f})")
    except ValueError as e:
        logger.error(f"Portfolio optimization failed: {e}")
```
