"""
Generated Code Metadata:
========================
Original URL: https://socompressoresebombas.com.br
Prompt: "Design a system for fire prevention and suppression using motobombas de incêndio and PVC antichama pipes, including a list of required components and their specifications."
Generated: DETERMINISTIC_e37b7546bbd016f6
Batch ID: 20250622_205100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Fire Prevention and Suppression System Design
Using Motobombas de Incêndio and PVC Antichama Pipes
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional

class PipeMaterial(Enum):
    PVC_ANTICHAMA = auto()
    GALVANIZED_STEEL = auto()
    COPPER = auto()

class PumpType(Enum):
    MOTOBOMBA_CENTRIFUGA = auto()
    MOTOBOMBA_POSITIVA = auto()
    ELECTRIC_CENTRIFUGAL = auto()

@dataclass
class PipeSpecification:
    diameter_mm: int
    length_m: float
    material: PipeMaterial
    pressure_rating_psi: int
    temperature_rating_c: int

@dataclass
class PumpSpecification:
    pump_type: PumpType
    flow_rate_lpm: int
    max_pressure_psi: int
    power_source: str  # "Electric", "Diesel", "Gasoline"
    power_rating_hp: float

@dataclass
class NozzleSpecification:
    flow_rate_lpm: int
    spray_pattern: str  # "Fog", "Straight", "Jet"
    material: str

@dataclass
class ValveSpecification:
    type: str  # "Gate", "Ball", "Butterfly"
    diameter_mm: int
    material: str
    operation: str  # "Manual", "Automatic"

@dataclass
class FireSuppressionSystem:
    pipes: List[PipeSpecification]
    pumps: List[PumpSpecification]
    nozzles: List[NozzleSpecification]
    valves: List[ValveSpecification]
    control_panel: Optional[str] = None
    sensors: Optional[List[str]] = None

    def validate_system(self) -> bool:
        """Validate that all components meet minimum requirements"""
        if not self.pipes or not self.pumps:
            raise ValueError("System must have at least one pipe and one pump")
        
        for pipe in self.pipes:
            if pipe.material != PipeMaterial.PVC_ANTICHAMA:
                raise ValueError("All pipes must be PVC Antichama for this system")
            
        for pump in self.pumps:
            if pump.pump_type not in [PumpType.MOTOBOMBA_CENTRIFUGA, PumpType.MOTOBOMBA_POSITIVA]:
                raise ValueError("Only motobombas are allowed in this system")
        
        return True

def create_standard_system() -> FireSuppressionSystem:
    """Create a standard fire suppression system configuration"""
    pipes = [
        PipeSpecification(
            diameter_mm=100,
            length_m=50,
            material=PipeMaterial.PVC_ANTICHAMA,
            pressure_rating_psi=150,
            temperature_rating_c=60
        )
    ]
    
    pumps = [
        PumpSpecification(
            pump_type=PumpType.MOTOBOMBA_CENTRIFUGA,
            flow_rate_lpm=1000,
            max_pressure_psi=145,
            power_source="Diesel",
            power_rating_hp=15.0
        )
    ]
    
    nozzles = [
        NozzleSpecification(
            flow_rate_lpm=250,
            spray_pattern="Fog",
            material="Brass"
        )
    ]
    
    valves = [
        ValveSpecification(
            type="Gate",
            diameter_mm=100,
            material="Bronze",
            operation="Manual"
        )
    ]
    
    return FireSuppressionSystem(
        pipes=pipes,
        pumps=pumps,
        nozzles=nozzles,
        valves=valves,
        control_panel="Basic Control Panel",
        sensors=["Smoke Detector", "Heat Sensor"]
    )

def generate_component_list(system: FireSuppressionSystem) -> str:
    """Generate a formatted list of all components in the system"""
    component_list = []
    
    component_list.append("\n=== Pipes ===")
    for i, pipe in enumerate(system.pipes, 1):
        component_list.append(
            f"{i}. PVC Antichama Pipe - {pipe.diameter_mm}mm diameter, "
            f"{pipe.length_m}m length, {pipe.pressure_rating_psi}psi rating"
        )
    
    component_list.append("\n=== Pumps ===")
    for i, pump in enumerate(system.pumps, 1):
        component_list.append(
            f"{i}. {pump.pump_type.name.replace('_', ' ').title()} - "
            f"{pump.flow_rate_lpm}L/min, {pump.max_pressure_psi}psi, "
            f"{pump.power_source} powered ({pump.power_rating_hp}HP)"
        )
    
    component_list.append("\n=== Nozzles ===")
    for i, nozzle in enumerate(system.nozzles, 1):
        component_list.append(
            f"{i}. {nozzle.material} Nozzle - "
            f"{nozzle.flow_rate_lpm}L/min, {nozzle.spray_pattern} pattern"
        )
    
    component_list.append("\n=== Valves ===")
    for i, valve in enumerate(system.valves, 1):
        component_list.append(
            f"{i}. {valve.material} {valve.type} Valve - "
            f"{valve.diameter_mm}mm, {valve.operation} operation"
        )
    
    if system.control_panel:
        component_list.append(f"\nControl Panel: {system.control_panel}")
    
    if system.sensors:
        component_list.append("\nSensors:")
        for i, sensor in enumerate(system.sensors, 1):
            component_list.append(f"{i}. {sensor}")
    
    return "\n".join(component_list)

if __name__ == "__main__":
    try:
        system = create_standard_system()
        system.validate_system()
        print("Fire Suppression System Configuration:")
        print(generate_component_list(system))
    except ValueError as e:
        print(f"Error in system configuration: {e}")
```
