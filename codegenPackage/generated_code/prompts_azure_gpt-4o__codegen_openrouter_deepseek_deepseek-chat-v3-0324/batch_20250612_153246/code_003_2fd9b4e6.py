"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Write code to model the statikai tulajdonságok (structural properties) of Hevestherm Deluxe-s 92 nyílászárók using Python and a material simulation library.
Generated: DETERMINISTIC_2fd9b4e6455d2290
Batch ID: 20250612_153246
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
from scipy.interpolate import interp1d
from typing import Tuple, Dict, Optional

class WindowMaterial:
    """
    Class representing material properties for window components.
    """
    def __init__(self, name: str, youngs_modulus: float, poissons_ratio: float, density: float):
        """
        Initialize material properties.
        
        Args:
            name: Name of the material
            youngs_modulus: Young's modulus in Pa
            poissons_ratio: Poisson's ratio (unitless)
            density: Density in kg/m³
        """
        self.name = name
        self.youngs_modulus = youngs_modulus
        self.poissons_ratio = poissons_ratio
        self.density = density

class WindowProfile:
    """
    Class representing a window profile with structural properties.
    """
    def __init__(self, material: WindowMaterial, cross_section_area: float, 
                 moment_of_inertia: float, torsional_constant: float):
        """
        Initialize window profile properties.
        
        Args:
            material: WindowMaterial object
            cross_section_area: Cross-sectional area in m²
            moment_of_inertia: Moment of inertia in m⁴
            torsional_constant: Torsional constant in m⁴
        """
        self.material = material
        self.cross_section_area = cross_section_area
        self.moment_of_inertia = moment_of_inertia
        self.torsional_constant = torsional_constant

class HevesthermDeluxe92:
    """
    Class modeling the structural properties of Hevestherm Deluxe-s 92 windows.
    """
    # Material properties (example values - should be replaced with actual data)
    PVC_MATERIAL = WindowMaterial(
        name="PVC",
        youngs_modulus=3.0e9,  # 3 GPa
        poissons_ratio=0.38,
        density=1380.0  # kg/m³
    )
    
    GLASS_MATERIAL = WindowMaterial(
        name="Glass",
        youngs_modulus=72e9,  # 72 GPa
        poissons_ratio=0.23,
        density=2500.0  # kg/m³
    )
    
    def __init__(self):
        """
        Initialize window system with default profile properties.
        """
        # Profile properties (example values - should be replaced with actual data)
        self.frame_profile = WindowProfile(
            material=self.PVC_MATERIAL,
            cross_section_area=4.2e-4,  # m²
            moment_of_inertia=8.5e-8,   # m⁴
            torsional_constant=1.2e-7   # m⁴
        )
        
        self.sash_profile = WindowProfile(
            material=self.PVC_MATERIAL,
            cross_section_area=3.8e-4,  # m²
            moment_of_inertia=7.2e-8,   # m⁴
            torsional_constant=1.0e-7   # m⁴
        )
        
        self.glass_thickness = 0.004  # 4mm glass thickness (single pane example)
        
    def calculate_deflection(self, load: float, span: float, profile: WindowProfile) -> float:
        """
        Calculate deflection under uniform load.
        
        Args:
            load: Uniform load in N/m
            span: Span length in m
            profile: WindowProfile object to calculate for
            
        Returns:
            Maximum deflection in meters
        """
        if load <= 0 or span <= 0:
            raise ValueError("Load and span must be positive values")
            
        # Simple beam deflection formula: (5 * load * span^4) / (384 * E * I)
        deflection = (5 * load * span**4) / (384 * profile.material.youngs_modulus * profile.moment_of_inertia)
        return deflection
    
    def calculate_stress(self, load: float, span: float, profile: WindowProfile) -> float:
        """
        Calculate maximum bending stress.
        
        Args:
            load: Uniform load in N/m
            span: Span length in m
            profile: WindowProfile object to calculate for
            
        Returns:
            Maximum bending stress in Pa
        """
        if load <= 0 or span <= 0:
            raise ValueError("Load and span must be positive values")
            
        # Simple beam stress formula: (load * span^2) / (8 * section_modulus)
        # Approximate section modulus as I / (height/2)
        section_modulus = profile.moment_of_inertia / 0.02  # Assuming 40mm profile height
        stress = (load * span**2) / (8 * section_modulus)
        return stress
    
    def analyze_window(self, width: float, height: float, wind_load: float) -> Dict:
        """
        Perform structural analysis of the window under wind load.
        
        Args:
            width: Window width in meters
            height: Window height in meters
            wind_load: Wind load in Pa
            
        Returns:
            Dictionary containing analysis results
        """
        if width <= 0 or height <= 0 or wind_load <= 0:
            raise ValueError("Dimensions and load must be positive values")
            
        results = {}
        
        # Convert wind load to line load (N/m)
        frame_load = wind_load * height
        sash_load = wind_load * (height - 0.1)  # Approximate sash height
        
        # Frame analysis (horizontal member)
        results['frame_deflection'] = self.calculate_deflection(frame_load, width, self.frame_profile)
        results['frame_stress'] = self.calculate_stress(frame_load, width, self.frame_profile)
        
        # Sash analysis (vertical member)
        results['sash_deflection'] = self.calculate_deflection(sash_load, height, self.sash_profile)
        results['sash_stress'] = self.calculate_stress(sash_load, height, self.sash_profile)
        
        # Glass analysis (simplified)
        glass_load = wind_load * width * height
        results['glass_deflection'] = self._calculate_glass_deflection(glass_load, width, height)
        
        return results
    
    def _calculate_glass_deflection(self, load: float, width: float, height: float) -> float:
        """
        Calculate glass deflection using simplified formula.
        
        Args:
            load: Total load in N
            width: Glass width in m
            height: Glass height in m
            
        Returns:
            Maximum deflection in meters
        """
        # Simplified glass deflection formula
        a = min(width, height)
        b = max(width, height)
        aspect_ratio = b / a
        
        # Empirical coefficients for simply supported rectangular glass
        if aspect_ratio >= 1.0 and aspect_ratio <= 5.0:
            alpha = 0.0448  # Coefficient for aspect ratio ~1.5
        else:
            alpha = 0.0138  # Conservative estimate
            
        deflection = alpha * (load * a**3) / (self.GLASS_MATERIAL.youngs_modulus * self.glass_thickness**3)
        return deflection

# Example usage
if __name__ == "__main__":
    window = HevesthermDeluxe92()
    
    # Analyze a 1.2m x 1.5m window under 1000 Pa wind load
    results = window.analyze_window(width=1.2, height=1.5, wind_load=1000)
    
    print("Structural Analysis Results:")
    print(f"Frame deflection: {results['frame_deflection']*1000:.2f} mm")
    print(f"Frame stress: {results['frame_stress']/1e6:.2f} MPa")
    print(f"Sash deflection: {results['sash_deflection']*1000:.2f} mm")
    print(f"Sash stress: {results['sash_stress']/1e6:.2f} MPa")
    print(f"Glass deflection: {results['glass_deflection']*1000:.2f} mm")
```
