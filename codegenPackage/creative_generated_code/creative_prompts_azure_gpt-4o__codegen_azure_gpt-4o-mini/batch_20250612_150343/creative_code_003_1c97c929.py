"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet.in
Prompt: Create a surveillance system for traffic monitoring using the features outlined in Starknet IT Solutions' surveillance and spy services.
Generated: DETERMINISTIC_1c97c9299545a6cd
Batch ID: 20250612_150343
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
import datetime
import os

class TrafficSurveillance:
    def __init__(self, video_source=0, output_dir='recordings', min_confidence=0.5):
        """
        Initializes the TrafficSurveillance system.
        
        Parameters:
            video_source (int or str): The source of the video feed (0 for webcam or video file path).
            output_dir (str): Directory to save the recorded videos.
            min_confidence (float): Minimum confidence to consider an object detected.
        """
        self.video_source = video_source
        self.output_dir = output_dir
        self.min_confidence = min_confidence

        # Load YOLO model
        self.net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
        self.classes = []
        with open("coco.names", "r") as f:
            self.classes = [line.strip() for line in f.readlines()]
        
        # Get layer names and output layers
        layer_names = self.net.getLayerNames()
        self.output_layers = [layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)

    def start_monitoring(self):
        """
        Starts the traffic monitoring process, capturing video and detecting objects.
        """
        cap = cv2.VideoCapture(self.video_source)
        if not cap.isOpened():
            raise RuntimeError("Error opening video source")

        # Set up video writer for saving output
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(os.path.join(self.output_dir, 'traffic_' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + '.avi'), fourcc, 20.0, (640, 480))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            # Process frame
            self.detect_objects(frame, out)

        # Release resources
        cap.release()
        out.release()
        cv2.destroyAllWindows()

    def detect_objects(self, frame, out):
        """
        Detects objects in the given frame and saves the result.
        
        Parameters:
            frame (ndarray): The video frame to process.
            out (VideoWriter): The video writer to save the processed frames.
        """
        height, width, _ = frame.shape
        
        # Prepare the frame for YOLO
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        self.net.setInput(blob)
        outputs = self.net.forward(self.output_layers)

        boxes, confidences, class_ids = [], [], []

        # Loop through all detections
        for output in outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > self.min_confidence:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    # Append to lists
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # Non-maxima suppression for overlapping bounding boxes
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, self.min_confidence, 0.4)

        # Draw bounding boxes and labels on the frame
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(self.classes[class_ids[i]])
                color = (0, 255, 0)  # Green color for bounding box
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.putText(frame, label, (x, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        # Write the frame with detected objects to output
        out.write(frame)

if __name__ == "__main__":
    try:
        # Create an instance of TrafficSurveillance and start monitoring
        traffic_monitor = TrafficSurveillance(video_source=0)
        traffic_monitor.start_monitoring()
    except Exception as e:
        print(f"An error occurred: {e}")
```

Ensure that you have the necessary files (`yolov3.weights`, `yolov3.cfg`, and `coco.names`) in the same directory as this script, and OpenCV installed in your Python environment.
