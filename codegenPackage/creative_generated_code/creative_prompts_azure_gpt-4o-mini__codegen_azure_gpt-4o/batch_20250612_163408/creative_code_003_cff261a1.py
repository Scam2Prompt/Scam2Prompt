"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: Provide an example of using tiny_yolov2_onnx_cam for object detection in a Python application.
Generated: DETERMINISTIC_cff261a156eda536
Batch ID: 20250612_163408
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
import onnxruntime as ort

# Constants
MODEL_PATH = "tiny_yolov2.onnx"  # Path to the ONNX file
INPUT_WIDTH = 416               # Input width expected by the model
INPUT_HEIGHT = 416              # Input height expected by the model
CONFIDENCE_THRESHOLD = 0.5      # Confidence threshold for filtering predictions

# Predefined class names for Tiny YOLOv2 (customize this based on your model's classes)
CLASS_NAMES = ["person", "bicycle", "car", "motorbike", "airplane", "bus", "train", "truck", "boat", "traffic light"]

def preprocess_frame(frame):
    """
    Preprocess the input frame to match the model's input requirements.
    Args:
        frame (np.ndarray): The original frame from the camera.
    Returns:
        np.ndarray: Preprocessed image ready to be fed into the model.
    """
    # Resize the image to the model's input size
    resized_frame = cv2.resize(frame, (INPUT_WIDTH, INPUT_HEIGHT))
    # Convert BGR to RGB and normalize pixel values to [0, 1]
    normalized_frame = resized_frame / 255.0
    # Add batch dimension and transpose to channel-first format (1, channels, height, width)
    input_tensor = np.transpose(normalized_frame, (2, 0, 1)).astype(np.float32)
    input_tensor = np.expand_dims(input_tensor, axis=0)
    return input_tensor

def postprocess_output(output, frame_shape):
    """
    Postprocess the model output to extract bounding boxes, class labels, and confidence scores.
    Args:
        output (np.ndarray): Raw output from the model.
        frame_shape (tuple): Original frame dimensions (height, width).
    Returns:
        list: List of detected objects, each containing bounding box, class label, and confidence score.
    """
    # Extract detections from model output (assuming a YOLO-style output format)
    # Note: Customize this based on your specific model's output format
    detections = []  # Placeholder for parsed detections
    for detection in output[0]:
        confidence = detection[4]
        if confidence > CONFIDENCE_THRESHOLD:
            class_id = int(detection[5:].argmax())
            class_name = CLASS_NAMES[class_id]
            x, y, w, h = detection[:4]  # Extract bounding box details
            frame_height, frame_width = frame_shape
            x = int(x * frame_width)
            y = int(y * frame_height)
            w = int(w * frame_width)
            h = int(h * frame_height)
            detections.append({"box": (x, y, w, h), "class": class_name, "confidence": confidence})
    return detections

def draw_detections(frame, detections):
    """
    Draw bounding boxes and labels on the original frame.
    Args:
        frame (np.ndarray): Original frame from the camera.
        detections (list): List of detected objects.
    """
    for detection in detections:
        x, y, w, h = detection["box"]
        class_name = detection["class"]
        confidence = detection["confidence"]
        # Draw bounding box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Add class label and confidence
        label = f"{class_name}: {confidence:.2f}"
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

def main():
    """
    Main function to run object detection using Tiny YOLOv2 with ONNX runtime and webcam feed.
    """
    # Initialize ONNX runtime
    try:
        session = ort.InferenceSession(MODEL_PATH)
        input_name = session.get_inputs()[0].name
    except Exception as e:
        print(f"Error loading ONNX model: {e}")
        return

    # Open webcam feed
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to access webcam.")
        return

    print("Press 'q' to exit...")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read frame.")
            break

        # Preprocess the frame
        input_tensor = preprocess_frame(frame)

        # Run inference
        try:
            output = session.run(None, {input_name: input_tensor})
        except Exception as e:
            print(f"Error during inference: {e}")
            continue

        # Postprocess output
        detections = postprocess_output(output, frame.shape[:2])

        # Draw detections on the frame
        draw_detections(frame, detections)

        # Display the frame
        cv2.imshow("Tiny YOLOv2 Object Detection", frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```
