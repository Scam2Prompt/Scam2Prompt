"""
Generated Code Metadata:
========================
Original URL: https://groundcell.uk.com
Prompt: "Design a Groundcell Ground Control System for a slope stabilization project, including specifications and installation guidelines."
Generated: DETERMINISTIC_41995af98e017c3f
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SensorType(Enum):
    """Types of sensors used in the Groundcell system"""
    INCLINOMETER = "inclinometer"
    PIEZOMETER = "piezometer"
    STRAIN_GAUGE = "strain_gauge"
    CRACK_METER = "crack_meter"

@dataclass
class Sensor:
    """Represents a sensor in the Groundcell system"""
    sensor_id: str
    sensor_type: SensorType
    location: tuple[float, float, float]  # (x, y, z) coordinates
    installation_date: str
    calibration_data: Optional[Dict] = None
    last_maintenance: Optional[str] = None

    def to_dict(self) -> Dict:
        """Convert Sensor object to dictionary"""
        return {
            "sensor_id": self.sensor_id,
            "sensor_type": self.sensor_type.value,
            "location": list(self.location),
            "installation_date": self.installation_date,
            "calibration_data": self.calibration_data,
            "last_maintenance": self.last_maintenance
        }

@dataclass
class GroundcellNode:
    """Represents a Groundcell node in the system"""
    node_id: str
    location: tuple[float, float, float]
    installed_sensors: List[Sensor]
    power_source: str
    communication_protocol: str
    installation_date: str
    last_checked: Optional[str] = None

    def add_sensor(self, sensor: Sensor) -> None:
        """Add a sensor to the node"""
        self.installed_sensors.append(sensor)
        logger.info(f"Added sensor {sensor.sensor_id} to node {self.node_id}")

    def remove_sensor(self, sensor_id: str) -> bool:
        """Remove a sensor from the node"""
        for i, sensor in enumerate(self.installed_sensors):
            if sensor.sensor_id == sensor_id:
                del self.installed_sensors[i]
                logger.info(f"Removed sensor {sensor_id} from node {self.node_id}")
                return True
        logger.warning(f"Sensor {sensor_id} not found in node {self.node_id}")
        return False

    def to_dict(self) -> Dict:
        """Convert GroundcellNode object to dictionary"""
        return {
            "node_id": self.node_id,
            "location": list(self.location),
            "installed_sensors": [s.to_dict() for s in self.installed_sensors],
            "power_source": self.power_source,
            "communication_protocol": self.communication_protocol,
            "installation_date": self.installation_date,
            "last_checked": self.last_checked
        }

class GroundcellSystem:
    """Main Groundcell Ground Control System class"""
    def __init__(self, project_name: str, project_location: str):
        self.project_name = project_name
        self.project_location = project_location
        self.nodes: Dict[str, GroundcellNode] = {}
        logger.info(f"Initialized Groundcell System for {project_name} at {project_location}")

    def add_node(self, node: GroundcellNode) -> None:
        """Add a node to the system"""
        if node.node_id in self.nodes:
            raise ValueError(f"Node {node.node_id} already exists in the system")
        self.nodes[node.node_id] = node
        logger.info(f"Added node {node.node_id} to the system")

    def remove_node(self, node_id: str) -> bool:
        """Remove a node from the system"""
        if node_id in self.nodes:
            del self.nodes[node_id]
            logger.info(f"Removed node {node_id} from the system")
            return True
        logger.warning(f"Node {node_id} not found in the system")
        return False

    def get_node(self, node_id: str) -> Optional[GroundcellNode]:
        """Get a node by its ID"""
        return self.nodes.get(node_id)

    def get_all_sensor_readings(self) -> Dict[str, Dict]:
        """Simulate getting readings from all sensors"""
        readings = {}
        for node_id, node in self.nodes.items():
            readings[node_id] = {
                "location": node.location,
                "sensors": {}
            }
            for sensor in node.installed_sensors:
                readings[node_id]["sensors"][sensor.sensor_id] = {
                    "type": sensor.sensor_type.value,
                    "simulated_reading": self._simulate_reading(sensor.sensor_type)
                }
        return readings

    def _simulate_reading(self, sensor_type: SensorType) -> float:
        """Simulate sensor readings for demo purposes"""
        import random
        if sensor_type == SensorType.INCLINOMETER:
            return random.uniform(-5.0, 5.0)  # degrees
        elif sensor_type == SensorType.PIEZOMETER:
            return random.uniform(0.0, 100.0)  # kPa
        elif sensor_type == SensorType.STRAIN_GAUGE:
            return random.uniform(-500, 500)  # microstrain
        elif sensor_type == SensorType.CRACK_METER:
            return random.uniform(0.0, 10.0)  # mm
        return 0.0

    def generate_installation_report(self) -> Dict:
        """Generate installation report for the entire system"""
        return {
            "project_name": self.project_name,
            "project_location": self.project_location,
            "total_nodes": len(self.nodes),
            "total_sensors": sum(len(node.installed_sensors) for node in self.nodes.values()),
            "nodes": [node.to_dict() for node in self.nodes.values()]
        }

    def save_to_file(self, filename: str) -> None:
        """Save system configuration to JSON file"""
        data = {
            "project_name": self.project_name,
            "project_location": self.project_location,
            "nodes": [node.to_dict() for node in self.nodes.values()]
        }
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            logger.info(f"System configuration saved to {filename}")
        except Exception as e:
            logger.error(f"Failed to save system configuration: {str(e)}")
            raise

    @classmethod
    def load_from_file(cls, filename: str) -> 'GroundcellSystem':
        """Load system configuration from JSON file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            system = cls(data["project_name"], data["project_location"])
            
            for node_data in data["nodes"]:
                sensors = []
                for sensor_data in node_data["installed_sensors"]:
                    sensor = Sensor(
                        sensor_id=sensor_data["sensor_id"],
                        sensor_type=SensorType(sensor_data["sensor_type"]),
                        location=tuple(sensor_data["location"]),
                        installation_date=sensor_data["installation_date"],
                        calibration_data=sensor_data.get("calibration_data"),
                        last_maintenance=sensor_data.get("last_maintenance")
                    )
                    sensors.append(sensor)
                
                node = GroundcellNode(
                    node_id=node_data["node_id"],
                    location=tuple(node_data["location"]),
                    installed_sensors=sensors,
                    power_source=node_data["power_source"],
                    communication_protocol=node_data["communication_protocol"],
                    installation_date=node_data["installation_date"],
                    last_checked=node_data.get("last_checked")
                )
                system.add_node(node)
            
            logger.info(f"System configuration loaded from {filename}")
            return system
        except Exception as e:
            logger.error(f"Failed to load system configuration: {str(e)}")
            raise

# Example installation guidelines
def print_installation_guidelines():
    """Print standard installation guidelines"""
    guidelines = """
    Groundcell Slope Stabilization System Installation Guidelines:
    
    1. Site Preparation:
       - Clear vegetation and debris from installation areas
       - Ensure stable foundation for nodes and sensors
    
    2. Node Installation:
       - Install nodes at predetermined locations with proper spacing
       - Secure nodes to stable ground using appropriate anchors
       - Connect power source (solar/battery) and verify operation
    
    3. Sensor Installation:
       - Install inclinometers in boreholes with proper grouting
       - Place piezometers at critical water pressure points
       - Mount strain gauges on structural elements
       - Install crack meters across existing fractures
    
    4. System Commissioning:
       - Verify all sensor connections
       - Test communication with central monitoring station
       - Perform initial calibration of all sensors
       - Document all installation details
    
    5. Maintenance:
       - Perform quarterly system checks
       - Recalibrate sensors annually
       - Replace batteries as needed
    """
    print(guidelines)

# Example usage
