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
import numpy as np
import cv2
import time

class SensorDataProcessor:
    """
    Class to process sensor data for object detection and motion tracking.
    Supports tripwire microwave sensors and thermal camera data.
    """

    def __init__(self):
        # Initialize detection and tracking parameters
        self.tracked_objects = {}
        self.object_id = 0
        self.motion_threshold = 10  # Minimum movement threshold in pixels
        self.tripwire_sensors = {}
        self.thermal_camera_data = None

    def add_tripwire_sensor(self, sensor_id, sensor_data):
        """
        Adds data from a tripwire microwave sensor.
        :param sensor_id: Unique ID for the sensor
        :param sensor_data: Sensor data indicating triggering state
        """
        self.tripwire_sensors[sensor_id] = sensor_data

    def update_thermal_camera_data(self, frame):
        """
        Updates the thermal camera frame for processing.
        :param frame: Numpy array representing the thermal camera image
        """
        self.thermal_camera_data = frame

    def detect_objects(self):
        """
        Detects objects using thermal camera data.
        Applies basic blob detection on thermal images.
        """
        if self.thermal_camera_data is None:
            raise ValueError("Thermal camera data is not available for processing.")

        # Preprocess the thermal image (e.g., thresholding)
        gray_frame = cv2.cvtColor(self.thermal_camera_data, cv2.COLOR_BGR2GRAY)
        _, thresholded = cv2.threshold(gray_frame, 100, 255, cv2.THRESH_BINARY)

        # Find contours (potential objects)
        contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        detected_objects = []
        for contour in contours:
            # Filter small or irrelevant contours based on area
            area = cv2.contourArea(contour)
            if area > 500:  # Example threshold for object detection
                x, y, w, h = cv2.boundingRect(contour)
                detected_objects.append((x, y, w, h))
        
        return detected_objects

    def track_objects(self, detected_objects):
        """
        Tracks detected objects using a simple distance-based approach.
        Updates the positions of tracked objects and assigns new IDs if necessary.
        :param detected_objects: List of bounding boxes (x, y, w, h) for detected objects
        """
        for bbox in detected_objects:
            x, y, w, h = bbox
            new_object = True

            # Compare detected object to existing tracked objects
            for obj_id, tracked_obj in self.tracked_objects.items():
                tx, ty, tw, th = tracked_obj['bbox']
                distance = np.sqrt((x - tx)**2 + (y - ty)**2)

                if distance < self.motion_threshold:
                    # Update tracked object
                    self.tracked_objects[obj_id]['bbox'] = bbox
                    self.tracked_objects[obj_id]['last_seen'] = time.time()
                    new_object = False
                    break

            if new_object:
                # Assign new ID to the object and start tracking
                self.object_id += 1
                self.tracked_objects[self.object_id] = {
                    'bbox': bbox,
                    'last_seen': time.time()
                }

        # Remove stale objects (not seen for a while)
        current_time = time.time()
        self.tracked_objects = {
            obj_id: obj_data
            for obj_id, obj_data in self.tracked_objects.items()
            if current_time - obj_data['last_seen'] < 5  # Example timeout
        }

    def process_tripwire_sensors(self):
        """
        Processes tripwire microwave sensor data to update motion events.
        """
        for sensor_id, sensor_data in self.tripwire_sensors.items():
            if sensor_data['triggered']:
                print(f"Tripwire sensor {sensor_id} triggered at {sensor_data['timestamp']}")

    def process_frame(self, frame):
        """
        Main processing method to handle a single frame of data.
        Combines data from thermal camera and tripwire sensors.
        :param frame: Numpy array representing the thermal camera frame
        """
        self.update_thermal_camera_data(frame)
        detected_objects = self.detect_objects()
        self.track_objects(detected_objects)

        # Process tripwire sensors independently
        self.process_tripwire_sensors()

        # Visualize the results (optional)
        for obj_id, obj_data in self.tracked_objects.items():
            x, y, w, h = obj_data['bbox']
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"ID {obj_id}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        cv2.imshow("Processed Frame", frame)
        cv2.waitKey(1)

# Example usage
if __name__ == "__main__":
    # Initialize processor
    processor = SensorDataProcessor()

    # Mock tripwire sensor data
    processor.add_tripwire_sensor("sensor1", {"triggered": True, "timestamp": time.time()})

    # Mock video feed from thermal camera
    cap = cv2.VideoCapture(0)  # Replace with actual thermal camera feed

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Process the frame
        try:
            processor.process_frame(frame)
        except ValueError as e:
            print(f"Error processing frame: {e}")

    cap.release()
    cv2.destroyAllWindows()
```
