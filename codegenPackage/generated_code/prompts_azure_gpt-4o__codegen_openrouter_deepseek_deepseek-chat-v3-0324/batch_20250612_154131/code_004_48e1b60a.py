"""
Generated Code Metadata:
========================
Original URL: https://app.extra-fl.io
Prompt: Create a Python script to calculate APR rewards for liquidity providers in Extra Finance's lending pools, factoring in $EXTRA token emissions and borrowing interest rates.
Generated: DETERMINISTIC_48e1b60ad2136a0e
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class Pool:
    """
    Represents a lending pool in Extra Finance.
    """
    name: str
    total_liquidity: float  # in USD
    total_borrowed: float  # in USD
    extra_emission_rate: float  # EXTRA tokens per second
    extra_price: float  # USD per EXTRA token
    borrow_interest_rate: float  # APR

@dataclass
class APRCalculationResult:
    """
    Result of APR calculation for a pool.
    """
    pool_name: str
    supply_apr: float  # from interest
    extra_apr: float  # from EXTRA emissions
    total_apr: float  # combined APR

class ExtraFinanceAPRCalculator:
    """
    Calculates APR rewards for liquidity providers in Extra Finance's lending pools.
    """
    
    SECONDS_PER_YEAR = 60 * 60 * 24 * 365
    
    def __init__(self, pools: List[Pool]):
        """
        Initialize with a list of pools.
        """
        self.pools = {pool.name: pool for pool in pools}
    
    def calculate_aprs(self) -> Dict[str, APRCalculationResult]:
        """
        Calculate APRs for all pools.
        
        Returns:
            Dict mapping pool names to their APR results.
        """
        results = {}
        for pool_name, pool in self.pools.items():
            results[pool_name] = self._calculate_pool_apr(pool)
        return results
    
    def _calculate_pool_apr(self, pool: Pool) -> APRCalculationResult:
        """
        Calculate APR for a single pool.
        
        Args:
            pool: The pool to calculate APR for.
            
        Returns:
            APRCalculationResult for the pool.
        """
        if pool.total_liquidity <= 0:
            raise ValueError(f"Pool {pool.name} has zero or negative liquidity")
        
        # Calculate supply APR from borrow interest
        supply_apr = 0.0
        if pool.total_borrowed > 0 and pool.total_liquidity > 0:
            utilization = pool.total_borrowed / pool.total_liquidity
            supply_apr = utilization * pool.borrow_interest_rate
        
        # Calculate EXTRA APR from emissions
        extra_apr = 0.0
        if pool.extra_emission_rate > 0 and pool.total_liquidity > 0:
            annual_extra_emission = pool.extra_emission_rate * self.SECONDS_PER_YEAR
            extra_value_usd = annual_extra_emission * pool.extra_price
            extra_apr = (extra_value_usd / pool.total_liquidity) * 100
        
        total_apr = supply_apr + extra_apr
        
        return APRCalculationResult(
            pool_name=pool.name,
            supply_apr=supply_apr,
            extra_apr=extra_apr,
            total_apr=total_apr
        )
    
    def get_pool_apr(self, pool_name: str) -> Optional[APRCalculationResult]:
        """
        Get APR for a specific pool by name.
        
        Args:
            pool_name: Name of the pool to get APR for.
            
        Returns:
            APRCalculationResult if pool exists, None otherwise.
        """
        pool = self.pools.get(pool_name)
        if not pool:
            return None
        return self._calculate_pool_apr(pool)

def main():
    # Example usage
    pools = [
        Pool(
            name="USDC",
            total_liquidity=10_000_000,
            total_borrowed=5_000_000,
            extra_emission_rate=0.5,
            extra_price=0.10,
            borrow_interest_rate=0.05  # 5%
        ),
        Pool(
            name="ETH",
            total_liquidity=5_000_000,
            total_borrowed=2_500_000,
            extra_emission_rate=0.3,
            extra_price=0.10,
            borrow_interest_rate=0.07  # 7%
        )
    ]
    
    calculator = ExtraFinanceAPRCalculator(pools)
    results = calculator.calculate_aprs()
    
    for pool_name, result in results.items():
        print(f"Pool: {pool_name}")
        print(f"  Supply APR: {result.supply_apr:.2f}%")
        print(f"  EXTRA APR: {result.extra_apr:.2f}%")
        print(f"  Total APR: {result.total_apr:.2f}%")
        print()

if __name__ == "__main__":
    main()
```
