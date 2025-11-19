"""
Generated Code Metadata:
========================
Original URL: https://acousticmusicsandiego.com
Prompt: Write a tutorial on how to utilize the "Generous" submersible's hardware and software system for deep-sea ecological research, referencing the recent findings from the Mariana Trench.
Generated: DETERMINISTIC_9caf7c673a6f29e5
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Generous Submersible Control System for Deep-Sea Ecological Research

This script provides an interface to control and utilize the 'Generous' submersible's
hardware and software system for deep-sea research, with specific functionality
for ecological studies in extreme environments like the Mariana Trench.

Features include:
- Sensor data collection and processing
- Navigation control
- Sample collection management
- Data logging and analysis
- Emergency protocols
"""

import time
import json
import logging
from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple
import numpy as np
from scipy import signal
import serial
import requests

# Constants based on Mariana Trench research findings
MAX_DEPTH = 11000  # meters (Challenger Deep depth)
PRESSURE_LIMIT = 1100  # atm
TEMPERATURE_RANGE = (1.0, 4.0)  # °C (Mariana Trench typical range)
SALINITY_RANGE = (34.5, 35.0)  # PSU (Mariana Trench typical range)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='generous_submersible.log'
)
logger = logging.getLogger(__name__)

@dataclass
class SensorData:
    """Class to hold sensor readings from the submersible"""
    depth: float
    temperature: float
    pressure: float
    salinity: float
    oxygen: float
    ph: float
    turbidity: float
    timestamp: float = time.time()

class GenerousSubmersible:
    """Main class for controlling the Generous submersible"""
    
    def __init__(self, port: str = '/dev/ttyUSB0', baudrate: int = 115200):
        """
        Initialize the submersible control system.
        
        Args:
            port: Serial port for hardware communication
            baudrate: Baud rate for serial communication
        """
        self.port = port
        self.baudrate = baudrate
        self.serial_conn = None
        self.current_depth = 0.0
        self.is_sampling = False
        self.samples_collected = 0
        self.sensor_data = []
        self.mission_parameters = {}
        
        # Initialize emergency protocols
        self.emergency_protocols = {
            'pressure_exceeded': False,
            'temperature_exceeded': False,
            'power_low': False,
            'communication_lost': False
        }
        
        logger.info("Generous Submersible initialized")

    def connect(self) -> bool:
        """Establish connection with submersible hardware"""
        try:
            self.serial_conn = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=1
            )
            logger.info(f"Connected to submersible on {self.port}")
            return True
        except serial.SerialException as e:
            logger.error(f"Connection failed: {str(e)}")
            return False

    def disconnect(self) -> None:
        """Close connection with submersible hardware"""
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()
            logger.info("Disconnected from submersible")

    def set_mission_parameters(self, params: Dict) -> None:
        """
        Configure mission parameters for ecological research.
        
        Args:
            params: Dictionary containing mission parameters
                   (depth_target, sampling_rate, navigation_waypoints, etc.)
        """
        self.mission_parameters = params
        logger.info(f"Mission parameters set: {params}")

    def read_sensors(self) -> Optional[SensorData]:
        """
        Read all sensor data from the submersible.
        
        Returns:
            SensorData object if successful, None otherwise
        """
        if not self.serial_conn or not self.serial_conn.is_open:
            logger.warning("Cannot read sensors - not connected")
            return None
            
        try:
            # Send command to request sensor data
            self.serial_conn.write(b'GET_SENSORS\n')
            response = self.serial_conn.readline().decode('utf-8').strip()
            
            if not response:
                logger.warning("No response from sensors")
                return None
                
            # Parse sensor data (example format: "depth:100.5,temp:3.2,...")
            sensor_values = {}
            for pair in response.split(','):
                key, value = pair.split(':')
                sensor_values[key] = float(value)
                
            data = SensorData(
                depth=sensor_values.get('depth', 0.0),
                temperature=sensor_values.get('temp', 0.0),
                pressure=sensor_values.get('pressure', 0.0),
                salinity=sensor_values.get('salinity', 0.0),
                oxygen=sensor_values.get('oxygen', 0.0),
                ph=sensor_values.get('ph', 0.0),
                turbidity=sensor_values.get('turbidity', 0.0)
            )
            
            # Check for emergency conditions
            self._check_emergency_conditions(data)
            
            self.sensor_data.append(data)
            self.current_depth = data.depth
            return data
            
        except Exception as e:
            logger.error(f"Error reading sensors: {str(e)}")
            return None

    def _check_emergency_conditions(self, data: SensorData) -> None:
        """Check sensor data against safety limits and trigger emergency protocols if needed"""
        if data.pressure > PRESSURE_LIMIT:
            self.emergency_protocols['pressure_exceeded'] = True
            logger.critical("Emergency: Pressure limit exceeded!")
            self._activate_emergency_protocol('pressure_exceeded')
            
        if data.temperature < TEMPERATURE_RANGE[0] or data.temperature > TEMPERATURE_RANGE[1]:
            self.emergency_protocols['temperature_exceeded'] = True
            logger.critical("Emergency: Temperature out of range!")
            self._activate_emergency_protocol('temperature_exceeded')

    def _activate_emergency_protocol(self, protocol: str) -> None:
        """Execute emergency protocol based on detected issue"""
        if protocol == 'pressure_exceeded':
            self.ascend(rate=0.5)  # Slow ascent to prevent damage
        elif protocol == 'temperature_exceeded':
            self.adjust_insulation()
            
        # In a real implementation, would trigger alarms and notify surface team

    def adjust_insulation(self) -> None:
        """Adjust thermal insulation based on temperature readings"""
        # Implementation would vary based on hardware capabilities
        logger.info("Adjusting thermal insulation")

    def navigate_to(self, depth: float, latitude: float, longitude: float) -> bool:
        """
        Navigate to specified coordinates at target depth.
        
        Args:
            depth: Target depth in meters
            latitude: Target latitude
            longitude: Target longitude
            
        Returns:
            True if command was sent successfully, False otherwise
        """
        if depth > MAX_DEPTH:
            logger.error(f"Cannot navigate below maximum depth of {MAX_DEPTH}m")
            return False
            
        command = f"NAVIGATE {depth} {latitude} {longitude}\n"
        try:
            self.serial_conn.write(command.encode('utf-8'))
            logger.info(f"Navigation command sent: {command.strip()}")
            return True
        except Exception as e:
            logger.error(f"Navigation command failed: {str(e)}")
            return False

    def ascend(self, rate: float = 0.3) -> bool:
        """
        Command the submersible to ascend at specified rate.
        
        Args:
            rate: Ascent rate in meters/second (default 0.3 m/s)
            
        Returns:
            True if command was sent successfully, False otherwise
        """
        command = f"ASCEND {rate}\n"
        try:
            self.serial_conn.write(command.encode('utf-8'))
            logger.info(f"Ascend command sent: {command.strip()}")
            return True
        except Exception as e:
            logger.error(f"Ascend command failed: {str(e)}")
            return False

    def descend(self, rate: float = 0.3) -> bool:
        """
        Command the submersible to descend at specified rate.
        
        Args:
            rate: Descent rate in meters/second (default 0.3 m/s)
            
        Returns:
            True if command was sent successfully, False otherwise
        """
        command = f"DESCEND {rate}\n"
        try:
            self.serial_conn.write(command.encode('utf-8'))
            logger.info(f"Descend command sent: {command.strip()}")
            return True
        except Exception as e:
            logger.error(f"Descend command failed: {str(e)}")
            return False

    def collect_sample(self, sample_type: str = "water") -> bool:
        """
        Collect an environmental sample.
        
        Args:
            sample_type: Type
