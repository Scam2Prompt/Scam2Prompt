"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://selinaphantom.github.io
Prompt: Create a Python function that utilizes YOLOv4 for traffic condition detection as outlined in 蘇李冠穎's self-driving car project.
Generated: DETERMINISTIC_41b8555524f3b4ff
Batch ID: 20250612_163224
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

class TrafficConditionDetector:
    def __init__(self, yolo_weights_path, yolo_cfg_path, classes_path):
        """
        Initialize the TrafficConditionDetector with YOLOv4 weights and configuration.
        
        :param yolo_weights_path: Path to the YOLOv4 weights file.
        :param yolo_cfg_path: Path to the YOLOv4 configuration file.
        :param classes_path: Path to the file containing class labels.
        """
        self.net = cv2.dnn.readNet(weights=yolo_weights_path, config=yolo_cfg_path)
        self.classes = self.load_classes(classes_path)
        self.layer_names = self.net.getLayerNames()
        self.output_layers = [self.layer_names[i - 1] for i in self.net.getUnconnectedOutLayers()]

    def load_classes(self, classes_path):
        """
        Load class labels from a text file.
        
        :param classes_path: Path to the file containing class labels.
        :return: List of class labels.
        """
        try:
            with open(classes_path, 'r') as f:
                classes = [line.strip() for line in f.readlines()]
            return classes
        except FileNotFoundError:
            raise Exception(f"Classes file not found at {classes_path}. Please check the path.")
    
    def detect_traffic_conditions(self, image):
        """
        Run YOLOv4 detection on the provided image to determine traffic conditions.
        
        :param image: Input image for traffic condition detection.
        :return: Detected objects with bounding boxes and class labels.
        """
        height, width = image.shape[:2]
        # Prepare the image for YOLO
        blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        self.net.setInput(blob)
        outputs = self.net.forward(self.output_layers)

        boxes = []
        confidences = []
        class_ids = []

        # Process the outputs
        for output in outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                
                # Filter out weak predictions
                if confidence > 0.5:  # You can adjust this threshold
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Calculate the coordinates of the bounding box
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    # Store the box, confidence, and class_id
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # Apply Non-Max Suppression to remove duplicates
        indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        detected_objects = []
        
        for i in indices:
            i = i[0]
            box = boxes[i]
            x, y, w, h = box
            detected_objects.append({
                "class": self.classes[class_ids[i]],
                "confidence": confidences[i],
                "box": box
            })

        return detected_objects

# Example usage
if __name__ == '__main__':
    # Paths to the model and classes files
    YOLO_WEIGHTS_PATH = 'yolov4.weights'
    YOLO_CFG_PATH = 'yolov4.cfg'
    CLASSES_PATH = 'coco.names'

    # Initialize the detector
    detector = TrafficConditionDetector(YOLO_WEIGHTS_PATH, YOLO_CFG_PATH, CLASSES_PATH)

    # Load an image (replace 'test_image.jpg' with your image path)
    image = cv2.imread('test_image.jpg')
    if image is None:
        raise Exception("Image not found. Please check the image path.")

    # Detect traffic conditions
    detected_conditions = detector.detect_traffic_conditions(image)

    # Print detected conditions
    for condition in detected_conditions:
        print(f"Detected {condition['class']} with confidence {condition['confidence']:.2f} at box {condition['box']}")
```
