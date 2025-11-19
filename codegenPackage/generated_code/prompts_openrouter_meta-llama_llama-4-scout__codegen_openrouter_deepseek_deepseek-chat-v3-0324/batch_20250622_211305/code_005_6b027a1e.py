"""
Generated Code Metadata:
========================
Original URL: https://immediate-bitxdr.org
Prompt: Design an algorithm for creating a diversified investment portfolio using asset allocation strategies, considering factors such as market trends, risk levels, and financial objectives.
Generated: DETERMINISTIC_6b027a1e8413da3f
Batch ID: 20250622_211305
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
from typing import Dict, List, Tuple
from enum import Enum
from dataclasses import dataclass
import yfinance as yf
from scipy.optimize import minimize

class RiskLevel(Enum):
    """Enum representing investor risk tolerance levels."""
    LOW = 1
    MODERATE = 2
    HIGH = 3

class FinancialObjective(Enum):
    """Enum representing financial objectives."""
    CAPITAL_PRESERVATION = 1
    INCOME = 2
    GROWTH = 3
    AGGRESSIVE_GROWTH = 4

@dataclass
class AssetClass:
    """Data class representing an asset class."""
    name: str
    tickers: List[str]
    expected_return: float
    risk: float
    correlation_matrix: np.ndarray

class PortfolioOptimizer:
    """Class for optimizing a diversified investment portfolio."""
    
    def __init__(self, risk_level: RiskLevel, financial_objective: FinancialObjective):
        """
        Initialize the PortfolioOptimizer with risk level and financial objective.
        
        Args:
            risk_level: RiskLevel enum value
            financial_objective: FinancialObjective enum value
        """
        self.risk_level = risk_level
        self.financial_objective = financial_objective
        self.asset_classes = self._initialize_asset_classes()
        
    def _initialize_asset_classes(self) -> Dict[str, AssetClass]:
        """
        Initialize asset classes with sample data.
        In production, this would be fetched from a database or API.
        
        Returns:
            Dict[str, AssetClass]: Dictionary of asset classes
        """
        # Sample data - replace with real data in production
        return {
            "Stocks": AssetClass(
                name="Stocks",
                tickers=["SPY", "QQQ", "VTI"],
                expected_return=0.08,
                risk=0.15,
                correlation_matrix=np.array([[1.0, 0.8, 0.7], [0.8, 1.0, 0.6], [0.7, 0.6, 1.0]])
            ),
            "Bonds": AssetClass(
                name="Bonds",
                tickers=["BND", "TLT", "AGG"],
                expected_return=0.03,
                risk=0.05,
                correlation_matrix=np.array([[1.0, 0.9, 0.85], [0.9, 1.0, 0.8], [0.85, 0.8, 1.0]])
            ),
            "Real Estate": AssetClass(
                name="Real Estate",
                tickers=["VNQ", "IYR", "XLRE"],
                expected_return=0.06,
                risk=0.10,
                correlation_matrix=np.array([[1.0, 0.7, 0.65], [0.7, 1.0, 0.6], [0.65, 0.6, 1.0]])
            ),
            "Commodities": AssetClass(
                name="Commodities",
                tickers=["GLD", "SLV", "DBC"],
                expected_return=0.05,
                risk=0.12,
                correlation_matrix=np.array([[1.0, 0.5, 0.4], [0.5, 1.0, 0.3], [0.4, 0.3, 1.0]])
            )
        }
    
    def _get_historical_data(self, tickers: List[str], period: str = "5y") -> pd.DataFrame:
        """
        Fetch historical market data for given tickers.
        
        Args:
            tickers: List of ticker symbols
            period: Time period for historical data (default: 5 years)
            
        Returns:
            pd.DataFrame: DataFrame containing historical returns
        """
        try:
            data = yf.download(tickers, period=period)['Adj Close']
            returns = data.pct_change().dropna()
            return returns
        except Exception as e:
            raise ValueError(f"Error fetching historical data: {str(e)}")
    
    def _calculate_portfolio_risk(self, weights: np.ndarray, cov_matrix: np.ndarray) -> float:
        """
        Calculate portfolio risk (standard deviation).
        
        Args:
            weights: Asset weights
            cov_matrix: Covariance matrix
            
        Returns:
            float: Portfolio risk
        """
        return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    
    def _calculate_portfolio_return(self, weights: np.ndarray, expected_returns: np.ndarray) -> float:
        """
        Calculate portfolio expected return.
        
        Args:
            weights: Asset weights
            expected_returns: Expected returns for each asset
            
        Returns:
            float: Portfolio expected return
        """
        return np.sum(weights * expected_returns)
    
    def _optimize_portfolio(self, expected_returns: np.ndarray, cov_matrix: np.ndarray) -> np.ndarray:
        """
        Optimize portfolio weights using Markowitz mean-variance optimization.
        
        Args:
            expected_returns: Expected returns for each asset
            cov_matrix: Covariance matrix
            
        Returns:
            np.ndarray: Optimized weights
        """
        num_assets = len(expected_returns)
        args = (expected_returns, cov_matrix)
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = tuple((0, 1) for _ in range(num_assets))
        
        # Adjust optimization based on risk level
        if self.risk_level == RiskLevel.LOW:
            target_return = np.min(expected_returns)
        elif self.risk_level == RiskLevel.MODERATE:
            target_return = np.mean(expected_returns)
        else:  # HIGH
            target_return = np.max(expected_returns)
            
        constraints = (
            {'type': 'eq', 'fun': lambda x: np.sum(x) - 1},
            {'type': 'eq', 'fun': lambda x: self._calculate_portfolio_return(x, expected_returns) - target_return}
        )
        
        result = minimize(
            self._calculate_portfolio_risk,
            num_assets * [1. / num_assets],
            args=args,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints
        )
        
        return result.x
    
    def _adjust_for_financial_objective(self, weights: Dict[str, float]) -> Dict[str, float]:
        """
        Adjust portfolio weights based on financial objective.
        
        Args:
            weights: Initial optimized weights
            
        Returns:
            Dict[str, float]: Adjusted weights
        """
        adjusted_weights = weights.copy()
        
        if self.financial_objective == FinancialObjective.CAPITAL_PRESERVATION:
            # Increase bonds, decrease high-risk assets
            adjusted_weights["Bonds"] = min(adjusted_weights["Bonds"] * 1.5, 0.7)
            adjusted_weights["Stocks"] = max(adjusted_weights["Stocks"] * 0.7, 0.1)
            adjusted_weights["Commodities"] = max(adjusted_weights["Commodities"] * 0.5, 0.05)
            
        elif self.financial_objective == FinancialObjective.INCOME:
            # Increase dividend-paying assets
            adjusted_weights["Stocks"] = min(adjusted_weights["Stocks"] * 1.2, 0.6)
            adjusted_weights["Real Estate"] = min(adjusted_weights["Real Estate"] * 1.3, 0.4)
            
        elif self.financial_objective == FinancialObjective.GROWTH:
            # Balanced approach
            pass  # Use optimized weights as-is
            
        elif self.financial_objective == FinancialObjective.AGGRESSIVE_GROWTH:
            # Increase high-growth assets
            adjusted_weights["Stocks"] = min(adjusted_weights["Stocks"] * 1.5, 0.8)
            adjusted_weights["Commodities"] = min(adjusted_weights["Commodities"] * 1.3, 0.3)
            adjusted_weights["Bonds"] = max(adjusted_weights["Bonds"] * 0.5, 0.05)
            
        # Normalize weights to sum to 1
        total = sum(adjusted_weights.values())
        return {k: v/total for k, v in adjusted_weights.items()}
    
    def generate_portfolio(self) -> Dict[str, float]:
        """
        Generate a diversified portfolio based on investor profile.
        
        Returns:
            Dict[str, float]: Dictionary of asset class to weight allocation
        """
        try:
            # Get expected returns and covariance matrix
            expected_returns = np.array([ac.expected_return for ac in self.asset_classes.values()])
            cov_matrix = np.zeros((len(self.asset_classes), len(self.asset_classes)))
            
            # Build composite covariance matrix
            for i, (_, ac1) in enumerate(self.asset_classes.items()):
                for j, (_, ac2) in enumerate(self.asset_classes.items()):
