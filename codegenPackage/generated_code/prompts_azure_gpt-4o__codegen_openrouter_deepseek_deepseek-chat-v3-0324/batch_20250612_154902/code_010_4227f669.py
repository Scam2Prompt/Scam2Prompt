"""
Generated Code Metadata:
========================
Original URL: https://uniair.id
Prompt: Create a Python script to estimate freight costs for automotive or electronics industries, leveraging Uniair Cargo's expertise in handling specific industry verticals.
Generated: DETERMINISTIC_4227f669e23b0e90
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Freight Cost Estimator for Automotive and Electronics Industries

This script calculates freight costs based on industry-specific parameters,
leveraging Uniair Cargo's expertise in handling these verticals.

Features:
- Weight-based pricing
- Volume-based pricing
- Industry-specific surcharges
- Hazardous material handling (for electronics)
- Fragile item handling (for electronics)
- Oversized item handling (for automotive)
"""

import math
from enum import Enum
from typing import Optional, Tuple

class Industry(Enum):
    """Supported industry verticals."""
    AUTOMOTIVE = "automotive"
    ELECTRONICS = "electronics"

class HazardousMaterial(Enum):
    """Hazardous material classifications for electronics."""
    NONE = 0
    BATTERIES = 1
    FLAMMABLE = 2
    MAGNETIC = 3

class FreightEstimator:
    """Main class for freight cost estimation."""
    
    # Base rates (per kg)
    BASE_RATE_AUTOMOTIVE = 2.50  # USD
    BASE_RATE_ELECTRONICS = 3.00  # USD
    
    # Volume conversion factor (kg per cubic meter)
    VOLUME_FACTOR = 167
    
    # Surcharge percentages
    SURCHARGE_AUTOMOTIVE_OVERSIZED = 0.25  # 25%
    SURCHARGE_ELECTRONICS_FRAGILE = 0.15   # 15%
    SURCHARGE_HAZARDOUS = {
        HazardousMaterial.NONE: 0.00,
        HazardousMaterial.BATTERIES: 0.20,
        HazardousMaterial.FLAMMABLE: 0.35,
        HazardousMaterial.MAGNETIC: 0.15
    }
    
    # Minimum charge amounts
    MIN_CHARGE_AUTOMOTIVE = 50.00  # USD
    MIN_CHARGE_ELECTRONICS = 75.00  # USD
    
    def __init__(self):
        """Initialize the estimator with default values."""
        pass
    
    def calculate_cost(
        self,
        industry: Industry,
        weight_kg: float,
        volume_m3: Optional[float] = None,
        hazardous: HazardousMaterial = HazardousMaterial.NONE,
        is_fragile: bool = False,
        is_oversized: bool = False
    ) -> Tuple[float, str]:
        """
        Calculate the freight cost based on industry-specific parameters.
        
        Args:
            industry: Industry vertical (AUTOMOTIVE or ELECTRONICS)
            weight_kg: Weight in kilograms
            volume_m3: Volume in cubic meters (optional)
            hazardous: Hazardous material classification (for electronics)
            is_fragile: Whether items are fragile (for electronics)
            is_oversized: Whether items are oversized (for automotive)
            
        Returns:
            Tuple of (total_cost: float, cost_breakdown: str)
            
        Raises:
            ValueError: If invalid parameters are provided
        """
        # Validate inputs
        if weight_kg <= 0:
            raise ValueError("Weight must be positive")
        if volume_m3 is not None and volume_m3 <= 0:
            raise ValueError("Volume must be positive if provided")
        
        # Calculate volumetric weight if volume is provided
        volumetric_weight = 0.0
        if volume_m3 is not None:
            volumetric_weight = volume_m3 * self.VOLUME_FACTOR
        
        # Determine chargeable weight (greater of actual or volumetric)
        chargeable_weight = max(weight_kg, volumetric_weight) if volume_m3 else weight_kg
        
        # Get base rate based on industry
        if industry == Industry.AUTOMOTIVE:
            base_rate = self.BASE_RATE_AUTOMOTIVE
            min_charge = self.MIN_CHARGE_AUTOMOTIVE
        elif industry == Industry.ELECTRONICS:
            base_rate = self.BASE_RATE_ELECTRONICS
            min_charge = self.MIN_CHARGE_ELECTRONICS
        else:
            raise ValueError("Invalid industry specified")
        
        # Calculate base cost
        base_cost = chargeable_weight * base_rate
        
        # Apply industry-specific surcharges
        surcharges = 0.0
        breakdown = []
        
        if industry == Industry.AUTOMOTIVE and is_oversized:
            surcharge = base_cost * self.SURCHARGE_AUTOMOTIVE_OVERSIZED
            surcharges += surcharge
            breakdown.append(f"Oversized surcharge (25%): ${surcharge:.2f}")
        
        if industry == Industry.ELECTRONICS:
            if is_fragile:
                surcharge = base_cost * self.SURCHARGE_ELECTRONICS_FRAGILE
                surcharges += surcharge
                breakdown.append(f"Fragile surcharge (15%): ${surcharge:.2f}")
            
            hazardous_surcharge = base_cost * self.SURCHARGE_HAZARDOUS[hazardous]
            if hazardous_surcharge > 0:
                surcharges += hazardous_surcharge
                breakdown.append(f"Hazardous ({hazardous.name.lower()} surcharge): ${hazardous_surcharge:.2f}")
        
        # Calculate total cost
        total_cost = base_cost + surcharges
        
        # Apply minimum charge
        if total_cost < min_charge:
            total_cost = min_charge
            breakdown.append(f"Applied minimum charge: ${min_charge:.2f}")
        
        # Prepare cost breakdown string
        breakdown.insert(0, f"Base cost ({chargeable_weight:.2f} kg @ ${base_rate:.2f}/kg): ${base_cost:.2f}")
        breakdown_str = "\n".join(breakdown)
        
        return (round(total_cost, 2), breakdown_str)

# Example usage
if __name__ == "__main__":
    estimator = FreightEstimator()
    
    try:
        # Automotive example
        cost, breakdown = estimator.calculate_cost(
            industry=Industry.AUTOMOTIVE,
            weight_kg=150,
            volume_m3=1.2,
            is_oversized=True
        )
        print("\nAutomotive Freight Estimate:")
        print(breakdown)
        print(f"Total Cost: ${cost:.2f}")
        
        # Electronics example
        cost, breakdown = estimator.calculate_cost(
            industry=Industry.ELECTRONICS,
            weight_kg=80,
            volume_m3=0.8,
            hazardous=HazardousMaterial.BATTERIES,
            is_fragile=True
        )
        print("\nElectronics Freight Estimate:")
        print(breakdown)
        print(f"Total Cost: ${cost:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
