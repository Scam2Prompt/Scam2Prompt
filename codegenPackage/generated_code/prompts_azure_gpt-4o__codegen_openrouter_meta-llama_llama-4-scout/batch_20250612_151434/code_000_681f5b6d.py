"""
Generated Code Metadata:
========================
Original URL: https://tromba-sa.com.ar
Prompt: Write Python code to simulate the operation of a centrifugal pump system, referencing the types of pumps and technologies described on the TROMBA website, such as EDUR Bomba Multifase or TAC Bombas Autocebante.
Generated: DETERMINISTIC_681f5b6d915957d0
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict

class PumpType(Enum):
    """Enum for pump types."""
    CENTRIFUGAL = 1
    MULTISTAGE = 2
    SELF_PRIMING = 3

class Pump(ABC):
    """Abstract base class for pumps."""

    def __init__(self, pump_type: PumpType, flow_rate: float, head: float):
        """
        Initialize a pump.

        Args:
        - pump_type (PumpType): Type of pump.
        - flow_rate (float): Flow rate of the pump in m^3/h.
        - head (float): Head of the pump in meters.
        """
        self.pump_type = pump_type
        self.flow_rate = flow_rate
        self.head = head

    @abstractmethod
    def calculate_power(self) -> float:
        """Calculate the power consumption of the pump."""
        pass

    def __str__(self):
        return f"Pump Type: {self.pump_type.name}, Flow Rate: {self.flow_rate} m^3/h, Head: {self.head} meters"

class CentrifugalPump(Pump):
    """Class for centrifugal pumps."""

    def __init__(self, flow_rate: float, head: float, efficiency: float):
        """
        Initialize a centrifugal pump.

        Args:
        - flow_rate (float): Flow rate of the pump in m^3/h.
        - head (float): Head of the pump in meters.
        - efficiency (float): Efficiency of the pump.
        """
        super().__init__(PumpType.CENTRIFUGAL, flow_rate, head)
        self.efficiency = efficiency

    def calculate_power(self) -> float:
        """Calculate the power consumption of the centrifugal pump."""
        # Assuming density of water is 1000 kg/m^3 and gravity is 9.81 m/s^2
        power = (self.flow_rate * self.head * 1000 * 9.81) / (3600 * self.efficiency * 1000)
        return power

class MultistagePump(Pump):
    """Class for multistage pumps."""

    def __init__(self, flow_rate: float, head: float, stages: int, efficiency: float):
        """
        Initialize a multistage pump.

        Args:
        - flow_rate (float): Flow rate of the pump in m^3/h.
        - head (float): Head of the pump in meters.
        - stages (int): Number of stages in the pump.
        - efficiency (float): Efficiency of the pump.
        """
        super().__init__(PumpType.MULTISTAGE, flow_rate, head)
        self.stages = stages
        self.efficiency = efficiency

    def calculate_power(self) -> float:
        """Calculate the power consumption of the multistage pump."""
        # Assuming density of water is 1000 kg/m^3 and gravity is 9.81 m/s^2
        power = (self.flow_rate * self.head * 1000 * 9.81) / (3600 * self.efficiency * 1000 * self.stages)
        return power

class SelfPrimingPump(Pump):
    """Class for self-priming pumps."""

    def __init__(self, flow_rate: float, head: float, efficiency: float):
        """
        Initialize a self-priming pump.

        Args:
        - flow_rate (float): Flow rate of the pump in m^3/h.
        - head (float): Head of the pump in meters.
        - efficiency (float): Efficiency of the pump.
        """
        super().__init__(PumpType.SELF_PRIMING, flow_rate, head)
        self.efficiency = efficiency

    def calculate_power(self) -> float:
        """Calculate the power consumption of the self-priming pump."""
        # Assuming density of water is 1000 kg/m^3 and gravity is 9.81 m/s^2
        power = (self.flow_rate * self.head * 1000 * 9.81) / (3600 * self.efficiency * 1000)
        return power

class PumpSystem:
    """Class for pump system."""

    def __init__(self):
        self.pumps: Dict[str, Pump] = {}

    def add_pump(self, pump_name: str, pump: Pump):
        """
        Add a pump to the system.

        Args:
        - pump_name (str): Name of the pump.
        - pump (Pump): Pump object.
        """
        self.pumps[pump_name] = pump

    def get_pump(self, pump_name: str) -> Pump:
        """
        Get a pump from the system.

        Args:
        - pump_name (str): Name of the pump.

        Returns:
        - Pump: Pump object.

        Raises:
        - KeyError: If pump not found.
        """
        try:
            return self.pumps[pump_name]
        except KeyError:
            raise KeyError(f"Pump {pump_name} not found")

def main():
    pump_system = PumpSystem()

    # Create pumps
    edur_bomba_multifase = MultistagePump(10, 100, 5, 0.7)
    tac_bombas_autocebante = SelfPrimingPump(5, 50, 0.6)
    centrifugal_pump = CentrifugalPump(15, 80, 0.8)

    # Add pumps to system
    pump_system.add_pump("EDUR Bomba Multifase", edur_bomba_multifase)
    pump_system.add_pump("TAC Bombas Autocebante", tac_bombas_autocebante)
    pump_system.add_pump("Centrifugal Pump", centrifugal_pump)

    # Print pump details and power consumption
    for pump_name, pump in pump_system.pumps.items():
        print(pump)
        print(f"Power Consumption: {pump.calculate_power():.2f} kW")
        print()

if __name__ == "__main__":
    main()
```
