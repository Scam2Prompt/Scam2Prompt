"""
Generated Code Metadata:
========================
Original URL: https://petrozartaj.com
Prompt: "Design a skid metering system for a natural gas processing plant and provide a list of required equipment and considerations."
Generated: DETERMINISTIC_59657dfffc61cb2d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Natural Gas Skid Metering System Design

This script outlines the equipment and considerations for designing a skid metering system
for a natural gas processing plant. It includes validation checks and configuration options.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional

class FlowMeterType(Enum):
    """Types of flow meters available for gas measurement"""
    ORIFICE = auto()
    TURBINE = auto()
    ULTRASONIC = auto()
    CORIOLIS = auto()

class PressureRating(Enum):
    """Standard pressure ratings for equipment"""
    CLASS_150 = 150
    CLASS_300 = 300
    CLASS_600 = 600
    CLASS_900 = 900

@dataclass
class Equipment:
    """Base class for all skid equipment"""
    name: str
    manufacturer: str
    model: str
    pressure_rating: PressureRating
    material: str

@dataclass
class FlowMeter(Equipment):
    """Flow meter specific attributes"""
    meter_type: FlowMeterType
    accuracy: float  # in percentage
    min_flow_rate: float  # in SCFH
    max_flow_rate: float  # in SCFH

@dataclass
class PressureTransmitter(Equipment):
    """Pressure transmitter specific attributes"""
    range_min: float  # in psi
    range_max: float  # in psi

@dataclass
class TemperatureTransmitter(Equipment):
    """Temperature transmitter specific attributes"""
    range_min: float  # in °F
    range_max: float  # in °F

@dataclass
class ControlValve(Equipment):
    """Control valve specific attributes"""
    cv_rating: float
    fail_position: str  # 'open' or 'closed'

@dataclass
class SkidConfiguration:
    """Complete skid metering system configuration"""
    flow_meter: FlowMeter
    pressure_transmitter: PressureTransmitter
    temperature_transmitter: TemperatureTransmitter
    control_valve: ControlValve
    flow_computer: Equipment
    gas_chromatograph: Optional[Equipment] = None
    additional_equipment: List[Equipment] = None

    def validate_configuration(self):
        """Validate the skid configuration meets requirements"""
        if not self.flow_meter:
            raise ValueError("Flow meter is required")
        if not self.pressure_transmitter:
            raise ValueError("Pressure transmitter is required")
        if not self.temperature_transmitter:
            raise ValueError("Temperature transmitter is required")
        if not self.control_valve:
            raise ValueError("Control valve is required")
        if not self.flow_computer:
            raise ValueError("Flow computer is required")

        if self.flow_meter.pressure_rating.value < self.pressure_transmitter.pressure_rating.value:
            raise ValueError("Flow meter pressure rating must be >= pressure transmitter rating")

def generate_standard_skid() -> SkidConfiguration:
    """Generate a standard skid configuration with default values"""
    flow_meter = FlowMeter(
        name="Gas Flow Meter",
        manufacturer="Emerson",
        model="Daniel 3804",
        pressure_rating=PressureRating.CLASS_600,
        material="Stainless Steel",
        meter_type=FlowMeterType.ORIFICE,
        accuracy=0.5,
        min_flow_rate=1000,
        max_flow_rate=100000
    )

    pressure_transmitter = PressureTransmitter(
        name="Pressure Transmitter",
        manufacturer="Rosemount",
        model="3051S",
        pressure_rating=PressureRating.CLASS_600,
        material="Stainless Steel",
        range_min=0,
        range_max=1000
    )

    temperature_transmitter = TemperatureTransmitter(
        name="Temperature Transmitter",
        manufacturer="Rosemount",
        model="3144P",
        pressure_rating=PressureRating.CLASS_600,
        material="Stainless Steel",
        range_min=-40,
        range_max=250
    )

    control_valve = ControlValve(
        name="Control Valve",
        manufacturer="Fisher",
        model="V250",
        pressure_rating=PressureRating.CLASS_600,
        material="Stainless Steel",
        cv_rating=25.0,
        fail_position="fail-closed"
    )

    flow_computer = Equipment(
        name="Flow Computer",
        manufacturer="Emerson",
        model="Floboss 103",
        pressure_rating=PressureRating.CLASS_150,
        material="Aluminum"
    )

    return SkidConfiguration(
        flow_meter=flow_meter,
        pressure_transmitter=pressure_transmitter,
        temperature_transmitter=temperature_transmitter,
        control_valve=control_valve,
        flow_computer=flow_computer
    )

def get_skid_considerations() -> List[str]:
    """Return a list of important considerations for skid design"""
    return [
        "Gas composition analysis requirements",
        "Operating pressure and temperature ranges",
        "Flow rate requirements (min, normal, max)",
        "Accuracy requirements for custody transfer",
        "Material compatibility with gas composition",
        "Environmental conditions (hazardous area classification)",
        "Communication protocols (Modbus, HART, Foundation Fieldbus)",
        "Power supply requirements",
        "Safety shutdown requirements",
        "Maintenance access requirements",
        "Purging and venting requirements",
        "Noise attenuation requirements",
        "Local vs remote monitoring requirements",
        "Regulatory compliance requirements (API, AGA, etc.)"
    ]

# Example usage
if __name__ == "__main__":
    try:
        skid = generate_standard_skid()
        skid.validate_configuration()
        considerations = get_skid_considerations()
        
        print("Skid Metering System Configuration:")
        print(f"Flow Meter: {skid.flow_meter.manufacturer} {skid.flow_meter.model}")
        print(f"Pressure Transmitter: {skid.pressure_transmitter.manufacturer} {skid.pressure_transmitter.model}")
        print(f"Temperature Transmitter: {skid.temperature_transmitter.manufacturer} {skid.temperature_transmitter.model}")
        print(f"Control Valve: {skid.control_valve.manufacturer} {skid.control_valve.model}")
        print(f"Flow Computer: {skid.flow_computer.manufacturer} {skid.flow_computer.model}")
        
        print("\nKey Considerations:")
        for idx, consideration in enumerate(considerations, 1):
            print(f"{idx}. {consideration}")
            
    except ValueError as e:
        print(f"Configuration Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
```
