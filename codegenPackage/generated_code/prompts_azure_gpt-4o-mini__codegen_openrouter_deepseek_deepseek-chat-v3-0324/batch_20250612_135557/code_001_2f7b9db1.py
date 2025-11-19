"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: Write a code snippet that simulates the preservation conditions for table grapes during international shipping, incorporating best practices from Osku's packaging methods.
Generated: DETERMINISTIC_2f7b9db1138d4800
Batch ID: 20250612_135557
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
from typing import List, Optional

class GrapeCondition(Enum):
    """Enum representing grape condition states."""
    EXCELLENT = auto()
    GOOD = auto()
    FAIR = auto()
    POOR = auto()
    SPOILED = auto()

class PackagingMaterial(Enum):
    """Enum representing different packaging materials."""
    VENTILATED_PLASTIC = auto()
    MODIFIED_ATMOSPHERE = auto()
    MICROPERFORATED = auto()
    STANDARD = auto()

@dataclass
class GrapePackage:
    """Class representing a package of grapes with preservation conditions."""
    temperature: float  # in Celsius
    humidity: float     # percentage
    co2_level: float    # percentage
    o2_level: float     # percentage
    packaging: PackagingMaterial
    grapes: List[GrapeCondition]
    
    def check_quality(self) -> GrapeCondition:
        """Determine the overall quality of grapes in the package."""
        if any(cond == GrapeCondition.SPOILED for cond in self.grapes):
            return GrapeCondition.SPOILED
        
        excellent_count = sum(1 for cond in self.grapes if cond == GrapeCondition.EXCELLENT)
        if excellent_count / len(self.grapes) > 0.8:
            return GrapeCondition.EXCELLENT
        
        good_count = sum(1 for cond in self.grapes if cond == GrapeCondition.GOOD)
        if (excellent_count + good_count) / len(self.grapes) > 0.7:
            return GrapeCondition.GOOD
        
        fair_count = sum(1 for cond in self.grapes if cond == GrapeCondition.FAIR)
        if (excellent_count + good_count + fair_count) / len(self.grapes) > 0.6:
            return GrapeCondition.FAIR
        
        return GrapeCondition.POOR

class GrapePreservationSimulator:
    """Simulator for grape preservation during shipping."""
    
    def __init__(self, initial_temp: float, initial_humidity: float, 
                 packaging: PackagingMaterial, num_grapes: int = 100):
        """Initialize the simulator with starting conditions."""
        self.temperature = initial_temp
        self.humidity = initial_humidity
        self.packaging = packaging
        self.co2_level = 5.0 if packaging == PackagingMaterial.MODIFIED_ATMOSPHERE else 0.5
        self.o2_level = 2.0 if packaging == PackagingMaterial.MODIFIED_ATMOSPHERE else 20.8
        self.grapes = [GrapeCondition.EXCELLENT] * num_grapes
    
    def _calculate_degradation_factor(self, hours: int) -> float:
        """Calculate degradation factor based on conditions."""
        temp_factor = max(0, (self.temperature - 1) / 5)  # Ideal temp is ~1°C
        humidity_factor = abs(self.humidity - 90) / 50    # Ideal humidity is ~90%
        packaging_factor = {
            PackagingMaterial.VENTILATED_PLASTIC: 0.3,
            PackagingMaterial.MODIFIED_ATMOSPHERE: 0.1,
            PackagingMaterial.MICROPERFORATED: 0.2,
            PackagingMaterial.STANDARD: 0.5
        }[self.packaging]
        
        return (temp_factor + humidity_factor) * packaging_factor * (hours / 24)
    
    def simulate_shipping(self, duration_hours: int, temp_variation: float = 0.5) -> GrapePackage:
        """Simulate shipping conditions over time."""
        for hour in range(duration_hours):
            # Simulate temperature fluctuations
            self.temperature += random.uniform(-temp_variation, temp_variation)
            self.temperature = max(-1, min(5, self.temperature))  # Keep within safe range
            
            # Simulate humidity changes
            self.humidity += random.uniform(-2, 2)
            self.humidity = max(70, min(95, self.humidity))  # Keep within safe range
            
            # Calculate degradation
            degradation = self._calculate_degradation_factor(1)
            
            # Update grape conditions
            for i in range(len(self.grapes)):
                if self.grapes[i] != GrapeCondition.SPOILED:
                    if random.random() < degradation * 0.01:
                        self.grapes[i] = GrapeCondition(min(self.grapes[i].value + 1, GrapeCondition.SPOILED.value))
        
        return GrapePackage(
            temperature=self.temperature,
            humidity=self.humidity,
            co2_level=self.co2_level,
            o2_level=self.o2_level,
            packaging=self.packaging,
            grapes=self.grapes
        )

# Example usage
if __name__ == "__main__":
    # Simulate optimal Osku's packaging conditions
    simulator = GrapePreservationSimulator(
        initial_temp=1.0,
        initial_humidity=90.0,
        packaging=PackagingMaterial.MODIFIED_ATMOSPHERE
    )
    
    # Simulate 14 days of shipping
    result = simulator.simulate_shipping(duration_hours=14*24)
    
    # Print results
    print(f"Final temperature: {result.temperature:.1f}°C")
    print(f"Final humidity: {result.humidity:.1f}%")
    print(f"Final CO2 level: {result.co2_level:.1f}%")
    print(f"Final O2 level: {result.o2_level:.1f}%")
    print(f"Grape quality: {result.check_quality().name}")
```
