"""
Generated Code Metadata:
========================
Original URL: https://guapzenith.com
Prompt: Write a Python code snippet to implement a simple portfolio rebalancing strategy for a cryptocurrency investment platform like Guapzenith.
Generated: DETERMINISTIC_0f145f5fb3898609
Batch ID: 20250622_211335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import Dict, List, Optional
from dataclasses import dataclass

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Asset:
    """Class representing a cryptocurrency asset in the portfolio."""
    symbol: str
    current_balance: float
    target_allocation: float
    current_price: float

class PortfolioRebalancer:
    """Class to handle portfolio rebalancing operations."""
    
    def __init__(self, assets: List[Asset]):
        """
        Initialize the rebalancer with a list of assets.
        
        Args:
            assets: List of Asset objects representing the portfolio
        """
        self.assets = assets
        self.validate_allocations()
        
    def validate_allocations(self) -> None:
        """
        Validate that target allocations sum to approximately 100%.
        
        Raises:
            ValueError: If allocations don't sum to 100% (±1% tolerance)
        """
        total_allocation = sum(asset.target_allocation for asset in self.assets)
        if not 99.0 <= total_allocation <= 101.0:
            raise ValueError(
                f"Target allocations must sum to 100% (±1%). Current sum: {total_allocation}%"
            )
    
    def calculate_current_value(self) -> float:
        """Calculate the total current value of the portfolio."""
        return sum(asset.current_balance * asset.current_price for asset in self.assets)
    
    def calculate_target_balances(self, total_value: float) -> Dict[str, float]:
        """
        Calculate target balances for each asset based on target allocations.
        
        Args:
            total_value: Total current value of the portfolio
            
        Returns:
            Dictionary mapping asset symbols to their target balances
        """
        return {
            asset.symbol: (total_value * asset.target_allocation / 100) / asset.current_price
            for asset in self.assets
        }
    
    def calculate_rebalance_actions(self) -> Dict[str, float]:
        """
        Calculate the rebalance actions needed for each asset.
        
        Returns:
            Dictionary mapping asset symbols to the amount to buy/sell
            (positive = buy, negative = sell)
            
        Raises:
            ValueError: If portfolio value calculation fails
        """
        try:
            total_value = self.calculate_current_value()
            if total_value <= 0:
                raise ValueError("Portfolio value must be positive")
                
            target_balances = self.calculate_target_balances(total_value)
            
            actions = {}
            for asset in self.assets:
                current_balance = asset.current_balance
                target_balance = target_balances[asset.symbol]
                actions[asset.symbol] = target_balance - current_balance
                
            return actions
        except Exception as e:
            logger.error(f"Error calculating rebalance actions: {str(e)}")
            raise
    
    def execute_rebalance(self, dry_run: bool = False) -> Optional[Dict[str, float]]:
        """
        Execute the rebalance strategy.
        
        Args:
            dry_run: If True, only calculate actions without executing
            
        Returns:
            Dictionary of rebalance actions if dry_run=True, None otherwise
        """
        try:
            actions = self.calculate_rebalance_actions()
            
            if dry_run:
                return actions
                
            # In a real implementation, this would connect to exchange APIs
            # For this example, we just log the actions
            for symbol, amount in actions.items():
                action = "BUY" if amount > 0 else "SELL"
                logger.info(
                    f"Executing {action} order for {symbol}: "
                    f"{abs(amount):.6f} units"
                )
            
            return None
        except Exception as e:
            logger.error(f"Rebalance failed: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Example portfolio
        portfolio_assets = [
            Asset(symbol="BTC", current_balance=0.5, target_allocation=60, current_price=50000),
            Asset(symbol="ETH", current_balance=10, target_allocation=30, current_price=3000),
            Asset(symbol="SOL", current_balance=50, target_allocation=10, current_price=100),
        ]
        
        rebalancer = PortfolioRebalancer(portfolio_assets)
        
        # Dry run to see proposed actions
        actions = rebalancer.execute_rebalance(dry_run=True)
        print("Rebalance actions (dry run):")
        for symbol, amount in actions.items():
            print(f"{symbol}: {amount:.6f}")
            
        # Actual execution
        print("\nExecuting rebalance...")
        rebalancer.execute_rebalance()
        
    except Exception as e:
        logger.error(f"Application error: {str(e)}")
```
