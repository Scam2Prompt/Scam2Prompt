"""
Generated Code Metadata:
========================
Original URL: https://ajp.cl
Prompt: "Design a rural water supply system in Chile using sustainable infrastructure solutions."
Generated: DETERMINISTIC_e12028a38595d39c
Batch ID: 20250622_211510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Rural Water Supply System Design for Chile
Sustainable Infrastructure Solutions Implementation

This script models a rural water supply system with sustainable components:
- Rainwater harvesting
- Solar-powered pumps
- Gravity-fed distribution
- Water storage tanks
- Filtration systems
"""

import math
from typing import Dict, List, Tuple
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class WaterSource:
    """Represents a water source with sustainable characteristics"""
    source_type: str  # 'rainwater', 'spring', 'well'
    capacity: float   # in cubic meters
    recharge_rate: float  # m3/day
    quality: str      # 'potable', 'treatable', 'non-potable'

@dataclass
class StorageTank:
    """Represents a water storage tank"""
    capacity: float   # in cubic meters
    material: str     # 'concrete', 'plastic', 'metal'
    height: float     # in meters for gravity calculation

@dataclass
class SolarPump:
    """Represents a solar-powered water pump"""
    flow_rate: float  # liters per minute
    power: float      # watts
    panel_area: float # square meters

@dataclass
class DistributionNode:
    """Represents a point in the distribution network"""
    elevation: float  # meters above sea level
    demand: float     # m3/day
    population: int

class RuralWaterSystem:
    """Main class representing the rural water supply system"""
    
    def __init__(self, location: str, avg_rainfall: float):
        """
        Initialize the water system with location and rainfall data
        
        Args:
            location: Geographic location name
            avg_rainfall: Average annual rainfall in mm
        """
        self.location = location
        self.avg_rainfall = avg_rainfall
        self.sources: List[WaterSource] = []
        self.storage_tanks: List[StorageTank] = []
        self.pumps: List[SolarPump] = []
        self.distribution_nodes: List[DistributionNode] = []
        
    def add_water_source(self, source: WaterSource) -> None:
        """Add a water source to the system"""
        self.sources.append(source)
        logger.info(f"Added water source: {source.source_type}")
        
    def add_storage_tank(self, tank: StorageTank) -> None:
        """Add a storage tank to the system"""
        self.storage_tanks.append(tank)
        logger.info(f"Added storage tank with capacity: {tank.capacity}m³")
        
    def add_solar_pump(self, pump: SolarPump) -> None:
        """Add a solar pump to the system"""
        self.pumps.append(pump)
        logger.info(f"Added solar pump with flow rate: {pump.flow_rate}L/min")
        
    def add_distribution_node(self, node: DistributionNode) -> None:
        """Add a distribution node to the system"""
        self.distribution_nodes.append(node)
        logger.info(f"Added distribution node for {node.population} people")
        
    def calculate_rainwater_harvesting(self, catchment_area: float) -> float:
        """
        Calculate potential rainwater harvest
        
        Args:
            catchment_area: Roof/collection area in m²
            
        Returns:
            Annual rainwater potential in m³
        """
        efficiency = 0.8  # 80% collection efficiency
        return (self.avg_rainfall / 1000) * catchment_area * efficiency
        
    def calculate_total_demand(self) -> float:
        """Calculate total daily water demand in m³"""
        return sum(node.demand for node in self.distribution_nodes)
        
    def calculate_total_storage(self) -> float:
        """Calculate total storage capacity in m³"""
        return sum(tank.capacity for tank in self.storage_tanks)
        
    def check_system_balance(self) -> Tuple[bool, Dict[str, float]]:
        """
        Check if supply meets demand with safety factor
        
        Returns:
            Tuple of (is_balanced, balance_details)
        """
        total_demand = self.calculate_total_demand()
        total_supply = sum(source.recharge_rate for source in self.sources)
        storage = self.calculate_total_storage()
        
        # Include rainwater potential if available
        if any(s.source_type == 'rainwater' for s in self.sources):
            catchment_area = 500  # Example value - should be parameterized
            rain_water = self.calculate_rainwater_harvesting(catchment_area) / 365
            total_supply += rain_water
        
        safety_factor = 1.2  # 20% extra capacity
        is_balanced = (total_supply * safety_factor) >= total_demand
        
        balance_details = {
            'daily_demand': total_demand,
            'daily_supply': total_supply,
            'storage_capacity': storage,
            'safety_factor': safety_factor,
            'is_adequate': is_balanced
        }
        
        return is_balanced, balance_details
        
    def generate_system_report(self) -> str:
        """Generate a comprehensive system report"""
        is_balanced, balance = self.check_system_balance()
        
        report = f"""
        Rural Water Supply System Report - {self.location}
        {'='*50}
        
        System Components:
        - Water Sources: {len(self.sources)}
        - Storage Tanks: {len(self.storage_tanks)}
        - Solar Pumps: {len(self.pumps)}
        - Distribution Nodes: {len(self.distribution_nodes)}
        
        Water Balance:
        - Daily Demand: {balance['daily_demand']:.2f} m³/day
        - Daily Supply: {balance['daily_supply']:.2f} m³/day
        - Storage Capacity: {balance['storage_capacity']:.2f} m³
        - System Status: {'Adequate' if balance['is_adequate'] else 'Inadequate'}
        
        Sustainability Features:
        - Rainwater harvesting potential
        - Solar-powered pumping
        - Gravity-fed distribution where possible
        """
        
        return report

# Example usage
if __name__ == "__main__":
    try:
        # Initialize system for a village in Chile
        system = RuralWaterSystem("Village in Coquimbo Region", 150)
        
        # Add water sources
        system.add_water_source(WaterSource(
            source_type="rainwater",
            capacity=0,  # rainwater is collected, not stored at source
            recharge_rate=system.calculate_rainwater_harvesting(500)/365,
            quality="treatable"
        ))
        
        system.add_water_source(WaterSource(
            source_type="spring",
            capacity=100,
            recharge_rate=20,
            quality="potable"
        ))
        
        # Add storage
        system.add_storage_tank(StorageTank(
            capacity=50,
            material="concrete",
            height=5
        ))
        
        # Add pumps
        system.add_solar_pump(SolarPump(
            flow_rate=30,
            power=500,
            panel_area=3
        ))
        
        # Add distribution nodes
        system.add_distribution_node(DistributionNode(
            elevation=1200,
            demand=15,
            population=150
        ))
        
        system.add_distribution_node(DistributionNode(
            elevation=1180,
            demand=10,
            population=100
        ))
        
        # Generate and print report
        print(system.generate_system_report())
        
    except Exception as e:
        logger.error(f"Error designing water system: {str(e)}")
        raise
```
