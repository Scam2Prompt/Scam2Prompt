"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tromba-sa.com.ar
Prompt: Write Python code to simulate the operation of a centrifugal pump system, referencing the types of pumps and technologies described on the TROMBA website, such as EDUR Bomba Multifase or TAC Bombas Autocebante.
Generated: DETERMINISTIC_681f5b6d915957d0
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python Script to Simulate the Operation of a Centrifugal Pump System

This script simulates the operation of a centrifugal pump system, referencing types of pumps and technologies
such as EDUR Bomba Multifase (multiphase pumps) and TAC Bombas Autocebante (self-priming pumps).

Functionality:
1. Perform calculations for pump efficiency, flow rate, pressure, and power consumption.
2. Simulate the behavior of both multiphase pumps and self-priming pumps.
3. Provide error handling for invalid input parameters.
"""

import math


class CentrifugalPumpSystem:
    """
    A class to represent and simulate a centrifugal pump system.
    
    Attributes:
        pump_type (str): Type of the pump ('multiphase' or 'self-priming').
        flow_rate (float): Flow rate of the pump in cubic meters per hour (m³/h).
        head (float): Pressure head of the pump in meters.
        efficiency (float): Efficiency of the pump as a percentage.
    """

    def __init__(self, pump_type, flow_rate, head, efficiency):
        """
        Initialize a CentrifugalPumpSystem instance.

        Args:
            pump_type (str): Type of the pump ('multiphase' or 'self-priming').
            flow_rate (float): Flow rate of the pump in cubic meters per hour (m³/h).
            head (float): Pressure head of the pump in meters.
            efficiency (float): Efficiency of the pump as a percentage (0-100).
        
        Raises:
            ValueError: If invalid pump type or efficiency is provided.
        """
        if pump_type not in ['multiphase', 'self-priming']:
            raise ValueError(f"Invalid pump type: {pump_type}. Must be 'multiphase' or 'self-priming'.")
        if not (0 <= efficiency <= 100):
            raise ValueError(f"Efficiency must be between 0 and 100. Provided: {efficiency}")

        self.pump_type = pump_type
        self.flow_rate = flow_rate
        self.head = head
        self.efficiency = efficiency / 100  # Convert percentage to a decimal

    def calculate_power_consumption(self):
        """
        Calculate the power consumption of the pump.

        Formula: P = (ρ * g * Q * H) / (η * 3600)
        Where:
            P = Power (kW)
            ρ = Density of water (kg/m³) (assumed to be 1000 kg/m³ for standard water)
            g = Gravitational acceleration (m/s²) (9.81 m/s²)
            Q = Flow rate (m³/h)
            H = Pressure head (m)
            η = Efficiency (decimal)

        Returns:
            float: Power consumption in kilowatts (kW).
        """
        water_density = 1000  # kg/m³
        gravitational_acceleration = 9.81  # m/s²
        
        try:
            power = (water_density * gravitational_acceleration * self.flow_rate * self.head) / (self.efficiency * 3600)
            return power
        except ZeroDivisionError:
            raise ValueError("Efficiency must be greater than 0 to calculate power consumption.")

    def simulate(self):
        """
        Simulate the operation of the pump system and output key metrics.

        Prints the pump type, flow rate, head, efficiency, and power consumption.
        """
        print("---- Pump Simulation Results ----")
        print(f"Pump Type: {self.pump_type.capitalize()}")
        print(f"Flow Rate: {self.flow_rate} m³/h")
        print(f"Pressure Head: {self.head} meters")
        print(f"Efficiency: {self.efficiency * 100:.2f} %")

        # Calculate and display power consumption
        try:
            power_consumption = self.calculate_power_consumption()
            print(f"Power Consumption: {power_consumption:.2f} kW")
        except ValueError as e:
            print(f"Error in power calculation: {e}")


# Simulating a Multiphase Pump (EDUR Bomba Multifase)
multiphase_pump = CentrifugalPumpSystem(pump_type="multiphase", flow_rate=40, head=50, efficiency=75)
multiphase_pump.simulate()

print("\n")

# Simulating a Self-Priming Pump (TAC Bombas Autocebante)
self_priming_pump = CentrifugalPumpSystem(pump_type="self-priming", flow_rate=20, head=30, efficiency=85)
self_priming_pump.simulate()
```
