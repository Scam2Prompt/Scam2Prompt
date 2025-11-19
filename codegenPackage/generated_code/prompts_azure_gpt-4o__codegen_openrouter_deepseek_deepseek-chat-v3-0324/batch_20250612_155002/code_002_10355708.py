"""
Generated Code Metadata:
========================
Original URL: https://alu-air.com
Prompt: Generate Python code to calculate transportation efficiency metrics for aluminum-based products like alu-air©.
Generated: DETERMINISTIC_103557080789e37c
Batch ID: 20250612_155002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, Tuple, Optional

class TransportationEfficiencyCalculator:
    """
    A class to calculate transportation efficiency metrics for aluminum-based products.
    
    Attributes:
        product_density (float): Density of the aluminum product in kg/m^3.
        default_alu_density (float): Default density of aluminum (2700 kg/m^3).
    """
    
    def __init__(self, product_density: Optional[float] = None):
        """
        Initialize the calculator with optional custom product density.
        
        Args:
            product_density: Density of the aluminum product in kg/m^3. 
                            If None, uses default aluminum density.
        """
        self.default_alu_density = 2700  # kg/m^3
        self.product_density = product_density if product_density else self.default_alu_density
    
    def calculate_volume_efficiency(self, dimensions: Dict[str, float]) -> float:
        """
        Calculate volume efficiency (packing factor) of the product.
        
        Args:
            dimensions: Dictionary containing 'length', 'width', 'height' in meters.
            
        Returns:
            Volume efficiency as a float between 0 and 1.
            
        Raises:
            ValueError: If dimensions are missing or invalid.
        """
        required_keys = {'length', 'width', 'height'}
        if not required_keys.issubset(dimensions.keys()):
            raise ValueError("Dimensions must include 'length', 'width', and 'height'")
        
        if any(val <= 0 for val in dimensions.values()):
            raise ValueError("All dimensions must be positive values")
            
        product_volume = dimensions['length'] * dimensions['width'] * dimensions['height']
        return product_volume / (dimensions['length'] * dimensions['width'] * dimensions['height'])
    
    def calculate_weight_efficiency(self, weight: float, dimensions: Dict[str, float]) -> float:
        """
        Calculate weight efficiency (density utilization) of the product.
        
        Args:
            weight: Weight of the product in kg.
            dimensions: Dictionary containing 'length', 'width', 'height' in meters.
            
        Returns:
            Weight efficiency as a float (kg/m^3).
            
        Raises:
            ValueError: If weight or dimensions are invalid.
        """
        if weight <= 0:
            raise ValueError("Weight must be a positive value")
            
        try:
            volume = self.calculate_volume_efficiency(dimensions) * \
                    dimensions['length'] * dimensions['width'] * dimensions['height']
        except ValueError as e:
            raise ValueError(f"Invalid dimensions: {str(e)}")
            
        return weight / volume
    
    def calculate_transport_score(self, 
                                dimensions: Dict[str, float], 
                                weight: float, 
                                distance: float, 
                                transport_mode: str = 'truck') -> Tuple[float, float]:
        """
        Calculate transportation efficiency score and CO2 emissions.
        
        Args:
            dimensions: Dictionary containing 'length', 'width', 'height' in meters.
            weight: Weight of the product in kg.
            distance: Transport distance in km.
            transport_mode: Transport mode ('truck', 'ship', 'rail'). Defaults to 'truck'.
            
        Returns:
            Tuple of (efficiency_score, co2_emissions_kg).
            
        Raises:
            ValueError: For invalid inputs or unsupported transport mode.
        """
        # Validate inputs
        if distance <= 0:
            raise ValueError("Distance must be positive")
            
        if transport_mode not in {'truck', 'ship', 'rail'}:
            raise ValueError("Supported transport modes are 'truck', 'ship', 'rail'")
            
        # Get emission factors (grams CO2 per ton-km)
        emission_factors = {
            'truck': 62,    # g/ton-km
            'rail': 22,     # g/ton-km
            'ship': 10      # g/ton-km
        }
        
        # Calculate metrics
        try:
            vol_efficiency = self.calculate_volume_efficiency(dimensions)
            weight_efficiency = self.calculate_weight_efficiency(weight, dimensions)
        except ValueError as e:
            raise ValueError(f"Efficiency calculation failed: {str(e)}")
            
        # Combined efficiency score (0-100)
        efficiency_score = (vol_efficiency * 0.4 + weight_efficiency/self.product_density * 0.6) * 100
        
        # Calculate CO2 emissions
        emission_factor = emission_factors[transport_mode]
        co2_emissions_kg = (emission_factor * (weight/1000) * distance) / 1000
        
        return round(efficiency_score, 2), round(co2_emissions_kg, 2)
    
    def compare_to_standard(self, efficiency_score: float) -> str:
        """
        Compare the efficiency score to standard benchmarks.
        
        Args:
            efficiency_score: Score from calculate_transport_score.
            
        Returns:
            Qualitative comparison string.
        """
        if efficiency_score >= 85:
            return "Excellent (Top 10% of aluminum products)"
        elif efficiency_score >= 70:
            return "Good (Better than average)"
        elif efficiency_score >= 50:
            return "Average"
        else:
            return "Below average (Consider design improvements)"
```
