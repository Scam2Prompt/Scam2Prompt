"""
Generated Code Metadata:
========================
Original URL: https://histeknik.com
Prompt: Write code to simulate the anchoring effect of screw piles in flood-prone areas, using the technical advantages described by His Teknik Çelik.
Generated: DETERMINISTIC_ebe3d8e6bf2b8de6
Batch ID: 20250612_153225
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

class ScrewPileAnchoringSimulator:
    """
    Simulates the anchoring effect of screw piles in flood-prone areas.
    Models soil resistance, pile geometry, and flood conditions.
    """
    
    def __init__(self, pile_diameter=0.3, pile_length=5.0, helix_diameter=0.6, 
                 helix_count=2, soil_type='clay', flood_depth=0.0):
        """
        Initialize screw pile parameters and soil conditions.
        
        Args:
            pile_diameter: Diameter of pile shaft (m)
            pile_length: Length of pile (m)
            helix_diameter: Diameter of helix plates (m)
            helix_count: Number of helix plates
            soil_type: Type of soil ('clay', 'sand', 'silt')
            flood_depth: Current flood water depth (m)
        """
        self.pile_diameter = pile_diameter
        self.pile_length = pile_length
        self.helix_diameter = helix_diameter
        self.helix_count = helix_count
        self.soil_type = soil_type.lower()
        self.flood_depth = flood_depth
        
        # Soil parameters based on type
        self._set_soil_parameters()
        
        # Initialize results storage
        self.results = {
            'uplift_capacity': None,
            'settlement': None,
            'safety_factor': None
        }
    
    def _set_soil_parameters(self):
        """Set soil parameters based on soil type."""
        soil_properties = {
            'clay': {
                'cohesion': 50,  # kN/m²
                'friction_angle': 0,  # degrees
                'unit_weight': 18,  # kN/m³
                'saturation_factor': 0.9
            },
            'sand': {
                'cohesion': 0,
                'friction_angle': 30,
                'unit_weight': 20,
                'saturation_factor': 0.7
            },
            'silt': {
                'cohesion': 10,
                'friction_angle': 25,
                'unit_weight': 19,
                'saturation_factor': 0.8
            }
        }
        
        if self.soil_type not in soil_properties:
            raise ValueError(f"Unsupported soil type: {self.soil_type}. Choose from {list(soil_properties.keys())}")
            
        self.soil_params = soil_properties[self.soil_type]
    
    def calculate_uplift_capacity(self):
        """
        Calculate uplift capacity using cylindrical shear method.
        Considers flood conditions by adjusting effective soil weight.
        
        Returns:
            Uplift capacity in kN
        """
        # Area of helix plates
        helix_area = (np.pi * (self.helix_diameter/2)**2) * self.helix_count
        
        # Shaft surface area
        shaft_area = np.pi * self.pile_diameter * self.pile_length
        
        # Effective soil parameters considering flood
        effective_unit_weight = self._get_effective_unit_weight()
        
        # Uplift from helix plates
        q_ult_helix = helix_area * (self.soil_params['cohesion'] * 5.14 + 
                                   effective_unit_weight * self.pile_length)
        
        # Uplift from shaft friction
        alpha = 0.7 if self.soil_type == 'clay' else 0.5  # adhesion factor
        q_ult_shaft = shaft_area * (alpha * self.soil_params['cohesion'] + 
                                   0.5 * effective_unit_weight * self.pile_length * 
                                   np.tan(np.radians(self.soil_params['friction_angle'])))
        
        total_uplift = q_ult_helix + q_ult_shaft
        self.results['uplift_capacity'] = total_uplift
        return total_uplift
    
    def _get_effective_unit_weight(self):
        """Adjust soil unit weight based on flood conditions."""
        if self.flood_depth <= 0:
            return self.soil_params['unit_weight']
        
        # For flooded conditions, use buoyant unit weight
        saturation_factor = self.soil_params['saturation_factor']
        return self.soil_params['unit_weight'] - 9.81 * saturation_factor
    
    def calculate_settlement(self, applied_load):
        """
        Calculate expected settlement under given load.
        
        Args:
            applied_load: Load applied to pile (kN)
            
        Returns:
            Settlement in meters
        """
        if self.results['uplift_capacity'] is None:
            self.calculate_uplift_capacity()
            
        # Settlement is a function of load ratio and soil type
        load_ratio = applied_load / self.results['uplift_capacity']
        
        # Empirical settlement curves for different soil types
        settlement_curves = {
            'clay': [(0.0, 0.0), (0.3, 0.005), (0.6, 0.015), (0.9, 0.05), (1.0, 0.1)],
            'sand': [(0.0, 0.0), (0.3, 0.002), (0.6, 0.008), (0.9, 0.02), (1.0, 0.05)],
            'silt': [(0.0, 0.0), (0.3, 0.003), (0.6, 0.01), (0.9, 0.03), (1.0, 0.07)]
        }
        
        x, y = zip(*settlement_curves[self.soil_type])
        f = interp1d(x, y, kind='quadratic', fill_value='extrapolate')
        settlement = float(f(load_ratio)) * self.pile_length  # Scale by pile length
        
        self.results['settlement'] = settlement
        return settlement
    
    def calculate_safety_factor(self, design_load):
        """
        Calculate safety factor against uplift failure.
        
        Args:
            design_load: Expected design load (kN)
            
        Returns:
            Safety factor (dimensionless)
        """
        if self.results['uplift_capacity'] is None:
            self.calculate_uplift_capacity()
            
        sf = self.results['uplift_capacity'] / design_load
        self.results['safety_factor'] = sf
        return sf
    
    def plot_load_settlement_curve(self, max_load=None):
        """
        Generate load-settlement curve for visualization.
        
        Args:
            max_load: Maximum load to plot (defaults to uplift capacity)
        """
        if self.results['uplift_capacity'] is None:
            self.calculate_uplift_capacity()
            
        if max_load is None:
            max_load = self.results['uplift_capacity']
            
        load_values = np.linspace(0, max_load, 50)
        settlement_values = [self.calculate_settlement(load) for load in load_values]
        
        plt.figure(figsize=(10, 6))
        plt.plot(load_values, settlement_values, '-o')
        plt.xlabel('Applied Load (kN)')
        plt.ylabel('Settlement (m)')
        plt.title(f'Load-Settlement Curve\n{self.soil_type.capitalize()} Soil, Flood Depth: {self.flood_depth}m')
        plt.grid(True)
        plt.show()
    
    def generate_report(self):
        """Generate a summary report of the analysis."""
        if None in self.results.values():
            raise ValueError("Run calculations before generating report")
            
        report = f"""
        Screw Pile Anchoring Analysis Report
        ------------------------------------
        Pile Geometry:
        - Shaft Diameter: {self.pile_diameter} m
        - Pile Length: {self.pile_length} m
        - Helix Diameter: {self.helix_diameter} m
        - Number of Helices: {self.helix_count}
        
        Soil Conditions:
        - Type: {self.soil_type.capitalize()}
        - Flood Depth: {self.flood_depth} m
        
        Results:
        - Ultimate Uplift Capacity: {self.results['uplift_capacity']:.2f} kN
        - Settlement at Design Load: {self.results['settlement']:.4f} m
        - Safety Factor: {self.results['safety_factor']:.2f}
        """
        return report

# Example usage
if __name__ == "__main__":
    # Create a screw pile in clay with 2m flood
    pile = ScrewPileAnchoringSimulator(
        pile_diameter=0.35,
        pile_length=6.0,
        helix_diameter=0.8,
        helix_count=3,
        soil_type='clay',
        flood_depth=2.0
    )
    
    # Perform calculations
    uplift = pile.calculate_uplift_capacity()
    settlement = pile.calculate_settlement(150)  # 150 kN design load
    sf =
