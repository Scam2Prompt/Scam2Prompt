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
import cv2
import numpy as np
import onnxruntime as ort

# Load the ONNX model
model_path = "tiny_yolov2.onnx"
session = ort.InferenceSession(model_path)

# Define the input dimensions and class names for the model
input_shape = (1, 3, 416, 416)  # Batch size, Channels, Height, Width
class_names = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", 
               "train", "truck", "boat", "traffic light", "fire hydrant", 
               "stop sign", "parking meter", "bench", "bird", "cat", "dog", 
               "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", 
               "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", 
               "skis", "snowboard", "sports ball", "kite", "baseball bat", 
               "baseball glove", "skateboard", "surfboard", "tennis racket", 
               "bottle", "wine glass", "cup", "fork", "knife", "spoon", 
               "bowl", "banana", "apple", "sandwich", "orange", "broccoli", 
               "carrot", "hot dog", "pizza", "donut", "cake", "chair", 
               "couch", "potted plant", "bed", "dining table", "toilet", 
               "TV", "laptop", "mouse", "remote", "keyboard", "cell phone", 
               "microwave", "oven", "toaster", "sink", "refrigerator", 
               "book", "clock", "vase", "scissors", "teddy bear", "hair drier", 
               "toothbrush"]

# Function to preprocess the image
def preprocess_image(image):
    """
    Preprocess the input image to satisfy the model input requirements.
    
    Parameters:
        image (numpy.ndarray): The input image to preprocess.
    
    Returns:
        numpy.ndarray: Preprocessed image.
    """
    # Resize the image to 416x416 pixels
    image_resized = cv2.resize(image, (416, 416))
    # Normalize the image to [0, 1]
    image_normalized = image_resized.astype(np.float32) / 255.0
    # Transpose the image from HWC to CHW format
    image_transposed = np.transpose(image_normalized, (2, 0, 1))
    # Add a batch dimension
    return np.expand_dims(image_transposed, axis=0)

# Function to draw bounding boxes on the image
def draw_bounding_boxes(image, boxes, confidences, class_ids):
    """
    Draw bounding boxes on the image.

    Parameters:
        image (numpy.ndarray): The original image.
        boxes (list): List of bounding boxes.
        confidences (list): List of confidence scores.
        class_ids (list): List of class IDs.
    
    Returns:
        numpy.ndarray: Image with bounding boxes drawn.
    """
    for box, confidence, class_id in zip(boxes, confidences, class_ids):
        x, y, w, h = box
        # Draw rectangle for detected object
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Prepare label with class name and confidence
        label = f"{class_names[class_id]}: {confidence:.2f}"
        # Draw label
        cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                    0.5, (0, 255, 0), 2)
    return image

# Main function for object detection using webcam
def main():
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame.")
                break
            
            # Preprocess the frame
            input_tensor = preprocess_image(frame)

            # Run inference
            outputs = session.run(None, {session.get_inputs()[0].name: input_tensor})

            # Extract bounding box coordinates, confidences, and class IDs
            boxes, confidences, class_ids = [], [], []
            for output in outputs:
                for detection in output:
                    confidence = detection[4]
                    if confidence > 0.5:  # Threshold for confidence
                        class_id = int(detection[5])
                        x1, y1, x2, y2 = int(detection[0] * frame.shape[1]), \
                                         int(detection[1] * frame.shape[0]), \
                                         int(detection[2] * frame.shape[1]), \
                                         int(detection[3] * frame.shape[0])
                        boxes.append([x1, y1, x2 - x1, y2 - y1])  # Convert to (x, y, width, height)
                        confidences.append(float(confidence))
                        class_ids.append(class_id)

            # Draw bounding boxes on the frame
            frame_with_boxes = draw_bounding_boxes(frame, boxes, confidences, class_ids)

            # Display the frame
            cv2.imshow('Object Detection', frame_with_boxes)

            # Exit on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Release resources
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```
