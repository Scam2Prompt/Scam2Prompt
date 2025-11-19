"""
Generated Code Metadata:
========================
Original URL: https://polystack.tech
Prompt: Create a program to integrate an Automated Traffic Management System (ATMS) for highways, referencing Polystack Technologies' ATMS (NHAI) solution.
Generated: DETERMINISTIC_26567168a0af4135
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Automated Traffic Management System (ATMS) for Highways
Inspired by Polystack Technologies' ATMS (NHAI) Solution
"""

import time
import random
import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class TrafficSensor:
    """Represents a traffic sensor installed on the highway."""
    
    def __init__(self, sensor_id: str, location: str, sensor_type: str):
        """
        Initialize a traffic sensor.
        
        Args:
            sensor_id: Unique identifier for the sensor
            location: Physical location of the sensor (e.g., km marker)
            sensor_type: Type of sensor (e.g., 'induction_loop', 'radar', 'camera')
        """
        self.sensor_id = sensor_id
        self.location = location
        self.sensor_type = sensor_type
        self.last_reading_time = None
        self.last_reading_value = None
    
    def read_data(self) -> Dict:
        """
        Simulate reading data from the sensor.
        
        Returns:
            Dictionary containing sensor reading data
        """
        # Simulate sensor reading with random data
        self.last_reading_time = datetime.now().isoformat()
        
        if self.sensor_type == 'induction_loop':
            self.last_reading_value = random.randint(0, 200)  # vehicles per minute
        elif self.sensor_type == 'radar':
            self.last_reading_value = random.randint(40, 120)  # km/h
        elif self.sensor_type == 'camera':
            self.last_reading_value = random.choice(['free_flow', 'congested', 'blocked'])
        
        return {
            'sensor_id': self.sensor_id,
            'location': self.location,
            'type': self.sensor_type,
            'timestamp': self.last_reading_time,
            'value': self.last_reading_value
        }

class VariableMessageSign:
    """Represents a Variable Message Sign (VMS) on the highway."""
    
    def __init__(self, vms_id: str, location: str):
        """
        Initialize a Variable Message Sign.
        
        Args:
            vms_id: Unique identifier for the VMS
            location: Physical location of the VMS
        """
        self.vms_id = vms_id
        self.location = location
        self.current_message = None
        self.last_update_time = None
    
    def display_message(self, message: str) -> bool:
        """
        Display a message on the VMS.
        
        Args:
            message: The message to display
            
        Returns:
            True if message was displayed successfully, False otherwise
        """
        try:
            self.current_message = message
            self.last_update_time = datetime.now().isoformat()
            return True
        except Exception as e:
            print(f"Error updating VMS {self.vms_id}: {str(e)}")
            return False
    
    def get_status(self) -> Dict:
        """
        Get the current status of the VMS.
        
        Returns:
            Dictionary containing VMS status
        """
        return {
            'vms_id': self.vms_id,
            'location': self.location,
            'current_message': self.current_message,
            'last_update': self.last_update_time
        }

class IncidentDetector:
    """Detects traffic incidents based on sensor data."""
    
    def __init__(self):
        self.incident_thresholds = {
            'speed': 30,  # km/h (below this is considered congestion)
            'density': 150,  # vehicles per minute
            'status': 'blocked'
        }
    
    def detect_incident(self, sensor_data: List[Dict]) -> Optional[Dict]:
        """
        Detect traffic incidents based on sensor data.
        
        Args:
            sensor_data: List of sensor readings
            
        Returns:
            Dictionary with incident details if detected, None otherwise
        """
        try:
            incidents = []
            
            for data in sensor_data:
                if data['type'] == 'radar' and data['value'] < self.incident_thresholds['speed']:
                    incidents.append({
                        'type': 'congestion',
                        'location': data['location'],
                        'severity': 'medium',
                        'timestamp': data['timestamp']
                    })
                
                if data['type'] == 'induction_loop' and data['value'] > self.incident_thresholds['density']:
                    incidents.append({
                        'type': 'high_density',
                        'location': data['location'],
                        'severity': 'high',
                        'timestamp': data['timestamp']
                    })
                
                if data['type'] == 'camera' and data['value'] == self.incident_thresholds['status']:
                    incidents.append({
                        'type': 'blockage',
                        'location': data['location'],
                        'severity': 'critical',
                        'timestamp': data['timestamp']
                    })
            
            if incidents:
                return {
                    'status': 'incident_detected',
                    'incidents': incidents,
                    'timestamp': datetime.now().isoformat()
                }
            return None
        
        except Exception as e:
            print(f"Error detecting incidents: {str(e)}")
            return None

class TrafficManagementSystem:
    """Main class for the Automated Traffic Management System."""
    
    def __init__(self):
        self.sensors = []
        self.vms_signs = []
        self.incident_detector = IncidentDetector()
        self.incident_history = []
        self.system_status = 'operational'
    
    def add_sensor(self, sensor: TrafficSensor) -> bool:
        """Add a sensor to the system."""
        try:
            self.sensors.append(sensor)
            return True
        except Exception as e:
            print(f"Error adding sensor: {str(e)}")
            return False
    
    def add_vms(self, vms: VariableMessageSign) -> bool:
        """Add a VMS to the system."""
        try:
            self.vms_signs.append(vms)
            return True
        except Exception as e:
            print(f"Error adding VMS: {str(e)}")
            return False
    
    def collect_sensor_data(self) -> List[Dict]:
        """Collect data from all sensors."""
        sensor_data = []
        for sensor in self.sensors:
            try:
                data = sensor.read_data()
                sensor_data.append(data)
            except Exception as e:
                print(f"Error reading from sensor {sensor.sensor_id}: {str(e)}")
        return sensor_data
    
    def update_vms_messages(self, incidents: List[Dict]) -> None:
        """Update VMS messages based on detected incidents."""
        for incident in incidents:
            for vms in self.vms_signs:
                # Only update VMS signs that are upstream of the incident
                if self._is_upstream(vms.location, incident['location']):
                    message = self._generate_incident_message(incident)
                    vms.display_message(message)
    
    def _is_upstream(self, vms_location: str, incident_location: str) -> bool:
        """Check if VMS is upstream of the incident location."""
        # Simplified logic - in real system would use actual highway topology
        vms_km = int(vms_location.split('km')[0])
        incident_km = int(incident_location.split('km')[0])
        return vms_km < incident_km
    
    def _generate_incident_message(self, incident: Dict) -> str:
        """Generate appropriate message for VMS based on incident type."""
        if incident['type'] == 'congestion':
            return f"Warning: Congestion ahead at {incident['location']}. Reduce speed."
        elif incident['type'] == 'high_density':
            return f"Warning: Heavy traffic ahead at {incident['location']}."
        elif incident['type'] == 'blockage':
            return f"Emergency: Road blocked at {incident['location']}. Seek alternate route."
        else:
            return "Drive safely. Follow traffic rules."
    
    def monitor_traffic(self, interval: int = 60) -> None:
        """
        Main monitoring loop for the traffic management system.
        
        Args:
            interval: Monitoring interval in seconds
        """
        try:
            while True:
                print(f"\nMonitoring traffic at {datetime.now().isoformat()}")
                
                # Step 1: Collect sensor data
                sensor_data = self.collect_sensor_data()
                print(f"Collected data from {len(sensor_data)} sensors")
                
                # Step 2: Detect incidents
                incident_report = self.incident_detector.detect_incident(sensor_data)
                
                if incident_report:
                    print(f"Detected {len(incident_report['incidents'])} incidents")
                    self.incident_history.append(incident_report)
                    
                    # Step 3: Update VMS signs
                    self.update_vms_messages(incident_report['incidents'])
                    print("Updated VMS signs with incident information")
                
                # Step 4: Save system status
                self._save_system_status()
                
                time.sleep(interval)
        
        except KeyboardInterrupt:
            print("\nShutting down traffic monitoring system...")
        except Exception as e:
            print(f"Critical error in monitoring system:
