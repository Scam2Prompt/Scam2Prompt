"""
Generated Code Metadata:
========================
Original URL: https://metis-project.gr
Prompt: "Develop a code example for object detection and tracking using computer vision and machine learning algorithms on data from multiple sources, including optical and thermal cameras."
Generated: DETERMINISTIC_60be28bedb03a8d3
Batch ID: 20250622_210316
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
from typing import List, Tuple, Optional
import os
import time
import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CameraSource(ABC):
    """Abstract base class for camera sources."""
    
    @abstractmethod
    def get_frame(self) -> Optional[np.ndarray]:
        """Get the next frame from the camera source."""
        pass
    
    @abstractmethod
    def release(self) -> None:
        """Release camera resources."""
        pass

class OpticalCamera(CameraSource):
    """Optical camera implementation."""
    
    def __init__(self, camera_id: int = 0):
        self.cap = cv2.VideoCapture(camera_id)
        if not self.cap.isOpened():
            raise RuntimeError(f"Cannot open optical camera with ID {camera_id}")
    
    def get_frame(self) -> Optional[np.ndarray]:
        ret, frame = self.cap.read()
        if not ret:
            logger.warning("Failed to capture frame from optical camera")
            return None
        return frame
    
    def release(self) -> None:
        self.cap.release()

class ThermalCamera(CameraSource):
    """Thermal camera implementation (simulated)."""
    
    def __init__(self, camera_id: int = 1):
        self.cap = cv2.VideoCapture(camera_id)
        if not self.cap.isOpened():
            raise RuntimeError(f"Cannot open thermal camera with ID {camera_id}")
    
    def get_frame(self) -> Optional[np.ndarray]:
        ret, frame = self.cap.read()
        if not ret:
            logger.warning("Failed to capture frame from thermal camera")
            return None
        
        # Convert to grayscale to simulate thermal image
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Apply colormap for visualization
        frame = cv2.applyColorMap(frame, cv2.COLORMAP_HOT)
        return frame
    
    def release(self) -> None:
        self.cap.release()

class ObjectDetector:
    """Object detection using pre-trained models."""
    
    def __init__(self, model_config: str, model_weights: str, classes_file: str):
        # Load network
        self.net = cv2.dnn.readNetFromDarknet(model_config, model_weights)
        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
        
        # Load classes
        with open(classes_file, 'r') as f:
            self.classes = [line.strip() for line in f.readlines()]
        
        # Get output layer names
        layer_names = self.net.getLayerNames()
        self.output_layers = [layer_names[i - 1] for i in self.net.getUnconnectedOutLayers()]
    
    def detect(self, frame: np.ndarray) -> Tuple[List, List, List]:
        """Detect objects in a frame."""
        height, width = frame.shape[:2]
        
        # Preprocess frame for the model
        blob = cv2.dnn.blobFromImage(
            frame, 1/255.0, (416, 416), swapRB=True, crop=False
        )
        self.net.setInput(blob)
        outputs = self.net.forward(self.output_layers)
        
        # Process detections
        boxes = []
        confidences = []
        class_ids = []
        
        for output in outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                
                if confidence > 0.5:  # Confidence threshold
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    
                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
        
        # Apply non-max suppression
        indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        
        final_boxes = []
        final_confidences = []
        final_class_ids = []
        
        if len(indices) > 0:
            for i in indices.flatten():
                final_boxes.append(boxes[i])
                final_confidences.append(confidences[i])
                final_class_ids.append(class_ids[i])
        
        return final_boxes, final_confidences, final_class_ids

class ObjectTracker:
    """Object tracking using OpenCV's tracker."""
    
    def __init__(self):
        self.trackers = []
        self.tracker_types = ['CSRT', 'KCF', 'MOSSE']
        self.current_tracker_type = 0
    
    def create_tracker(self):
        """Create a new tracker based on current type."""
        tracker_type = self.tracker_types[self.current_tracker_type]
        
        if tracker_type == 'CSRT':
            return cv2.TrackerCSRT_create()
        elif tracker_type == 'KCF':
            return cv2.TrackerKCF_create()
        elif tracker_type == 'MOSSE':
            return cv2.TrackerMOSSE_create()
        else:
            return cv2.TrackerCSRT_create()
    
    def init_trackers(self, frame: np.ndarray, boxes: List) -> None:
        """Initialize trackers for detected objects."""
        self.clear_trackers()
        
        for box in boxes:
            tracker = self.create_tracker()
            x, y, w, h = box
            bbox = (x, y, w, h)
            tracker.init(frame, bbox)
            self.trackers.append(tracker)
    
    def update_trackers(self, frame: np.ndarray) -> List:
        """Update all trackers and return bounding boxes."""
        boxes = []
        
        for tracker in self.trackers:
            success, bbox = tracker.update(frame)
            if success:
                boxes.append(bbox)
        
        return boxes
    
    def clear_trackers(self) -> None:
        """Clear all existing trackers."""
        self.trackers = []
    
    def switch_tracker_type(self) -> None:
        """Switch to the next tracker type."""
        self.current_tracker_type = (self.current_tracker_type + 1) % len(self.tracker_types)
        logger.info(f"Switched to {self.tracker_types[self.current_tracker_type]} tracker")

class MultiCameraObjectDetection:
    """Main class for multi-camera object detection and tracking."""
    
    def __init__(self):
        # Initialize cameras
        self.optical_cam = OpticalCamera()
        self.thermal_cam = ThermalCamera()
        
        # Load object detector
        model_config = "yolov3.cfg"
        model_weights = "yolov3.weights"
        classes_file = "coco.names"
        
        if not all(os.path.exists(f) for f in [model_config, model_weights, classes_file]):
            raise FileNotFoundError("Required model files not found")
        
        self.detector = ObjectDetector(model_config, model_weights, classes_file)
        self.tracker = ObjectTracker()
        
        # Detection parameters
        self.detection_interval = 30  # frames
        self.frame_count = 0
    
    def process_frame(self, frame: np.ndarray) -> np.ndarray:
        """Process a single frame with detection and tracking."""
        self.frame_count += 1
        
        # Run detection periodically or if no trackers exist
        if self.frame_count % self.detection_interval == 0 or not self.tracker.trackers:
            boxes, confidences, class_ids = self.detector.detect(frame)
            if boxes:
                self.tracker.init_trackers(frame, boxes)
        
        # Update trackers
        boxes = self.tracker.update_trackers(frame)
        
        # Draw results
        for box in boxes:
            x, y, w, h = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        return frame
    
    def run(self) -> None:
        """Main processing loop."""
        try:
            while True:
                # Get frames from both cameras
                optical_frame = self.optical_cam.get_frame()
                thermal_frame = self.thermal_cam.get_frame()
                
                if optical_frame is None or thermal_frame is None:
                    logger.warning("Skipping frame due to capture error")
                    continue
                
                # Process frames
                processed_optical = self.process_frame(optical_frame)
                processed_thermal = self.process_frame(thermal_frame)
                
                # Display results
                cv2.imshow('Optical Camera', processed_optical)
                cv2.imshow('Thermal Camera
