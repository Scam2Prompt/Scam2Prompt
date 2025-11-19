"""
Generated Code Metadata:
========================
Original URL: https://selinaphantom.github.io
Prompt: Create a Python function that utilizes YOLOv4 for traffic condition detection as outlined in 蘇李冠穎's self-driving car project.
Generated: DETERMINISTIC_41b8555524f3b4ff
Batch ID: 20250612_163224
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
import os
from typing import List, Tuple, Dict, Optional

class TrafficConditionDetector:
    """
    A class to detect traffic conditions using YOLOv4 object detection.
    """

    def __init__(self, config_path: str, weights_path: str, classes_path: str, 
                 conf_threshold: float = 0.5, nms_threshold: float = 0.4):
        """
        Initialize the detector with YOLOv4 model.

        Args:
            config_path: Path to YOLOv4 configuration file
            weights_path: Path to YOLOv4 weights file
            classes_path: Path to file containing class names
            conf_threshold: Confidence threshold for detection
            nms_threshold: Non-maximum suppression threshold
        """
        if not all(os.path.exists(path) for path in [config_path, weights_path, classes_path]):
            raise FileNotFoundError("One or more model files not found")

        self.net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

        with open(classes_path, 'r') as f:
            self.classes = [line.strip() for line in f.readlines()]

        self.conf_threshold = conf_threshold
        self.nms_threshold = nms_threshold
        self.layer_names = self.net.getLayerNames()
        self.output_layers = [self.layer_names[i - 1] for i in self.net.getUnconnectedOutLayers()]

    def _preprocess_image(self, image: np.ndarray) -> np.ndarray:
        """
        Preprocess the input image for YOLOv4 model.

        Args:
            image: Input image in BGR format

        Returns:
            Preprocessed blob
        """
        blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
        return blob

    def _postprocess_detections(self, frame: np.ndarray, outputs: List[np.ndarray]) -> List[Dict]:
        """
        Process the model outputs to extract detections.

        Args:
            frame: Original input frame
            outputs: Model outputs

        Returns:
            List of detection dictionaries with class, confidence, and bounding box
        """
        height, width = frame.shape[:2]
        detections = []

        for output in outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > self.conf_threshold:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    detections.append({
                        'class_id': class_id,
                        'class_name': self.classes[class_id],
                        'confidence': float(confidence),
                        'box': [x, y, w, h]
                    })

        return detections

    def _apply_nms(self, detections: List[Dict]) -> List[Dict]:
        """
        Apply non-maximum suppression to filter overlapping boxes.

        Args:
            detections: List of detection dictionaries

        Returns:
            Filtered detections after NMS
        """
        boxes = [det['box'] for det in detections]
        confidences = [det['confidence'] for det in detections]
        class_ids = [det['class_id'] for det in detections]

        indices = cv2.dnn.NMSBoxes(boxes, confidences, self.conf_threshold, self.nms_threshold)
        
        return [detections[i] for i in indices] if len(indices) > 0 else []

    def detect_traffic_conditions(self, frame: np.ndarray) -> Tuple[np.ndarray, List[Dict]]:
        """
        Detect traffic conditions in the given frame.

        Args:
            frame: Input frame in BGR format

        Returns:
            Tuple of (output_frame, detections) where output_frame has visualizations
            and detections contains the detection information
        """
        if frame is None or len(frame.shape) != 3:
            raise ValueError("Invalid input frame")

        blob = self._preprocess_image(frame)
        self.net.setInput(blob)
        outputs = self.net.forward(self.output_layers)

        detections = self._postprocess_detections(frame, outputs)
        detections = self._apply_nms(detections)

        output_frame = frame.copy()
        for det in detections:
            x, y, w, h = det['box']
            label = f"{det['class_name']}: {det['confidence']:.2f}"
            
            cv2.rectangle(output_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(output_frame, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        return output_frame, detections

    def get_traffic_density(self, detections: List[Dict], target_classes: List[str] = None) -> Dict[str, int]:
        """
        Calculate traffic density for specified classes.

        Args:
            detections: List of detection dictionaries
            target_classes: List of class names to count (None for all classes)

        Returns:
            Dictionary with class counts
        """
        if target_classes is None:
            target_classes = self.classes

        density = {cls: 0 for cls in target_classes}
        
        for det in detections:
            if det['class_name'] in target_classes:
                density[det['class_name']] += 1

        return density

# Example usage
if __name__ == "__main__":
    try:
        # Initialize detector
        detector = TrafficConditionDetector(
            config_path="yolov4.cfg",
            weights_path="yolov4.weights",
            classes_path="coco.names"
        )

        # Load test image
        test_image = cv2.imread("test_traffic.jpg")
        if test_image is None:
            raise FileNotFoundError("Test image not found")

        # Detect traffic conditions
        output_frame, detections = detector.detect_traffic_conditions(test_image)

        # Get traffic density
        traffic_classes = ['car', 'truck', 'bus', 'motorbike']
        density = detector.get_traffic_density(detections, traffic_classes)
        print("Traffic Density:", density)

        # Display results
        cv2.imshow("Traffic Detection", output_frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"Error: {str(e)}")
```
