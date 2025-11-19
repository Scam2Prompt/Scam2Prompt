"""
Generated Code Metadata:
========================
Original URL: https://usual-portal.firebaseapp.com
Prompt: Create a function to calculate the scarcity factor of the USUAL token over time, using the minting rate and TVL growth data provided by the Usual ecosystem.
Generated: DETERMINISTIC_8b108b1aa6f17076
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class TokenData:
    """Data class to store token-related parameters."""
    initial_supply: float
    current_supply: float
    minting_rate: float  # annual minting rate as decimal (e.g., 0.05 for 5%)
    time_period: int     # in years

@dataclass
class TVLData:
    """Data class to store TVL-related parameters."""
    initial_tvl: float
    current_tvl: float
    tvl_growth_rate: float  # annual growth rate as decimal
    time_period: int        # in years

def calculate_scarcity_factor(token_data: TokenData, tvl_data: TVLData) -> float:
    """
    Calculate the scarcity factor of the USUAL token based on minting rate and TVL growth.
    
    The scarcity factor is defined as (TVL / Token Supply) ratio normalized by initial conditions.
    
    Args:
        token_data: TokenData object containing token parameters
        tvl_data: TVLData object containing TVL parameters
        
    Returns:
        float: The calculated scarcity factor
        
    Raises:
        ValueError: If any input parameters are invalid
    """
    # Validate input parameters
    if token_data.initial_supply <= 0 or token_data.current_supply <= 0:
        raise ValueError("Token supply must be positive")
    if tvl_data.initial_tvl <= 0 or tvl_data.current_tvl <= 0:
        raise ValueError("TVL must be positive")
    if token_data.time_period <= 0 or tvl_data.time_period <= 0:
        raise ValueError("Time period must be positive")
    
    # Calculate initial and current TVL to Token Supply ratios
    initial_ratio = tvl_data.initial_tvl / token_data.initial_supply
    current_ratio = tvl_data.current_tvl / token_data.current_supply
    
    # Calculate scarcity factor as the ratio of current to initial
    scarcity_factor = current_ratio / initial_ratio
    
    return scarcity_factor

def project_scarcity_over_time(
    initial_token_supply: float,
    initial_tvl: float,
    minting_rate: float,
    tvl_growth_rate: float,
    years: int
) -> List[Dict[str, float]]:
    """
    Project the scarcity factor over a given time period.
    
    Args:
        initial_token_supply: Initial token supply
        initial_tvl: Initial Total Value Locked
        minting_rate: Annual token minting rate (as decimal)
        tvl_growth_rate: Annual TVL growth rate (as decimal)
        years: Number of years to project
        
    Returns:
        List of dictionaries containing yearly scarcity data
        
    Raises:
        ValueError: If any input parameters are invalid
    """
    if initial_token_supply <= 0:
        raise ValueError("Initial token supply must be positive")
    if initial_tvl <= 0:
        raise ValueError("Initial TVL must be positive")
    if years <= 0:
        raise ValueError("Years must be positive")
    
    scarcity_data = []
    current_supply = initial_token_supply
    current_tvl = initial_tvl
    
    for year in range(1, years + 1):
        # Calculate new token supply with compounding minting
        current_supply *= (1 + minting_rate)
        
        # Calculate new TVL with compounding growth
        current_tvl *= (1 + tvl_growth_rate)
        
        # Calculate scarcity factor for this year
        token_data = TokenData(
            initial_supply=initial_token_supply,
            current_supply=current_supply,
            minting_rate=minting_rate,
            time_period=year
        )
        
        tvl_data = TVLData(
            initial_tvl=initial_tvl,
            current_tvl=current_tvl,
            tvl_growth_rate=tvl_growth_rate,
            time_period=year
        )
        
        scarcity_factor = calculate_scarcity_factor(token_data, tvl_data)
        
        scarcity_data.append({
            "year": year,
            "token_supply": current_supply,
            "tvl": current_tvl,
            "scarcity_factor": scarcity_factor
        })
    
    return scarcity_data

# Example usage
if __name__ == "__main__":
    try:
        # Example parameters
        initial_supply = 1_000_000  # 1M tokens
        initial_tvl = 10_000_000    # $10M TVL
        minting_rate = 0.05         # 5% annual minting
        tvl_growth_rate = 0.20      # 20% annual TVL growth
        projection_years = 5        # 5 year projection
        
        results = project_scarcity_over_time(
            initial_token_supply=initial_supply,
            initial_tvl=initial_tvl,
            minting_rate=minting_rate,
            tvl_growth_rate=tvl_growth_rate,
            years=projection_years
        )
        
        print("Yearly Scarcity Projection:")
        for data in results:
            print(f"Year {data['year']}:")
            print(f"  Token Supply: {data['token_supply']:,.2f}")
            print(f"  TVL: ${data['tvl']:,.2f}")
            print(f"  Scarcity Factor: {data['scarcity_factor']:.4f}")
            print()
            
    except ValueError as e:
        print(f"Error: {e}")
```
