"""
Generated Code Metadata:
========================
Original URL: https://aktivrorteknikk.no
Prompt: Generate code for a pipe cleaning simulation that uses customizable cleaning plugs for various pipe dimensions, as outlined in Aktiv Rørteknikk AS's plug cleaning services.
Generated: DETERMINISTIC_f15381ae9bb088d5
Batch ID: 20250612_154209
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
from typing import List, Dict, Optional, Tuple

class PlugMaterial(Enum):
    RUBBER = "rubber"
    POLYURETHANE = "polyurethane"
    SILICONE = "silicone"

class PlugType(Enum):
    STANDARD = "standard"
    INFLATABLE = "inflatable"
    BRUSH = "brush"

class PipeMaterial(Enum):
    STEEL = "steel"
    PVC = "pvc"
    CONCRETE = "concrete"
    CAST_IRON = "cast_iron"

class CleaningPlug:
    """
    Represents a customizable cleaning plug for pipe cleaning operations.
    """
    def __init__(
        self,
        diameter: float,
        length: float,
        material: PlugMaterial,
        plug_type: PlugType,
        max_pressure: float = 10.0
    ):
        """
        Initialize a cleaning plug with specified parameters.
        
        Args:
            diameter: Diameter of the plug in millimeters
            length: Length of the plug in millimeters
            material: Material of the plug
            plug_type: Type of the plug
            max_pressure: Maximum operating pressure in bar
        """
        self.diameter = diameter
        self.length = length
        self.material = material
        self.type = plug_type
        self.max_pressure = max_pressure
        self._validate_parameters()
    
    def _validate_parameters(self) -> None:
        """Validate plug parameters."""
        if self.diameter <= 0:
            raise ValueError("Diameter must be positive")
        if self.length <= 0:
            raise ValueError("Length must be positive")
        if self.max_pressure <= 0:
            raise ValueError("Max pressure must be positive")
    
    def calculate_volume(self) -> float:
        """Calculate the volume of the plug (approximated as cylinder)."""
        radius = self.diameter / 2
        return math.pi * (radius ** 2) * self.length
    
    def __str__(self) -> str:
        return (f"CleaningPlug(diameter={self.diameter}mm, length={self.length}mm, "
                f"material={self.material.value}, type={self.type.value}, "
                f"max_pressure={self.max_pressure}bar)")

class Pipe:
    """
    Represents a pipe to be cleaned.
    """
    def __init__(
        self,
        diameter: float,
        length: float,
        material: PipeMaterial,
        roughness: float = 0.1
    ):
        """
        Initialize a pipe with specified parameters.
        
        Args:
            diameter: Inner diameter of the pipe in millimeters
            length: Length of the pipe in meters
            material: Material of the pipe
            roughness: Surface roughness in millimeters
        """
        self.diameter = diameter
        self.length = length
        self.material = material
        self.roughness = roughness
        self._validate_parameters()
    
    def _validate_parameters(self) -> None:
        """Validate pipe parameters."""
        if self.diameter <= 0:
            raise ValueError("Diameter must be positive")
        if self.length <= 0:
            raise ValueError("Length must be positive")
        if self.roughness < 0:
            raise ValueError("Roughness cannot be negative")
    
    def is_plug_compatible(self, plug: CleaningPlug) -> bool:
        """
        Check if a cleaning plug is compatible with this pipe.
        
        Args:
            plug: Cleaning plug to check
            
        Returns:
            bool: True if compatible, False otherwise
        """
        # Plug diameter should be slightly larger than pipe diameter for effective cleaning
        return plug.diameter >= self.diameter * 0.95 and plug.diameter <= self.diameter * 1.1
    
    def __str__(self) -> str:
        return (f"Pipe(diameter={self.diameter}mm, length={self.length}m, "
                f"material={self.material.value}, roughness={self.roughness}mm)")

class CleaningSimulation:
    """
    Simulates the pipe cleaning process using customizable plugs.
    """
    def __init__(self):
        self.plugs: List[CleaningPlug] = []
        self.pipes: List[Pipe] = []
    
    def add_plug(self, plug: CleaningPlug) -> None:
        """Add a cleaning plug to the simulation."""
        self.plugs.append(plug)
    
    def add_pipe(self, pipe: Pipe) -> None:
        """Add a pipe to the simulation."""
        self.pipes.append(pipe)
    
    def find_compatible_plugs(self, pipe: Pipe) -> List[CleaningPlug]:
        """
        Find all plugs compatible with a given pipe.
        
        Args:
            pipe: Pipe to find compatible plugs for
            
        Returns:
            List of compatible CleaningPlug objects
        """
        return [plug for plug in self.plugs if pipe.is_plug_compatible(plug)]
    
    def simulate_cleaning(
        self,
        pipe: Pipe,
        plug: CleaningPlug,
        water_flow_rate: float,
        pressure: float
    ) -> Dict:
        """
        Simulate a cleaning operation.
        
        Args:
            pipe: Pipe to clean
            plug: Plug to use for cleaning
            water_flow_rate: Water flow rate in liters per minute
            pressure: Operating pressure in bar
            
        Returns:
            Dictionary containing simulation results
            
        Raises:
            ValueError: If parameters are invalid or incompatible
        """
        if not pipe.is_plug_compatible(plug):
            raise ValueError("Plug is not compatible with the pipe")
        
        if pressure > plug.max_pressure:
            raise ValueError(f"Pressure exceeds plug's maximum ({plug.max_pressure} bar)")
        
        if water_flow_rate <= 0:
            raise ValueError("Water flow rate must be positive")
        
        # Simplified cleaning effectiveness calculation
        effectiveness = min(1.0, 
                          (plug.diameter / pipe.diameter) * 
                          (pressure / plug.max_pressure) * 
                          (water_flow_rate / 100))  # Normalized
        
        # Estimated cleaning time (simplified)
        cleaning_time = pipe.length / (water_flow_rate * 0.01)  # minutes
        
        return {
            "pipe": str(pipe),
            "plug": str(plug),
            "water_flow_rate": water_flow_rate,
            "pressure": pressure,
            "cleaning_effectiveness": round(effectiveness, 2),
            "estimated_cleaning_time": round(cleaning_time, 2),
            "success": effectiveness >= 0.7  # Threshold for successful cleaning
        }
    
    def batch_simulate(
        self,
        water_flow_rate: float,
        pressure: float
    ) -> List[Dict]:
        """
        Run simulations for all compatible pipe-plug combinations.
        
        Args:
            water_flow_rate: Water flow rate in liters per minute
            pressure: Operating pressure in bar
            
        Returns:
            List of simulation results for all compatible combinations
        """
        results = []
        for pipe in self.pipes:
            compatible_plugs = self.find_compatible_plugs(pipe)
            for plug in compatible_plugs:
                try:
                    result = self.simulate_cleaning(pipe, plug, water_flow_rate, pressure)
                    results.append(result)
                except ValueError as e:
                    print(f"Skipping incompatible combination: {e}")
        return results

# Example usage
if __name__ == "__main__":
    # Create simulation instance
    simulation = CleaningSimulation()
    
    # Add some plugs
    simulation.add_plug(CleaningPlug(
        diameter=100,
        length=200,
        material=PlugMaterial.RUBBER,
        plug_type=PlugType.STANDARD,
        max_pressure=8
    ))
    
    simulation.add_plug(CleaningPlug(
        diameter=150,
        length=250,
        material=PlugMaterial.POLYURETHANE,
        plug_type=PlugType.INFLATABLE,
        max_pressure=12
    ))
    
    # Add some pipes
    simulation.add_pipe(Pipe(
        diameter=100,
        length=50,
        material=PipeMaterial.STEEL,
        roughness=0.2
    ))
    
    simulation.add_pipe(Pipe(
        diameter=150,
        length=30,
        material=PipeMaterial.PVC,
        roughness=0.05
    ))
    
    # Run a single simulation
    pipe_to_clean = simulation.pipes[0]
    plug_to_use = simulation.find_compatible_plugs(pipe_to_clean)[0]
    
    print("Single simulation result:")
    result = simulation.simulate_cleaning(
        pipe=pipe_to_clean,
        plug=plug_to_use,
        water_flow_rate=80,
        pressure=6
    )
    for key, value in result.items():
        print(f"{key}: {value}")
    
    # Run batch simulations
    print("\nBatch simulation results:")
    batch_results = simulation.batch_simulate(water_flow_rate=100, pressure=8)
    for res in batch_results:
        print(f"\nPipe: {res['pipe']}")
        print(f"Plug: {res['plug']}")
        print(f"
