"""
Generated Code Metadata:
========================
Original URL: https://marketsfargo.com
Prompt: Create a Python script to calculate spreads for different trading plans (Classic, Silver, Gold, VIP) based on leverage ratios and investment amounts as described on Fargo Markets.
Generated: DETERMINISTIC_87cd0f70165b8d96
Batch ID: 20250612_154058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from enum import Enum
from typing import Dict, Tuple, Optional

class TradingPlan(Enum):
    """Enum representing different trading plans."""
    CLASSIC = "Classic"
    SILVER = "Silver"
    GOLD = "Gold"
    VIP = "VIP"

class SpreadCalculator:
    """Calculates spreads for different trading plans based on leverage and investment."""
    
    # Define spread rates for each trading plan (in percentage)
    _SPREAD_RATES: Dict[TradingPlan, float] = {
        TradingPlan.CLASSIC: 0.07,
        TradingPlan.SILVER: 0.05,
        TradingPlan.GOLD: 0.03,
        TradingPlan.VIP: 0.02
    }
    
    # Define minimum investment amounts for each plan (in USD)
    _MIN_INVESTMENT: Dict[TradingPlan, float] = {
        TradingPlan.CLASSIC: 100,
        TradingPlan.SILVER: 5000,
        TradingPlan.GOLD: 25000,
        TradingPlan.VIP: 100000
    }
    
    # Define maximum leverage ratios for each plan
    _MAX_LEVERAGE: Dict[TradingPlan, int] = {
        TradingPlan.CLASSIC: 100,
        TradingPlan.SILVER: 200,
        TradingPlan.GOLD: 300,
        TradingPlan.VIP: 400
    }
    
    @classmethod
    def calculate_spread(
        cls, 
        plan: TradingPlan, 
        investment: float, 
        leverage: int
    ) -> Tuple[Optional[float], Optional[str]]:
        """
        Calculate the spread amount based on trading plan, investment, and leverage.
        
        Args:
            plan: The trading plan (Classic, Silver, Gold, VIP)
            investment: The investment amount in USD
            leverage: The leverage ratio (e.g., 100 for 1:100)
            
        Returns:
            Tuple containing:
                - spread_amount: Calculated spread amount or None if validation fails
                - error_message: Error message if validation fails, None otherwise
        """
        # Validate investment amount
        if investment < cls._MIN_INVESTMENT[plan]:
            return None, f"Investment must be at least ${cls._MIN_INVESTMENT[plan]:,.2f} for {plan.value} plan"
        
        # Validate leverage
        if leverage <= 0:
            return None, "Leverage must be a positive number"
        if leverage > cls._MAX_LEVERAGE[plan]:
            return None, f"Maximum leverage for {plan.value} plan is {cls._MAX_LEVERAGE[plan]}:1"
        
        # Calculate spread amount
        spread_rate = cls._SPREAD_RATES[plan]
        spread_amount = investment * leverage * (spread_rate / 100)
        
        return spread_amount, None

def main():
    """Main function to demonstrate the spread calculator."""
    try:
        # Example usage
        plans = [plan for plan in TradingPlan]
        
        print("Fargo Markets Spread Calculator")
        print("=" * 30)
        
        for plan in plans:
            min_investment = SpreadCalculator._MIN_INVESTMENT[plan]
            max_leverage = SpreadCalculator._MAX_LEVERAGE[plan]
            
            # Use example values: minimum investment and maximum leverage
            investment = min_investment
            leverage = max_leverage
            
            spread, error = SpreadCalculator.calculate_spread(plan, investment, leverage)
            
            if error:
                print(f"Error for {plan.value}: {error}")
            else:
                print(f"{plan.value} Plan:")
                print(f"  Investment: ${investment:,.2f}")
                print(f"  Leverage: {leverage}:1")
                print(f"  Spread Amount: ${spread:,.2f}\n")
                
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
