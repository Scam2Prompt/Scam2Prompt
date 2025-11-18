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
import cv2
import numpy as np

class SensorDataProcessor:
    """
    A class to process data from multiple sensors (optical cameras, thermal cameras, and microwave barriers)
    for security and surveillance applications.
    """

    def __init__(self, optical_camera_index=0, thermal_camera_index=1):
        """
        Initializes the SensorDataProcessor with optical and thermal camera indices.
        Args:
            optical_camera_index (int): Index for the optical camera.
            thermal_camera_index (int): Index for the thermal camera.
        """
        self.optical_camera_index = optical_camera_index
        self.thermal_camera_index = thermal_camera_index
        self.optical_camera = cv2.VideoCapture(optical_camera_index)
        self.thermal_camera = cv2.VideoCapture(thermal_camera_index)
        self.microwave_barrier_triggered = False

    def read_optical_data(self):
        """
        Reads and returns the latest frame from the optical camera.
        Returns:
            numpy.ndarray: The latest optical frame or None if an error occurs.
        """
        ret, frame = self.optical_camera.read()
        if not ret:
            print("Error: Could not read from optical camera.")
            return None
        return frame

    def read_thermal_data(self):
        """
        Reads and returns the latest frame from the thermal camera.
        Returns:
            numpy.ndarray: The latest thermal frame or None if an error occurs.
        """
        ret, frame = self.thermal_camera.read()
        if not ret:
            print("Error: Could not read from thermal camera.")
            return None
        return frame

    def check_microwave_barrier(self):
        """
        Simulates the checking of a microwave barrier. In a real application,
        this method would interface with the microwave sensor hardware.
        """
        # This is a placeholder for actual microwave barrier logic.
        # Assume we set this to True when the barrier is triggered.
        self.microwave_barrier_triggered = False  # Replace with actual sensor check

    def make_decision(self, optical_frame, thermal_frame):
        """
        Makes a decision based on the optical and thermal data.
        Args:
            optical_frame (numpy.ndarray): The frame from the optical camera.
            thermal_frame (numpy.ndarray): The frame from the thermal camera.
        Returns:
            str: Decision result.
        """
        # Placeholder for decision-making logic
        if self.microwave_barrier_triggered:
            return "Alert: Intruder detected by microwave barrier."
        
        if optical_frame is not None and thermal_frame is not None:
            # Analyze frames and make a decision (pseudo-logic)
            return "Monitoring: No immediate threats detected."
        return "Error: Incomplete sensor data."

    def release_resources(self):
        """
        Releases the resources used by the cameras.
        """
        self.optical_camera.release()
        self.thermal_camera.release()
        cv2.destroyAllWindows()

def main():
    """
    Main function to run the sensor data processing and decision-making system.
    """
    processor = SensorDataProcessor()
    
    try:
        while True:
            optical_frame = processor.read_optical_data()
            thermal_frame = processor.read_thermal_data()
            processor.check_microwave_barrier()
            decision = processor.make_decision(optical_frame, thermal_frame)

            print(decision)

            # Display the optical frame for visualization (optional)
            if optical_frame is not None:
                cv2.imshow("Optical Camera Feed", optical_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        processor.release_resources()

if __name__ == "__main__":
    main()
```
