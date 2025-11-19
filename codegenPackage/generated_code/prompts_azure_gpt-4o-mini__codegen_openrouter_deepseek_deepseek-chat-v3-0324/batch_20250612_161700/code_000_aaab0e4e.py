"""
Generated Code Metadata:
========================
Original URL: https://ingeostar.com
Prompt: Generate a Python script to perform precise GNSS surveys for engineering projects, incorporating techniques for topographic and geodetic measurements as described on IngeoStar's website.
Generated: DETERMINISTIC_aaab0e4e456a1069
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GNSS Survey Script for Engineering Projects

This script performs precise GNSS surveys for topographic and geodetic measurements.
It incorporates techniques described on IngeoStar's website for high-precision positioning.

Features:
- RTK and PPK survey methods
- Coordinate transformation
- Data quality checks
- Survey logging
"""

import sys
import time
import math
import logging
from datetime import datetime
from typing import Tuple, List, Dict, Optional
import json
import socket
import serial
import numpy as np
from pyproj import CRS, Transformer

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('gnss_survey.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('GNSS_Survey')

class GNSSReceiver:
    """Class to interface with GNSS receiver hardware"""
    
    def __init__(self, port: str, baudrate: int = 115200):
        """
        Initialize GNSS receiver connection
        
        Args:
            port: Serial port name (e.g., '/dev/ttyUSB0')
            baudrate: Communication baud rate
        """
        self.port = port
        self.baudrate = baudrate
        self.connection = None
        
    def connect(self) -> bool:
        """Establish connection to GNSS receiver"""
        try:
            self.connection = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=2
            )
            logger.info(f"Connected to GNSS receiver on {self.port}")
            return True
        except serial.SerialException as e:
            logger.error(f"Failed to connect to GNSS receiver: {e}")
            return False
            
    def disconnect(self):
        """Close connection to GNSS receiver"""
        if self.connection and self.connection.is_open:
            self.connection.close()
            logger.info("Disconnected from GNSS receiver")
            
    def get_position(self) -> Optional[Dict]:
        """
        Get current position from GNSS receiver
        
        Returns:
            Dictionary with position data or None if error
        """
        if not self.connection or not self.connection.is_open:
            logger.error("No connection to GNSS receiver")
            return None
            
        try:
            # Send command to request position (example for NMEA)
            self.connection.write(b'$GPGGA\r\n')
            response = self.connection.readline().decode('ascii', errors='ignore')
            
            if response.startswith('$GPGGA'):
                parts = response.split(',')
                if len(parts) >= 10:
                    return {
                        'timestamp': parts[1],
                        'latitude': self._nmea_to_decimal(parts[2], parts[3]),
                        'longitude': self._nmea_to_decimal(parts[4], parts[5]),
                        'quality': int(parts[6]),
                        'satellites': int(parts[7]),
                        'hdop': float(parts[8]),
                        'altitude': float(parts[9]),
                        'units': parts[10]
                    }
            return None
        except Exception as e:
            logger.error(f"Error getting position: {e}")
            return None
            
    def _nmea_to_decimal(self, value: str, direction: str) -> float:
        """Convert NMEA coordinate to decimal degrees"""
        try:
            degrees = float(value[:2]) if len(value) > 2 else float(value[:1])
            minutes = float(value[2:])
            decimal = degrees + (minutes / 60.0)
            if direction in ['S', 'W']:
                decimal *= -1
            return decimal
        except (ValueError, IndexError):
            logger.error("Invalid NMEA coordinate format")
            return 0.0

class CoordinateTransformer:
    """Class for coordinate transformations between reference systems"""
    
    def __init__(self, source_crs: str = 'EPSG:4326', target_crs: str = 'EPSG:32633'):
        """
        Initialize coordinate transformer
        
        Args:
            source_crs: Source coordinate reference system (default: WGS84)
            target_crs: Target coordinate reference system (default: UTM zone 33N)
        """
        self.source_crs = CRS.from_string(source_crs)
        self.target_crs = CRS.from_string(target_crs)
        self.transformer = Transformer.from_crs(self.source_crs, self.target_crs)
        
    def transform(self, lat: float, lon: float, alt: float = 0.0) -> Tuple[float, float, float]:
        """
        Transform coordinates from source to target CRS
        
        Args:
            lat: Latitude in degrees
            lon: Longitude in degrees
            alt: Altitude in meters
            
        Returns:
            Tuple of (easting, northing, elevation) in target CRS
        """
        try:
            easting, northing, elevation = self.transformer.transform(lon, lat, alt)
            return easting, northing, elevation
        except Exception as e:
            logger.error(f"Coordinate transformation failed: {e}")
            return (0.0, 0.0, 0.0)

class GNSSSurvey:
    """Main class for performing GNSS surveys"""
    
    def __init__(self, config_file: str = 'config.json'):
        """
        Initialize GNSS survey system
        
        Args:
            config_file: Path to configuration file
        """
        self.config = self._load_config(config_file)
        self.receiver = GNSSReceiver(
            port=self.config.get('port', '/dev/ttyUSB0'),
            baudrate=self.config.get('baudrate', 115200)
        )
        self.transformer = CoordinateTransformer(
            source_crs=self.config.get('source_crs', 'EPSG:4326'),
            target_crs=self.config.get('target_crs', 'EPSG:32633')
        )
        self.measurements = []
        
    def _load_config(self, config_file: str) -> Dict:
        """Load configuration from JSON file"""
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logger.warning(f"Failed to load config file: {e}. Using defaults.")
            return {}
            
    def connect_receiver(self) -> bool:
        """Connect to GNSS receiver"""
        return self.receiver.connect()
        
    def disconnect_receiver(self):
        """Disconnect from GNSS receiver"""
        self.receiver.disconnect()
        
    def perform_measurement(self, point_name: str, duration: int = 30) -> bool:
        """
        Perform a single measurement at a point
        
        Args:
            point_name: Identifier for the measurement point
            duration: Measurement duration in seconds
            
        Returns:
            True if measurement was successful, False otherwise
        """
        logger.info(f"Starting measurement for point {point_name}")
        
        # Collect measurements over specified duration
        measurements = []
        start_time = time.time()
        
        while time.time() - start_time < duration:
            position = self.receiver.get_position()
            if position and position['quality'] >= self.config.get('min_quality', 4):
                measurements.append(position)
                time.sleep(1)
                
        if not measurements:
            logger.error(f"No valid measurements for point {point_name}")
            return False
            
        # Calculate average position
        avg_lat = np.mean([m['latitude'] for m in measurements])
        avg_lon = np.mean([m['longitude'] for m in measurements])
        avg_alt = np.mean([m['altitude'] for m in measurements])
        
        # Transform coordinates
        easting, northing, elevation = self.transformer.transform(avg_lat, avg_lon, avg_alt)
        
        # Calculate precision metrics
        std_lat = np.std([m['latitude'] for m in measurements])
        std_lon = np.std([m['longitude'] for m in measurements])
        std_alt = np.std([m['altitude'] for m in measurements])
        
        # Store measurement
        measurement = {
            'point_name': point_name,
            'timestamp': datetime.utcnow().isoformat(),
            'latitude': avg_lat,
            'longitude': avg_lon,
            'altitude': avg_alt,
            'easting': easting,
            'northing': northing,
            'elevation': elevation,
            'std_latitude': std_lat,
            'std_longitude': std_lon,
            'std_altitude': std_alt,
            'satellites': np.mean([m['satellites'] for m in measurements]),
            'hdop': np.mean([m['hdop'] for m in measurements]),
            'measurement_duration': duration,
            'num_measurements': len(measurements)
        }
        
        self.measurements.append(measurement)
        logger.info(f"Completed measurement for point {point_name}")
        return True
        
    def save_measurements(self, output_file: str = '
