"""
Generated Code Metadata:
========================
Original URL: https://infinite-v2.vercel.app
Prompt: Create a function that calculates risk factors for vaults in a DeFi trading environment, inspired by the metrics discussed on Infinite Trading's site.
Generated: DETERMINISTIC_e01962ef0ca9db2b
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass

@dataclass
class VaultMetrics:
    """Data class to store vault risk metrics"""
    collateral_ratio: float
    liquidation_ratio: float
    utilization_rate: float
    volatility: float
    liquidity_depth: float
    oracle_freshness: int  # in seconds
    historical_liquidation_count: int

@dataclass
class RiskFactors:
    """Data class to store calculated risk factors"""
    collateral_risk: float
    liquidation_risk: float
    market_risk: float
    oracle_risk: float
    liquidity_risk: float
    overall_risk: float

def calculate_risk_factors(vault_metrics: VaultMetrics) -> RiskFactors:
    """
    Calculate risk factors for a DeFi vault based on various metrics.
    
    Args:
        vault_metrics: VaultMetrics object containing vault parameters
        
    Returns:
        RiskFactors object with calculated risk scores (0-1 scale where 1 is highest risk)
    """
    # Collateral Risk (based on collateral ratio and liquidation ratio)
    collateral_risk = max(
        0,
        min(
            1,
            (vault_metrics.liquidation_ratio * 1.1 - vault_metrics.collateral_ratio) 
            / (vault_metrics.liquidation_ratio * 0.5)
        )
    )
    
    # Liquidation Risk (based on proximity to liquidation)
    liquidation_risk = max(
        0,
        min(
            1,
            (vault_metrics.liquidation_ratio - vault_metrics.collateral_ratio) 
            / (vault_metrics.liquidation_ratio * 0.2)
        )
    )
    
    # Market Risk (based on volatility and historical liquidations)
    market_risk = min(
        1,
        (vault_metrics.volatility * 0.5) 
        + (math.log1p(vault_metrics.historical_liquidation_count) * 0.2)
    )
    
    # Oracle Risk (based on data freshness)
    oracle_risk = min(1, vault_metrics.oracle_freshness / 3600)  # 1 hour = max risk
    
    # Liquidity Risk (based on utilization and depth)
    liquidity_risk = min(
        1,
        (vault_metrics.utilization_rate * 0.7) 
        + ((1 / (1 + vault_metrics.liquidity_depth)) * 0.3)
    )
    
    # Overall weighted risk score
    weights = {
        'collateral': 0.25,
        'liquidation': 0.25,
        'market': 0.2,
        'oracle': 0.15,
        'liquidity': 0.15
    }
    
    overall_risk = (
        collateral_risk * weights['collateral']
        + liquidation_risk * weights['liquidation']
        + market_risk * weights['market']
        + oracle_risk * weights['oracle']
        + liquidity_risk * weights['liquidity']
    )
    
    return RiskFactors(
        collateral_risk=round(collateral_risk, 4),
        liquidation_risk=round(liquidation_risk, 4),
        market_risk=round(market_risk, 4),
        oracle_risk=round(oracle_risk, 4),
        liquidity_risk=round(liquidity_risk, 4),
        overall_risk=round(overall_risk, 4)
    )

def validate_vault_metrics(metrics: VaultMetrics) -> bool:
    """
    Validate that vault metrics are within reasonable bounds.
    
    Args:
        metrics: VaultMetrics object to validate
        
    Returns:
        bool: True if metrics are valid, False otherwise
    """
    if metrics.collateral_ratio <= 0:
        return False
    if metrics.liquidation_ratio <= 0 or metrics.liquidation_ratio > 10:
        return False
    if metrics.utilization_rate < 0 or metrics.utilization_rate > 1:
        return False
    if metrics.volatility < 0:
        return False
    if metrics.liquidity_depth < 0:
        return False
    if metrics.oracle_freshness < 0:
        return False
    if metrics.historical_liquidation_count < 0:
        return False
    return True

def get_vault_risk(vault_metrics: VaultMetrics) -> RiskFactors:
    """
    Main function to get risk factors for a vault with validation.
    
    Args:
        vault_metrics: VaultMetrics object containing vault parameters
        
    Returns:
        RiskFactors object with calculated risk scores
        
    Raises:
        ValueError: If vault metrics are invalid
    """
    if not validate_vault_metrics(vault_metrics):
        raise ValueError("Invalid vault metrics provided")
    
    return calculate_risk_factors(vault_metrics)
```
