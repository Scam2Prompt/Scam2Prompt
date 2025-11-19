"""
Generated Code Metadata:
========================
Original URL: https://technicalpower.us
Prompt: Generate a script to perform infrared scans for detecting hot spots in electrical connections, incorporating vibration, torque, and corrosion checks as outlined by Technical Power Service, Inc.
Generated: DETERMINISTIC_3af46ba2065f5825
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import cv2
import numpy as np
import pandas as pd
import time
from datetime import datetime
import os
import json
from scipy import signal
import serial
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class ElectricalConnectionScanner:
    """
    A class to perform infrared scans for detecting hot spots in electrical connections,
    incorporating vibration, torque, and corrosion checks.
    """
    
    def __init__(self, config_file='config.json'):
        """
        Initialize the scanner with configuration settings.
        
        Args:
            config_file (str): Path to the configuration file.
        """
        self.config = self._load_config(config_file)
        self.camera = None
        self.serial_conn = None
        self.data_log = []
        self.setup()
        
    def _load_config(self, config_file):
        """
        Load configuration from a JSON file.
        
        Args:
            config_file (str): Path to the configuration file.
            
        Returns:
            dict: Configuration settings.
        """
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file {config_file} not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in configuration file {config_file}.")
    
    def setup(self):
        """
        Set up the camera and serial connections.
        """
        # Initialize thermal camera
        try:
            self.camera = cv2.VideoCapture(self.config['camera_index'])
            if not self.camera.isOpened():
                raise RuntimeError("Failed to initialize thermal camera.")
        except Exception as e:
            raise RuntimeError(f"Camera initialization error: {str(e)}")
        
        # Initialize serial connection for sensors
        try:
            self.serial_conn = serial.Serial(
                port=self.config['serial_port'],
                baudrate=self.config['baud_rate'],
                timeout=self.config['serial_timeout']
            )
        except Exception as e:
            raise RuntimeError(f"Serial connection error: {str(e)}")
    
    def capture_thermal_image(self):
        """
        Capture a thermal image from the camera.
        
        Returns:
            numpy.ndarray: Thermal image as a NumPy array.
        """
        ret, frame = self.camera.read()
        if not ret:
            raise RuntimeError("Failed to capture thermal image.")
        return frame
    
    def read_sensor_data(self):
        """
        Read vibration, torque, and corrosion data from sensors.
        
        Returns:
            dict: Sensor readings.
        """
        try:
            # Send command to request sensor data
            self.serial_conn.write(b'GET_DATA\n')
            
            # Read response
            response = self.serial_conn.readline().decode('utf-8').strip()
            
            # Parse response (assuming format: "vibration,torque,corrosion")
            parts = response.split(',')
            if len(parts) != 3:
                raise ValueError("Invalid sensor data format.")
                
            return {
                'vibration': float(parts[0]),
                'torque': float(parts[1]),
                'corrosion': float(parts[2])
            }
        except Exception as e:
            raise RuntimeError(f"Sensor read error: {str(e)}")
    
    def detect_hotspots(self, thermal_image):
        """
        Detect hotspots in a thermal image.
        
        Args:
            thermal_image (numpy.ndarray): Thermal image to analyze.
            
        Returns:
            list: List of detected hotspots (x, y, temperature).
        """
        try:
            # Convert to grayscale
            gray = cv2.cvtColor(thermal_image, cv2.COLOR_BGR2GRAY)
            
            # Apply threshold to find hot regions
            _, thresholded = cv2.threshold(gray, self.config['temperature_threshold'], 255, cv2.THRESH_BINARY)
            
            # Find contours
            contours, _ = cv2.findContours(thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            
            hotspots = []
            for contour in contours:
                if cv2.contourArea(contour) > self.config['min_hotspot_area']:
                    M = cv2.moments(contour)
                    if M['m00'] != 0:
                        cx = int(M['m10'] / M['m00'])
                        cy = int(M['m01'] / M['m00'])
                        # Get temperature at centroid (simplified)
                        temperature = gray[cy, cx]
                        hotspots.append((cx, cy, temperature))
            
            return hotspots
        except Exception as e:
            raise RuntimeError(f"Hotspot detection error: {str(e)}")
    
    def analyze_vibration(self, vibration_data):
        """
        Analyze vibration data for abnormalities.
        
        Args:
            vibration_data (float): Vibration reading.
            
        Returns:
            bool: True if vibration is abnormal, False otherwise.
        """
        return vibration_data > self.config['vibration_threshold']
    
    def analyze_torque(self, torque_data):
        """
        Analyze torque data for abnormalities.
        
        Args:
            torque_data (float): Torque reading.
            
        Returns:
            bool: True if torque is abnormal, False otherwise.
        """
        return torque_data < self.config['torque_min'] or torque_data > self.config['torque_max']
    
    def analyze_corrosion(self, corrosion_data):
        """
        Analyze corrosion data for abnormalities.
        
        Args:
            corrosion_data (float): Corrosion reading.
            
        Returns:
            bool: True if corrosion is abnormal, False otherwise.
        """
        return corrosion_data > self.config['corrosion_threshold']
    
    def log_data(self, timestamp, hotspots, sensor_data, abnormalities):
        """
        Log scan data to memory and optionally to disk.
        
        Args:
            timestamp (str): Timestamp of the scan.
            hotspots (list): Detected hotspots.
            sensor_data (dict): Sensor readings.
            abnormalities (dict): Detected abnormalities.
        """
        log_entry = {
            'timestamp': timestamp,
            'hotspots': hotspots,
            'sensor_data': sensor_data,
            'abnormalities': abnormalities
        }
        self.data_log.append(log_entry)
        
        # Save to CSV if configured
        if self.config.get('log_to_csv', False):
            self._save_to_csv(log_entry)
    
    def _save_to_csv(self, log_entry):
        """
        Save log entry to a CSV file.
        
        Args:
            log_entry (dict): Data to log.
        """
        csv_file = self.config.get('csv_log_file', 'scan_log.csv')
        df = pd.DataFrame([{
            'timestamp': log_entry['timestamp'],
            'hotspot_count': len(log_entry['hotspots']),
            'vibration': log_entry['sensor_data']['vibration'],
            'torque': log_entry['sensor_data']['torque'],
            'corrosion': log_entry['sensor_data']['corrosion'],
            'vibration_abnormal': log_entry['abnormalities']['vibration'],
            'torque_abnormal': log_entry['abnormalities']['torque'],
            'corrosion_abnormal': log_entry['abnormalities']['corrosion']
        }])
        
        if not os.path.exists(csv_file):
            df.to_csv(csv_file, index=False)
        else:
            df.to_csv(csv_file, mode='a', header=False, index=False)
    
    def perform_scan(self):
        """
        Perform a complete scan including thermal imaging and sensor checks.
        
        Returns:
            dict: Scan results.
        """
        timestamp = datetime.now().isoformat()
        
        try:
            # Capture thermal image
            thermal_image = self.capture_thermal_image()
            
            # Detect hotspots
            hotspots = self.detect_hotspots(thermal_image)
            
            # Read sensor data
            sensor_data = self.read_sensor_data()
            
            # Analyze sensor data
            abnormalities = {
                'vibration': self.analyze_vibration(sensor_data['vibration']),
                'torque': self.analyze_torque(sensor_data['torque']),
                'corrosion': self.analyze_corrosion(sensor_data['corrosion'])
            }
            
            # Log data
            self.log_data(timestamp, hotspots, sensor_data, abnormalities)
            
            return {
                'status': 'success',
                'timestamp': timestamp,
                'hotspots': hotspots,
                'sensor_data': sensor_data,
                'abnormalities': abnormalities
            }
        except Exception as e:
            return {
                'status': 'error',
                'timestamp': timestamp,
                'error': str(e)
            }
    
    def cleanup(self):
        """
        Clean up resources (camera and serial connections).
        """
        if self.camera and self.camera.isOpened():
            self.camera.release()
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()

def main():
    """
    Main function to run the electrical connection scanner.
    """
    try:
        scanner = ElectricalConnectionScanner()
        
        # Perform continuous scans
        while True:
            result = scanner.perform_scan()
            print(f"Scan at {result['timestamp']}:")
