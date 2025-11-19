"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: Write a Python function to calculate the cost-effectiveness of Engel coolers over time, considering durability, ice retention, and purchase price.
Generated: DETERMINISTIC_e6089fb5e1870aef
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, Optional, Tuple

class EngelCoolerCostEffectiveness:
    """
    A class to calculate the cost-effectiveness of Engel coolers over time.
    Takes into account durability, ice retention, and purchase price.
    """
    
    def __init__(
        self,
        purchase_price: float,
        durability_years: float,
        daily_ice_retention_hours: float,
        daily_usage_hours: float,
        ice_cost_per_day: float,
        discount_rate: float = 0.05
    ):
        """
        Initialize the Engel cooler cost-effectiveness calculator.
        
        Args:
            purchase_price: Initial purchase price of the cooler in USD
            durability_years: Expected lifespan of the cooler in years
            daily_ice_retention_hours: Hours the cooler retains ice per day
            daily_usage_hours: Hours the cooler is used per day
            ice_cost_per_day: Cost of ice per day in USD
            discount_rate: Annual discount rate for present value calculations (default: 0.05)
        """
        self.purchase_price = purchase_price
        self.durability_years = durability_years
        self.daily_ice_retention_hours = daily_ice_retention_hours
        self.daily_usage_hours = daily_usage_hours
        self.ice_cost_per_day = ice_cost_per_day
        self.discount_rate = discount_rate
        
        # Validate inputs
        self._validate_inputs()
    
    def _validate_inputs(self) -> None:
        """Validate that all inputs are positive numbers where applicable."""
        if self.purchase_price <= 0:
            raise ValueError("Purchase price must be positive")
        if self.durability_years <= 0:
            raise ValueError("Durability years must be positive")
        if self.daily_ice_retention_hours <= 0:
            raise ValueError("Daily ice retention hours must be positive")
        if self.daily_usage_hours <= 0:
            raise ValueError("Daily usage hours must be positive")
        if self.ice_cost_per_day < 0:
            raise ValueError("Ice cost per day cannot be negative")
        if not 0 <= self.discount_rate <= 1:
            raise ValueError("Discount rate must be between 0 and 1")
    
    def calculate_ice_replacement_cost(self) -> float:
        """
        Calculate the daily ice replacement cost based on retention vs usage.
        
        Returns:
            Daily cost of additional ice needed due to imperfect retention
        """
        if self.daily_ice_retention_hours >= self.daily_usage_hours:
            return 0.0
        
        # Calculate fraction of day needing ice replacement
        replacement_fraction = (self.daily_usage_hours - self.daily_ice_retention_hours) / self.daily_usage_hours
        return self.ice_cost_per_day * replacement_fraction
    
    def calculate_total_cost(self) -> float:
        """
        Calculate the total cost of ownership over the cooler's lifespan.
        
        Returns:
            Total cost including purchase price and ice replacement costs
        """
        daily_ice_cost = self.calculate_ice_replacement_cost()
        annual_ice_cost = daily_ice_cost * 365
        total_ice_cost = 0.0
        
        # Calculate present value of ice costs over durability years
        for year in range(1, int(self.durability_years) + 1):
            discounted_ice_cost = annual_ice_cost / ((1 + self.discount_rate) ** year)
            total_ice_cost += discounted_ice_cost
        
        return self.purchase_price + total_ice_cost
    
    def calculate_cost_per_year(self) -> float:
        """
        Calculate the equivalent annual cost of the cooler.
        
        Returns:
            Annualized cost considering purchase price and ice replacement
        """
        total_cost = self.calculate_total_cost()
        
        # Calculate annuity factor for durability years
        if self.discount_rate == 0:
            annuity_factor = self.durability_years
        else:
            annuity_factor = (1 - (1 + self.discount_rate) ** -self.durability_years) / self.discount_rate
        
        return total_cost / annuity_factor
    
    def compare_with_alternative(
        self,
        alt_purchase_price: float,
        alt_durability_years: float,
        alt_daily_ice_retention_hours: float
    ) -> Dict[str, float]:
        """
        Compare cost-effectiveness with an alternative cooler.
        
        Args:
            alt_purchase_price: Alternative cooler's purchase price
            alt_durability_years: Alternative cooler's durability
            alt_daily_ice_retention_hours: Alternative cooler's ice retention
            
        Returns:
            Dictionary with comparison metrics
        """
        # Calculate metrics for this cooler
        this_cost = self.calculate_total_cost()
        this_annual = self.calculate_cost_per_year()
        
        # Calculate metrics for alternative
        alt_cooler = EngelCoolerCostEffectiveness(
            purchase_price=alt_purchase_price,
            durability_years=alt_durability_years,
            daily_ice_retention_hours=alt_daily_ice_retention_hours,
            daily_usage_hours=self.daily_usage_hours,
            ice_cost_per_day=self.ice_cost_per_day,
            discount_rate=self.discount_rate
        )
        alt_cost = alt_cooler.calculate_total_cost()
        alt_annual = alt_cooler.calculate_cost_per_year()
        
        return {
            "engel_total_cost": this_cost,
            "engel_annual_cost": this_annual,
            "alternative_total_cost": alt_cost,
            "alternative_annual_cost": alt_annual,
            "total_cost_difference": this_cost - alt_cost,
            "annual_cost_difference": this_annual - alt_annual
        }


def calculate_engel_cost_effectiveness(
    purchase_price: float,
    durability_years: float,
    daily_ice_retention_hours: float,
    daily_usage_hours: float,
    ice_cost_per_day: float,
    discount_rate: float = 0.05,
    alt_purchase_price: Optional[float] = None,
    alt_durability_years: Optional[float] = None,
    alt_daily_ice_retention_hours: Optional[float] = None
) -> Dict[str, float]:
    """
    Calculate and compare cost-effectiveness of an Engel cooler.
    
    Args:
        purchase_price: Initial purchase price of the Engel cooler
        durability_years: Expected lifespan of the Engel cooler
        daily_ice_retention_hours: Hours the Engel cooler retains ice per day
        daily_usage_hours: Hours the cooler is used per day
        ice_cost_per_day: Cost of ice per day
        discount_rate: Annual discount rate (default: 0.05)
        alt_purchase_price: Optional alternative cooler purchase price
        alt_durability_years: Optional alternative cooler durability
        alt_daily_ice_retention_hours: Optional alternative cooler ice retention
        
    Returns:
        Dictionary with cost-effectiveness metrics
    """
    engel_cooler = EngelCoolerCostEffectiveness(
        purchase_price=purchase_price,
        durability_years=durability_years,
        daily_ice_retention_hours=daily_ice_retention_hours,
        daily_usage_hours=daily_usage_hours,
        ice_cost_per_day=ice_cost_per_day,
        discount_rate=discount_rate
    )
    
    results = {
        "total_cost": engel_cooler.calculate_total_cost(),
        "annual_cost": engel_cooler.calculate_cost_per_year(),
        "daily_ice_cost": engel_cooler.calculate_ice_replacement_cost()
    }
    
    # Add comparison if alternative parameters are provided
    if all([alt_purchase_price, alt_durability_years, alt_daily_ice_retention_hours]):
        comparison = engel_cooler.compare_with_alternative(
            alt_purchase_price=alt_purchase_price,
            alt_durability_years=alt_durability_years,
            alt_daily_ice_retention_hours=alt_daily_ice_retention_hours
        )
        results.update(comparison)
    
    return results
```
