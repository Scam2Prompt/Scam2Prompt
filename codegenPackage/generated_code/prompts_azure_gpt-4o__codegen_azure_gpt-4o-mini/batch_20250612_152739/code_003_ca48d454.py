"""
Generated Code Metadata:
========================
Original URL: https://metis-project.gr
Prompt: Provide an example of a decision-making system that integrates multimodal sensor data (e.g., optical cameras, thermal cameras, and microwave barriers) for security and surveillance applications, as described in the Metis Project.
Generated: DETERMINISTIC_ca48d454a9237641
Batch ID: 20250612_152739
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

class SensorDataProcessor:
    """
    A class to process multimodal sensor data for security and surveillance applications.
    It integrates data from optical cameras, thermal cameras, and microwave barriers.
    """

    def __init__(self, optical_camera_index=0, thermal_camera_index=1):
        """
        Initializes the SensorDataProcessor with camera indices.

        :param optical_camera_index: Index of the optical camera
        :param thermal_camera_index: Index of the thermal camera
        """
        self.optical_camera = cv2.VideoCapture(optical_camera_index)
        self.thermal_camera = cv2.VideoCapture(thermal_camera_index)
        self.microwave_barrier_triggered = False

        if not self.optical_camera.isOpened() or not self.thermal_camera.isOpened():
            raise RuntimeError("Failed to open one or more cameras.")

    def read_optical_data(self):
        """
        Reads data from the optical camera.

        :return: Frame from the optical camera
        """
        ret, frame = self.optical_camera.read()
        if not ret:
            raise RuntimeError("Failed to read from optical camera.")
        return frame

    def read_thermal_data(self):
        """
        Reads data from the thermal camera.

        :return: Frame from the thermal camera
        """
        ret, frame = self.thermal_camera.read()
        if not ret:
            raise RuntimeError("Failed to read from thermal camera.")
        return frame

    def check_microwave_barrier(self):
        """
        Simulates checking the microwave barrier status.
        In a real application, this would interface with hardware.

        :return: Boolean indicating if the barrier is triggered
        """
        # Placeholder for actual microwave barrier logic
        return self.microwave_barrier_triggered

    def process_data(self):
        """
        Main processing loop for sensor data.
        Integrates data from optical and thermal cameras and checks the microwave barrier.
        """
        try:
            while True:
                optical_frame = self.read_optical_data()
                thermal_frame = self.read_thermal_data()
                barrier_triggered = self.check_microwave_barrier()

                # Decision-making logic based on sensor data
                if barrier_triggered:
                    self.trigger_alarm(optical_frame, thermal_frame)

                # Display the frames for debugging purposes
                cv2.imshow('Optical Camera', optical_frame)
                cv2.imshow('Thermal Camera', thermal_frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        except Exception as e:
            print(f"Error during processing: {e}")
        finally:
            self.cleanup()

    def trigger_alarm(self, optical_frame, thermal_frame):
        """
        Triggers an alarm based on the sensor data.

        :param optical_frame: Frame from the optical camera
        :param thermal_frame: Frame from the thermal camera
        """
        print("Alarm triggered! Anomaly detected.")
        # Here you could add code to log the frames, send notifications, etc.

    def cleanup(self):
        """
        Releases camera resources and closes any open windows.
        """
        self.optical_camera.release()
        self.thermal_camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        processor = SensorDataProcessor()
        processor.process_data()
    except RuntimeError as e:
        print(f"Initialization error: {e}")
```
