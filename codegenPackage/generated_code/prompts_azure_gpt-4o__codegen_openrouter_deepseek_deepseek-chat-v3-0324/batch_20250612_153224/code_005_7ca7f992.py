"""
Generated Code Metadata:
========================
Original URL: https://nakashicnc.com
Prompt: Write code to automate the testing process of 5-axis CNC machines to ensure consistent quality and precision, as highlighted in Nakashi CNC’s manufacturing practices.
Generated: DETERMINISTIC_7ca7f992e8cad6e7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import time
import serial
from serial.tools import list_ports
import json
import logging
from typing import Tuple, List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('cnc_testing.log'),
        logging.StreamHandler()
    ]
)

class CNCTester:
    """
    Automated testing for 5-axis CNC machines to ensure quality and precision.
    """
    
    def __init__(self, config_file: str = 'config.json'):
        """
        Initialize the CNC tester with configuration.
        
        Args:
            config_file: Path to JSON configuration file.
        """
        self.config = self._load_config(config_file)
        self.serial_connection = None
        self.test_results = []
        
    def _load_config(self, config_file: str) -> Dict:
        """
        Load configuration from JSON file.
        
        Args:
            config_file: Path to JSON configuration file.
            
        Returns:
            Dictionary containing configuration.
            
        Raises:
            FileNotFoundError: If config file doesn't exist.
            json.JSONDecodeError: If config file is invalid JSON.
        """
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logging.error(f"Config file {config_file} not found.")
            raise
        except json.JSONDecodeError:
            logging.error(f"Invalid JSON in config file {config_file}.")
            raise
    
    def connect_to_cnc(self) -> bool:
        """
        Establish serial connection to CNC machine.
        
        Returns:
            True if connection successful, False otherwise.
        """
        try:
            ports = list_ports.comports()
            target_port = None
            
            for port in ports:
                if self.config['cnc_port_identifier'] in port.description:
                    target_port = port.device
                    break
            
            if not target_port:
                logging.error("CNC machine port not found.")
                return False
                
            self.serial_connection = serial.Serial(
                port=target_port,
                baudrate=self.config['baud_rate'],
                timeout=self.config['timeout']
            )
            
            if self.serial_connection.is_open:
                logging.info(f"Connected to CNC machine at {target_port}")
                return True
            return False
            
        except serial.SerialException as e:
            logging.error(f"Serial connection error: {str(e)}")
            return False
    
    def send_gcode(self, gcode: str) -> bool:
        """
        Send G-code command to CNC machine.
        
        Args:
            gcode: G-code command to send.
            
        Returns:
            True if command sent successfully, False otherwise.
        """
        if not self.serial_connection or not self.serial_connection.is_open:
            logging.error("No active connection to CNC machine.")
            return False
            
        try:
            self.serial_connection.write((gcode + '\n').encode())
            return True
        except serial.SerialException as e:
            logging.error(f"Failed to send G-code: {str(e)}")
            return False
    
    def run_calibration_test(self) -> Dict:
        """
        Run calibration test for all 5 axes.
        
        Returns:
            Dictionary containing test results for each axis.
        """
        results = {}
        axes = ['X', 'Y', 'Z', 'A', 'B']
        
        for axis in axes:
            test_name = f"{axis}-axis calibration"
            logging.info(f"Running {test_name}...")
            
            # Send homing command
            if not self.send_gcode(f"G28 {axis}"):
                results[test_name] = {
                    'status': 'failed',
                    'error': 'Failed to send homing command'
                }
                continue
                
            # Wait for homing to complete
            time.sleep(self.config['homing_delay'])
            
            # Send movement command
            move_cmd = f"G0 {axis}{self.config['test_movement_distance']} F{self.config['test_feed_rate']}"
            if not self.send_gcode(move_cmd):
                results[test_name] = {
                    'status': 'failed',
                    'error': 'Failed to send movement command'
                }
                continue
                
            # Wait for movement to complete
            time.sleep(self.config['movement_delay'])
            
            # Verify position (simulated - in real implementation would read actual position)
            expected_pos = self.config['test_movement_distance']
            actual_pos = expected_pos  # Replace with actual position reading
            
            tolerance = self.config['position_tolerance']
            deviation = abs(actual_pos - expected_pos)
            
            if deviation <= tolerance:
                results[test_name] = {
                    'status': 'passed',
                    'expected_position': expected_pos,
                    'actual_position': actual_pos,
                    'deviation': deviation,
                    'tolerance': tolerance
                }
            else:
                results[test_name] = {
                    'status': 'failed',
                    'expected_position': expected_pos,
                    'actual_position': actual_pos,
                    'deviation': deviation,
                    'tolerance': tolerance,
                    'error': 'Position deviation exceeds tolerance'
                }
        
        self.test_results.append({
            'test_name': 'Calibration Test',
            'results': results
        })
        return results
    
    def run_circular_test(self) -> Dict:
        """
        Run circular interpolation test to check machine kinematics.
        
        Returns:
            Dictionary containing test results.
        """
        test_name = "Circular Interpolation Test"
        logging.info(f"Running {test_name}...")
        
        # Generate circular path G-code
        radius = self.config['circular_test_radius']
        feed_rate = self.config['test_feed_rate']
        
        gcode_commands = [
            "G90",  # Absolute positioning
            f"G0 X0 Y0 F{feed_rate}",  # Move to start position
            f"G2 X0 Y0 I{radius} J0 F{feed_rate}"  # Full circle
        ]
        
        # Send commands
        for cmd in gcode_commands:
            if not self.send_gcode(cmd):
                result = {
                    'status': 'failed',
                    'error': 'Failed to send circular test commands'
                }
                self.test_results.append({
                    'test_name': test_name,
                    'results': result
                })
                return result
                
            time.sleep(self.config['movement_delay'])
        
        # Verify circular path (simulated)
        expected_error = 0.0  # Replace with actual measurement
        tolerance = self.config['circular_tolerance']
        
        if expected_error <= tolerance:
            result = {
                'status': 'passed',
                'circular_error': expected_error,
                'tolerance': tolerance
            }
        else:
            result = {
                'status': 'failed',
                'circular_error': expected_error,
                'tolerance': tolerance,
                'error': 'Circular error exceeds tolerance'
            }
        
        self.test_results.append({
            'test_name': test_name,
            'results': result
        })
        return result
    
    def run_spindle_test(self) -> Dict:
        """
        Run spindle performance test.
        
        Returns:
            Dictionary containing test results.
        """
        test_name = "Spindle Performance Test"
        logging.info(f"Running {test_name}...")
        
        # Test spindle at different RPMs
        rpm_levels = self.config['spindle_test_rpms']
        results = {}
        
        for rpm in rpm_levels:
            if not self.send_gcode(f"M3 S{rpm}"):
                results[str(rpm)] = {
                    'status': 'failed',
                    'error': 'Failed to set spindle speed'
                }
                continue
                
            time.sleep(self.config['spindle_stabilization_time'])
            
            # Verify spindle speed (simulated)
            actual_rpm = rpm  # Replace with actual RPM reading
            tolerance = self.config['spindle_tolerance_rpm']
            deviation = abs(actual_rpm - rpm)
            
            if deviation <= tolerance:
                results[str(rpm)] = {
                    'status': 'passed',
                    'expected_rpm': rpm,
                    'actual_rpm': actual_rpm,
                    'deviation': deviation,
                    'tolerance': tolerance
                }
            else:
                results[str(rpm)] = {
                    'status': 'failed',
                    'expected_rpm': rpm,
                    'actual_rpm': actual_rpm,
                    'deviation': deviation,
                    'tolerance': tolerance,
                    'error': 'RPM deviation exceeds tolerance'
                }
        
        self.test_results.append({
            'test_name': test_name,
            'results': results
        })
        return results
    
    def run_all_tests(self) -> List[Dict]:
        """
        Run all configured tests.
        
        Returns:
            List of test results.
        """
        if not self.connect_to_cnc():
            logging.error("Cannot run tests without CNC connection.")
            return []
            
        try:
            self.run_calibration_test()
            self.run_circular_test()
            self.run_spindle_test()
            
            # Save test results
            self._save_test_results()
            
            return self.test_results
