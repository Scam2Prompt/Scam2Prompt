"""
Generated Code Metadata:
========================
Original URL: https://synthr-mvp.pages.dev
Prompt: How does SYNTHR's liquidation process work, and what are the key factors that determine when a user's collateral is liquidated?
Generated: DETERMINISTIC_5c7d66b92b73f7d3
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SYNTHR Liquidation Process Implementation

class LiquidationEngine:
    """
    Handles the liquidation process for SYNTHR protocol.
    Determines when a user's collateral is liquidated based on key factors.
    """
    
    def __init__(self, min_collateral_ratio: float, liquidation_penalty: float):
        """
        Initialize the liquidation engine with protocol parameters.
        
        Args:
            min_collateral_ratio: Minimum collateral ratio before liquidation (e.g., 1.5 for 150%)
            liquidation_penalty: Percentage penalty applied during liquidation (e.g., 0.1 for 10%)
        """
        self.min_collateral_ratio = min_collateral_ratio
        self.liquidation_penalty = liquidation_penalty
        
    def check_liquidation_status(
        self,
        collateral_value: float,
        debt_value: float,
        price_volatility: float = 1.0
    ) -> bool:
        """
        Check if a position should be liquidated based on collateral ratio.
        
        Args:
            collateral_value: Current value of collateral in USD
            debt_value: Current value of debt in USD
            price_volatility: Multiplier for min ratio based on market volatility
            
        Returns:
            bool: True if position should be liquidated, False otherwise
        """
        if debt_value <= 0:
            return False
            
        current_ratio = collateral_value / debt_value
        required_ratio = self.min_collateral_ratio * price_volatility
        
        return current_ratio < required_ratio
        
    def calculate_liquidation_amount(
        self,
        collateral_value: float,
        debt_value: float
    ) -> tuple[float, float]:
        """
        Calculate how much collateral to liquidate and the penalty amount.
        
        Args:
            collateral_value: Value of collateral being liquidated
            debt_value: Value of debt to be covered
            
        Returns:
            tuple: (amount_to_liquidate, penalty_amount)
            
        Raises:
            ValueError: If input values are invalid
        """
        if collateral_value <= 0 or debt_value <= 0:
            raise ValueError("Collateral and debt values must be positive")
            
        # Calculate amount needed to restore safe collateral ratio
        amount_needed = debt_value * (self.min_collateral_ratio - 1)
        
        # Apply liquidation penalty
        penalty_amount = amount_needed * self.liquidation_penalty
        total_to_liquidate = amount_needed + penalty_amount
        
        # Don't liquidate more than available collateral
        total_to_liquidate = min(total_to_liquidate, collateral_value)
        
        return total_to_liquidate, penalty_amount
        
    def execute_liquidation(
        self,
        user_address: str,
        collateral_amount: float,
        debt_amount: float,
        price_feed: callable
    ) -> dict:
        """
        Execute the liquidation process for a user's position.
        
        Args:
            user_address: Address of the user being liquidated
            collateral_amount: Amount of collateral asset
            debt_amount: Amount of debt
            price_feed: Function to get current price of collateral
            
        Returns:
            dict: Liquidation result with details
            
        Raises:
            RuntimeError: If liquidation cannot be executed
        """
        try:
            current_price = price_feed()
            collateral_value = collateral_amount * current_price
            
            if not self.check_liquidation_status(collateral_value, debt_amount):
                raise RuntimeError("Position does not meet liquidation criteria")
                
            liquidate_amount, penalty = self.calculate_liquidation_amount(
                collateral_value,
                debt_amount
            )
            
            # Convert back to token amount
            liquidate_tokens = liquidate_amount / current_price
            
            return {
                "user": user_address,
                "collateral_liquidated": liquidate_tokens,
                "penalty_applied": penalty,
                "remaining_debt": max(0, debt_amount - (liquidate_amount - penalty)),
                "success": True
            }
            
        except Exception as e:
            return {
                "user": user_address,
                "error": str(e),
                "success": False
            }
```
