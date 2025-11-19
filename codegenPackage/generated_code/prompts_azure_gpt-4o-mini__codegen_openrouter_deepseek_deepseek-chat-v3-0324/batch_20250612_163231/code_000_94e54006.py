"""
Generated Code Metadata:
========================
Original URL: https://phantom-ss.com
Prompt: Write a code snippet that simulates the performance metrics of a Chevrolet Cobalt SS/TC, including its lap time at Nürburgring and modifications like the Borg Wagner Turbo and K&N Cold Air Intake.
Generated: DETERMINISTIC_94e54006626f55f6
Batch ID: 20250612_163231
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
from typing import List, Optional

@dataclass
class CarModification:
    """Represents a car modification with its performance impact."""
    name: str
    horsepower_gain: float
    torque_gain: float
    weight_reduction: float  # in kg

@dataclass
class PerformanceMetrics:
    """Stores performance metrics of a car."""
    lap_time: float  # in seconds
    horsepower: float
    torque: float  # in Nm
    weight: float  # in kg

class ChevroletCobaltSSTC:
    """Simulates the Chevrolet Cobalt SS/TC performance metrics."""
    
    # Base specifications for Chevrolet Cobalt SS/TC
    BASE_HORSEPOWER = 260  # hp
    BASE_TORQUE = 353  # Nm
    BASE_WEIGHT = 1315  # kg
    BASE_LAP_TIME = 8 * 60 + 22  # 8 minutes 22 seconds in seconds
    
    def __init__(self):
        self.mods: List[CarModification] = []
        self.performance = PerformanceMetrics(
            lap_time=self.BASE_LAP_TIME,
            horsepower=self.BASE_HORSEPOWER,
            torque=self.BASE_TORQUE,
            weight=self.BASE_WEIGHT
        )
    
    def add_modification(self, mod: CarModification) -> None:
        """Adds a modification and updates performance metrics."""
        self.mods.append(mod)
        self._update_performance()
    
    def _update_performance(self) -> None:
        """Recalculates performance metrics based on modifications."""
        total_hp_gain = sum(mod.horsepower_gain for mod in self.mods)
        total_torque_gain = sum(mod.torque_gain for mod in self.mods)
        total_weight_reduction = sum(mod.weight_reduction for mod in self.mods)
        
        self.performance.horsepower = self.BASE_HORSEPOWER + total_hp_gain
        self.performance.torque = self.BASE_TORQUE + total_torque_gain
        self.performance.weight = self.BASE_WEIGHT - total_weight_reduction
        
        # Simulate lap time improvement based on modifications
        # Formula: base_time * (1 - (total_improvement_factor))
        # Improvement factors are arbitrary but realistic for simulation
        hp_factor = total_hp_gain / 1000  # 0.1% improvement per 1hp
        weight_factor = total_weight_reduction / 2000  # 0.05% improvement per 1kg
        total_improvement = hp_factor + weight_factor
        
        # Add some randomness to simulate track conditions
        randomness = random.uniform(-0.02, 0.02)  # ±2% variation
        improvement_factor = 1 - (total_improvement + randomness)
        
        self.performance.lap_time = max(
            self.BASE_LAP_TIME * improvement_factor,
            self.BASE_LAP_TIME * 0.7  # 30% improvement cap
        )
    
    def get_performance(self) -> PerformanceMetrics:
        """Returns current performance metrics."""
        return self.performance

# Example modifications
BORG_WARNER_TURBO = CarModification(
    name="Borg Warner Turbo",
    horsepower_gain=50,
    torque_gain=60,
    weight_reduction=0
)

KN_COLD_AIR_INTAKE = CarModification(
    name="K&N Cold Air Intake",
    horsepower_gain=10,
    torque_gain=5,
    weight_reduction=2
)

# Example usage
if __name__ == "__main__":
    cobalt = ChevroletCobaltSSTC()
    print("Base Performance:", cobalt.get_performance())
    
    cobalt.add_modification(BORG_WARNER_TURBO)
    cobalt.add_modification(KN_COLD_AIR_INTAKE)
    
    print("Modified Performance:", cobalt.get_performance())
```
