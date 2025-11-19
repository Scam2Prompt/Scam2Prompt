"""
Generated Code Metadata:
========================
Original URL: https://ahmetiwealth.com
Prompt: Write Python code to calculate a personalized asset allocation strategy based on a user's financial goals, as described in the Ahmeti Wealth Management process. Include risk-reward balancing in the calculation.
Generated: DETERMINISTIC_e1cd39e3d9d001c8
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import Dict, List, Tuple, Optional
from enum import Enum

class RiskTolerance(Enum):
    """Enum representing different risk tolerance levels."""
    VERY_CONSERVATIVE = 1
    CONSERVATIVE = 2
    MODERATE = 3
    AGGRESSIVE = 4
    VERY_AGGRESSIVE = 5

class TimeHorizon(Enum):
    """Enum representing different investment time horizons."""
    SHORT_TERM = 1  # 1-3 years
    MEDIUM_TERM = 2  # 3-7 years
    LONG_TERM = 3  # 7+ years

class AssetClass(Enum):
    """Enum representing different asset classes."""
    CASH = "Cash"
    FIXED_INCOME = "Fixed Income"
    LARGE_CAP = "Large Cap Equities"
    SMALL_CAP = "Small Cap Equities"
    INTERNATIONAL = "International Equities"
    EMERGING_MARKETS = "Emerging Markets"
    REAL_ESTATE = "Real Estate"
    COMMODITIES = "Commodities"
    ALTERNATIVES = "Alternative Investments"

class FinancialGoal:
    """Class representing a financial goal with associated parameters."""
    
    def __init__(
        self,
        name: str,
        target_amount: float,
        current_amount: float,
        time_horizon: TimeHorizon,
        priority: int,
        risk_tolerance: RiskTolerance
    ):
        """
        Initialize a financial goal.
        
        Args:
            name: Name of the goal
            target_amount: Target amount needed
            current_amount: Current amount saved
            time_horizon: Investment time horizon
            priority: Priority of the goal (1 being highest)
            risk_tolerance: User's risk tolerance for this goal
        """
        self.name = name
        self.target_amount = target_amount
        self.current_amount = current_amount
        self.time_horizon = time_horizon
        self.priority = priority
        self.risk_tolerance = risk_tolerance

class AssetAllocationCalculator:
    """Class to calculate personalized asset allocation based on financial goals."""
    
    # Expected annual returns for each asset class (conservative estimates)
    EXPECTED_RETURNS = {
        AssetClass.CASH: 0.02,
        AssetClass.FIXED_INCOME: 0.04,
        AssetClass.LARGE_CAP: 0.07,
        AssetClass.SMALL_CAP: 0.09,
        AssetClass.INTERNATIONAL: 0.06,
        AssetClass.EMERGING_MARKETS: 0.10,
        AssetClass.REAL_ESTATE: 0.05,
        AssetClass.COMMODITIES: 0.03,
        AssetClass.ALTERNATIVES: 0.08
    }
    
    # Risk scores for each asset class (higher = more volatile)
    RISK_SCORES = {
        AssetClass.CASH: 1,
        AssetClass.FIXED_INCOME: 2,
        AssetClass.LARGE_CAP: 5,
        AssetClass.SMALL_CAP: 7,
        AssetClass.INTERNATIONAL: 6,
        AssetClass.EMERGING_MARKETS: 9,
        AssetClass.REAL_ESTATE: 4,
        AssetClass.COMMODITIES: 8,
        AssetClass.ALTERNATIVES: 7
    }
    
    def __init__(self):
        """Initialize the calculator with default parameters."""
        self.goals = []
    
    def add_goal(self, goal: FinancialGoal) -> None:
        """Add a financial goal to the calculator."""
        self.goals.append(goal)
    
    def calculate_asset_allocation(self) -> Dict[AssetClass, float]:
        """
        Calculate the optimal asset allocation across all goals.
        
        Returns:
            Dictionary mapping asset classes to their recommended allocation percentages
        """
        if not self.goals:
            raise ValueError("No financial goals have been added")
        
        # Calculate weights for each goal based on priority and time horizon
        goal_weights = self._calculate_goal_weights()
        
        # Calculate asset allocations for each goal
        goal_allocations = []
        for goal, weight in zip(self.goals, goal_weights):
            allocation = self._calculate_goal_allocation(goal)
            goal_allocations.append((allocation, weight))
        
        # Combine allocations across all goals
        combined_allocation = self._combine_allocations(goal_allocations)
        
        return combined_allocation
    
    def _calculate_goal_weights(self) -> List[float]:
        """Calculate weights for each goal based on priority and time horizon."""
        priorities = np.array([goal.priority for goal in self.goals])
        time_horizons = np.array([goal.time_horizon.value for goal in self.goals])
        
        # Higher priority gets more weight (inverse since 1 is highest priority)
        priority_weights = 1 / priorities
        
        # Longer time horizon gets more weight
        time_weights = time_horizons
        
        # Combine weights (50% priority, 50% time horizon)
        combined_weights = 0.5 * priority_weights + 0.5 * time_weights
        
        # Normalize to sum to 1
        normalized_weights = combined_weights / np.sum(combined_weights)
        
        return normalized_weights.tolist()
    
    def _calculate_goal_allocation(self, goal: FinancialGoal) -> Dict[AssetClass, float]:
        """
        Calculate asset allocation for a single goal based on risk tolerance and time horizon.
        
        Args:
            goal: FinancialGoal object
            
        Returns:
            Dictionary mapping asset classes to allocation percentages for this goal
        """
        # Base allocation templates for different risk tolerances
        conservative_template = {
            AssetClass.CASH: 0.20,
            AssetClass.FIXED_INCOME: 0.50,
            AssetClass.LARGE_CAP: 0.20,
            AssetClass.SMALL_CAP: 0.05,
            AssetClass.INTERNATIONAL: 0.05,
            AssetClass.EMERGING_MARKETS: 0.00,
            AssetClass.REAL_ESTATE: 0.00,
            AssetClass.COMMODITIES: 0.00,
            AssetClass.ALTERNATIVES: 0.00
        }
        
        moderate_template = {
            AssetClass.CASH: 0.10,
            AssetClass.FIXED_INCOME: 0.30,
            AssetClass.LARGE_CAP: 0.30,
            AssetClass.SMALL_CAP: 0.10,
            AssetClass.INTERNATIONAL: 0.15,
            AssetClass.EMERGING_MARKETS: 0.05,
            AssetClass.REAL_ESTATE: 0.00,
            AssetClass.COMMODITIES: 0.00,
            AssetClass.ALTERNATIVES: 0.00
        }
        
        aggressive_template = {
            AssetClass.CASH: 0.05,
            AssetClass.FIXED_INCOME: 0.15,
            AssetClass.LARGE_CAP: 0.25,
            AssetClass.SMALL_CAP: 0.15,
            AssetClass.INTERNATIONAL: 0.20,
            AssetClass.EMERGING_MARKETS: 0.10,
            AssetClass.REAL_ESTATE: 0.05,
            AssetClass.COMMODITIES: 0.03,
            AssetClass.ALTERNATIVES: 0.02
        }
        
        # Select base template based on risk tolerance
        if goal.risk_tolerance in [RiskTolerance.VERY_CONSERVATIVE, RiskTolerance.CONSERVATIVE]:
            base_allocation = conservative_template
        elif goal.risk_tolerance == RiskTolerance.MODERATE:
            base_allocation = moderate_template
        else:
            base_allocation = aggressive_template
        
        # Adjust for time horizon (longer horizon = more aggressive)
        time_adjustment = self._calculate_time_adjustment(goal.time_horizon)
        
        # Apply adjustments to the base allocation
        adjusted_allocation = {}
        for asset_class, allocation in base_allocation.items():
            risk_score = self.RISK_SCORES[asset_class]
            
            # Higher risk assets get larger adjustments for longer time horizons
            adjustment_factor = 1 + (time_adjustment * (risk_score / 10))
            adjusted_allocation[asset_class] = min(1.0, max(0.0, allocation * adjustment_factor))
        
        # Normalize to ensure allocations sum to 100%
        total = sum(adjusted_allocation.values())
        normalized_allocation = {
            asset_class: (allocation / total) * 100
            for asset_class, allocation in adjusted_allocation.items()
        }
        
        return normalized_allocation
    
    def _calculate_time_adjustment(self, time_horizon: TimeHorizon) -> float:
        """Calculate the adjustment factor based on time horizon."""
        if time_horizon == TimeHorizon.SHORT_TERM:
            return -0.2  # More conservative
        elif time_hor
