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
from typing import List, Tuple

# Load pre-trained object detection model (e.g., YOLOv4 or SSD)
# Ensure you have the model weights and configuration files in the correct paths
MODEL_CONFIG = "yolov4.cfg"
MODEL_WEIGHTS = "yolov4.weights"
LABELS_FILE = "coco.names"

# Load labels for detected objects
with open(LABELS_FILE, "r") as f:
    LABELS = f.read().strip().split("\n")

# Initialize the neural network
net = cv2.dnn.readNetFromDarknet(MODEL_CONFIG, MODEL_WEIGHTS)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

# Function to perform object detection on a single frame
def detect_objects(frame: np.ndarray) -> List[Tuple[int, float, Tuple[int, int, int, int]]]:
    """
    Detect objects in a given frame using the pre-trained model.

    Args:
        frame (np.ndarray): Input image frame.

    Returns:
        List[Tuple[int, float, Tuple[int, int, int, int]]]: List of detected objects with class ID, confidence, and bounding box.
    """
    # Prepare the frame for the model
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)

    # Get output layer names
    layer_names = net.getUnconnectedOutLayersNames()

    # Perform forward pass
    outputs = net.forward(layer_names)

    # Initialize results
    height, width = frame.shape[:2]
    results = []

    # Process outputs
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            # Filter weak detections
            if confidence > 0.5:  # Confidence threshold
                box = detection[0:4] * np.array([width, height, width, height])
                (center_x, center_y, box_width, box_height) = box.astype("int")

                # Calculate top-left corner of the bounding box
                x = int(center_x - (box_width / 2))
                y = int(center_y - (box_height / 2))

                # Append detection result
                results.append((class_id, confidence, (x, y, int(box_width), int(box_height))))

    return results

# Function to track objects across frames
def track_objects(detections: List[Tuple[int, float, Tuple[int, int, int, int]]], tracker: cv2.Tracker) -> List[Tuple[int, Tuple[int, int, int, int]]]:
    """
    Track objects across frames using a tracker.

    Args:
        detections (List[Tuple[int, float, Tuple[int, int, int, int]]]): Detected objects in the current frame.
        tracker (cv2.Tracker): Tracker object.

    Returns:
        List[Tuple[int, Tuple[int, int, int, int]]]: List of tracked objects with class ID and bounding box.
    """
    tracked_objects = []
    for class_id, confidence, bbox in detections:
        # Initialize tracker for each detected object
        tracker.init(frame, bbox)
        success, tracked_bbox = tracker.update(frame)
        if success:
            tracked_objects.append((class_id, tracked_bbox))
    return tracked_objects

# Main function to process video streams from multiple sources
def process_video_streams(sources: List[str]):
    """
    Process video streams from multiple sources for object detection and tracking.

    Args:
        sources (List[str]): List of video source paths (e.g., optical and thermal cameras).
    """
    # Open video streams
    caps = [cv2.VideoCapture(source) for source in sources]

    # Check if all sources are opened
    if not all(cap.isOpened() for cap in caps):
        raise ValueError("One or more video sources could not be opened.")

    # Initialize tracker (e.g., KCF tracker)
    tracker = cv2.TrackerKCF_create()

    while True:
        frames = []
        for cap in caps:
            ret, frame = cap.read()
            if not ret:
                print("Failed to read frame from source.")
                continue
            frames.append(frame)

        # Process each frame
        for i, frame in enumerate(frames):
            detections = detect_objects(frame)
            tracked_objects = track_objects(detections, tracker)

            # Draw detections and tracked objects on the frame
            for class_id, confidence, bbox in detections:
                x, y, w, h = bbox
                label = f"{LABELS[class_id]}: {confidence:.2f}"
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            for class_id, bbox in tracked_objects:
                x, y, w, h = bbox
                label = f"Tracked: {LABELS[class_id]}"
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

            # Display the frame
            cv2.imshow(f"Source {i}", frame)

        # Break loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    for cap in caps:
        cap.release()
    cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    video_sources = ["optical_camera.mp4", "thermal_camera.mp4"]  # Replace with actual paths
    process_video_streams(video_sources)
```
