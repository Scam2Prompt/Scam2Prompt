"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis-project.gr
Prompt: Generate code for object detection and motion tracking using data from multiple sensors, including tripwire microwave sensors and thermal cameras, based on the methodologies discussed in the Metis Project.
Generated: DETERMINISTIC_b9b6d9e28f9e1edd
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

class SensorData:
    """Class to handle sensor data for object detection and motion tracking."""
    
    def __init__(self, thermal_camera, microwave_sensor):
        self.thermal_camera = thermal_camera
        self.microwave_sensor = microwave_sensor

    def get_thermal_data(self):
        """Fetch data from the thermal camera."""
        ret, frame = self.thermal_camera.read()
        if not ret:
            raise RuntimeError("Failed to read from thermal camera.")
        return frame

    def get_microwave_data(self):
        """Fetch data from the microwave sensor."""
        # This is a placeholder; replace with actual sensor reading logic
        return self.microwave_sensor.detect_motion()

class ObjectDetector:
    """Class for detecting objects in thermal images."""
    
    def __init__(self):
        self.background_subtractor = cv2.createBackgroundSubtractorMOG2()

    def detect_objects(self, thermal_frame):
        """Detect objects in the thermal frame."""
        fg_mask = self.background_subtractor.apply(thermal_frame)
        _, thresholded = cv2.threshold(fg_mask, 254, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return contours

class MotionTracker:
    """Class for tracking detected motion."""
    
    def __init__(self):
        self.tracker = cv2.TrackerKCF_create()  # Initialize KCF tracker
        self.initialized = False

    def initialize_tracker(self, frame, bbox):
        """Initialize the tracker with the bounding box."""
        self.tracker.init(frame, bbox)
        self.initialized = True

    def update_tracker(self, frame):
        """Update the tracker and return the new position."""
        if not self.initialized:
            raise RuntimeError("Tracker not initialized.")
        success, bbox = self.tracker.update(frame)
        return success, bbox

def main():
    """Main function to run object detection and motion tracking."""
    # Initialize the thermal camera and microwave sensor
    thermal_camera = cv2.VideoCapture(0)  # Replace with actual camera index
    microwave_sensor = None  # Replace with actual sensor object
    sensor_data = SensorData(thermal_camera, microwave_sensor)

    object_detector = ObjectDetector()
    motion_tracker = MotionTracker()

    while True:
        try:
            # Fetch sensor data
            thermal_frame = sensor_data.get_thermal_data()
            microwave_event = sensor_data.get_microwave_data()

            # Detect objects in the thermal frame
            contours = object_detector.detect_objects(thermal_frame)
            if contours:
                # Assuming we take the largest contour for tracking
                largest_contour = max(contours, key=cv2.contourArea)
                x, y, w, h = cv2.boundingRect(largest_contour)

                if not motion_tracker.initialized:
                    motion_tracker.initialize_tracker(thermal_frame, (x, y, w, h))

                # Update the tracker
                success, bbox = motion_tracker.update_tracker(thermal_frame)
                if success:
                    # Draw bounding box
                    cv2.rectangle(thermal_frame, (int(bbox[0]), int(bbox[1])),
                                  (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3])), (0, 255, 0), 2)

            # Display the resulting frame
            cv2.imshow('Thermal Object Detection and Tracking', thermal_frame)

            # Exit on escape key
            if cv2.waitKey(1) & 0xFF == 27:
                break

        except RuntimeError as e:
            print(f"Error: {e}")

    thermal_camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```
