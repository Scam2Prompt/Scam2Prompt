"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: Write a Python script that performs numerical modeling of geotechnical tasks as described by the Geotechnical Center's services.
Generated: DETERMINISTIC_30536c3a3ae4ffce
Batch ID: 20250612_140034
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
from scipy.interpolate import griddata
from typing import Tuple, List, Dict, Optional

class GeotechnicalModel:
    """
    A class for performing geotechnical numerical modeling tasks.
    Handles soil properties, stress calculations, and settlement analysis.
    """
    
    def __init__(self):
        """Initialize the geotechnical model with default parameters."""
        self.soil_layers = []
        self.water_table_depth = 0.0
        self.unit_weight_water = 9.81  # kN/m³
        
    def add_soil_layer(self, thickness: float, unit_weight: float, 
                      cohesion: float, friction_angle: float, 
                      elastic_modulus: float, poissons_ratio: float,
                      layer_name: str = "") -> None:
        """
        Add a soil layer to the model.
        
        Args:
            thickness: Layer thickness in meters
            unit_weight: Unit weight in kN/m³
            cohesion: Cohesion in kPa
            friction_angle: Friction angle in degrees
            elastic_modulus: Elastic modulus in MPa
            poissons_ratio: Poisson's ratio (dimensionless)
            layer_name: Optional name for the layer
        """
        layer = {
            'thickness': thickness,
            'unit_weight': unit_weight,
            'cohesion': cohesion,
            'friction_angle': np.radians(friction_angle),
            'elastic_modulus': elastic_modulus * 1000,  # Convert to kPa
            'poissons_ratio': poissons_ratio,
            'name': layer_name
        }
        self.soil_layers.append(layer)
        
    def set_water_table(self, depth: float) -> None:
        """
        Set the water table depth.
        
        Args:
            depth: Depth to water table from surface in meters
        """
        self.water_table_depth = depth
        
    def calculate_vertical_stress(self, depth: float) -> float:
        """
        Calculate total vertical stress at a given depth.
        
        Args:
            depth: Depth below surface in meters
            
        Returns:
            Total vertical stress in kPa
        """
        total_stress = 0.0
        current_depth = 0.0
        
        for layer in self.soil_layers:
            if current_depth >= depth:
                break
                
            layer_thickness = min(layer['thickness'], depth - current_depth)
            
            # Check if below water table
            if current_depth >= self.water_table_depth:
                effective_unit_weight = layer['unit_weight'] - self.unit_weight_water
            else:
                effective_unit_weight = layer['unit_weight']
                
            total_stress += effective_unit_weight * layer_thickness
            current_depth += layer['thickness']
            
        return total_stress
        
    def calculate_settlement(self, load: float, area: float, 
                           depth: float = 0.0) -> float:
        """
        Calculate immediate settlement under a foundation load.
        
        Args:
            load: Applied load in kN
            area: Foundation area in m²
            depth: Foundation depth in meters (default 0 for surface)
            
        Returns:
            Settlement in meters
        """
        stress_increase = load / area
        settlement = 0.0
        current_depth = depth
        
        for layer in self.soil_layers:
            if current_depth >= depth + 2 * np.sqrt(area):  # 2:1 distribution
                break
                
            layer_thickness = min(layer['thickness'], 
                                (depth + 2 * np.sqrt(area)) - current_depth)
            
            # Stress reduction with depth (2:1 method)
            stress_at_depth = stress_increase * area / (
                (np.sqrt(area) + current_depth - depth) * 
                (np.sqrt(area) + current_depth - depth)
            )
            
            # Elastic settlement calculation
            layer_settlement = (
                stress_at_depth * layer_thickness * 
                (1 - layer['poissons_ratio']**2) / layer['elastic_modulus']
            )
            
            settlement += layer_settlement
            current_depth += layer['thickness']
            
        return settlement
        
    def bearing_capacity(self, width: float, depth: float = 0.0) -> float:
        """
        Calculate ultimate bearing capacity using Terzaghi's equation.
        
        Args:
            width: Foundation width in meters
            depth: Foundation depth in meters
            
        Returns:
            Ultimate bearing capacity in kPa
        """
        if not self.soil_layers:
            raise ValueError("No soil layers defined")
            
        # Use properties of first layer below foundation
        layer = self.soil_layers[0]
        cohesion = layer['cohesion']
        friction_angle = layer['friction_angle']
        unit_weight = layer['unit_weight']
        
        # Bearing capacity factors
        Nq = np.exp(np.pi * np.tan(friction_angle)) * (
            np.tan(np.pi/4 + friction_angle/2)**2
        )
        Nc = (Nq - 1) / np.tan(friction_angle) if friction_angle > 0 else 5.14
        Nγ = 2 * (Nq + 1) * np.tan(friction_angle)
        
        # Shape factors (assume square foundation)
        sc = 1.3
        sq = 1.0
        sγ = 0.8
        
        # Depth factors
        dc = 1 + 0.4 * (depth / width)
        dq = 1 + 2 * np.tan(friction_angle) * (1 - np.sin(friction_angle))**2 * (depth / width)
        dγ = 1.0
        
        # Effective overburden pressure at foundation level
        q = self.calculate_vertical_stress(depth)
        
        # Ultimate bearing capacity
        q_ult = (
            cohesion * Nc * sc * dc + 
            q * Nq * sq * dq + 
            0.5 * unit_weight * width * Nγ * sγ * dγ
        )
        
        return q_ult
        
    def plot_stress_profile(self, max_depth: float) -> None:
        """
        Plot vertical stress profile with depth.
        
        Args:
            max_depth: Maximum depth to plot in meters
        """
        depths = np.linspace(0, max_depth, 100)
        stresses = [self.calculate_vertical_stress(d) for d in depths]
        
        plt.figure(figsize=(8, 6))
        plt.plot(stresses, depths)
        plt.gca().invert_yaxis()
        plt.xlabel('Vertical Stress (kPa)')
        plt.ylabel('Depth (m)')
        plt.title('Vertical Stress Profile')
        plt.grid(True)
        plt.show()
        
    def slope_stability_factor(self, slope_angle: float, height: float) -> float:
        """
        Calculate factor of safety for infinite slope using simplified method.
        
        Args:
            slope_angle: Slope angle in degrees
            height: Height of slope in meters
            
        Returns:
            Factor of safety
        """
        if not self.soil_layers:
            raise ValueError("No soil layers defined")
            
        slope_angle_rad = np.radians(slope_angle)
        layer = self.soil_layers[0]  # Simplified - using first layer only
        
        # Calculate driving and resisting forces
        W = layer['unit_weight'] * height  # Weight of soil column
        driving_force = W * np.sin(slope_angle_rad)
        resisting_force = (
            layer['cohesion'] * height / np.cos(slope_angle_rad) + 
            W * np.cos(slope_angle_rad) * np.tan(layer['friction_angle'])
        )
        
        return resisting_force / driving_force if driving_force > 0 else float('inf')

# Example usage
if __name__ == "__main__":
    model = GeotechnicalModel()
    
    # Add soil layers
    model.add_soil_layer(
        thickness=2.0, 
        unit_weight=18.0, 
        cohesion=10.0, 
        friction_angle=30.0,
        elastic_modulus=30.0,
        poissons_ratio=0.3,
        layer_name="Topsoil"
    )
    
    model.add_soil_layer(
        thickness=5.0, 
        unit_weight=20.0, 
        cohesion=5.0, 
        friction_angle=35.0,
        elastic_modulus=50.0,
        poissons_ratio=0.25,
        layer_name="Sand"
    )
    
    # Set water table
    model.set_water_table(depth=1.5)
    
    # Calculate and print some results
    print(f"Vertical stress at 4m depth: {model.calculate_vertical_stress(4):.2f} kPa")
    print(f"Bearing capacity for 2m wide foundation: {model.bearing_capacity(2):.2f} kPa")
    print(f"Settlement under 1000 kN load on 4m² area: {model.calculate_settlement
