"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis-project.gr
Prompt: Provide an example of a decision-making system that integrates multimodal sensor data (e.g., optical cameras, thermal cameras, and microwave barriers) for security and surveillance applications, as described in the Metis Project.
Generated: DETERMINISTIC_ca48d454a9237641
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import cv2  # OpenCV for optical camera processing
import threading
import logging

# Set up logging for the system
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MultimodalSecuritySystem:
    """
    A decision-making system that integrates multimodal sensor data
    (optical camera, thermal camera, microwave barriers) for security
    and surveillance applications.
    """

    def __init__(self):
        # Initialize the system sensors
        self.optical_camera_feed = None  # Placeholder for optical camera feed
        self.thermal_camera_feed = None  # Placeholder for thermal camera feed
        self.microwave_barrier_signal = False  # Placeholder for microwave barrier status
        
        # Thresholds for detection
        self.motion_threshold = 50  # Optical motion detection threshold
        self.thermal_threshold = 40.0  # Thermal detection temperature threshold (in degrees Celsius)
        self.microwave_signal_active = True  # Microwave barrier active signal
        
        # Decision flags
        self.security_breach_detected = False

    def process_optical_camera(self, frame):
        """
        Process the optical camera feed to detect motion.
        :param frame: Optical camera frame
        :return: Boolean - True if motion is detected
        """
        try:
            # Convert frame to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Simple motion detection logic (difference from background)
            _, threshold_frame = cv2.threshold(gray_frame, self.motion_threshold, 255, cv2.THRESH_BINARY)
            motion_detected = np.sum(threshold_frame) > 0
            return motion_detected
        except Exception as e:
            logging.error(f"Error processing optical camera: {e}")
            return False

    def process_thermal_camera(self, thermal_data):
        """
        Process the thermal camera feed to detect heat signatures.
        :param thermal_data: NumPy array of thermal values
        :return: Boolean - True if heat signature above threshold is detected
        """
        try:
            # Check if any temperature in the thermal feed exceeds the threshold
            heat_detected = np.any(thermal_data > self.thermal_threshold)
            return heat_detected
        except Exception as e:
            logging.error(f"Error processing thermal camera: {e}")
            return False

    def process_microwave_barrier(self, signal_status):
        """
        Process the microwave barrier signal to detect intrusions.
        :param signal_status: Boolean - Microwave barrier status
        :return: Boolean - True if barrier signal is active
        """
        try:
            return signal_status == self.microwave_signal_active
        except Exception as e:
            logging.error(f"Error processing microwave barrier signal: {e}")
            return False

    def make_decision(self, optical_result, thermal_result, microwave_result):
        """
        Make a decision based on the results from all sensors.
        :param optical_result: Boolean - Optical camera result
        :param thermal_result: Boolean - Thermal camera result
        :param microwave_result: Boolean - Microwave barrier result
        :return: None
        """
        # Decision logic: If any sensor detects an anomaly, security breach is flagged
        if optical_result or thermal_result or microwave_result:
            self.security_breach_detected = True
            logging.warning("Security breach detected!")
        else:
            self.security_breach_detected = False
            logging.info("System secure.")

    def run_system(self):
        """
        Main function to run the multimodal security system.
        :return: None
        """
        try:
            while True:
                # Simulated sensor data input
                optical_frame = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)  # Example optical frame
                thermal_data = np.random.uniform(20, 50, (100, 100))  # Example thermal data
                microwave_signal = np.random.choice([True, False])  # Example microwave signal
                
                # Process each sensor
                optical_result = self.process_optical_camera(optical_frame)
                thermal_result = self.process_thermal_camera(thermal_data)
                microwave_result = self.process_microwave_barrier(microwave_signal)
                
                # Make a decision based on sensor data
                self.make_decision(optical_result, thermal_result, microwave_result)
        except KeyboardInterrupt:
            logging.info("Security system stopped.")
        except Exception as e:
            logging.error(f"Unexpected error in system: {e}")


if __name__ == "__main__":
    # Instantiate and run the security system
    system = MultimodalSecuritySystem()
    # Run the system in a separate thread for better control in production
    system_thread = threading.Thread(target=system.run_system)
    system_thread.start()
```
