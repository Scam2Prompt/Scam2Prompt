"""
Generated Code Metadata:
========================
Original URL: https://maximuslimited.com
Prompt: Create a program to model capital investment strategies for raising funds in new markets, referencing Maximus Limited’s consultancy services.
Generated: DETERMINISTIC_da83fb1726866080
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Capital Investment Strategy Model for New Market Fundraising

This program models various capital investment strategies for raising funds in new markets,
inspired by Maximus Limited's consultancy services. It includes options for equity financing,
debt financing, and hybrid approaches with risk assessment and ROI projections.

Key Features:
- Equity vs Debt financing analysis
- Risk assessment based on market conditions
- ROI projections under different scenarios
- Sensitivity analysis for key variables
"""

import numpy as np
import pandas as pd
from typing import Dict, Tuple, Optional, List
from enum import Enum
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FinancingType(Enum):
    """Enum representing different financing options"""
    EQUITY = "Equity Financing"
    DEBT = "Debt Financing"
    HYBRID = "Hybrid Financing"

class MarketRiskLevel(Enum):
    """Enum representing market risk levels"""
    LOW = "Low Risk"
    MEDIUM = "Medium Risk"
    HIGH = "High Risk"

@dataclass
class MarketConditions:
    """Data class representing market conditions"""
    risk_level: MarketRiskLevel
    growth_rate: float
    inflation_rate: float
    political_stability: float  # 0-1 scale

@dataclass
class InvestmentStrategy:
    """Data class representing an investment strategy"""
    financing_type: FinancingType
    capital_amount: float
    expected_term: int  # in years
    equity_percentage: Optional[float] = None  # for hybrid financing
    interest_rate: Optional[float] = None  # for debt/hybrid financing

class CapitalInvestmentModel:
    """Main class for modeling capital investment strategies"""
    
    def __init__(self, market_conditions: MarketConditions):
        self.market_conditions = market_conditions
        self.strategies: List[InvestmentStrategy] = []
        
    def add_strategy(self, strategy: InvestmentStrategy) -> None:
        """Add an investment strategy to the model"""
        self._validate_strategy(strategy)
        self.strategies.append(strategy)
        logger.info(f"Added strategy: {strategy.financing_type.value}")
        
    def _validate_strategy(self, strategy: InvestmentStrategy) -> None:
        """Validate the investment strategy parameters"""
        if strategy.capital_amount <= 0:
            raise ValueError("Capital amount must be positive")
        if strategy.expected_term <= 0:
            raise ValueError("Investment term must be positive")
            
        if strategy.financing_type == FinancingType.HYBRID:
            if strategy.equity_percentage is None or not (0 < strategy.equity_percentage < 1):
                raise ValueError("Hybrid financing requires equity percentage between 0 and 1")
            if strategy.interest_rate is None or strategy.interest_rate <= 0:
                raise ValueError("Hybrid financing requires positive interest rate")
                
        elif strategy.financing_type == FinancingType.DEBT:
            if strategy.interest_rate is None or strategy.interest_rate <= 0:
                raise ValueError("Debt financing requires positive interest rate")
    
    def calculate_roi(self, strategy: InvestmentStrategy) -> Dict[str, float]:
        """
        Calculate projected ROI for a given strategy
        Returns dictionary with ROI metrics
        """
        try:
            if strategy.financing_type == FinancingType.EQUITY:
                return self._calculate_equity_roi(strategy)
            elif strategy.financing_type == FinancingType.DEBT:
                return self._calculate_debt_roi(strategy)
            else:
                return self._calculate_hybrid_roi(strategy)
        except Exception as e:
            logger.error(f"Error calculating ROI: {str(e)}")
            raise
            
    def _calculate_equity_roi(self, strategy: InvestmentStrategy) -> Dict[str, float]:
        """Calculate ROI for equity financing"""
        base_growth = self.market_conditions.growth_rate
        risk_factor = self._get_risk_factor()
        
        # Simple model: ROI = (growth - inflation) adjusted by risk
        annual_return = (base_growth - self.market_conditions.inflation_rate) * risk_factor
        total_return = ((1 + annual_return) ** strategy.expected_term - 1) * 100
        
        return {
            "annual_return_pct": annual_return * 100,
            "total_return_pct": total_return,
            "risk_adjusted_return": annual_return * risk_factor * 100
        }
    
    def _calculate_debt_roi(self, strategy: InvestmentStrategy) -> Dict[str, float]:
        """Calculate ROI for debt financing"""
        if strategy.interest_rate is None:
            raise ValueError("Interest rate required for debt financing")
            
        base_growth = self.market_conditions.growth_rate
        risk_factor = self._get_risk_factor()
        
        # Debt ROI considers interest payments and market growth
        net_growth = base_growth - strategy.interest_rate
        annual_return = net_growth * risk_factor
        total_return = ((1 + annual_return) ** strategy.expected_term - 1) * 100
        
        return {
            "annual_return_pct": annual_return * 100,
            "total_return_pct": total_return,
            "interest_cost": strategy.interest_rate * 100,
            "risk_adjusted_return": annual_return * risk_factor * 100
        }
    
    def _calculate_hybrid_roi(self, strategy: InvestmentStrategy) -> Dict[str, float]:
        """Calculate ROI for hybrid financing"""
        if strategy.equity_percentage is None or strategy.interest_rate is None:
            raise ValueError("Hybrid financing requires equity percentage and interest rate")
            
        # Calculate equity and debt components separately
        equity_roi = self._calculate_equity_roi(strategy)
        debt_roi = self._calculate_debt_roi(strategy)
        
        # Weighted average based on equity percentage
        equity_weight = strategy.equity_percentage
        debt_weight = 1 - equity_weight
        
        annual_return = (equity_roi["annual_return_pct"] * equity_weight + 
                        debt_roi["annual_return_pct"] * debt_weight)
        
        total_return = (equity_roi["total_return_pct"] * equity_weight + 
                       debt_roi["total_return_pct"] * debt_weight)
        
        return {
            "annual_return_pct": annual_return,
            "total_return_pct": total_return,
            "equity_component_pct": equity_roi["annual_return_pct"],
            "debt_component_pct": debt_roi["annual_return_pct"],
            "equity_weight": equity_weight * 100,
            "debt_weight": debt_weight * 100
        }
    
    def _get_risk_factor(self) -> float:
        """Get risk adjustment factor based on market conditions"""
        risk_map = {
            MarketRiskLevel.LOW: 1.0,
            MarketRiskLevel.MEDIUM: 0.8,
            MarketRiskLevel.HIGH: 0.5
        }
        base_factor = risk_map[self.market_conditions.risk_level]
        
        # Adjust for political stability
        return base_factor * self.market_conditions.political_stability
    
    def compare_strategies(self) -> pd.DataFrame:
        """Compare all strategies and return results as DataFrame"""
        results = []
        for strategy in self.strategies:
            roi = self.calculate_roi(strategy)
            result = {
                "strategy": strategy.financing_type.value,
                "capital": strategy.capital_amount,
                "term": strategy.expected_term,
                **roi
            }
            results.append(result)
        
        return pd.DataFrame(results)
    
    def sensitivity_analysis(self, strategy: InvestmentStrategy, 
                           variable: str, range_values: List[float]) -> pd.DataFrame:
        """
        Perform sensitivity analysis on a key variable
        Args:
            strategy: Investment strategy to analyze
            variable: Variable to test ('growth_rate', 'interest_rate', etc.)
            range_values: List of values to test for the variable
        Returns:
            DataFrame with sensitivity analysis results
        """
        results = []
        original_conditions = self.market_conditions
        
        try:
            for value in range_values:
                # Create modified market conditions
                modified_conditions = MarketConditions(
                    risk_level=original_conditions.risk_level,
                    growth_rate=value if variable == "growth_rate" else original_conditions.growth_rate,
                    inflation_rate=value if variable == "inflation_rate" else original_conditions.inflation_rate,
                    political_stability=value if variable == "political_stability" else original_conditions.political_stability
                )
                
                # Temporarily replace market conditions
                self.market_conditions = modified_conditions
                
                # Calculate ROI with modified conditions
                roi = self.calculate_roi(strategy)
                results.append({
                    variable: value,
                    "annual_return_pct": roi["annual_return_pct"],
                    "total_return_pct": roi["total_return_pct"]
                })
                
            return pd.DataFrame(results)
            
        finally:
            # Restore original market
