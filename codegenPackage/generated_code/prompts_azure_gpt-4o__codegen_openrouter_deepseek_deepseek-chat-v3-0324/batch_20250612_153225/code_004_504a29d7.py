"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Write code to calculate the environmental impact of a Kallimos pocket neighborhood, factoring in native gardens, sheltered paths, and indoor/outdoor living spaces.
Generated: DETERMINISTIC_504a29d718701935
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from enum import Enum
from typing import List, Dict, Optional

class ImpactFactor(Enum):
    """Enumeration of environmental impact factors."""
    NATIVE_GARDENS = "native_gardens"
    SHELTERED_PATHS = "sheltered_paths"
    INDOOR_OUTDOOR_LIVING = "indoor_outdoor_living"

class EnvironmentalImpactCalculator:
    """
    A calculator for assessing the environmental impact of a Kallimos pocket neighborhood.
    Factors include native gardens, sheltered paths, and indoor/outdoor living spaces.
    """
    
    # Default impact weights (can be customized)
    DEFAULT_WEIGHTS = {
        ImpactFactor.NATIVE_GARDENS: 0.4,
        ImpactFactor.SHELTERED_PATHS: 0.3,
        ImpactFactor.INDOOR_OUTDOOR_LIVING: 0.3
    }
    
    # Conversion factors (kg CO2 equivalent per unit)
    CONVERSION_FACTORS = {
        ImpactFactor.NATIVE_GARDENS: 50,    # per 100 sqm
        ImpactFactor.SHELTERED_PATHS: 20,   # per 100 linear meters
        ImpactFactor.INDOOR_OUTDOOR_LIVING: 30  # per dwelling
    }
    
    def __init__(self, custom_weights: Optional[Dict[ImpactFactor, float]] = None):
        """
        Initialize the calculator with optional custom weights.
        
        Args:
            custom_weights: Optional dictionary to override default impact weights.
                           Keys are ImpactFactor enums, values are weights (0-1).
        """
        self.weights = custom_weights if custom_weights else self.DEFAULT_WEIGHTS
        self._validate_weights()
    
    def _validate_weights(self):
        """Validate that weights sum to approximately 1."""
        total = sum(self.weights.values())
        if not math.isclose(total, 1.0, abs_tol=0.01):
            raise ValueError(f"Impact weights must sum to 1 (current sum: {total})")
    
    def calculate_impact(
        self,
        native_garden_area: float,
        sheltered_path_length: float,
        dwelling_count: int
    ) -> Dict[str, float]:
        """
        Calculate the total environmental impact of the neighborhood.
        
        Args:
            native_garden_area: Total area of native gardens (square meters)
            sheltered_path_length: Total length of sheltered paths (meters)
            dwelling_count: Number of dwellings with indoor/outdoor living spaces
            
        Returns:
            Dictionary containing:
            - 'total_impact': Total environmental impact (kg CO2 equivalent)
            - 'impact_breakdown': Breakdown by factor
            - 'normalized_breakdown': Percentage contribution of each factor
        """
        try:
            # Calculate individual impacts
            garden_impact = (native_garden_area / 100) * self.CONVERSION_FACTORS[ImpactFactor.NATIVE_GARDENS]
            path_impact = (sheltered_path_length / 100) * self.CONVERSION_FACTORS[ImpactFactor.SHELTERED_PATHS]
            living_impact = dwelling_count * self.CONVERSION_FACTORS[ImpactFactor.INDOOR_OUTDOOR_LIVING]
            
            # Apply weights
            weighted_impacts = {
                ImpactFactor.NATIVE_GARDENS: garden_impact * self.weights[ImpactFactor.NATIVE_GARDENS],
                ImpactFactor.SHELTERED_PATHS: path_impact * self.weights[ImpactFactor.SHELTERED_PATHS],
                ImpactFactor.INDOOR_OUTDOOR_LIVING: living_impact * self.weights[ImpactFactor.INDOOR_OUTDOOR_LIVING]
            }
            
            total_impact = sum(weighted_impacts.values())
            
            # Calculate normalized breakdown
            if total_impact > 0:
                normalized = {k: (v / total_impact) * 100 for k, v in weighted_impacts.items()}
            else:
                normalized = {k: 0 for k in weighted_impacts.keys()}
            
            return {
                'total_impact': total_impact,
                'impact_breakdown': {
                    'native_gardens': garden_impact,
                    'sheltered_paths': path_impact,
                    'indoor_outdoor_living': living_impact
                },
                'normalized_breakdown': {
                    'native_gardens': normalized[ImpactFactor.NATIVE_GARDENS],
                    'sheltered_paths': normalized[ImpactFactor.SHELTERED_PATHS],
                    'indoor_outdoor_living': normalized[ImpactFactor.INDOOR_OUTDOOR_LIVING]
                }
            }
            
        except Exception as e:
            raise ValueError(f"Error calculating environmental impact: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        calculator = EnvironmentalImpactCalculator()
        
        # Sample data for a neighborhood
        result = calculator.calculate_impact(
            native_garden_area=500,    # 500 sqm of native gardens
            sheltered_path_length=300, # 300 meters of sheltered paths
            dwelling_count=20          # 20 dwellings
        )
        
        print(f"Total Environmental Impact: {result['total_impact']:.2f} kg CO2 equivalent")
        print("Impact Breakdown:")
        for factor, impact in result['impact_breakdown'].items():
            print(f"  - {factor.replace('_', ' ').title()}: {impact:.2f} kg")
        print("Normalized Contribution:")
        for factor, percent in result['normalized_breakdown'].items():
            print(f"  - {factor.replace('_', ' ').title()}: {percent:.1f}%")
            
    except ValueError as e:
        print(f"Error: {e}")
```
