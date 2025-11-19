"""
Generated Code Metadata:
========================
Original URL: https://visit-ethena.pages.dev
Prompt: Generate a code example for creating a fixed-rate bond exposure using Ethena's product suite, specifically utilizing expiring futures or perpetual swaps, and explain how it achieves price stability through delta-neutral hedging.
Generated: DETERMINISTIC_a5ddfac28ab3307e
Batch ID: 20250622_205955
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
from typing import Optional, Tuple

class FixedRateBond:
    """
    A class to represent a fixed-rate bond exposure using Ethena's product suite.
    This implementation uses expiring futures and perpetual swaps to achieve price stability
    through delta-neutral hedging.
    """
    
    def __init__(self, notional: float, fixed_rate: float, maturity_days: int):
        """
        Initialize the fixed-rate bond exposure.
        
        Args:
            notional: The notional amount of the bond
            fixed_rate: The fixed interest rate (annualized)
            maturity_days: Time to maturity in days
        """
        self.notional = notional
        self.fixed_rate = fixed_rate
        self.maturity_days = maturity_days
        self.futures_position = 0.0
        self.perps_position = 0.0
        
    def calculate_delta_neutral_hedge(self, futures_price: float, perps_price: float) -> Tuple[float, float]:
        """
        Calculate the required futures and perpetual swap positions to achieve delta neutrality.
        
        Args:
            futures_price: Current price of the expiring futures contract
            perps_price: Current price of the perpetual swap
            
        Returns:
            Tuple of (futures_position, perps_position) in notional terms
        """
        try:
            # Calculate hedge ratio (simplified example - in practice would use more sophisticated models)
            hedge_ratio = futures_price / perps_price
            
            # Calculate positions (negative sign indicates hedging/short position)
            futures_position = -self.notional * hedge_ratio
            perps_position = self.notional
            
            return futures_position, perps_position
        except ZeroDivisionError:
            raise ValueError("Prices cannot be zero")
        except Exception as e:
            raise RuntimeError(f"Error calculating delta-neutral hedge: {str(e)}")
    
    def update_hedge(self, futures_price: float, perps_price: float) -> None:
        """
        Update the hedge positions based on current market prices.
        
        Args:
            futures_price: Current price of the expiring futures contract
            perps_price: Current price of the perpetual swap
        """
        try:
            self.futures_position, self.perps_position = self.calculate_delta_neutral_hedge(futures_price, perps_price)
        except Exception as e:
            print(f"Failed to update hedge: {str(e)}")
            raise
    
    def calculate_pnl(self, futures_price: float, perps_price: float, days_passed: int) -> float:
        """
        Calculate the profit and loss of the position.
        
        Args:
            futures_price: Current price of the expiring futures contract
            perps_price: Current price of the perpetual swap
            days_passed: Number of days since position was opened
            
        Returns:
            The net PnL of the position
        """
        try:
            if days_passed > self.maturity_days:
                raise ValueError("Days passed cannot exceed maturity days")
                
            # Calculate interest accrued
            interest = self.notional * self.fixed_rate * (days_passed / 365)
            
            # Calculate futures and perps PnL
            futures_pnl = self.futures_position * (1 - futures_price)
            perps_pnl = self.perps_position * (perps_price - 1)
            
            return interest + futures_pnl + perps_pnl
        except Exception as e:
            raise RuntimeError(f"Error calculating PnL: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a fixed-rate bond with $1M notional, 5% fixed rate, 90-day maturity
        bond = FixedRateBond(notional=1_000_000, fixed_rate=0.05, maturity_days=90)
        
        # Current market prices
        futures_price = 1.02
        perps_price = 1.01
        
        # Update hedge positions
        bond.update_hedge(futures_price, perps_price)
        
        # Calculate PnL after 30 days
        pnl = bond.calculate_pnl(futures_price=1.03, perps_price=1.02, days_passed=30)
        print(f"Current PnL: ${pnl:,.2f}")
        
    except Exception as e:
        print(f"Error in bond example: {str(e)}")
```
