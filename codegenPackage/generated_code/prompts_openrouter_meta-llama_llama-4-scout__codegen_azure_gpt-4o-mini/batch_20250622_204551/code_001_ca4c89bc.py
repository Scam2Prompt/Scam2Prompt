"""
Generated Code Metadata:
========================
Original URL: https://nvidiatechnologies.com
Prompt: Write a Python code for a postgraduate research project on AI-powered surveillance systems using OpenCV and TensorFlow.
Generated: DETERMINISTIC_ca4c89bc8422aaec
Batch ID: 20250622_204551
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
import tensorflow as tf

# Load the pre-trained model for object detection
MODEL_PATH = 'path/to/your/model.h5'  # Update with your model path
model = tf.keras.models.load_model(MODEL_PATH)

# Define the labels for the detected objects
LABELS = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 
          'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 
          'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 
          'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 
          'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 
          'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 
          'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 
          'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 
          'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 
          'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 
          'couch', 'potted plant', 'bed', 'dining table', 'toilet', 
          'TV', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 
          'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 
          'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 
          'toothbrush']

# Function to process video frames
def process_frame(frame):
    """
    Process a single video frame for object detection.

    Args:
        frame: The video frame to process.

    Returns:
        detections: List of detected objects with their bounding boxes and labels.
    """
    # Resize frame for model input
    input_frame = cv2.resize(frame, (224, 224))
    input_frame = np.expand_dims(input_frame, axis=0) / 255.0  # Normalize

    # Perform object detection
    predictions = model.predict(input_frame)
    detections = []

    # Process predictions
    for i, pred in enumerate(predictions[0]):
        if pred > 0.5:  # Confidence threshold
            label = LABELS[i]
            detections.append((label, pred))

    return detections

# Main function to run the surveillance system
def run_surveillance():
    """
    Run the AI-powered surveillance system using webcam input.
    """
    # Open video capture
    cap = cv2.VideoCapture(0)  # Use 0 for webcam, or provide video file path

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame.")
                break

            # Process the frame
            detections = process_frame(frame)

            # Draw detections on the frame
            for label, confidence in detections:
                cv2.putText(frame, f"{label}: {confidence:.2f}", (10, 30), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

            # Display the frame
            cv2.imshow('Surveillance System', frame)

            # Exit on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Release video capture and close windows
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    run_surveillance()
```

**Note:** Ensure you have the necessary libraries installed (`opencv-python`, `tensorflow`, `numpy`) and replace the `MODEL_PATH` with the actual path to your trained model. Adjust the input size in `process_frame` according to your model's requirements.
