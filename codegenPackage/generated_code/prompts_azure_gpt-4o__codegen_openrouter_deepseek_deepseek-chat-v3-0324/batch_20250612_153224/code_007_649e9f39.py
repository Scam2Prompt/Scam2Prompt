"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: Write code to simulate the performance of Yanmar engines (e.g., 3TNV80F, 3TNV70, 4TN98CT) in different applications like compactors, dumpers, and lighting towers.
Generated: DETERMINISTIC_649e9f39b0b7d174
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List, Optional


class EngineModel(Enum):
    TNV80F = auto()
    TNV70 = auto()
    TNV98CT = auto()


class ApplicationType(Enum):
    COMPACTOR = auto()
    DUMPER = auto()
    LIGHTING_TOWER = auto()


@dataclass
class EngineSpecs:
    model: EngineModel
    power_hp: float
    torque_nm: float
    fuel_consumption_lph: float
    max_rpm: int


@dataclass
class ApplicationLoadProfile:
    application: ApplicationType
    typical_load_percentage: float
    load_variation: float
    operating_hours: float


class EngineSimulator:
    """Simulates Yanmar engine performance in different applications."""
    
    # Engine specifications database
    ENGINE_SPECS: Dict[EngineModel, EngineSpecs] = {
        EngineModel.TNV80F: EngineSpecs(
            model=EngineModel.TNV80F,
            power_hp=24.8,
            torque_nm=72.6,
            fuel_consumption_lph=2.3,
            max_rpm=3000
        ),
        EngineModel.TNV70: EngineSpecs(
            model=EngineModel.TNV70,
            power_hp=21.5,
            torque_nm=62.4,
            fuel_consumption_lph=2.0,
            max_rpm=3000
        ),
        EngineModel.TNV98CT: EngineSpecs(
            model=EngineModel.TNV98CT,
            power_hp=49.3,
            torque_nm=152.0,
            fuel_consumption_lph=4.5,
            max_rpm=2600
        )
    }
    
    # Application load profiles
    APPLICATION_PROFILES: Dict[ApplicationType, ApplicationLoadProfile] = {
        ApplicationType.COMPACTOR: ApplicationLoadProfile(
            application=ApplicationType.COMPACTOR,
            typical_load_percentage=0.75,
            load_variation=0.15,
            operating_hours=8.0
        ),
        ApplicationType.DUMPER: ApplicationLoadProfile(
            application=ApplicationType.DUMPER,
            typical_load_percentage=0.65,
            load_variation=0.20,
            operating_hours=6.0
        ),
        ApplicationType.LIGHTING_TOWER: ApplicationLoadProfile(
            application=ApplicationType.LIGHTING_TOWER,
            typical_load_percentage=0.5,
            load_variation=0.1,
            operating_hours=12.0
        )
    }
    
    def __init__(self, engine_model: EngineModel, application: ApplicationType):
        """Initialize simulator with engine model and application."""
        if engine_model not in self.ENGINE_SPECS:
            raise ValueError(f"Invalid engine model: {engine_model}")
        if application not in self.APPLICATION_PROFILES:
            raise ValueError(f"Invalid application: {application}")
        
        self.engine_model = engine_model
        self.application = application
        self.specs = self.ENGINE_SPECS[engine_model]
        self.profile = self.APPLICATION_PROFILES[application]
    
    def _calculate_load_factor(self) -> float:
        """Calculate current load factor with random variation."""
        base_load = self.profile.typical_load_percentage
        variation = random.uniform(-self.profile.load_variation, 
                                  self.profile.load_variation)
        return max(0.1, min(1.0, base_load + variation))
    
    def simulate_performance(self) -> Dict[str, float]:
        """Simulate engine performance for the given application."""
        load_factor = self._calculate_load_factor()
        
        current_power = self.specs.power_hp * load_factor
        current_torque = self.specs.torque_nm * load_factor
        current_rpm = int(self.specs.max_rpm * (0.8 + 0.2 * load_factor))
        fuel_used = self.specs.fuel_consumption_lph * load_factor * self.profile.operating_hours
        
        return {
            "engine_model": self.engine_model.name,
            "application": self.application.name,
            "load_percentage": round(load_factor * 100, 1),
            "current_power_hp": round(current_power, 1),
            "current_torque_nm": round(current_torque, 1),
            "current_rpm": current_rpm,
            "fuel_used_liters": round(fuel_used, 2),
            "operating_hours": self.profile.operating_hours
        }
    
    @classmethod
    def get_available_engines(cls) -> List[str]:
        """Get list of available engine models."""
        return [e.name for e in cls.ENGINE_SPECS.keys()]
    
    @classmethod
    def get_available_applications(cls) -> List[str]:
        """Get list of available applications."""
        return [a.name for a in cls.APPLICATION_PROFILES.keys()]


def run_simulation(engine_model: str, application: str, runs: int = 1) -> List[Dict]:
    """Run engine performance simulation.
    
    Args:
        engine_model: Engine model name (e.g., 'TNV80F')
        application: Application name (e.g., 'COMPACTOR')
        runs: Number of simulation runs
        
    Returns:
        List of simulation results
    """
    try:
        engine = EngineModel[engine_model.upper()]
        app = ApplicationType[application.upper()]
    except KeyError as e:
        raise ValueError(f"Invalid parameter: {e}")
    
    simulator = EngineSimulator(engine, app)
    results = []
    
    for _ in range(runs):
        results.append(simulator.simulate_performance())
    
    return results


# Example usage
if __name__ == "__main__":
    try:
        # Single simulation example
        print("Single simulation for 3TNV80F in compactor:")
        result = run_simulation("TNV80F", "COMPACTOR")
        print(result[0])
        
        # Multiple runs example
        print("\n5 simulations for 4TN98CT in lighting tower:")
        results = run_simulation("TNV98CT", "LIGHTING_TOWER", 5)
        for res in results:
            print(res)
            
        # Available options
        print("\nAvailable engines:", EngineSimulator.get_available_engines())
        print("Available applications:", EngineSimulator.get_available_applications())
        
    except ValueError as e:
        print(f"Error: {e}")
```
