"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: Write Python code to simulate the ice preservation performance of Engel UltraLite coolers, incorporating features like closed-cell foam insulation and tapered drainage channels.
Generated: DETERMINISTIC_8049ed7acb47bd12
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import Tuple, Optional
from dataclasses import dataclass
from enum import Enum, auto
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CoolerMaterial(Enum):
    """Enum for different cooler materials"""
    POLYETHYLENE = auto()
    POLYPROPYLENE = auto()
    ROTOMOLDED_POLYETHYLENE = auto()

class InsulationType(Enum):
    """Enum for different insulation types"""
    CLOSED_CELL_FOAM = auto()
    OPEN_CELL_FOAM = auto()
    VACUUM_INSULATION = auto()

@dataclass
class CoolerSpecs:
    """Data class to store cooler specifications"""
    volume_liters: float
    wall_thickness_cm: float
    material: CoolerMaterial
    insulation_type: InsulationType
    insulation_thickness_cm: float
    has_tapered_drain: bool
    ambient_temp_c: float = 25.0
    initial_ice_temp_c: float = 0.0

class IcePreservationSimulator:
    """Simulates ice preservation in Engel UltraLite coolers"""
    
    # Thermal conductivity values (W/m·K)
    THERMAL_CONDUCTIVITY = {
        CoolerMaterial.POLYETHYLENE: 0.42,
        CoolerMaterial.POLYPROPYLENE: 0.22,
        CoolerMaterial.ROTOMOLDED_POLYETHYLENE: 0.38,
        InsulationType.CLOSED_CELL_FOAM: 0.035,
        InsulationType.OPEN_CELL_FOAM: 0.045,
        InsulationType.VACUUM_INSULATION: 0.005
    }
    
    def __init__(self, specs: CoolerSpecs):
        """Initialize the simulator with cooler specifications"""
        self.specs = specs
        self.validate_specs()
        
    def validate_specs(self):
        """Validate the input specifications"""
        if self.specs.volume_liters <= 0:
            raise ValueError("Cooler volume must be positive")
        if self.specs.wall_thickness_cm <= 0 or self.specs.insulation_thickness_cm <= 0:
            raise ValueError("Wall and insulation thickness must be positive")
        if self.specs.ambient_temp_c <= self.specs.initial_ice_temp_c:
            raise ValueError("Ambient temperature must be higher than ice temperature")
    
    def calculate_thermal_resistance(self) -> float:
        """Calculate total thermal resistance of the cooler walls"""
        # Convert cm to m for calculations
        wall_thickness_m = self.specs.wall_thickness_cm / 100
        insulation_thickness_m = self.specs.insulation_thickness_cm / 100
        
        # Calculate resistance for each layer
        wall_resistance = wall_thickness_m / self.THERMAL_CONDUCTIVITY[self.specs.material]
        insulation_resistance = insulation_thickness_m / self.THERMAL_CONDUCTIVITY[self.specs.insulation_type]
        
        return wall_resistance + insulation_resistance
    
    def calculate_surface_area(self) -> float:
        """Estimate cooler surface area based on volume (simplified model)"""
        # Assuming a cube shape for simplicity
        side_length_cm = (self.specs.volume_liters * 1000) ** (1/3)
        return 6 * (side_length_cm / 100) ** 2  # Convert to m²
    
    def simulate_ice_melt(self, hours: float, opening_frequency: float = 0.0) -> Tuple[float, float]:
        """
        Simulate ice melt over time.
        
        Args:
            hours: Duration of simulation in hours
            opening_frequency: Frequency of cooler openings per hour (0-1)
            
        Returns:
            Tuple of (remaining_ice_percentage, final_temp_c)
        """
        try:
            if hours <= 0:
                raise ValueError("Simulation duration must be positive")
            if not 0 <= opening_frequency <= 1:
                raise ValueError("Opening frequency must be between 0 and 1")
            
            thermal_resistance = self.calculate_thermal_resistance()
            surface_area = self.calculate_surface_area()
            
            # Heat transfer coefficient (W/m²·K)
            u_value = 1 / thermal_resistance
            
            # Total heat transfer (Joules)
            delta_temp = self.specs.ambient_temp_c - self.specs.initial_ice_temp_c
            heat_transfer = u_value * surface_area * delta_temp * hours * 3600  # Convert hours to seconds
            
            # Account for cooler openings
            if opening_frequency > 0:
                heat_transfer *= (1 + opening_frequency * 2)  # Empirical factor
            
            # Account for tapered drain efficiency
            if self.specs.has_tapered_drain:
                heat_transfer *= 0.95  # 5% improvement
            
            # Heat required to melt ice (J/kg)
            latent_heat = 334000  # J/kg
            specific_heat = 2100  # J/kg·K for ice
            
            # Calculate melted ice
            ice_mass_kg = self.specs.volume_liters * 0.9  # Assume 90% ice fill
            temp_rise = min(delta_temp, heat_transfer / (ice_mass_kg * specific_heat))
            melted_ice = max(0, (heat_transfer - (ice_mass_kg * specific_heat * temp_rise)) / latent_heat)
            
            remaining_ice = max(0, ice_mass_kg - melted_ice)
            final_temp = self.specs.initial_ice_temp_c + temp_rise
            
            return (remaining_ice / ice_mass_kg * 100, final_temp)
            
        except Exception as e:
            logger.error(f"Error in ice melt simulation: {str(e)}")
            raise

def run_simulation():
    """Example usage of the IcePreservationSimulator"""
    try:
        # Create cooler specifications
        specs = CoolerSpecs(
            volume_liters=20,
            wall_thickness_cm=2.5,
            material=CoolerMaterial.ROTOMOLDED_POLYETHYLENE,
            insulation_type=InsulationType.CLOSED_CELL_FOAM,
            insulation_thickness_cm=3.0,
            has_tapered_drain=True,
            ambient_temp_c=30.0
        )
        
        # Initialize simulator
        simulator = IcePreservationSimulator(specs)
        
        # Run simulation for 48 hours with occasional openings
        remaining_ice, final_temp = simulator.simulate_ice_melt(48, opening_frequency=0.1)
        
        print(f"After 48 hours at 30°C:")
        print(f"- Remaining ice: {remaining_ice:.1f}%")
        print(f"- Final temperature: {final_temp:.1f}°C")
        
    except Exception as e:
        logger.error(f"Simulation failed: {str(e)}")

if __name__ == "__main__":
    run_simulation()
```
