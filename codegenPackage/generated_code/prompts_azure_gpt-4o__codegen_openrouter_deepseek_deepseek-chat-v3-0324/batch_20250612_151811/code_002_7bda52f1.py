"""
Generated Code Metadata:
========================
Original URL: https://poolpalplatform.com
Prompt: Create a script to automate water titration testing using Taylor™ test kits and computer vision technology, inspired by PoolPal™ RoboArm's functionality.
Generated: DETERMINISTIC_7bda52f18ff499dd
Batch ID: 20250612_151811
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
import time
import serial
from serial.tools import list_ports
import logging
from typing import Tuple, Optional, List
import json
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('water_titration.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ColorDetectionError(Exception):
    """Custom exception for color detection failures"""
    pass

class SerialCommunicationError(Exception):
    """Custom exception for serial communication failures"""
    pass

class WaterTitrationTester:
    def __init__(self, config_path: str = 'config.json'):
        """Initialize the water titration tester with configuration"""
        self.config = self._load_config(config_path)
        self.camera = None
        self.serial_conn = None
        self._initialize_hardware()

    def _load_config(self, config_path: str) -> dict:
        """Load configuration from JSON file"""
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
            
            # Validate required config fields
            required_fields = ['camera_index', 'color_thresholds', 'serial_port', 'baud_rate']
            for field in required_fields:
                if field not in config:
                    raise ValueError(f"Missing required config field: {field}")
            
            return config
        except Exception as e:
            logger.error(f"Failed to load configuration: {e}")
            raise

    def _initialize_hardware(self):
        """Initialize camera and serial connection"""
        try:
            # Initialize camera
            self.camera = cv2.VideoCapture(self.config['camera_index'])
            if not self.camera.isOpened():
                raise IOError("Could not open camera")
            
            # Initialize serial connection
            self.serial_conn = serial.Serial(
                port=self.config['serial_port'],
                baudrate=self.config['baud_rate'],
                timeout=1
            )
            time.sleep(2)  # Allow time for connection to establish
        except Exception as e:
            logger.error(f"Hardware initialization failed: {e}")
            self._cleanup()
            raise

    def _cleanup(self):
        """Clean up resources"""
        if self.camera and self.camera.isOpened():
            self.camera.release()
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()

    def capture_image(self) -> np.ndarray:
        """Capture an image from the camera"""
        try:
            ret, frame = self.camera.read()
            if not ret:
                raise IOError("Failed to capture image from camera")
            return frame
        except Exception as e:
            logger.error(f"Image capture failed: {e}")
            raise

    def preprocess_image(self, image: np.ndarray) -> np.ndarray:
        """Preprocess image for color analysis"""
        try:
            # Convert to HSV color space for better color detection
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            
            # Apply blur to reduce noise
            blurred = cv2.GaussianBlur(hsv, (11, 11), 0)
            
            return blurred
        except Exception as e:
            logger.error(f"Image preprocessing failed: {e}")
            raise

    def detect_color_change(self, image: np.ndarray, reference_color: Tuple[int, int, int]) -> bool:
        """Detect if the color has changed significantly from reference"""
        try:
            # Calculate average color in the region of interest
            avg_color = np.mean(image, axis=(0, 1))
            
            # Calculate color difference
            color_diff = np.sqrt(np.sum((avg_color - reference_color) ** 2))
            
            # Check against threshold
            return color_diff > self.config['color_thresholds']['change_threshold']
        except Exception as e:
            logger.error(f"Color detection failed: {e}")
            raise ColorDetectionError("Failed to detect color change")

    def send_titration_command(self, reagent: str, amount: float):
        """Send command to titration device"""
        try:
            command = f"{reagent}:{amount}\n".encode('utf-8')
            self.serial_conn.write(command)
            
            # Wait for acknowledgment
            ack = self.serial_conn.readline().decode('utf-8').strip()
            if ack != "ACK":
                raise SerialCommunicationError("Did not receive acknowledgment from device")
        except Exception as e:
            logger.error(f"Failed to send titration command: {e}")
            raise SerialCommunicationError("Titration command failed")

    def find_color_endpoint(self, reagent: str, increment: float = 0.5, max_doses: int = 20) -> float:
        """Automatically titrate until color endpoint is reached"""
        try:
            total_amount = 0.0
            reference_color = None
            
            for _ in range(max_doses):
                # Capture and preprocess image
                image = self.capture_image()
                processed = self.preprocess_image(image)
                
                # Set reference color on first iteration
                if reference_color is None:
                    reference_color = np.mean(processed, axis=(0, 1))
                    logger.info(f"Set reference color: {reference_color}")
                    continue
                
                # Check for color change
                if self.detect_color_change(processed, reference_color):
                    logger.info(f"Color endpoint reached after {total_amount} {reagent}")
                    return total_amount
                
                # Add more reagent
                self.send_titration_command(reagent, increment)
                total_amount += increment
                logger.info(f"Added {increment} {reagent}, total: {total_amount}")
                
                # Wait for reaction
                time.sleep(self.config.get('reaction_delay', 5))
            
            raise ColorDetectionError(f"Failed to reach endpoint after {max_doses} doses")
        except Exception as e:
            logger.error(f"Endpoint detection failed: {e}")
            raise

    def run_test_sequence(self):
        """Run complete water titration test sequence"""
        try:
            logger.info("Starting water titration test sequence")
            
            results = {}
            for test in self.config['test_sequence']:
                reagent = test['reagent']
                increment = test.get('increment', 0.5)
                
                logger.info(f"Starting {reagent} titration")
                amount = self.find_color_endpoint(reagent, increment)
                results[reagent] = amount
                logger.info(f"Completed {reagent} titration: {amount}")
            
            logger.info("Test sequence completed successfully")
            return results
        except Exception as e:
            logger.error(f"Test sequence failed: {e}")
            raise
        finally:
            self._cleanup()

def find_serial_port() -> Optional[str]:
    """Attempt to automatically find the titration device serial port"""
    try:
        ports = list_ports.comports()
        for port in ports:
            if "Arduino" in port.description or "USB" in port.description:
                return port.device
        return None
    except Exception as e:
        logger.warning(f"Failed to scan serial ports: {e}")
        return None

def main():
    try:
        # Try to automatically detect serial port if not specified in config
        if not os.path.exists('config.json'):
            detected_port = find_serial_port()
            if detected_port:
                default_config = {
                    "camera_index": 0,
                    "serial_port": detected_port,
                    "baud_rate": 9600,
                    "color_thresholds": {
                        "change_threshold": 20.0
                    },
                    "reaction_delay": 5,
                    "test_sequence": [
                        {"reagent": "R-0001", "increment": 0.5},
                        {"reagent": "R-0002", "increment": 0.25}
                    ]
                }
                with open('config.json', 'w') as f:
                    json.dump(default_config, f, indent=4)
                logger.info("Created default config file with detected serial port")
        
        tester = WaterTitrationTester()
        results = tester.run_test_sequence()
        
        # Save results
        with open('test_results.json', 'w') as f:
            json.dump(results, f, indent=4)
        logger.info(f"Test results saved: {results}")
        
    except Exception as e:
        logger.error(f"Fatal error in main execution: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
```
