"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: Write code to simulate the response time of a sprinkler system in reducing heat, flames, and smoke during a fire, based on the benefits outlined by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_bbdd1c249346f0ac
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
import time
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Optional

class FireSeverity(Enum):
    """Enum representing the severity levels of a fire."""
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()

@dataclass
class FireMetrics:
    """Data class to hold fire metrics."""
    heat_level: float  # in °C
    flame_intensity: float  # 0-100 scale
    smoke_density: float  # 0-100 scale

class SprinklerSystem:
    """Simulates a sprinkler system's response to a fire."""
    
    def __init__(self):
        self.response_time: float = 0.0  # in seconds
        self.is_activated: bool = False
        self.efficiency: Dict[FireSeverity, float] = {
            FireSeverity.LOW: 0.9,    # 90% efficiency
            FireSeverity.MEDIUM: 0.7, # 70% efficiency
            FireSeverity.HIGH: 0.5    # 50% efficiency
        }
    
    def activate(self) -> None:
        """Activate the sprinkler system."""
        if not self.is_activated:
            self.is_activated = True
            self.response_time = time.time()
    
    def reduce_fire_metrics(self, metrics: FireMetrics, severity: FireSeverity) -> FireMetrics:
        """
        Reduce fire metrics based on sprinkler efficiency and response time.
        
        Args:
            metrics: Current fire metrics.
            severity: Severity of the fire.
        
        Returns:
            Updated fire metrics after sprinkler action.
        """
        if not self.is_activated:
            raise RuntimeError("Sprinkler system is not activated.")
        
        efficiency = self.efficiency.get(severity, 0.5)
        time_factor = min(1.0, (time.time() - self.response_time) / 10.0)  # Normalize over 10 seconds
        
        # Apply reduction based on efficiency and time factor
        new_heat = max(20.0, metrics.heat_level * (1 - efficiency * time_factor))
        new_flames = max(0.0, metrics.flame_intensity * (1 - efficiency * time_factor))
        new_smoke = max(0.0, metrics.smoke_density * (1 - efficiency * time_factor))
        
        return FireMetrics(new_heat, new_flames, new_smoke)

def simulate_fire_response(initial_metrics: FireMetrics, severity: FireSeverity) -> List[FireMetrics]:
    """
    Simulate the sprinkler system's response to a fire over time.
    
    Args:
        initial_metrics: Initial fire metrics.
        severity: Severity of the fire.
    
    Returns:
        List of fire metrics at each simulation step.
    """
    sprinkler = SprinklerSystem()
    metrics_history = [initial_metrics]
    
    # Simulate detection delay (0.5-2 seconds)
    detection_delay = random.uniform(0.5, 2.0)
    time.sleep(detection_delay)
    
    sprinkler.activate()
    
    # Simulate for 20 seconds in 0.5-second steps
    for _ in range(40):
        current_metrics = metrics_history[-1]
        updated_metrics = sprinkler.reduce_fire_metrics(current_metrics, severity)
        metrics_history.append(updated_metrics)
        time.sleep(0.5)
    
    return metrics_history

if __name__ == "__main__":
    # Example usage
    initial_fire = FireMetrics(heat_level=500.0, flame_intensity=80.0, smoke_density=70.0)
    severity = FireSeverity.MEDIUM
    
    print("Simulating sprinkler system response...")
    history = simulate_fire_response(initial_fire, severity)
    
    print("\nResults:")
    for i, metrics in enumerate(history):
        print(f"Step {i}: Heat={metrics.heat_level:.1f}°C, Flames={metrics.flame_intensity:.1f}%, Smoke={metrics.smoke_density:.1f}%")
```
