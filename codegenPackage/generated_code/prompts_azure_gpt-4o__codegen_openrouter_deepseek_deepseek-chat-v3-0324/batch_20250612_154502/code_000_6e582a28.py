"""
Generated Code Metadata:
========================
Original URL: https://loghouses-woodcraft.com
Prompt: Write Python code to calculate the flow rate for a QS15-52 water pump based on specifications provided by industrial equipment manufacturers.
Generated: DETERMINISTIC_6e582a28a4b0f2bd
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class QS1552PumpFlowRateCalculator:
    """
    A class to calculate the flow rate of a QS15-52 water pump based on manufacturer specifications.
    
    Attributes:
        pump_head (float): The pump head in meters (m).
        pump_power (float): The pump power in kilowatts (kW).
        efficiency (float): The pump efficiency as a decimal (0 to 1).
        gravity (float): Acceleration due to gravity in m/s² (default: 9.81).
    """
    
    def __init__(self, pump_head: float, pump_power: float, efficiency: float = 0.75):
        """
        Initialize the QS15-52 pump flow rate calculator with required parameters.
        
        Args:
            pump_head (float): Pump head in meters (m).
            pump_power (float): Pump power in kilowatts (kW).
            efficiency (float, optional): Pump efficiency (0 to 1). Defaults to 0.75.
            
        Raises:
            ValueError: If any input parameter is invalid.
        """
        if pump_head <= 0:
            raise ValueError("Pump head must be a positive number.")
        if pump_power <= 0:
            raise ValueError("Pump power must be a positive number.")
        if not (0 < efficiency <= 1):
            raise ValueError("Efficiency must be between 0 and 1.")
            
        self.pump_head = pump_head
        self.pump_power = pump_power
        self.efficiency = efficiency
        self.gravity = 9.81  # m/s²
    
    def calculate_flow_rate(self, water_density: float = 1000) -> float:
        """
        Calculate the flow rate of the pump in cubic meters per second (m³/s).
        
        Formula: Q = (P * η) / (ρ * g * H)
        Where:
            Q = Flow rate (m³/s)
            P = Power (W)
            η = Efficiency
            ρ = Water density (kg/m³)
            g = Gravity (m/s²)
            H = Head (m)
            
        Args:
            water_density (float, optional): Density of water in kg/m³. Defaults to 1000.
            
        Returns:
            float: Flow rate in m³/s.
            
        Raises:
            ValueError: If water density is not positive.
        """
        if water_density <= 0:
            raise ValueError("Water density must be a positive number.")
            
        # Convert power from kW to W
        power_watts = self.pump_power * 1000
        
        # Calculate flow rate
        flow_rate = (power_watts * self.efficiency) / (water_density * self.gravity * self.pump_head)
        
        return flow_rate
    
    def flow_rate_in_liters_per_minute(self) -> float:
        """
        Calculate the flow rate in liters per minute (L/min).
        
        Returns:
            float: Flow rate in L/min.
        """
        flow_rate_m3s = self.calculate_flow_rate()
        return flow_rate_m3s * 60000  # Convert m³/s to L/min (1 m³ = 1000 L, 1 min = 60 s)
    
    def flow_rate_in_gallons_per_minute(self) -> float:
        """
        Calculate the flow rate in gallons per minute (GPM).
        
        Returns:
            float: Flow rate in GPM.
        """
        flow_rate_m3s = self.calculate_flow_rate()
        return flow_rate_m3s * 15850.3  # Convert m³/s to GPM (1 m³ = 264.172 gallons, 1 min = 60 s)
```
