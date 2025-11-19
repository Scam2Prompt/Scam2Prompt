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
from imutils.video import VideoStream
import time

class ObjectDetector:
    def __init__(self, model_path, config_path, classes_path, confidence_threshold=0.5):
        """
        Initializes the ObjectDetector with the specified model and configuration.

        :param model_path: Path to the pre-trained model file.
        :param config_path: Path to the configuration file for the model.
        :param classes_path: Path to the file containing class labels.
        :param confidence_threshold: Minimum confidence threshold for detections.
        """
        self.net = cv2.dnn.readNetFromDarknet(config_path, model_path)
        self.classes = self.load_classes(classes_path)
        self.confidence_threshold = confidence_threshold

    def load_classes(self, classes_path):
        """
        Loads class labels from a file.

        :param classes_path: Path to the file containing class labels.
        :return: List of class labels.
        """
        with open(classes_path, 'r') as f:
            return [line.strip() for line in f.readlines()]

    def detect_objects(self, frame):
        """
        Detects objects in a given frame.

        :param frame: The input frame from the camera.
        :return: List of detected objects with their bounding boxes and confidence scores.
        """
        height, width = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        self.net.setInput(blob)
        layer_names = self.net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]
        outputs = self.net.forward(output_layers)

        boxes, confidences, class_ids = [], [], []
        for output in outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > self.confidence_threshold:
                    center_x, center_y = int(detection[0] * width), int(detection[1] * height)
                    w, h = int(detection[2] * width), int(detection[3] * height)
                    x, y = int(center_x - w / 2), int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indices = cv2.dnn.NMSBoxes(boxes, confidences, self.confidence_threshold, 0.4)
        detected_objects = [(boxes[i], confidences[i], class_ids[i]) for i in indices.flatten()]
        return detected_objects

    def draw_detections(self, frame, detections):
        """
        Draws bounding boxes and labels on the frame for detected objects.

        :param frame: The input frame from the camera.
        :param detections: List of detected objects with their bounding boxes and confidence scores.
        """
        for (box, confidence, class_id) in detections:
            x, y, w, h = box
            label = f"{self.classes[class_id]}: {confidence:.2f}"
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

def main():
    # Initialize video streams for optical and thermal cameras
    optical_camera = VideoStream(src=0).start()  # Change src for optical camera
    thermal_camera = VideoStream(src=1).start()  # Change src for thermal camera
    time.sleep(2.0)  # Allow camera to warm up

    # Initialize object detector
    detector = ObjectDetector(
        model_path='yolov3.weights',
        config_path='yolov3.cfg',
        classes_path='coco.names'
    )

    try:
        while True:
            # Read frames from both cameras
            optical_frame = optical_camera.read()
            thermal_frame = thermal_camera.read()

            # Detect objects in both frames
            optical_detections = detector.detect_objects(optical_frame)
            thermal_detections = detector.detect_objects(thermal_frame)

            # Draw detections on both frames
            detector.draw_detections(optical_frame, optical_detections)
            detector.draw_detections(thermal_frame, thermal_detections)

            # Display the frames
            cv2.imshow("Optical Camera", optical_frame)
            cv2.imshow("Thermal Camera", thermal_frame)

            # Break the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Cleanup
        optical_camera.stop()
        thermal_camera.stop()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```

**Note**: Ensure you have the required files (`yolov3.weights`, `yolov3.cfg`, `coco.names`) and the necessary libraries installed (`opencv-python`, `imutils`, `numpy`). Adjust the camera source indices as needed for your setup.
