"""
Generated Code Metadata:
========================
Original URL: https://metis-project.gr
Prompt: Generate code for object detection and motion tracking using data from multiple sensors, including tripwire microwave sensors and thermal cameras, based on the methodologies discussed in the Metis Project.
Generated: DETERMINISTIC_b9b6d9e28f9e1edd
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
import threading
from collections import deque
from typing import List, Dict, Tuple, Optional
import json
import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('metis_detection.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class SensorInterface:
    """Base class for sensor interfaces."""
    def __init__(self, sensor_id: str, config: Dict):
        self.sensor_id = sensor_id
        self.config = config
        self.is_active = False
        self.last_update = None

    def initialize(self) -> bool:
        """Initialize the sensor connection."""
        raise NotImplementedError

    def read_data(self) -> Optional[Dict]:
        """Read data from the sensor."""
        raise NotImplementedError

    def close(self):
        """Close the sensor connection."""
        raise NotImplementedError

class MicrowaveTripwire(SensorInterface):
    """Microwave tripwire sensor implementation."""
    def __init__(self, sensor_id: str, config: Dict):
        super().__init__(sensor_id, config)
        self.threshold = config.get('threshold', 0.5)
        self.calibration_samples = config.get('calibration_samples', 100)
        self.baseline = None
        self.samples = deque(maxlen=self.calibration_samples)

    def initialize(self) -> bool:
        try:
            # Simulate sensor initialization
            time.sleep(0.1)
            self.is_active = True
            logger.info(f"Microwave sensor {self.sensor_id} initialized")
            return True
        except Exception as e:
            logger.error(f"Failed to initialize microwave sensor {self.sensor_id}: {e}")
            return False

    def calibrate(self):
        """Calibrate the sensor to establish baseline."""
        if not self.is_active:
            return False

        logger.info(f"Calibrating microwave sensor {self.sensor_id}")
        for _ in range(self.calibration_samples):
            sample = self._read_raw()
            if sample is not None:
                self.samples.append(sample)

        if len(self.samples) > 0:
            self.baseline = np.mean(self.samples)
            logger.info(f"Calibration complete. Baseline: {self.baseline:.2f}")
            return True
        return False

    def _read_raw(self) -> Optional[float]:
        """Simulate reading raw sensor data."""
        try:
            # Simulate sensor reading (0-1 range)
            return np.random.uniform(0, 0.2)  # Normally quiet environment
        except Exception as e:
            logger.error(f"Error reading microwave sensor {self.sensor_id}: {e}")
            return None

    def read_data(self) -> Optional[Dict]:
        if not self.is_active:
            return None

        raw_value = self._read_raw()
        if raw_value is None:
            return None

        timestamp = datetime.now().isoformat()
        detection = raw_value > (self.baseline + self.threshold) if self.baseline else False

        return {
            'sensor_id': self.sensor_id,
            'timestamp': timestamp,
            'value': raw_value,
            'detection': detection,
            'baseline': self.baseline
        }

    def close(self):
        self.is_active = False
        logger.info(f"Microwave sensor {self.sensor_id} closed")

class ThermalCamera(SensorInterface):
    """Thermal camera implementation."""
    def __init__(self, sensor_id: str, config: Dict):
        super().__init__(sensor_id, config)
        self.capture_width = config.get('width', 640)
        self.capture_height = config.get('height', 480)
        self.temp_threshold = config.get('temp_threshold', 30.0)  # Celsius
        self.cap = None
        self.fps = config.get('fps', 10)
        self.last_frame = None
        self.background_model = None
        self.background_accumulator = None
        self.background_frames = config.get('background_frames', 30)

    def initialize(self) -> bool:
        try:
            # Simulate camera initialization
            self.cap = cv2.VideoCapture(0)  # Replace with actual thermal camera interface
            if not self.cap.isOpened():
                raise RuntimeError("Could not open thermal camera")
            
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.capture_width)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.capture_height)
            self.cap.set(cv2.CAP_PROP_FPS, self.fps)
            
            self.is_active = True
            logger.info(f"Thermal camera {self.sensor_id} initialized")
            return True
        except Exception as e:
            logger.error(f"Failed to initialize thermal camera {self.sensor_id}: {e}")
            return False

    def _capture_frame(self) -> Optional[np.ndarray]:
        """Capture a single frame from the camera."""
        if not self.is_active or self.cap is None:
            return None

        ret, frame = self.cap.read()
        if not ret:
            logger.warning(f"Failed to capture frame from thermal camera {self.sensor_id}")
            return None

        # Convert to grayscale (thermal cameras often provide single-channel data)
        if len(frame.shape) == 3:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        return frame

    def _initialize_background_model(self):
        """Initialize the background model for motion detection."""
        frames = []
        for _ in range(self.background_frames):
            frame = self._capture_frame()
            if frame is not None:
                frames.append(frame)
        
        if len(frames) > 0:
            self.background_model = np.median(frames, axis=0).astype(np.uint8)
            logger.info(f"Background model initialized for thermal camera {self.sensor_id}")

    def _detect_motion(self, frame: np.ndarray) -> Tuple[Optional[np.ndarray], List[Dict]]:
        """Detect motion using background subtraction."""
        if self.background_model is None:
            return None, []

        # Compute absolute difference between current frame and background
        diff = cv2.absdiff(frame, self.background_model)
        
        # Apply threshold to get binary image
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
        
        # Apply morphological operations to remove noise
        kernel = np.ones((5, 5), np.uint8)
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
        
        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        detections = []
        for contour in contours:
            if cv2.contourArea(contour) < 500:  # Minimum area threshold
                continue
                
            x, y, w, h = cv2.boundingRect(contour)
            detections.append({
                'bbox': (x, y, w, h),
                'area': cv2.contourArea(contour),
                'centroid': (x + w//2, y + h//2)
            })
        
        return thresh, detections

    def read_data(self) -> Optional[Dict]:
        if not self.is_active:
            return None

        frame = self._capture_frame()
        if frame is None:
            return None

        timestamp = datetime.now().isoformat()
        motion_mask, detections = self._detect_motion(frame)
        
        # Update background model periodically
        if self.background_accumulator is None:
            self.background_accumulator = frame.copy().astype(np.float32)
        else:
            cv2.accumulateWeighted(frame, self.background_accumulator, 0.05)
            self.background_model = self.background_accumulator.astype(np.uint8)

        return {
            'sensor_id': self.sensor_id,
            'timestamp': timestamp,
            'frame': frame,
            'motion_mask': motion_mask,
            'detections': detections,
            'num_detections': len(detections)
        }

    def close(self):
        self.is_active = False
        if self.cap is not None:
            self.cap.release()
        logger.info(f"Thermal camera {self.sensor_id} closed")

class ObjectTracker:
    """Multi-sensor object tracker."""
    def __init__(self, config: Dict):
        self.config = config
        self.sensors: Dict[str, SensorInterface] = {}
        self
