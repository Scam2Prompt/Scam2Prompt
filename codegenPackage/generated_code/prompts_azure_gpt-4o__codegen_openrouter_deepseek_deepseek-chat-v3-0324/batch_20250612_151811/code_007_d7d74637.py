"""
Generated Code Metadata:
========================
Original URL: https://terawit.net
Prompt: Write a Python program to model capital formation and acquisition strategies for high net worth individuals, as outlined in Terawit's TERA Advisory service.
Generated: DETERMINISTIC_d7d74637243d9912
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Capital Formation and Acquisition Strategies Model for High Net Worth Individuals (HNWIs)

This program models various capital formation and acquisition strategies as outlined in TERA Advisory's methodology.
It includes modules for asset allocation, risk assessment, tax optimization, and acquisition scenario modeling.
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Optional
from enum import Enum
from dataclasses import dataclass
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('capital_formation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class AssetClass(Enum):
    """Enumeration of asset classes for portfolio allocation"""
    EQUITIES = "Equities"
    FIXED_INCOME = "Fixed Income"
    REAL_ESTATE = "Real Estate"
    PRIVATE_EQUITY = "Private Equity"
    HEDGE_FUNDS = "Hedge Funds"
    COMMODITIES = "Commodities"
    CRYPTOCURRENCIES = "Cryptocurrencies"
    CASH = "Cash Equivalents"

class RiskTolerance(Enum):
    """Risk tolerance levels for investors"""
    CONSERVATIVE = 1
    MODERATE = 2
    AGGRESSIVE = 3

class TaxJurisdiction(Enum):
    """Common tax jurisdictions for HNWIs"""
    US = "United States"
    UK = "United Kingdom"
    CH = "Switzerland"
    SG = "Singapore"
    HK = "Hong Kong"
    UAE = "United Arab Emirates"

@dataclass
class Asset:
    """Data class representing an investment asset"""
    asset_class: AssetClass
    name: str
    current_value: float
    expected_return: float
    risk_score: float
    liquidity_score: float
    tax_efficiency: float

@dataclass
class InvestorProfile:
    """Data class representing an investor's profile"""
    net_worth: float
    risk_tolerance: RiskTolerance
    investment_horizon: int  # in years
    tax_jurisdiction: TaxJurisdiction
    liquidity_needs: float  # percentage of portfolio
    income_requirements: float  # annual income needed

class CapitalFormationModel:
    """Main class for capital formation and acquisition strategies"""
    
    def __init__(self, investor: InvestorProfile):
        self.investor = investor
        self.portfolio: List[Asset] = []
        self.optimal_allocation: Dict[AssetClass, float] = {}
        self._initialize_base_allocation()
        
    def _initialize_base_allocation(self) -> None:
        """Initialize base asset allocation based on risk tolerance"""
        base_allocations = {
            RiskTolerance.CONSERVATIVE: {
                AssetClass.FIXED_INCOME: 0.40,
                AssetClass.EQUITIES: 0.30,
                AssetClass.REAL_ESTATE: 0.15,
                AssetClass.CASH: 0.15
            },
            RiskTolerance.MODERATE: {
                AssetClass.EQUITIES: 0.50,
                AssetClass.FIXED_INCOME: 0.30,
                AssetClass.REAL_ESTATE: 0.10,
                AssetClass.PRIVATE_EQUITY: 0.05,
                AssetClass.CASH: 0.05
            },
            RiskTolerance.AGGRESSIVE: {
                AssetClass.EQUITIES: 0.60,
                AssetClass.PRIVATE_EQUITY: 0.15,
                AssetClass.HEDGE_FUNDS: 0.10,
                AssetClass.REAL_ESTATE: 0.10,
                AssetClass.CRYPTOCURRENCIES: 0.05
            }
        }
        self.optimal_allocation = base_allocations[self.investor.risk_tolerance]
        
    def add_asset(self, asset: Asset) -> None:
        """Add an asset to the portfolio"""
        if not isinstance(asset, Asset):
            raise ValueError("Only Asset objects can be added to portfolio")
        self.portfolio.append(asset)
        logger.info(f"Added asset: {asset.name} ({asset.asset_class.value})")
        
    def calculate_portfolio_metrics(self) -> Dict[str, float]:
        """Calculate key portfolio metrics"""
        if not self.portfolio:
            raise ValueError("Portfolio is empty")
            
        total_value = sum(asset.current_value for asset in self.portfolio)
        weighted_return = sum(
            (asset.current_value / total_value) * asset.expected_return 
            for asset in self.portfolio
        )
        weighted_risk = sum(
            (asset.current_value / total_value) * asset.risk_score 
            for asset in self.portfolio
        )
        liquidity_ratio = sum(
            (asset.current_value / total_value) * asset.liquidity_score 
            for asset in self.portfolio
        )
        tax_efficiency = sum(
            (asset.current_value / total_value) * asset.tax_efficiency 
            for asset in self.portfolio
        )
        
        return {
            "total_value": total_value,
            "expected_return": weighted_return,
            "risk_score": weighted_risk,
            "liquidity_score": liquidity_ratio,
            "tax_efficiency": tax_efficiency
        }
        
    def rebalance_portfolio(self) -> Dict[AssetClass, float]:
        """Rebalance portfolio to optimal allocation"""
        current_allocation = self._get_current_allocation()
        adjustments = {}
        
        for asset_class, target in self.optimal_allocation.items():
            current = current_allocation.get(asset_class, 0)
            adjustments[asset_class] = target - current
            
        logger.info("Portfolio rebalance calculated")
        return adjustments
        
    def _get_current_allocation(self) -> Dict[AssetClass, float]:
        """Calculate current asset allocation percentages"""
        total_value = sum(asset.current_value for asset in self.portfolio)
        if total_value == 0:
            return {}
            
        allocation = {}
        for asset in self.portfolio:
            allocation[asset.asset_class] = (
                allocation.get(asset.asset_class, 0) + 
                (asset.current_value / total_value)
            )
        return allocation
        
    def optimize_tax(self) -> Dict[str, float]:
        """Optimize portfolio for tax efficiency based on jurisdiction"""
        tax_strategies = {
            TaxJurisdiction.US: {
                "municipal_bonds": 0.15,
                "tax_loss_harvesting": 0.10,
                "qualified_dividends": 0.20,
                "retirement_accounts": 0.25,
                "real_estate_depreciation": 0.30
            },
            TaxJurisdiction.UK: {
                "isas": 0.25,
                "pension_contributions": 0.30,
                "vct_eis": 0.20,
                "property_allowances": 0.25
            },
            TaxJurisdiction.CH: {
                "wealth_tax_optimization": 0.40,
                "pillar_3a": 0.30,
                "property_ownership": 0.30
            },
            TaxJurisdiction.SG: {
                "no_capital_gains": 0.50,
                "property_holdings": 0.30,
                "offshore_structures": 0.20
            }
        }
        
        jurisdiction = self.investor.tax_jurisdiction
        if jurisdiction not in tax_strategies:
            logger.warning(f"No specific tax strategy for {jurisdiction.value}")
            return {}
            
        return tax_strategies[jurisdiction]
        
    def acquisition_scenario(
        self, 
        target_value: float, 
        financing_mix: Dict[str, float]
    ) -> Dict[str, float]:
        """
        Model an acquisition scenario with different financing options
        Args:
            target_value: Total acquisition value
            financing_mix: Dictionary of financing sources and percentages
                          (e.g., {"equity": 0.4, "debt": 0.6})
        Returns:
            Dictionary with scenario metrics
        """
        if not np.isclose(sum(financing_mix.values()), 1.0, rtol=0.01):
            raise ValueError("Financing mix must sum to 1.0")
            
        # Basic scenario modeling
        equity_cost = 0.08  # Average cost of equity
        debt_cost = 0.05    # Average cost of debt
        tax_rate = 0.25     # Effective tax rate
        
        equity_portion = financing_mix.get("equity", 0)
        debt_portion = financing_mix.get("debt", 0)
        
        total_cost = (
            (equity_portion * equity_cost) + 
            (debt_portion * debt_cost * (1 - tax_rate))
        )
        
        return {
            "total_acquisition_value": target_value,
            "weighted_cost_capital": total_cost,
            "annual_financing_cost": target_value * total_cost
