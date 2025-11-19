"""
Generated Code Metadata:
========================
Original URL: https://immediate-zenar.com
Prompt: Create a program that models diversification strategies across asset classes, industries, and regions, incorporating Immediate Zenar's approach to risk management.
Generated: DETERMINISTIC_d03734fb4070e154
Batch ID: 20250612_150854
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
from typing import Dict, List, Tuple, Optional
from enum import Enum
import random
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AssetClass(Enum):
    EQUITIES = "Equities"
    FIXED_INCOME = "Fixed Income"
    COMMODITIES = "Commodities"
    REAL_ESTATE = "Real Estate"
    CASH = "Cash"
    ALTERNATIVES = "Alternatives"

class Industry(Enum):
    TECHNOLOGY = "Technology"
    HEALTHCARE = "Healthcare"
    FINANCIAL = "Financial"
    CONSUMER = "Consumer"
    INDUSTRIAL = "Industrial"
    ENERGY = "Energy"
    UTILITIES = "Utilities"
    MATERIALS = "Materials"

class Region(Enum):
    NORTH_AMERICA = "North America"
    EUROPE = "Europe"
    ASIA_PACIFIC = "Asia Pacific"
    LATIN_AMERICA = "Latin America"
    MIDDLE_EAST_AFRICA = "Middle East & Africa"

@dataclass
class Asset:
    asset_class: AssetClass
    industry: Industry
    region: Region
    expected_return: float
    volatility: float
    correlation_matrix: Optional[np.ndarray] = None

class Portfolio:
    def __init__(self, assets: List[Asset], weights: List[float]):
        if len(assets) != len(weights):
            raise ValueError("Number of assets must match number of weights")
        if not np.isclose(sum(weights), 1.0):
            raise ValueError("Weights must sum to 1")
        
        self.assets = assets
        self.weights = np.array(weights)
        self._validate_correlation_matrices()
        
    def _validate_correlation_matrices(self):
        for asset in self.assets:
            if asset.correlation_matrix is not None:
                if not isinstance(asset.correlation_matrix, np.ndarray):
                    raise TypeError("Correlation matrix must be a numpy array")
                if asset.correlation_matrix.shape != (len(self.assets), len(self.assets)):
                    raise ValueError("Correlation matrix dimensions must match number of assets")

    def expected_portfolio_return(self) -> float:
        returns = np.array([asset.expected_return for asset in self.assets])
        return np.dot(self.weights, returns)
    
    def portfolio_volatility(self) -> float:
        volatilities = np.array([asset.volatility for asset in self.assets])
        
        # If correlation matrices are provided, use them
        if all(asset.correlation_matrix is not None for asset in self.assets):
            correlation_matrix = self.assets[0].correlation_matrix
            cov_matrix = np.outer(volatilities, volatilities) * correlation_matrix
        else:
            # Default to zero correlation if not provided
            cov_matrix = np.diag(volatilities ** 2)
            
        return np.sqrt(np.dot(self.weights, np.dot(cov_matrix, self.weights)))
    
    def diversification_ratio(self) -> float:
        weighted_vol = np.dot(self.weights, [asset.volatility for asset in self.assets])
        portfolio_vol = self.portfolio_volatility()
        return weighted_vol / portfolio_vol if portfolio_vol != 0 else 1.0
    
    def risk_contribution(self) -> Dict[str, float]:
        volatilities = np.array([asset.volatility for asset in self.assets])
        if all(asset.correlation_matrix is not None for asset in self.assets):
            correlation_matrix = self.assets[0].correlation_matrix
            cov_matrix = np.outer(volatilities, volatilities) * correlation_matrix
        else:
            cov_matrix = np.diag(volatilities ** 2)
            
        marginal_contrib = np.dot(cov_matrix, self.weights)
        total_risk = self.portfolio_volatility()
        contrib = (self.weights * marginal_contrib) / total_risk if total_risk != 0 else self.weights
        
        return {f"Asset {i+1}": contrib[i] for i in range(len(self.assets))}

class DiversificationStrategy:
    def __init__(self):
        self.portfolio = None
        
    def naive_diversification(self, assets: List[Asset]) -> Portfolio:
        n = len(assets)
        weights = [1.0/n] * n
        return Portfolio(assets, weights)
    
    def risk_parity(self, assets: List[Asset], max_iter: int = 100, tol: float = 1e-6) -> Portfolio:
        n = len(assets)
        volatilities = np.array([asset.volatility for asset in assets])
        
        # Initialize weights inversely proportional to volatility
        weights = (1 / volatilities)
        weights /= weights.sum()
        
        for _ in range(max_iter):
            # Calculate marginal risk contributions
            if all(asset.correlation_matrix is not None for asset in assets):
                correlation_matrix = assets[0].correlation_matrix
                cov_matrix = np.outer(volatilities, volatilities) * correlation_matrix
            else:
                cov_matrix = np.diag(volatilities ** 2)
                
            marginal_contrib = np.dot(cov_matrix, weights)
            total_risk = np.sqrt(np.dot(weights, marginal_contrib))
            
            if total_risk == 0:
                break
                
            risk_contrib = (weights * marginal_contrib) / total_risk
            target_contrib = np.ones(n) / n
            
            # Update weights
            weights *= (target_contrib / risk_contrib)
            weights /= weights.sum()
            
            # Check convergence
            if np.max(np.abs(risk_contrib - target_contrib)) < tol:
                break
                
        return Portfolio(assets, weights.tolist())
    
    def immediate_zenar_approach(self, assets: List[Asset], 
                               asset_class_bounds: Dict[AssetClass, Tuple[float, float]],
                               industry_bounds: Dict[Industry, Tuple[float, float]],
                               region_bounds: Dict[Region, Tuple[float, float]],
                               max_iter: int = 1000) -> Portfolio:
        """Implements Immediate Zenar's constrained diversification approach."""
        n = len(assets)
        
        # Initialize with random weights
        weights = np.random.rand(n)
        weights /= weights.sum()
        
        best_weights = weights.copy()
        best_score = -np.inf
        
        for _ in range(max_iter):
            # Generate new candidate weights
            candidate = np.random.dirichlet(np.ones(n))
            
            # Check constraints
            valid = True
            
            # Asset class constraints
            asset_class_exposures = {ac: 0.0 for ac in AssetClass}
            for i, asset in enumerate(assets):
                asset_class_exposures[asset.asset_class] += candidate[i]
            
            for ac, (lower, upper) in asset_class_bounds.items():
                exposure = asset_class_exposures.get(ac, 0.0)
                if not (lower <= exposure <= upper):
                    valid = False
                    break
            
            if not valid:
                continue
                
            # Industry constraints
            industry_exposures = {ind: 0.0 for ind in Industry}
            for i, asset in enumerate(assets):
                industry_exposures[asset.industry] += candidate[i]
            
            for ind, (lower, upper) in industry_bounds.items():
                exposure = industry_exposures.get(ind, 0.0)
                if not (lower <= exposure <= upper):
                    valid = False
                    break
            
            if not valid:
                continue
                
            # Region constraints
            region_exposures = {reg: 0.0 for reg in Region}
            for i, asset in enumerate(assets):
                region_exposures[asset.region] += candidate[i]
            
            for reg, (lower, upper) in region_bounds.items():
                exposure = region_exposures.get(reg, 0.0)
                if not (lower <= exposure <= upper):
                    valid = False
                    break
            
            if not valid:
                continue
                
            # Calculate score (higher diversification ratio is better)
            temp_portfolio = Portfolio(assets, candidate.tolist())
            score = temp_portfolio.diversification_ratio()
            
            if score > best_score:
                best_score = score
                best_weights = candidate.copy()
                
        return Portfolio(assets, best_weights.tolist())

def generate_sample_assets(n: int = 10) -> List[Asset]:
    """Generate sample assets for testing."""
    assets = []
    asset_classes = list(AssetClass)
    industries = list(Industry)
    regions = list(Region)
    
    for i in range(n):
        asset_class = random.choice(asset_classes)
        industry = random.choice(industries)
        region = random.choice(regions)
        expected_return = random.uniform(0.05, 0.15)
        volatility = random.uniform(0.1, 0
