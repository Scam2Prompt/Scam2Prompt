"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: "Generate a Python code for numerical modeling of geotechnical tasks as per the services offered by Научно-образовательный центр «Геотехника» им. З.Г. Тер-Мартиросяна."
Generated: DETERMINISTIC_31583fd20855833a
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy import interpolate
from typing import Tuple, Optional, Union

class GeotechnicalModel:
    """
    Numerical modeling of geotechnical tasks as per the services offered by 
    Научно-образовательный центр «Геотехника» им. З.Г. Тер-Мартиросяна.
    
    This class provides methods for common geotechnical calculations including:
    - Soil settlement analysis
    - Slope stability calculations
    - Bearing capacity of foundations
    - Stress distribution in soil masses
    """
    
    def __init__(self):
        """Initialize the geotechnical model with default parameters"""
        self.soil_layers = []
        self.water_table_depth = None
        self.gravity = 9.81  # m/s²
        
    def add_soil_layer(self, thickness: float, unit_weight: float, 
                      cohesion: float, friction_angle: float, 
                      elastic_modulus: float, poissons_ratio: float) -> None:
        """
        Add a soil layer to the model
        
        Args:
            thickness: Layer thickness (m)
            unit_weight: Unit weight of soil (kN/m³)
            cohesion: Cohesion of soil (kPa)
            friction_angle: Internal friction angle (degrees)
            elastic_modulus: Young's modulus (MPa)
            poissons_ratio: Poisson's ratio (dimensionless)
        """
        self.soil_layers.append({
            'thickness': thickness,
            'unit_weight': unit_weight,
            'cohesion': cohesion,
            'friction_angle': np.radians(friction_angle),
            'elastic_modulus': elastic_modulus * 1000,  # Convert to kPa
            'poissons_ratio': poissons_ratio
        })
    
    def set_water_table(self, depth: float) -> None:
        """
        Set the water table depth
        
        Args:
            depth: Depth to water table from surface (m)
        """
        self.water_table_depth = depth
        
    def calculate_settlement(self, foundation_pressure: float, 
                            foundation_width: float, 
                            foundation_length: float = None) -> Tuple[float, np.ndarray]:
        """
        Calculate immediate settlement using elastic theory
        
        Args:
            foundation_pressure: Applied pressure (kPa)
            foundation_width: Foundation width (m)
            foundation_length: Foundation length (m). If None, assumes circular foundation
            
        Returns:
            Tuple of (total settlement, settlement at each layer)
        """
        if not self.soil_layers:
            raise ValueError("No soil layers defined")
            
        if foundation_length is None:
            # Circular foundation
            shape_factor = 0.8
            influence_factor = 1.0
        else:
            # Rectangular foundation
            shape_factor = 1.12
            L_over_B = foundation_length / foundation_width
            influence_factor = 1 - (0.1 * L_over_B)
            
        settlements = []
        depth = 0
        total_settlement = 0
        
        for layer in self.soil_layers:
            # Calculate stress increase at depth using Boussinesq's method
            z = depth + layer['thickness']/2
            B = foundation_width
            stress_increase = self._calculate_stress_increase(
                foundation_pressure, B, z, influence_factor)
            
            # Calculate settlement for this layer
            E = layer['elastic_modulus']
            mu = layer['poissons_ratio']
            settlement = (stress_increase * shape_factor * (1 - mu**2) * 
                         layer['thickness'] / E)
            
            settlements.append(settlement)
            total_settlement += settlement
            depth += layer['thickness']
            
        return total_settlement, np.array(settlements)
    
    def _calculate_stress_increase(self, q: float, B: float, z: float, 
                                 influence_factor: float) -> float:
        """
        Calculate vertical stress increase below a foundation using Boussinesq's method
        
        Args:
            q: Applied pressure (kPa)
            B: Foundation width (m)
            z: Depth below foundation (m)
            influence_factor: Shape factor
            
        Returns:
            Vertical stress increase (kPa)
        """
        m = B / z
        n = B / z  # For square foundation
        I = 0.25 * np.log((m**2 + n**2 + 1)/(m**2 * n**2)) + \
            (m * n) / (2 * np.pi) * np.arctan2(m * n, np.sqrt(m**2 + n**2 + 1))
        return q * I * influence_factor
    
    def calculate_bearing_capacity(self, foundation_depth: float, 
                                  foundation_width: float, 
                                  foundation_length: float = None) -> float:
        """
        Calculate ultimate bearing capacity using Terzaghi's method
        
        Args:
            foundation_depth: Depth of foundation base (m)
            foundation_width: Foundation width (m)
            foundation_length: Foundation length (m). If None, assumes square foundation
            
        Returns:
            Ultimate bearing capacity (kPa)
        """
        if not self.soil_layers:
            raise ValueError("No soil layers defined")
            
        # Use properties of first soil layer below foundation
        layer = self.soil_layers[0]
        cohesion = layer['cohesion']
        phi = layer['friction_angle']
        gamma = layer['unit_weight']
        
        # Shape factors
        if foundation_length is None:
            # Square foundation
            Nq = np.exp(np.pi * np.tan(phi)) * (np.tan(np.pi/4 + phi/2))**2
            Nc = (Nq - 1) / np.tan(phi) if phi > 0 else 5.14
            Ngamma = 0.8 * (Nq - 1) * np.tan(phi)
            sc = 1.3
            sq = 1.2
            sgamma = 0.8
        else:
            # Rectangular foundation
            Nq = np.exp(np.pi * np.tan(phi)) * (np.tan(np.pi/4 + phi/2))**2
            Nc = (Nq - 1) / np.tan(phi) if phi > 0 else 5.14
            Ngamma = 2 * (Nq + 1) * np.tan(phi)
            L_over_B = foundation_length / foundation_width
            sc = 1 + 0.2 * L_over_B
            sq = 1 + 0.1 * L_over_B * np.sin(phi)
            sgamma = 1 - 0.4 * L_over_B
            
        # Depth factors
        D_over_B = foundation_depth / foundation_width
        dc = 1 + 0.2 * D_over_B * np.sqrt(Nq)
        dq = 1 + 0.1 * D_over_B * np.sqrt(Nq) if phi > 0 else 1
        dgamma = 1
        
        # Effective overburden pressure
        q = gamma * foundation_depth
        
        # Water table correction
        if self.water_table_depth is not None:
            if self.water_table_depth < foundation_depth:
                gamma = gamma - 9.81  # Buoyant unit weight
            elif self.water_table_depth < foundation_depth + foundation_width:
                gamma = gamma - 9.81 * (self.water_table_depth - foundation_depth) / foundation_width
        
        # Bearing capacity equation
        q_ult = (cohesion * Nc * sc * dc + 
                 q * Nq * sq * dq + 
                 0.5 * gamma * foundation_width * Ngamma * sgamma * dgamma)
        
        return q_ult
    
    def calculate_slope_stability(self, slope_angle: float, 
                                 slope_height: float, 
                                 method: str = 'ordinary') -> float:
        """
        Calculate factor of safety for slope stability using method of slices
        
        Args:
            slope_angle: Angle of slope (degrees)
            slope_height: Height of slope (m)
            method: Analysis method ('ordinary', 'bishop', 'janbu')
            
        Returns:
            Factor of safety
        """
        if not self.soil_layers:
            raise ValueError("No soil layers defined")
            
        slope_angle = np.radians(slope_angle)
        phi = self.soil_layers[0]['friction_angle']
        cohesion = self.soil_layers[0]['cohesion']
        gamma = self.soil_layers[0]['unit_weight']
        
        # Simplified circular failure surface
        R = slope_height / (1 - np.cos(slope_angle))  # Radius of failure circle
        L = R * slope_angle  # Arc length
        
        if method == 'ordinary':
            # Ordinary method of slices (Fellenius)
            W = 0.5 * gamma * slope_height**2 * np.tan(slope_angle)
            driving_moment = W * R * np.sin(slope_angle)
            resisting_moment = (cohesion * L * R + 
                                W * np.cos(slope_angle) * np.tan(phi) * R
