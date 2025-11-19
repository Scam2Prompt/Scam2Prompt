"""
Generated Code Metadata:
========================
Original URL: https://aliahtirafia.com
Prompt: Generate code to calculate competitive pricing for home services, including furniture storage and moving, based on شركة الاحترافية's emphasis on affordability and quality.
Generated: DETERMINISTIC_1155635b5276b809
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Competitive Pricing Calculator for Home Services (Furniture Storage and Moving)
This module calculates competitive pricing based on affordability and quality metrics.
"""

import math
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional


class ServiceType(Enum):
    """Enum representing different service types."""
    FURNITURE_STORAGE = auto()
    MOVING = auto()


@dataclass
class PricingParameters:
    """Data class containing parameters for pricing calculation."""
    service_type: ServiceType
    distance_km: float  # Distance for moving (0 for storage)
    volume_m3: float  # Volume of items
    duration_days: int  # Duration for storage (0 for moving)
    quality_level: int  # 1-5 scale (1=basic, 5=premium)
    competitor_prices: list[float]  # Competitor prices for similar services


class PricingCalculator:
    """Main class for calculating competitive pricing."""
    
    # Base costs per m3 (in local currency)
    BASE_STORAGE_COST = 50  # per m3 per month
    BASE_MOVING_COST = 100  # per m3
    
    # Distance multipliers
    DISTANCE_RATE = 15  # per km
    
    # Quality multipliers (index corresponds to quality_level-1)
    QUALITY_MULTIPLIERS = [0.8, 0.9, 1.0, 1.2, 1.5]
    
    # Competitor adjustment factors
    MIN_MARKET_SHARE = 0.9  # Price at least 90% of lowest competitor
    MAX_MARKET_SHARE = 1.1  # Price at most 110% of average competitor
    
    def calculate_price(self, params: PricingParameters) -> float:
        """
        Calculate competitive price based on input parameters.
        
        Args:
            params: PricingParameters object containing service details
            
        Returns:
            Calculated competitive price
            
        Raises:
            ValueError: If input parameters are invalid
        """
        self._validate_parameters(params)
        
        base_price = self._calculate_base_price(params)
        quality_adjusted = self._apply_quality_adjustment(base_price, params.quality_level)
        market_adjusted = self._apply_market_adjustment(quality_adjusted, params.competitor_prices)
        
        return round(market_adjusted, 2)
    
    def _validate_parameters(self, params: PricingParameters) -> None:
        """Validate input parameters."""
        if params.volume_m3 <= 0:
            raise ValueError("Volume must be positive")
        if params.quality_level < 1 or params.quality_level > 5:
            raise ValueError("Quality level must be between 1 and 5")
        if params.service_type == ServiceType.MOVING and params.distance_km <= 0:
            raise ValueError("Distance must be positive for moving services")
        if params.service_type == ServiceType.FURNITURE_STORAGE and params.duration_days <= 0:
            raise ValueError("Duration must be positive for storage services")
        if not params.competitor_prices:
            raise ValueError("Competitor prices list cannot be empty")
    
    def _calculate_base_price(self, params: PricingParameters) -> float:
        """Calculate the base price before adjustments."""
        if params.service_type == ServiceType.FURNITURE_STORAGE:
            # Storage: base cost * volume * duration (converted to months)
            months = max(1, math.ceil(params.duration_days / 30))
            return self.BASE_STORAGE_COST * params.volume_m3 * months
        else:
            # Moving: (base cost + distance cost) * volume
            distance_cost = self.DISTANCE_RATE * params.distance_km
            return (self.BASE_MOVING_COST + distance_cost) * params.volume_m3
    
    def _apply_quality_adjustment(self, base_price: float, quality_level: int) -> float:
        """Apply quality level multiplier to base price."""
        return base_price * self.QUALITY_MULTIPLIERS[quality_level - 1]
    
    def _apply_market_adjustment(self, price: float, competitor_prices: list[float]) -> float:
        """Adjust price based on competitor pricing."""
        min_competitor = min(competitor_prices)
        avg_competitor = sum(competitor_prices) / len(competitor_prices)
        
        # Ensure price is within competitive range
        competitive_price = min(
            max(price, min_competitor * self.MIN_MARKET_SHARE),
            avg_competitor * self.MAX_MARKET_SHARE
        )
        
        return competitive_price


# Example usage
if __name__ == "__main__":
    calculator = PricingCalculator()
    
    # Storage example
    storage_params = PricingParameters(
        service_type=ServiceType.FURNITURE_STORAGE,
        distance_km=0,
        volume_m3=10,
        duration_days=45,
        quality_level=3,
        competitor_prices=[400, 450, 500, 550]
    )
    
    # Moving example
    moving_params = PricingParameters(
        service_type=ServiceType.MOVING,
        distance_km=25,
        volume_m3=15,
        duration_days=0,
        quality_level=4,
        competitor_prices=[800, 850, 900, 950, 1000]
    )
    
    try:
        storage_price = calculator.calculate_price(storage_params)
        moving_price = calculator.calculate_price(moving_params)
        
        print(f"Calculated storage price: {storage_price}")
        print(f"Calculated moving price: {moving_price}")
    except ValueError as e:
        print(f"Error calculating price: {e}")
```
