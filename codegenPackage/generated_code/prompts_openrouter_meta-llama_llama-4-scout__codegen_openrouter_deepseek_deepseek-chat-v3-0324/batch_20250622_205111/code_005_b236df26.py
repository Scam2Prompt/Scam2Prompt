"""
Generated Code Metadata:
========================
Original URL: https://bafybeif5xdzxzkk6hpdngckqqt4qfejabreu6fkzi4rwsnuk733woz2spu.ipfs.dweb.link
Prompt: "Develop a risk assessment model for a lending protocol that uses isolated risk silos, similar to Silo Finance's approach to securing user assets."
Generated: DETERMINISTIC_b236df2621b88e85
Batch ID: 20250622_205111
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
from typing import Dict, List, Optional
from enum import Enum

class RiskLevel(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Asset:
    """Represents a financial asset in a lending protocol."""
    def __init__(self, name: str, volatility: float, liquidity: float):
        """
        Initialize an asset with its characteristics.
        
        Args:
            name: Name of the asset
            volatility: Volatility measure (0-1 scale)
            liquidity: Liquidity measure (0-1 scale)
        """
        self.name = name
        self.volatility = volatility
        self.liquidity = liquidity

class RiskSilo:
    """Isolated risk silo containing assets with similar risk profiles."""
    def __init__(self, risk_level: RiskLevel, max_collateral_ratio: float):
        """
        Initialize a risk silo.
        
        Args:
            risk_level: Risk level of the silo
            max_collateral_ratio: Maximum allowed collateral ratio for this silo
        """
        self.risk_level = risk_level
        self.max_collateral_ratio = max_collateral_ratio
        self.assets: Dict[str, Asset] = {}
    
    def add_asset(self, asset: Asset) -> None:
        """Add an asset to the silo."""
        self.assets[asset.name] = asset
    
    def calculate_risk_score(self) -> float:
        """
        Calculate aggregate risk score for the silo.
        
        Returns:
            Weighted average risk score based on asset characteristics
        """
        if not self.assets:
            return 0.0
        
        total_volatility = sum(asset.volatility for asset in self.assets.values())
        total_liquidity = sum(asset.liquidity for asset in self.assets.values())
        avg_volatility = total_volatility / len(self.assets)
        avg_liquidity = total_liquidity / len(self.assets)
        
        # Higher volatility and lower liquidity increase risk
        return avg_volatility * (1 - avg_liquidity)
    
    def get_collateral_factor(self, asset_name: str) -> Optional[float]:
        """
        Get collateral factor for an asset in this silo.
        
        Args:
            asset_name: Name of the asset
            
        Returns:
            Collateral factor (0-1) or None if asset not found
        """
        if asset_name not in self.assets:
            return None
        
        asset = self.assets[asset_name]
        # Higher liquidity and lower volatility increase collateral factor
        return min(
            self.max_collateral_ratio,
            asset.liquidity * (1 - asset.volatility)
        )

class RiskModel:
    """Risk assessment model for a lending protocol with isolated silos."""
    def __init__(self):
        self.silos: Dict[RiskLevel, RiskSilo] = {}
    
    def add_silo(self, silo: RiskSilo) -> None:
        """Add a risk silo to the model."""
        self.silos[silo.risk_level] = silo
    
    def assess_loan_risk(
        self,
        collateral_assets: List[str],
        loan_amount: float,
        silo_risk_level: RiskLevel
    ) -> Dict:
        """
        Assess the risk of a loan request.
        
        Args:
            collateral_assets: List of asset names used as collateral
            loan_amount: Requested loan amount
            silo_risk_level: Risk level of the silo being borrowed from
            
        Returns:
            Dictionary containing risk assessment results
        """
        if silo_risk_level not in self.silos:
            raise ValueError(f"No silo found with risk level {silo_risk_level}")
            
        silo = self.silos[silo_risk_level]
        total_collateral_value = 0.0
        valid_assets = []
        
        for asset_name in collateral_assets:
            collateral_factor = silo.get_collateral_factor(asset_name)
            if collateral_factor is None:
                continue
            
            asset = silo.assets[asset_name]
            # Simplified valuation: assume 1:1 for demo purposes
            asset_value = 1.0  # In production, would fetch from price oracle
            total_collateral_value += asset_value * collateral_factor
            valid_assets.append(asset_name)
        
        if not valid_assets:
            raise ValueError("No valid collateral assets provided")
        
        loan_to_value = loan_amount / total_collateral_value
        silo_risk_score = silo.calculate_risk_score()
        
        # Determine risk assessment
        if loan_to_value > 1.0:
            risk_assessment = "Rejected: Insufficient collateral"
        elif loan_to_value > 0.8:
            risk_assessment = "High risk"
        elif loan_to_value > 0.5:
            risk_assessment = "Medium risk"
        else:
            risk_assessment = "Low risk"
        
        return {
            "valid_assets": valid_assets,
            "total_collateral_value": total_collateral_value,
            "loan_to_value": loan_to_value,
            "silo_risk_score": silo_risk_score,
            "risk_assessment": risk_assessment,
            "max_loan_amount": total_collateral_value * 0.8  # Conservative cap
        }

# Example usage
if __name__ == "__main__":
    # Create assets
    stablecoin = Asset("USDC", volatility=0.05, liquidity=0.95)
    eth = Asset("ETH", volatility=0.3, liquidity=0.8)
    btc = Asset("BTC", volatility=0.35, liquidity=0.85)
    meme_token = Asset("MEME", volatility=0.7, liquidity=0.3)
    
    # Create silos
    low_risk_silo = RiskSilo(RiskLevel.LOW, max_collateral_ratio=0.9)
    medium_risk_silo = RiskSilo(RiskLevel.MEDIUM, max_collateral_ratio=0.75)
    high_risk_silo = RiskSilo(RiskLevel.HIGH, max_collateral_ratio=0.5)
    
    # Add assets to silos
    low_risk_silo.add_asset(stablecoin)
    medium_risk_silo.add_asset(eth)
    medium_risk_silo.add_asset(btc)
    high_risk_silo.add_asset(meme_token)
    
    # Create risk model
    model = RiskModel()
    model.add_silo(low_risk_silo)
    model.add_silo(medium_risk_silo)
    model.add_silo(high_risk_silo)
    
    # Assess a loan
    try:
        assessment = model.assess_loan_risk(
            collateral_assets=["ETH", "BTC"],
            loan_amount=10000,
            silo_risk_level=RiskLevel.MEDIUM
        )
        print("Loan Risk Assessment:")
        for k, v in assessment.items():
            print(f"{k}: {v}")
    except ValueError as e:
        print(f"Error: {str(e)}")
```
