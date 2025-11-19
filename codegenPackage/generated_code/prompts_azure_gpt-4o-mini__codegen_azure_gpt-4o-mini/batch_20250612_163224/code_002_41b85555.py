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

class TrafficConditionDetector:
    def __init__(self, yolo_weights: str, yolo_cfg: str, classes_file: str):
        """
        Initializes the TrafficConditionDetector with YOLOv4 model parameters.

        :param yolo_weights: Path to the YOLOv4 weights file.
        :param yolo_cfg: Path to the YOLOv4 configuration file.
        :param classes_file: Path to the file containing class names.
        """
        self.net = cv2.dnn.readNet(yolo_weights, yolo_cfg)
        self.classes = self.load_classes(classes_file)
        self.layer_names = self.net.getLayerNames()
        self.output_layers = [self.layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

    @staticmethod
    def load_classes(classes_file: str) -> list:
        """
        Loads class names from a file.

        :param classes_file: Path to the classes file.
        :return: List of class names.
        """
        try:
            with open(classes_file, 'r') as f:
                classes = [line.strip() for line in f.readlines()]
            return classes
        except Exception as e:
            raise FileNotFoundError(f"Error loading classes file: {e}")

    def detect_traffic_conditions(self, image: np.ndarray) -> list:
        """
        Detects traffic conditions in the provided image using YOLOv4.

        :param image: Input image as a NumPy array.
        :return: List of detected objects with their class names and confidence scores.
        """
        height, width, _ = image.shape
        blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        self.net.setInput(blob)
        outputs = self.net.forward(self.output_layers)

        boxes, confidences, class_ids = [], [], []
        for output in outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:  # Confidence threshold
                    center_x, center_y, w, h = (detection[0:4] * np.array([width, height, width, height])).astype('int')
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # Apply Non-Maximum Suppression to eliminate redundant overlapping boxes
        indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        detected_objects = []
        for i in indices:
            i = i[0]
            box = boxes[i]
            label = str(self.classes[class_ids[i]])
            confidence = confidences[i]
            detected_objects.append({'label': label, 'confidence': confidence, 'box': box})

        return detected_objects

# Example usage:
if __name__ == "__main__":
    # Paths to the YOLOv4 model files
    yolo_weights_path = 'yolov4.weights'
    yolo_cfg_path = 'yolov4.cfg'
    classes_file_path = 'coco.names'

    # Initialize the traffic condition detector
    detector = TrafficConditionDetector(yolo_weights_path, yolo_cfg_path, classes_file_path)

    # Load an image for detection
    image_path = 'traffic_image.jpg'
    image = cv2.imread(image_path)

    if image is not None:
        # Detect traffic conditions
        detected_conditions = detector.detect_traffic_conditions(image)
        print(detected_conditions)
    else:
        print("Error: Image not found or unable to load.")
```
