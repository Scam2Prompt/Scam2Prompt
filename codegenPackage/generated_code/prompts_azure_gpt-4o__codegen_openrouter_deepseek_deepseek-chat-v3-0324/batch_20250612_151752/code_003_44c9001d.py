"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: Provide a Python script for developing geotechnical models to assess the stability of foundations and structures, incorporating the principles of soil mechanics discussed on the Научно-образовательный центр «Геотехника» website.
Generated: DETERMINISTIC_44c9001d0b830009
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from typing import Tuple, List, Optional, Union

class SoilMechanics:
    """
    A class to implement geotechnical calculations based on soil mechanics principles.
    Includes methods for foundation stability analysis, bearing capacity, settlement, etc.
    """
    
    def __init__(self, soil_type: str, unit_weight: float, cohesion: float, friction_angle: float):
        """
        Initialize soil parameters.
        
        Args:
            soil_type: Type of soil (e.g., 'clay', 'sand', 'silt')
            unit_weight: Unit weight of soil (kN/m³)
            cohesion: Cohesion of soil (kPa)
            friction_angle: Internal friction angle (degrees)
        """
        self.soil_type = soil_type.lower()
        self.unit_weight = unit_weight
        self.cohesion = cohesion
        self.friction_angle = np.radians(friction_angle)  # Convert to radians
        
        # Validate input parameters
        if unit_weight <= 0:
            raise ValueError("Unit weight must be positive")
        if cohesion < 0:
            raise ValueError("Cohesion cannot be negative")
        if not 0 <= friction_angle <= np.pi/2:
            raise ValueError("Friction angle must be between 0 and 90 degrees")

    def bearing_capacity(self, foundation_width: float, foundation_length: float, 
                        depth: float, water_table_depth: Optional[float] = None) -> float:
        """
        Calculate the ultimate bearing capacity of a shallow foundation using Terzaghi's equation.
        
        Args:
            foundation_width: Width of foundation (m)
            foundation_length: Length of foundation (m)
            depth: Depth of foundation base below ground surface (m)
            water_table_depth: Depth to water table from ground surface (m), None if not present
            
        Returns:
            Ultimate bearing capacity (kPa)
        """
        # Shape factors
        if foundation_length / foundation_width > 10:
            shape_factors = (1.0, 1.0, 1.0)  # Strip footing
        else:
            shape_factors = (
                1 + 0.3 * (foundation_width / foundation_length),  # Nc
                1 + 0.2 * (foundation_width / foundation_length),  # Nq
                1 - 0.4 * (foundation_width / foundation_length)   # Nγ
            )
        
        # Depth factors (assuming D/B <= 1)
        depth_factors = (
            1 + 0.2 * (depth / foundation_width),  # dc
            1 + 0.1 * (depth / foundation_width),  # dq
            1.0                                    # dγ
        )
        
        # Bearing capacity factors
        Nq = np.exp(np.pi * np.tan(self.friction_angle)) * (np.tan(np.pi/4 + self.friction_angle/2))**2
        Nc = (Nq - 1) / np.tan(self.friction_angle) if self.friction_angle > 0 else 5.14
        Nγ = 2 * (Nq + 1) * np.tan(self.friction_angle)
        
        # Effective unit weight considering water table
        if water_table_depth is not None and water_table_depth <= depth + foundation_width:
            effective_unit_weight = self.unit_weight - 9.81  # Subtract water unit weight
        else:
            effective_unit_weight = self.unit_weight
        
        # Calculate bearing capacity
        q_ult = (self.cohesion * Nc * shape_factors[0] * depth_factors[0] +
                 self.unit_weight * depth * Nq * shape_factors[1] * depth_factors[1] +
                 0.5 * effective_unit_weight * foundation_width * Nγ * shape_factors[2] * depth_factors[2])
        
        return q_ult

    def settlement_immediate(self, foundation_width: float, foundation_length: float,
                            net_pressure: float, poissons_ratio: float, 
                            elastic_modulus: float, influence_depth: float = 5.0) -> float:
        """
        Calculate immediate (elastic) settlement of a foundation.
        
        Args:
            foundation_width: Width of foundation (m)
            foundation_length: Length of foundation (m)
            net_pressure: Net foundation pressure (kPa)
            poissons_ratio: Poisson's ratio of soil
            elastic_modulus: Elastic modulus of soil (kPa)
            influence_depth: Depth of influence below foundation (m)
            
        Returns:
            Immediate settlement (m)
        """
        # Shape and rigidity factors
        if foundation_length / foundation_width > 10:
            # Strip footing
            shape_factor = 1.0
            rigidity_factor = 0.85
        else:
            # Rectangular footing
            L_B_ratio = foundation_length / foundation_width
            shape_factor = 1.12 - 0.16 * np.sqrt(L_B_ratio)
            rigidity_factor = 0.8
        
        # Depth factor
        depth_factor = min(1.0, 1.0 - 0.1 * (influence_depth / foundation_width))
        
        # Calculate settlement
        settlement = (net_pressure * foundation_width * shape_factor * rigidity_factor * depth_factor *
                     (1 - poissons_ratio**2) / elastic_modulus)
        
        return settlement

    def slope_stability_factor(self, slope_height: float, slope_angle: float, 
                              water_table_height: Optional[float] = None) -> float:
        """
        Calculate factor of safety for infinite slope stability.
        
        Args:
            slope_height: Height of slope (m)
            slope_angle: Angle of slope (degrees)
            water_table_height: Height of water table from slope base (m), None if dry
            
        Returns:
            Factor of safety
        """
        slope_angle_rad = np.radians(slope_angle)
        
        if water_table_height is None:
            # Dry slope
            FS = (self.cohesion / (self.unit_weight * slope_height * np.sin(slope_angle_rad) * np.cos(slope_angle_rad)) +
                  np.tan(self.friction_angle) / np.tan(slope_angle_rad))
        else:
            # Submerged slope
            ru = 0.5 * (water_table_height / slope_height)**2  # Pore pressure ratio
            FS = (self.cohesion / (self.unit_weight * slope_height * np.sin(slope_angle_rad) * np.cos(slope_angle_rad)) +
                  (1 - ru) * np.tan(self.friction_angle) / np.tan(slope_angle_rad))
        
        return FS

    def plot_bearing_capacity_vs_width(self, width_range: Tuple[float, float], num_points: int = 50,
                                      foundation_length: float = 1.0, depth: float = 1.0,
                                      water_table_depth: Optional[float] = None) -> plt.Figure:
        """
        Plot bearing capacity vs foundation width.
        
        Args:
            width_range: Tuple of (min_width, max_width) in meters
            num_points: Number of points to plot
            foundation_length: Length of foundation (m)
            depth: Depth of foundation (m)
            water_table_depth: Depth to water table (m)
            
        Returns:
            Matplotlib figure object
        """
        widths = np.linspace(width_range[0], width_range[1], num_points)
        capacities = [self.bearing_capacity(w, foundation_length, depth, water_table_depth) for w in widths]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(widths, capacities, 'b-', linewidth=2)
        ax.set_xlabel('Foundation Width (m)', fontsize=12)
        ax.set_ylabel('Bearing Capacity (kPa)', fontsize=12)
        ax.set_title('Bearing Capacity vs Foundation Width', fontsize=14)
        ax.grid(True)
        
        return fig

class PileFoundation:
    """
    A class for analyzing pile foundations.
    """
    
    def __init__(self, pile_diameter: float, pile_length: float, soil_layers: List[dict]):
        """
        Initialize pile foundation parameters.
        
        Args:
            pile_diameter: Diameter of pile (m)
            pile_length: Length of pile (m)
            soil_layers: List of dictionaries containing soil layer properties:
                        [{'thickness': float, 'unit_weight': float, 
                          'cohesion': float, 'friction_angle': float,
                          'elastic_modulus': float}, ...]
        """
        self.pile_diameter = pile_diameter
        self.pile_length = pile_length
        self.soil_layers = soil_layers
        
        # Validate input
        if pile_diameter <= 0 or pile_length <= 0:
            raise ValueError("Pile dimensions must be positive")
        if not soil_layers:
            raise ValueError("At least one soil layer must be provided")
        
        total_thickness = sum(layer['thickness'] for layer in soil
