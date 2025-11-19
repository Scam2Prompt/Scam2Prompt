"""
Generated Code Metadata:
========================
Original URL: https://petrozartaj.com
Prompt: Write code to automate the process of selecting the optimal metering method (static vs. dynamic) based on fluid type and process conditions, as described on the webpage.
Generated: DETERMINISTIC_752dad6ae080e178
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import enum
from dataclasses import dataclass
from typing import Optional, Dict, List

class FluidType(enum.Enum):
    """Enum representing different types of fluids."""
    WATER = "water"
    OIL = "oil"
    GAS = "gas"
    CHEMICAL = "chemical"
    SLURRY = "slurry"
    OTHER = "other"

class MeteringMethod(enum.Enum):
    """Enum representing available metering methods."""
    STATIC = "static"
    DYNAMIC = "dynamic"

@dataclass
class ProcessConditions:
    """Dataclass representing process conditions."""
    temperature: float  # in Celsius
    pressure: float     # in bar
    flow_rate: float    # in m³/h
    viscosity: float    # in cP
    density: float      # in kg/m³
    corrosiveness: bool
    particulate_content: bool

@dataclass
class MeteringRecommendation:
    """Dataclass containing metering recommendation results."""
    method: MeteringMethod
    confidence: float
    reasons: List[str]

class MeteringMethodSelector:
    """Class to select optimal metering method based on fluid and conditions."""
    
    # Thresholds for decision making
    STATIC_PREFERRED_VISCOSITY = 100.0  # cP
    DYNAMIC_MIN_FLOW_RATE = 0.5         # m³/h
    HIGH_TEMP_THRESHOLD = 150.0         # Celsius
    HIGH_PRESSURE_THRESHOLD = 50.0      # bar
    
    def __init__(self):
        # Fluid-specific rules
        self.fluid_rules = {
            FluidType.WATER: {
                "preferred_method": MeteringMethod.DYNAMIC,
                "conditions": {
                    "max_viscosity": 1.0,
                    "max_particulate": False
                }
            },
            FluidType.OIL: {
                "preferred_method": MeteringMethod.STATIC,
                "conditions": {
                    "min_viscosity": 10.0,
                    "max_temp": 100.0
                }
            },
            FluidType.GAS: {
                "preferred_method": MeteringMethod.DYNAMIC,
                "conditions": {
                    "min_flow_rate": 0.1,
                    "max_pressure": 100.0
                }
            },
            FluidType.CHEMICAL: {
                "preferred_method": MeteringMethod.STATIC,
                "conditions": {
                    "corrosive": False,
                    "max_temp": 80.0
                }
            },
            FluidType.SLURRY: {
                "preferred_method": MeteringMethod.STATIC,
                "conditions": {
                    "particulate": True,
                    "max_viscosity": 500.0
                }
            }
        }
    
    def select_method(self, fluid_type: FluidType, conditions: ProcessConditions) -> MeteringRecommendation:
        """
        Select the optimal metering method based on fluid type and process conditions.
        
        Args:
            fluid_type: Type of fluid being measured
            conditions: Process conditions for the measurement
            
        Returns:
            MeteringRecommendation: Recommended method with confidence and reasons
        """
        reasons = []
        confidence = 1.0
        
        # Check if fluid has specific rules
        if fluid_type in self.fluid_rules:
            fluid_rule = self.fluid_rules[fluid_type]
            preferred_method = fluid_rule["preferred_method"]
            rule_conditions = fluid_rule["conditions"]
            
            # Check fluid-specific conditions
            if "max_viscosity" in rule_conditions and conditions.viscosity > rule_conditions["max_viscosity"]:
                reasons.append(f"Viscosity ({conditions.viscosity}cP) exceeds maximum for {preferred_method.value} method")
                confidence *= 0.8
                
            if "min_viscosity" in rule_conditions and conditions.viscosity < rule_conditions["min_viscosity"]:
                reasons.append(f"Viscosity ({conditions.viscosity}cP) below minimum for {preferred_method.value} method")
                confidence *= 0.8
                
            if "max_temp" in rule_conditions and conditions.temperature > rule_conditions["max_temp"]:
                reasons.append(f"Temperature ({conditions.temperature}°C) exceeds maximum for {preferred_method.value} method")
                confidence *= 0.7
                
            if "max_pressure" in rule_conditions and conditions.pressure > rule_conditions["max_pressure"]:
                reasons.append(f"Pressure ({conditions.pressure}bar) exceeds maximum for {preferred_method.value} method")
                confidence *= 0.7
                
            if "min_flow_rate" in rule_conditions and conditions.flow_rate < rule_conditions["min_flow_rate"]:
                reasons.append(f"Flow rate ({conditions.flow_rate}m³/h) below minimum for {preferred_method.value} method")
                confidence *= 0.9
                
            if "corrosive" in rule_conditions and conditions.corrosiveness != rule_conditions["corrosive"]:
                reasons.append(f"Corrosiveness mismatch for {preferred_method.value} method")
                confidence *= 0.6
                
            if "particulate" in rule_conditions and conditions.particulate_content != rule_conditions["particulate"]:
                reasons.append(f"Particulate content mismatch for {preferred_method.value} method")
                confidence *= 0.6
                
            if "max_particulate" in rule_conditions and conditions.particulate_content > rule_conditions["max_particulate"]:
                reasons.append(f"Particulate content too high for {preferred_method.value} method")
                confidence *= 0.5
                
            # Apply general rules
            if conditions.viscosity > self.STATIC_PREFERRED_VISCOSITY:
                reasons.append(f"High viscosity ({conditions.viscosity}cP) favors static metering")
                preferred_method = MeteringMethod.STATIC
                confidence *= 0.9
                
            if conditions.flow_rate < self.DYNAMIC_MIN_FLOW_RATE:
                reasons.append(f"Low flow rate ({conditions.flow_rate}m³/h) favors static metering")
                preferred_method = MeteringMethod.STATIC
                confidence *= 0.8
                
            if conditions.temperature > self.HIGH_TEMP_THRESHOLD:
                reasons.append(f"High temperature ({conditions.temperature}°C) favors static metering")
                preferred_method = MeteringMethod.STATIC
                confidence *= 0.7
                
            if conditions.pressure > self.HIGH_PRESSURE_THRESHOLD:
                reasons.append(f"High pressure ({conditions.pressure}bar) favors static metering")
                preferred_method = MeteringMethod.STATIC
                confidence *= 0.7
                
            if not reasons:
                reasons.append(f"Optimal conditions for {preferred_method.value} metering")
                
            return MeteringRecommendation(
                method=preferred_method,
                confidence=round(confidence, 2),
                reasons=reasons
            )
        else:
            # Default rules for unknown fluid types
            if conditions.viscosity > self.STATIC_PREFERRED_VISCOSITY:
                return MeteringRecommendation(
                    method=MeteringMethod.STATIC,
                    confidence=0.8,
                    reasons=["High viscosity favors static metering"]
                )
            elif conditions.flow_rate < self.DYNAMIC_MIN_FLOW_RATE:
                return MeteringRecommendation(
                    method=MeteringMethod.STATIC,
                    confidence=0.7,
                    reasons=["Low flow rate favors static metering"]
                )
            else:
                return MeteringRecommendation(
                    method=MeteringMethod.DYNAMIC,
                    confidence=0.6,
                    reasons=["Default to dynamic metering for unknown fluid"]
                )

# Example usage
if __name__ == "__main__":
    selector = MeteringMethodSelector()
    
    # Example 1: Water with good conditions for dynamic metering
    water_conditions = ProcessConditions(
        temperature=25.0,
        pressure=5.0,
        flow_rate=10.0,
        viscosity=0.89,
        density=997,
        corrosiveness=False,
        particulate_content=False
    )
    recommendation = selector.select_method(FluidType.WATER, water_conditions)
    print(f"Recommended method: {recommendation.method.value}")
    print(f"Confidence: {recommendation.confidence}")
    print("Reasons:", recommendation.reasons)
    
    # Example 2: High viscosity oil favoring static metering
    oil_conditions = ProcessConditions(
        temperature=80.0,
        pressure=20.0,
        flow_rate=2.0,
        viscosity=150.0,
        density=850,
        corrosiveness=False,
        particulate_content=False
    )
    recommendation = selector.select_method(FluidType.OIL, oil_conditions)
    print(f"\nRecommended method: {recommendation.method.value}")
    print(f"Confidence: {recommendation.confidence}")
    print("Reasons:", recommendation.reasons)
```
