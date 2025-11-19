"""
Generated Code Metadata:
========================
Original URL: https://nakashicnc.com
Prompt: Generate a Python script to control a 5-axis CNC machine for engraving precision parts in the automotive and medical sectors, incorporating energy-efficient practices.
Generated: DETERMINISTIC_dd8ec5612c4ac3fd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import serial
import logging
from typing import Tuple, List, Optional
from enum import Enum, auto

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('cnc_controller.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class Axis(Enum):
    """Enumeration for CNC machine axes"""
    X = auto()
    Y = auto()
    Z = auto()
    A = auto()
    B = auto()

class CNCController:
    """
    Controller for a 5-axis CNC machine with energy-efficient features.
    Designed for precision engraving in automotive and medical sectors.
    """
    
    def __init__(self, port: str, baudrate: int = 115200, timeout: float = 1.0):
        """
        Initialize the CNC controller.
        
        Args:
            port: Serial port to connect to the CNC machine
            baudrate: Communication baud rate
            timeout: Serial connection timeout in seconds
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_conn = None
        self.is_connected = False
        self.current_position = {axis: 0.0 for axis in Axis}
        self.energy_saving_mode = False
        self.spindle_on = False
        self.coolant_on = False
        
    def connect(self) -> bool:
        """Establish connection with the CNC machine."""
        try:
            self.serial_conn = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            self.is_connected = True
            logger.info(f"Connected to CNC machine on port {self.port}")
            return True
        except serial.SerialException as e:
            logger.error(f"Failed to connect to CNC machine: {e}")
            return False
    
    def disconnect(self) -> None:
        """Close the connection with the CNC machine."""
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()
            self.is_connected = False
            logger.info("Disconnected from CNC machine")
    
    def send_command(self, command: str, wait_for_response: bool = True) -> Optional[str]:
        """
        Send a G-code command to the CNC machine.
        
        Args:
            command: G-code command to send
            wait_for_response: Whether to wait for and return the response
            
        Returns:
            Response from the machine if wait_for_response is True, else None
        """
        if not self.is_connected:
            logger.error("Cannot send command - not connected to CNC machine")
            return None
            
        try:
            self.serial_conn.write((command + '\n').encode('utf-8'))
            logger.debug(f"Sent command: {command}")
            
            if wait_for_response:
                response = self.serial_conn.readline().decode('utf-8').strip()
                logger.debug(f"Received response: {response}")
                return response
            return None
        except serial.SerialException as e:
            logger.error(f"Error sending command: {e}")
            return None
    
    def home_all_axes(self) -> bool:
        """Home all machine axes."""
        response = self.send_command("$H")
        if response and "ok" in response.lower():
            for axis in Axis:
                self.current_position[axis] = 0.0
            logger.info("All axes homed successfully")
            return True
        logger.error("Failed to home axes")
        return False
    
    def move_to_position(
        self,
        x: Optional[float] = None,
        y: Optional[float] = None,
        z: Optional[float] = None,
        a: Optional[float] = None,
        b: Optional[float] = None,
        feed_rate: float = 1000.0,
        relative: bool = False
    ) -> bool:
        """
        Move to specified position with given feed rate.
        
        Args:
            x, y, z, a, b: Target positions for each axis (None means don't move that axis)
            feed_rate: Movement speed in mm/min
            relative: Whether movement is relative to current position
            
        Returns:
            True if movement was successful, False otherwise
        """
        if not any([x, y, z, a, b]):
            logger.warning("No movement specified - at least one axis must be provided")
            return False
            
        command = "G91" if relative else "G90"
        command += f" F{feed_rate}"
        
        if x is not None:
            command += f" X{x}"
            self.current_position[Axis.X] = x if relative else self.current_position[Axis.X] + x
        if y is not None:
            command += f" Y{y}"
            self.current_position[Axis.Y] = y if relative else self.current_position[Axis.Y] + y
        if z is not None:
            command += f" Z{z}"
            self.current_position[Axis.Z] = z if relative else self.current_position[Axis.Z] + z
        if a is not None:
            command += f" A{a}"
            self.current_position[Axis.A] = a if relative else self.current_position[Axis.A] + a
        if b is not None:
            command += f" B{b}"
            self.current_position[Axis.B] = b if relative else self.current_position[Axis.B] + b
            
        response = self.send_command(command)
        if response and "ok" in response.lower():
            logger.info(f"Moved to position: {self.current_position}")
            return True
        logger.error("Movement failed")
        return False
    
    def set_spindle_state(self, on: bool, speed: Optional[int] = None) -> bool:
        """
        Turn spindle on/off and optionally set speed.
        
        Args:
            on: True to turn spindle on, False to turn off
            speed: RPM for spindle (None to keep current speed)
            
        Returns:
            True if command was successful, False otherwise
        """
        if on:
            command = "M3"
            if speed is not None:
                command += f" S{speed}"
            self.spindle_on = True
        else:
            command = "M5"
            self.spindle_on = False
            
        response = self.send_command(command)
        if response and "ok" in response.lower():
            logger.info(f"Spindle {'started' if on else 'stopped'} successfully")
            return True
        logger.error(f"Failed to {'start' if on else 'stop'} spindle")
        return False
    
    def set_coolant_state(self, on: bool) -> bool:
        """
        Turn coolant on/off.
        
        Args:
            on: True to turn coolant on, False to turn off
            
        Returns:
            True if command was successful, False otherwise
        """
        command = "M8" if on else "M9"
        self.coolant_on = on
        
        response = self.send_command(command)
        if response and "ok" in response.lower():
            logger.info(f"Coolant {'started' if on else 'stopped'} successfully")
            return True
        logger.error(f"Failed to {'start' if on else 'stop'} coolant")
        return False
    
    def set_energy_saving_mode(self, enable: bool) -> bool:
        """
        Enable or disable energy saving mode.
        
        Args:
            enable: True to enable energy saving, False to disable
            
        Returns:
            True if mode was set successfully, False otherwise
        """
        command = "M80" if enable else "M81"
        self.energy_saving_mode = enable
        
        response = self.send_command(command)
        if response and "ok" in response.lower():
            logger.info(f"Energy saving mode {'enabled' if enable else 'disabled'}")
            return True
        logger.error(f"Failed to {'enable' if enable else 'disable'} energy saving mode")
        return False
    
    def run_gcode_program(self, gcode_lines: List[str]) -> bool:
        """
        Execute a G-code program line by line.
        
        Args:
            gcode_lines: List of G-code commands to execute
            
        Returns:
            True if all commands executed successfully, False otherwise
        """
        if not gcode_lines:
            logger.warning("No G-code commands provided")
            return False
            
        all_success = True
        for line in gcode_lines:
            stripped_line = line.strip()
            if not stripped_line or stripped_line.startswith(';'):
                continue  # Skip empty lines and comments
                
            response = self.send_command(stripped_line)
            if not response or "ok" not in response.lower():
                logger.error(f"Command failed: {stripped_line}")
                all_success = False
                break
                
        return all_success
    
    def emergency_stop(self) -> None:
        """Immediately stop all machine operations."""
        self.send_command("M112", wait_for_response=False)
        self.spindle_on = False
        self.coolant_on = False
        logger.warning("Emergency stop activated")

# Example
