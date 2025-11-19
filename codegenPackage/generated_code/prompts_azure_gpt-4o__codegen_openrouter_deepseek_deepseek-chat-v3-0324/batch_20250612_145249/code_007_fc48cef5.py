"""
Generated Code Metadata:
========================
Original URL: https://www.premierpointing.com.au
Prompt: Write a function to calculate the effectiveness of water repellant treatments, factoring in chemical reactions with brick surfaces, as described in Premier Pointing's use of Westox Water Repellant.
Generated: DETERMINISTIC_fc48cef599b18a1c
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import Dict, Tuple, Optional

class WaterRepellentEffectivenessCalculator:
    """
    A class to calculate the effectiveness of water repellent treatments on brick surfaces.
    Factors in chemical reactions, surface properties, and environmental conditions.
    """
    
    def __init__(self, 
                 chemical_properties: Dict[str, float],
                 brick_properties: Dict[str, float],
                 environmental_factors: Dict[str, float]):
        """
        Initialize the calculator with chemical, brick, and environmental properties.
        
        Args:
            chemical_properties: Dictionary containing chemical properties like concentration, pH, etc.
            brick_properties: Dictionary containing brick properties like porosity, surface_area, etc.
            environmental_factors: Dictionary containing environmental factors like temperature, humidity.
        """
        self.chemical_properties = chemical_properties
        self.brick_properties = brick_properties
        self.environmental_factors = environmental_factors
        
        # Validate input parameters
        self._validate_inputs()
        
    def _validate_inputs(self) -> None:
        """Validate that all required parameters are present and within reasonable ranges."""
        required_chemical = {'concentration', 'ph', 'viscosity'}
        required_brick = {'porosity', 'surface_area', 'absorption_rate'}
        required_env = {'temperature', 'humidity', 'exposure_time'}
        
        if not required_chemical.issubset(self.chemical_properties.keys()):
            raise ValueError(f"Chemical properties must include {required_chemical}")
        if not required_brick.issubset(self.brick_properties.keys()):
            raise ValueError(f"Brick properties must include {required_brick}")
        if not required_env.issubset(self.environmental_factors.keys()):
            raise ValueError(f"Environmental factors must include {required_env}")
            
        if not (0 <= self.chemical_properties['concentration'] <= 1):
            raise ValueError("Concentration must be between 0 and 1")
        if not (0 <= self.chemical_properties['ph'] <= 14):
            raise ValueError("pH must be between 0 and 14")
        if not (0 <= self.brick_properties['porosity'] <= 1):
            raise ValueError("Porosity must be between 0 and 1")
        
    def calculate_effectiveness(self) -> Tuple[float, Optional[Dict[str, float]]]:
        """
        Calculate the effectiveness of the water repellent treatment.
        
        Returns:
            Tuple containing:
                - effectiveness_score (0-1 scale)
                - Optional dictionary of intermediate calculations (for debugging/analysis)
        """
        try:
            # Calculate chemical reaction factor
            reaction_factor = self._calculate_reaction_factor()
            
            # Calculate surface interaction factor
            surface_factor = self._calculate_surface_factor()
            
            # Calculate environmental impact factor
            env_factor = self._calculate_environmental_factor()
            
            # Combine factors with weighted importance
            effectiveness = (
                0.5 * reaction_factor + 
                0.3 * surface_factor + 
                0.2 * env_factor
            )
            
            # Ensure the result is within bounds
            effectiveness = np.clip(effectiveness, 0, 1)
            
            # Optional debug info
            debug_info = {
                'reaction_factor': reaction_factor,
                'surface_factor': surface_factor,
                'env_factor': env_factor,
                'raw_effectiveness': effectiveness
            }
            
            return effectiveness, debug_info
            
        except Exception as e:
            raise ValueError(f"Error calculating effectiveness: {str(e)}")
    
    def _calculate_reaction_factor(self) -> float:
        """Calculate the chemical reaction component of effectiveness."""
        conc = self.chemical_properties['concentration']
        ph = self.chemical_properties['ph']
        viscosity = self.chemical_properties['viscosity']
        
        # Normalized pH factor (optimal around pH 7-9 for silane/siloxane)
        ph_factor = 1 - abs(ph - 8) / 8
        
        # Viscosity impact (lower viscosity penetrates better)
        visc_factor = 1 / (1 + np.log(1 + viscosity))
        
        return conc * ph_factor * visc_factor
    
    def _calculate_surface_factor(self) -> float:
        """Calculate the surface interaction component of effectiveness."""
        porosity = self.brick_properties['porosity']
        surface_area = self.brick_properties['surface_area']
        absorption = self.brick_properties['absorption_rate']
        
        # Porosity helps with penetration but too much reduces effectiveness
        porosity_factor = 0.5 + (0.5 * (1 - abs(porosity - 0.5)))
        
        # Larger surface area means more treatment needed
        area_factor = 1 / (1 + np.log(1 + surface_area / 1000))
        
        # Absorption rate affects how well treatment penetrates
        absorption_factor = np.tanh(absorption * 10)  # Cap absorption impact
        
        return porosity_factor * area_factor * absorption_factor
    
    def _calculate_environmental_factor(self) -> float:
        """Calculate the environmental impact component of effectiveness."""
        temp = self.environmental_factors['temperature']
        humidity = self.environmental_factors['humidity']
        exposure = self.environmental_factors['exposure_time']
        
        # Temperature effect (optimal around 20°C)
        temp_factor = np.exp(-0.5 * ((temp - 20) / 15) ** 2)
        
        # Humidity effect (lower is better during application)
        humidity_factor = 1 - (humidity / 100) * 0.5
        
        # Exposure time (longer is better up to a point)
        exposure_factor = np.tanh(exposure / 24)  # Cap at ~24 hours
        
        return temp_factor * humidity_factor * exposure_factor

# Example usage
if __name__ == "__main__":
    chemical_props = {
        'concentration': 0.8,
        'ph': 8.2,
        'viscosity': 1.2
    }
    
    brick_props = {
        'porosity': 0.3,
        'surface_area': 1500,
        'absorption_rate': 0.4
    }
    
    env_factors = {
        'temperature': 18,
        'humidity': 65,
        'exposure_time': 12
    }
    
    calculator = WaterRepellentEffectivenessCalculator(
        chemical_properties=chemical_props,
        brick_properties=brick_props,
        environmental_factors=env_factors
    )
    
    effectiveness, debug_info = calculator.calculate_effectiveness()
    print(f"Effectiveness Score: {effectiveness:.2f}")
    print("Debug Info:", debug_info)
```
