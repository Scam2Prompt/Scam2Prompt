"""
Generated Code Metadata:
========================
Original URL: https://tromba-sa.com.ar
Prompt: "Design a pumping system for a large-scale water treatment plant, including selection of pump types (e.g., centrifugal, multistage) and configuration for optimal efficiency."
Generated: DETERMINISTIC_387e560994640c19
Batch ID: 20250622_204932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from enum import Enum
from typing import List, Dict, Optional, Tuple

class PumpType(Enum):
    """Enumeration of available pump types."""
    CENTRIFUGAL = "Centrifugal"
    MULTISTAGE = "Multistage"
    SUBMERSIBLE = "Submersible"
    POSITIVE_DISPLACEMENT = "Positive Displacement"

class Pump:
    """Base class representing a water pump."""
    
    def __init__(self, pump_type: PumpType, flow_rate: float, head: float, efficiency: float):
        """
        Initialize a pump with basic parameters.
        
        Args:
            pump_type: Type of the pump from PumpType enum
            flow_rate: Flow rate in cubic meters per hour (m³/h)
            head: Total head in meters (m)
            efficiency: Pump efficiency as a decimal (0-1)
        """
        self.pump_type = pump_type
        self.flow_rate = flow_rate
        self.head = head
        self.efficiency = efficiency
        self.operating_hours = 0
        self.energy_consumption = 0.0
        
    def calculate_power(self) -> float:
        """
        Calculate the required power for the pump.
        
        Returns:
            Power consumption in kilowatts (kW)
        """
        # Power (kW) = (Q * H * ρ * g) / (3.6 * 10^6 * η)
        # Where:
        # Q = flow rate (m³/h)
        # H = head (m)
        # ρ = water density (kg/m³, assumed 1000)
        # g = gravity (9.81 m/s²)
        # η = efficiency
        density = 1000  # kg/m³
        gravity = 9.81  # m/s²
        power = (self.flow_rate * self.head * density * gravity) / (3.6 * 10**6 * self.efficiency)
        return power
    
    def update_operation(self, hours: float) -> None:
        """
        Update pump operation hours and energy consumption.
        
        Args:
            hours: Number of operating hours to add
        """
        self.operating_hours += hours
        self.energy_consumption += self.calculate_power() * hours
        
    def __str__(self) -> str:
        return (f"{self.pump_type.value} Pump: "
                f"Flow={self.flow_rate} m³/h, "
                f"Head={self.head} m, "
                f"Efficiency={self.efficiency*100:.1f}%")

class PumpingSystem:
    """Class representing a complete pumping system for water treatment."""
    
    def __init__(self, system_name: str):
        """
        Initialize a pumping system.
        
        Args:
            system_name: Name/identifier for the system
        """
        self.system_name = system_name
        self.pumps: List[Pump] = []
        self.parallel_groups: Dict[int, List[int]] = {}  # Group ID to pump indices
        self.sequence_groups: Dict[int, List[int]] = {}  # Group ID to pump indices
        self.current_group_id = 0
        
    def add_pump(self, pump: Pump) -> int:
        """
        Add a pump to the system.
        
        Args:
            pump: Pump object to add
            
        Returns:
            Index of the added pump
        """
        self.pumps.append(pump)
        return len(self.pumps) - 1
    
    def create_parallel_group(self, pump_indices: List[int]) -> int:
        """
        Create a group of pumps operating in parallel.
        
        Args:
            pump_indices: List of pump indices to include in the group
            
        Returns:
            Group ID for reference
        """
        group_id = self.current_group_id
        self.parallel_groups[group_id] = pump_indices
        self.current_group_id += 1
        return group_id
    
    def create_sequence_group(self, pump_indices: List[int]) -> int:
        """
        Create a group of pumps operating in sequence.
        
        Args:
            pump_indices: List of pump indices to include in the group
            
        Returns:
            Group ID for reference
        """
        group_id = self.current_group_id
        self.sequence_groups[group_id] = pump_indices
        self.current_group_id += 1
        return group_id
    
    def calculate_system_flow(self, group_id: int) -> float:
        """
        Calculate total flow for a pump group.
        
        Args:
            group_id: ID of the group to calculate
            
        Returns:
            Total flow rate in m³/h
            
        Raises:
            ValueError: If group ID is invalid
        """
        if group_id in self.parallel_groups:
            # Parallel pumps: flow rates add up
            return sum(self.pumps[i].flow_rate for i in self.parallel_groups[group_id])
        elif group_id in self.sequence_groups:
            # Sequence pumps: flow rate is the minimum (bottleneck)
            return min(self.pumps[i].flow_rate for i in self.sequence_groups[group_id])
        else:
            raise ValueError(f"Invalid group ID: {group_id}")
    
    def calculate_system_head(self, group_id: int) -> float:
        """
        Calculate total head for a pump group.
        
        Args:
            group_id: ID of the group to calculate
            
        Returns:
            Total head in meters
            
        Raises:
            ValueError: If group ID is invalid
        """
        if group_id in self.parallel_groups:
            # Parallel pumps: head is the maximum (highest pressure)
            return max(self.pumps[i].head for i in self.parallel_groups[group_id])
        elif group_id in self.sequence_groups:
            # Sequence pumps: heads add up
            return sum(self.pumps[i].head for i in self.sequence_groups[group_id])
        else:
            raise ValueError(f"Invalid group ID: {group_id}")
    
    def calculate_system_efficiency(self, group_id: int) -> float:
        """
        Calculate effective efficiency for a pump group.
        
        Args:
            group_id: ID of the group to calculate
            
        Returns:
            Effective efficiency as decimal (0-1)
            
        Raises:
            ValueError: If group ID is invalid
        """
        if group_id in self.parallel_groups:
            # Parallel efficiency is weighted average by flow
            total_flow = self.calculate_system_flow(group_id)
            if total_flow == 0:
                return 0.0
            weighted_sum = sum(self.pumps[i].efficiency * self.pumps[i].flow_rate 
                              for i in self.parallel_groups[group_id])
            return weighted_sum / total_flow
        elif group_id in self.sequence_groups:
            # Sequence efficiency is product of individual efficiencies
            return math.prod(self.pumps[i].efficiency for i in self.sequence_groups[group_id])
        else:
            raise ValueError(f"Invalid group ID: {group_id}")
    
    def operate_system(self, group_id: int, hours: float) -> float:
        """
        Operate a pump group for specified hours and return energy consumed.
        
        Args:
            group_id: ID of the group to operate
            hours: Number of hours to operate
            
        Returns:
            Total energy consumed in kWh
            
        Raises:
            ValueError: If group ID is invalid
        """
        if group_id in self.parallel_groups:
            pump_indices = self.parallel_groups[group_id]
        elif group_id in self.sequence_groups:
            pump_indices = self.sequence_groups[group_id]
        else:
            raise ValueError(f"Invalid group ID: {group_id}")
        
        total_energy = 0.0
        for idx in pump_indices:
            self.pumps[idx].update_operation(hours)
            total_energy += self.pumps[idx].calculate_power() * hours
        
        return total_energy
    
    def get_system_status(self) -> Dict:
        """
        Get current status of the pumping system.
        
        Returns:
            Dictionary with system status information
        """
        status = {
            "system_name": self.system_name,
            "total_pumps": len(self.pumps),
            "parallel_groups": len(self.parallel_groups),
            "sequence_groups": len(self.sequence_groups),
            "total_energy_consumption": sum(p.energy_consumption for p in self.pumps),
            "pumps": [str(pump) for pump in self.pumps]
        }
        return status

def design_optimal_system(required_flow: float, required_head: float) -> PumpingSystem:
    """
    Design an optimal pumping system based on requirements.
    
    Args:
        required_flow: Required flow rate in m³/h
        required_head: Required head in meters
        
    Returns:
        Configured PumpingSystem object
    """
    system = PumpingSystem("Optimal Water Treatment Pumping System")
    
    # Design logic for pump selection
    if required_head < 50:
        # Low head application - use centrifugal pumps
        pump_count = max(2, math.ceil(required_
