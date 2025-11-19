"""
Generated Code Metadata:
========================
Original URL: https://aktivrorteknikk.no
Prompt: Generate a code snippet for a pipe inspection system that uses CCTV cameras and sensor data to detect defects and anomalies in pipe networks.
Generated: DETERMINISTIC_115d517efad2f1f5
Batch ID: 20250622_211504
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
import logging
from typing import List, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PipeInspectionSystem:
    def __init__(self, camera_index: int):
        """
        Initializes the Pipe Inspection System with a CCTV camera.

        :param camera_index: Index of the camera to be used for inspection.
        """
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(camera_index)

        if not self.cap.isOpened():
            logging.error("Camera could not be opened.")
            raise ValueError("Camera not accessible")

    def capture_frame(self) -> np.ndarray:
        """
        Captures a single frame from the CCTV camera.

        :return: Captured frame as a numpy array.
        """
        ret, frame = self.cap.read()
        if not ret:
            logging.error("Failed to capture frame from camera.")
            raise RuntimeError("Frame capture failed")
        return frame

    def process_frame(self, frame: np.ndarray) -> List[Tuple[int, int, int, int]]:
        """
        Processes the captured frame to detect defects and anomalies.

        :param frame: The frame to be processed.
        :return: List of detected anomalies as bounding boxes (x, y, width, height).
        """
        # Convert frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise
        blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

        # Use Canny edge detection to find edges
        edges = cv2.Canny(blurred_frame, 50, 150)

        # Find contours in the edges
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        anomalies = []
        for contour in contours:
            # Filter out small contours
            if cv2.contourArea(contour) > 100:
                x, y, w, h = cv2.boundingRect(contour)
                anomalies.append((x, y, w, h))
                logging.info(f"Detected anomaly at: x={x}, y={y}, width={w}, height={h}")

        return anomalies

    def run_inspection(self):
        """
        Runs the pipe inspection process, capturing frames and detecting anomalies.
        """
        try:
            while True:
                frame = self.capture_frame()
                anomalies = self.process_frame(frame)

                # Display the frame with detected anomalies
                for (x, y, w, h) in anomalies:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                cv2.imshow('Pipe Inspection', frame)

                # Exit on 'q' key press
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        except Exception as e:
            logging.error(f"An error occurred during inspection: {e}")
        finally:
            self.cap.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        inspection_system = PipeInspectionSystem(camera_index=0)
        inspection_system.run_inspection()
    except Exception as e:
        logging.error(f"Failed to initialize Pipe Inspection System: {e}")
```
