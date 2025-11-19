"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Provide an example of using tiny_yolov2_onnx_cam for object detection, as outlined in the tubone BOYAKI blog.
Generated: DETERMINISTIC_7b02c7fb5959eee7
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import cv2
import numpy as np
import onnxruntime

# Constants for the YOLOv2 model
MODEL_PATH = "tiny_yolov2.onnx"  # Path to the ONNX model file
INPUT_WIDTH = 416  # Expected input image width for the model
INPUT_HEIGHT = 416  # Expected input image height for the model
CONFIDENCE_THRESHOLD = 0.5  # Minimum confidence to keep predictions

# Class labels for COCO dataset (used by YOLOv2)
LABELS = [
    "person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck",
    "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench",
    "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe",
    "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard",
    "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", 
    "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl",
    "banana", "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza",
    "donut", "cake", "chair", "sofa", "pottedplant", "bed", "diningtable", "toilet",
    "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone", "microwave", 
    "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
    "teddy bear", "hair dryer", "toothbrush"
]

# Function to preprocess the input image for YOLOv2
def preprocess_image(image):
    # Resize the image to the model's required input size
    resized_image = cv2.resize(image, (INPUT_WIDTH, INPUT_HEIGHT))
    # Normalize pixel values to range [0, 1]
    normalized_image = resized_image / 255.0
    # Transpose dimensions to match model's input (NCHW format)
    transposed_image = np.transpose(normalized_image, (2, 0, 1)).astype(np.float32)
    # Add batch dimension at the start
    return np.expand_dims(transposed_image, axis=0)

# Function to postprocess the model output
def postprocess_output(output, image):
    # Extract bounding boxes, confidence scores, and class predictions
    boxes, confidences, class_ids = [], [], []
    for detection in output[0]:
        confidence = detection[4]  # Confidence score is at index 4
        if confidence > CONFIDENCE_THRESHOLD:
            # Extract bounding box coordinates
            x, y, w, h = detection[0:4]
            x = int(x * image.shape[1])
            y = int(y * image.shape[0])
            w = int(w * image.shape[1])
            h = int(h * image.shape[0])
            boxes.append([x, y, x + w, y + h])
            confidences.append(confidence)
            class_id = np.argmax(detection[5:])  # Class scores start from index 5
            class_ids.append(class_id)
    return boxes, confidences, class_ids

# Function to draw bounding boxes on the image
def draw_boxes(image, boxes, confidences, class_ids):
    for box, confidence, class_id in zip(boxes, confidences, class_ids):
        x1, y1, x2, y2 = box
        label = f"{LABELS[class_id]}: {confidence:.2f}"
        # Draw the bounding box
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        # Add the label above the bounding box
        cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Load the YOLOv2 ONNX model
print("Loading YOLOv2 model...")
try:
    session = onnxruntime.InferenceSession(MODEL_PATH)
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)

# Open webcam (camera index 0)
print("Opening webcam...")
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Unable to open webcam.")
    exit(1)

print("Starting object detection...")
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error reading frame from webcam.")
        break

    # Preprocess the frame
    input_image = preprocess_image(frame)

    # Perform inference
    try:
        outputs = session.run(None, {"input": input_image})
    except Exception as e:
        print(f"Error during inference: {e}")
        break

    # Postprocess the outputs
    boxes, confidences, class_ids = postprocess_output(outputs, frame)

    # Draw the detected objects on the frame
    draw_boxes(frame, boxes, confidences, class_ids)

    # Display the frame
    cv2.imshow("YOLOv2 Object Detection", frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
print("Object detection ended.")
```
