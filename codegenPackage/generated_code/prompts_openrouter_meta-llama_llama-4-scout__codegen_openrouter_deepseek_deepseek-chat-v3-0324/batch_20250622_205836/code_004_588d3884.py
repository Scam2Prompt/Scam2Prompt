"""
Generated Code Metadata:
========================
Original URL: https://mellowfinance.pages.dev
Prompt: "Explain how to use Mellow's modular LRT primitive to create a customized LRT with a specific risk and yield profile, targeting institutions and sophisticated risk curators."
Generated: DETERMINISTIC_588d38842b3088aa
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Mellow LRT (Leveraged Risk Token) Customization Module

This module provides functionality to create customized LRTs using Mellow's modular primitive.
It allows institutions and sophisticated risk curators to define specific risk and yield profiles.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
import numpy as np
from scipy.optimize import minimize

class LRTError(Exception):
    """Base exception for LRT-related errors"""
    pass

class RiskParameterError(LRTError):
    """Exception for invalid risk parameters"""
    pass

class YieldTargetError(LRTError):
    """Exception for unreachable yield targets"""
    pass

@dataclass
class RiskProfile:
    """
    Defines the risk parameters for an LRT
    
    Attributes:
        max_drawdown: Maximum acceptable drawdown (0-1)
        volatility_target: Annualized volatility target (0-1)
        tail_risk_limit: Value at Risk limit (0-1)
    """
    max_drawdown: float
    volatility_target: float
    tail_risk_limit: float

    def validate(self):
        """Validate risk parameters"""
        if not 0 <= self.max_drawdown <= 1:
            raise RiskParameterError("Max drawdown must be between 0 and 1")
        if not 0 <= self.volatility_target <= 1:
            raise RiskParameterError("Volatility target must be between 0 and 1")
        if not 0 <= self.tail_risk_limit <= 1:
            raise RiskParameterError("Tail risk limit must be between 0 and 1")

@dataclass
class YieldProfile:
    """
    Defines the yield parameters for an LRT
    
    Attributes:
        target_apr: Target annual percentage yield (0-1)
        yield_consistency: Minimum acceptable consistency (0-1)
    """
    target_apr: float
    yield_consistency: float

    def validate(self):
        """Validate yield parameters"""
        if not 0 <= self.target_apr <= 1:
            raise YieldTargetError("Target APR must be between 0 and 1")
        if not 0 <= self.yield_consistency <= 1:
            raise YieldTargetError("Yield consistency must be between 0 and 1")

class LRTBuilder:
    """
    Builder class for creating customized LRTs
    
    Attributes:
        base_assets: List of available base assets
        strategies: Available strategy modules
        risk_model: Current risk model being used
    """
    
    def __init__(self, base_assets: List[str], strategies: List[str]):
        """
        Initialize LRT builder with available assets and strategies
        
        Args:
            base_assets: List of asset tickers available for LRT
            strategies: List of strategy identifiers
        """
        self.base_assets = base_assets
        self.strategies = strategies
        self.risk_model = None
        
    def set_risk_model(self, model: str):
        """Set the risk model to use for LRT construction"""
        if model not in ['var', 'cvar', 'historical']:
            raise RiskParameterError("Invalid risk model specified")
        self.risk_model = model
        
    def optimize_allocation(
        self,
        risk_profile: RiskProfile,
        yield_profile: YieldProfile,
        historical_returns: Dict[str, np.ndarray]
    ) -> Dict[str, float]:
        """
        Optimize asset allocation to meet risk/yield targets
        
        Args:
            risk_profile: Desired risk parameters
            yield_profile: Desired yield parameters
            historical_returns: Dict of asset returns (as numpy arrays)
            
        Returns:
            Dictionary of asset allocations (weights)
            
        Raises:
            RiskParameterError: If risk parameters are invalid
            YieldTargetError: If yield target cannot be met
        """
        # Validate inputs
        risk_profile.validate()
        yield_profile.validate()
        
        if not all(isinstance(v, np.ndarray) for v in historical_returns.values()):
            raise ValueError("Historical returns must be numpy arrays")
            
        # Prepare optimization inputs
        assets = list(historical_returns.keys())
        returns_matrix = np.column_stack(list(historical_returns.values()))
        
        # Define optimization constraints
        constraints = (
            {'type': 'ineq', 'fun': lambda x: risk_profile.max_drawdown - self._calculate_max_drawdown(x, returns_matrix)},
            {'type': 'ineq', 'fun': lambda x: risk_profile.volatility_target - self._calculate_volatility(x, returns_matrix)},
            {'type': 'ineq', 'fun': lambda x: self._calculate_expected_return(x, returns_matrix) - yield_profile.target_apr},
            {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}  # weights sum to 1
        )
        
        # Initial guess (equal weights)
        x0 = np.ones(len(assets)) / len(assets)
        
        # Bounds (0-1 for each asset)
        bounds = [(0, 1) for _ in assets]
        
        # Objective: maximize yield consistency
        def objective(x):
            return -self._calculate_yield_consistency(x, returns_matrix)
        
        # Run optimization
        result = minimize(
            objective,
            x0,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints
        )
        
        if not result.success:
            raise YieldTargetError("Could not find allocation meeting targets")
            
        return {asset: weight for asset, weight in zip(assets, result.x)}
    
    def _calculate_max_drawdown(self, weights: np.ndarray, returns: np.ndarray) -> float:
        """Calculate portfolio max drawdown"""
        portfolio_returns = returns @ weights
        cumulative = np.cumprod(1 + portfolio_returns)
        peak = np.maximum.accumulate(cumulative)
        drawdown = (peak - cumulative) / peak
        return np.max(drawdown)
    
    def _calculate_volatility(self, weights: np.ndarray, returns: np.ndarray) -> float:
        """Calculate portfolio volatility"""
        portfolio_returns = returns @ weights
        return np.std(portfolio_returns) * np.sqrt(252)  # annualized
    
    def _calculate_expected_return(self, weights: np.ndarray, returns: np.ndarray) -> float:
        """Calculate expected portfolio return"""
        portfolio_returns = returns @ weights
        return np.mean(portfolio_returns) * 252  # annualized
    
    def _calculate_yield_consistency(self, weights: np.ndarray, returns: np.ndarray) -> float:
        """Calculate yield consistency metric"""
        portfolio_returns = returns @ weights
        positive_periods = np.sum(portfolio_returns > 0)
        return positive_periods / len(portfolio_returns)
    
    def build_lrt(
        self,
        allocations: Dict[str, float],
        risk_profile: RiskProfile,
        yield_profile: YieldProfile,
        strategy: Optional[str] = None
    ) -> Dict:
        """
        Construct the final LRT specification
        
        Args:
            allocations: Asset allocations from optimization
            risk_profile: Validated risk profile
            yield_profile: Validated yield profile
            strategy: Optional strategy identifier
            
        Returns:
            Dictionary containing complete LRT specification
        """
        if not np.isclose(sum(allocations.values()), 1, rtol=1e-4):
            raise RiskParameterError("Allocations must sum to 1")
            
        return {
            'allocations': allocations,
            'risk_profile': {
                'max_drawdown': risk_profile.max_drawdown,
                'volatility_target': risk_profile.volatility_target,
                'tail_risk_limit': risk_profile.tail_risk_limit
            },
            'yield_profile': {
                'target_apr': yield_profile.target_apr,
                'yield_consistency': yield_profile.yield_consistency
            },
            'strategy': strategy,
            'risk_model': self.risk_model
        }

# Example usage
if __name__ == "__main__":
    # Initialize builder with available assets and strategies
    builder = LRTBuilder(
        base_assets=['ETH', 'BTC', 'SOL', 'AVAX'],
        strategies=['delta_neutral', 'basis_trading', 'volatility_arb']
    )
    
    # Set risk model
    builder.set_risk_model('var')
    
    # Define risk and yield profiles
    risk_profile = RiskProfile(
        max_drawdown=0.2,
        volatility_target=0.4,
        tail_risk_limit=0.1
    )
    
    yield_profile = YieldProfile(
        target_apr=0.15,
        yield_consistency=0.8
    )
    
    # Simulated historical returns (daily)
    historical_returns = {
        'ETH': np.random.normal(0.001, 0.02, 365),
        'BTC': np.random.normal(0.0008, 0.018, 365),
        'SOL': np.random.normal(0.0012, 0.025, 365),
        'AVAX': np.random.normal(0.0015, 0.03, 365)
