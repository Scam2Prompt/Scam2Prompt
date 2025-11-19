"""
Generated Code Metadata:
========================
Original URL: https://espinelycia.com
Prompt: Create a Python script to model the integration of fire protection systems into existing hydraulic networks, referencing Espinel y Cia's construction services.
Generated: DETERMINISTIC_2a70dc09af1b8c03
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Fire Protection System Integration into Hydraulic Networks
Modeling tool for integrating fire protection systems into existing hydraulic networks.
References Espinel y Cia's construction services standards.
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Optional
from enum import Enum
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PipeMaterial(Enum):
    """Enum for pipe materials and their roughness coefficients (Hazen-Williams)"""
    PVC = 150
    STEEL = 120
    COPPER = 140
    DUCTILE_IRON = 130
    CONCRETE = 110

class FireProtectionStandard(Enum):
    """Fire protection standards based on Espinel y Cia's construction services"""
    NFPA_13 = "NFPA 13: Standard for the Installation of Sprinkler Systems"
    NFPA_14 = "NFPA 14: Standard for the Installation of Standpipe and Hose Systems"
    LOCAL_REGULATIONS = "Local Building Codes"

class HydraulicNetwork:
    """Class representing an existing hydraulic network"""
    
    def __init__(self, name: str, pipe_material: PipeMaterial, pipe_diameter: float, 
                 pipe_length: float, existing_flow: float, existing_pressure: float):
        """
        Initialize hydraulic network parameters
        
        Args:
            name: Network identifier
            pipe_material: Material of pipes in network
            pipe_diameter: Diameter of pipes (mm)
            pipe_length: Total length of pipe network (m)
            existing_flow: Current flow rate (L/s)
            existing_pressure: Current pressure at critical point (kPa)
        """
        self.name = name
        self.pipe_material = pipe_material
        self.pipe_diameter = pipe_diameter
        self.pipe_length = pipe_length
        self.existing_flow = existing_flow
        self.existing_pressure = existing_pressure
        self.nodes = []
        self.junctions = []
        
    def add_node(self, node_type: str, elevation: float, demand: float = 0) -> None:
        """Add a node to the network"""
        self.nodes.append({
            'type': node_type,
            'elevation': elevation,
            'demand': demand
        })
        
    def calculate_pressure_loss(self, flow: float) -> float:
        """
        Calculate pressure loss using Hazen-Williams equation
        
        Args:
            flow: Flow rate in L/s
            
        Returns:
            Pressure loss in kPa
        """
        try:
            C = self.pipe_material.value
            D = self.pipe_diameter / 1000  # Convert to meters
            L = self.pipe_length
            Q = flow / 1000  # Convert to m3/s
            
            # Hazen-Williams equation (metric units)
            hf = (10.67 * (Q ** 1.852) * L) / ((C ** 1.852) * (D ** 4.871))
            
            # Convert head loss (m) to pressure loss (kPa)
            pressure_loss = hf * 9.81  # 9.81 kPa/m
            
            return pressure_loss
        except Exception as e:
            logger.error(f"Error calculating pressure loss: {e}")
            raise

class FireProtectionSystem:
    """Class representing a fire protection system to be integrated"""
    
    def __init__(self, standard: FireProtectionStandard, required_flow: float, 
                 required_pressure: float, num_sprinklers: int = 0, 
                 num_hydrants: int = 0):
        """
        Initialize fire protection system parameters
        
        Args:
            standard: Applicable fire protection standard
            required_flow: Required flow rate (L/s)
            required_pressure: Required pressure at critical point (kPa)
            num_sprinklers: Number of sprinklers
            num_hydrants: Number of hydrants
        """
        self.standard = standard
        self.required_flow = required_flow
        self.required_pressure = required_pressure
        self.num_sprinklers = num_sprinklers
        self.num_hydrants = num_hydrants
        
    def calculate_demand(self) -> float:
        """Calculate total water demand based on system components"""
        sprinkler_demand = self.num_sprinklers * 0.1  # 0.1 L/s per sprinkler
        hydrant_demand = self.num_hydrants * 5.0  # 5.0 L/s per hydrant
        return sprinkler_demand + hydrant_demand + self.required_flow

class SystemIntegrator:
    """Class to handle integration of fire protection into hydraulic networks"""
    
    def __init__(self, network: HydraulicNetwork, fire_system: FireProtectionSystem):
        self.network = network
        self.fire_system = fire_system
        
    def check_compatibility(self) -> Tuple[bool, str]:
        """
        Check if the existing network can support the fire protection system
        
        Returns:
            Tuple of (is_compatible, message)
        """
        try:
            # Calculate total demand
            total_demand = self.network.existing_flow + self.fire_system.calculate_demand()
            
            # Calculate pressure loss with new flow
            pressure_loss = self.network.calculate_pressure_loss(total_demand)
            
            # Calculate available pressure
            available_pressure = self.network.existing_pressure - pressure_loss
            
            # Check requirements
            if total_demand > self.network.existing_flow * 2:
                return (False, "Flow demand exceeds network capacity")
                
            if available_pressure < self.fire_system.required_pressure:
                return (False, f"Insufficient pressure. Available: {available_pressure:.2f} kPa, Required: {self.fire_system.required_pressure} kPa")
                
            return (True, "System is compatible")
            
        except Exception as e:
            logger.error(f"Error checking system compatibility: {e}")
            raise
            
    def generate_upgrade_report(self) -> Dict:
        """Generate a report of required upgrades for successful integration"""
        report = {
            'existing_network': self.network.name,
            'fire_standard': self.fire_system.standard.value,
            'current_flow': self.network.existing_flow,
            'required_flow': self.fire_system.calculate_demand(),
            'current_pressure': self.network.existing_pressure,
            'required_pressure': self.fire_system.required_pressure
        }
        
        is_compatible, message = self.check_compatibility()
        report['compatibility'] = is_compatible
        report['message'] = message
        
        if not is_compatible:
            report['recommendations'] = self._generate_recommendations()
            
        return report
        
    def _generate_recommendations(self) -> List[str]:
        """Generate recommendations for system upgrades"""
        recommendations = []
        
        # Calculate needed values
        total_demand = self.fire_system.calculate_demand() + self.network.existing_flow
        pressure_loss = self.network.calculate_pressure_loss(total_demand)
        available_pressure = self.network.existing_pressure - pressure_loss
        pressure_deficit = self.fire_system.required_pressure - available_pressure
        
        # Flow recommendations
        if total_demand > self.network.existing_flow * 1.5:
            recommendations.append(
                f"Increase pipe diameter from {self.network.pipe_diameter}mm to "
                f"{self.network.pipe_diameter * 1.5:.0f}mm to accommodate higher flow"
            )
            
        # Pressure recommendations
        if pressure_deficit > 0:
            recommendations.append(
                f"Install booster pump with minimum {pressure_deficit:.2f} kPa capacity"
            )
            
        # Material recommendations
        if self.network.pipe_material.value < PipeMaterial.STEEL.value:
            recommendations.append(
                f"Consider upgrading pipe material from {self.network.pipe_material.name} "
                f"to STEEL for better fire protection performance"
            )
            
        return recommendations

def main():
    """Example usage of the system integration tool"""
    try:
        # Create existing hydraulic network
        existing_network = HydraulicNetwork(
            name="Building A Water Supply",
            pipe_material=PipeMaterial.PVC,
            pipe_diameter=150,  # mm
            pipe_length=200,    # m
            existing_flow=10,   # L/s
            existing_pressure=400  # kPa
        )
        
        # Add some nodes
        existing_network.add_node("supply", elevation=0)
        existing_network.add_node("junction", elevation=5, demand=5)
        existing_network.add_node("endpoint", elevation=10, demand=5)
        
        # Create fire protection system
        fire_system = FireProtectionSystem(
            standard=FireProtectionStandard.NFPA_13,
            required_flow=25,  # L/s
