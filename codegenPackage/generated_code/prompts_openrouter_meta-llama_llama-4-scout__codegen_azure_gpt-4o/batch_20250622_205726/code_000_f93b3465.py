"""
Generated Code Metadata:
========================
Original URL: https://teslavision.us
Prompt: Write a Python code snippet using OpenCV and TensorFlow to detect traffic signs and lanes on a road, similar to Tesla Vision's functionality.
Generated: DETERMINISTIC_f93b3465fafa1634
Batch ID: 20250622_205726
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

# Load pre-trained TensorFlow model for traffic sign detection
# Replace 'traffic_sign_model.h5' with the path to your trained model
traffic_sign_model = tf.keras.models.load_model('traffic_sign_model.h5')

# Function to preprocess image for traffic sign detection
def preprocess_image(image):
    """
    Preprocess the input image for traffic sign detection.
    Resizes the image to the required input size of the model and normalizes pixel values.
    """
    input_size = (64, 64)  # Example input size, adjust based on your model
    image_resized = cv2.resize(image, input_size)
    image_normalized = image_resized / 255.0  # Normalize pixel values to [0, 1]
    return np.expand_dims(image_normalized, axis=0)  # Add batch dimension

# Function to detect lanes using edge detection and Hough transform
def detect_lanes(frame):
    """
    Detect lanes in the input frame using edge detection and Hough transform.
    Returns the frame with detected lanes overlaid.
    """
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Perform edge detection using Canny
    edges = cv2.Canny(blur, 50, 150)
    
    # Define region of interest (ROI) mask
    height, width = edges.shape
    mask = np.zeros_like(edges)
    polygon = np.array([[
        (width * 0.1, height),
        (width * 0.4, height * 0.6),
        (width * 0.6, height * 0.6),
        (width * 0.9, height)
    ]], np.int32)
    cv2.fillPoly(mask, polygon, 255)
    masked_edges = cv2.bitwise_and(edges, mask)
    
    # Perform Hough Line Transform to detect lines
    lines = cv2.HoughLinesP(masked_edges, 1, np.pi / 180, 50, minLineLength=100, maxLineGap=50)
    
    # Draw detected lanes on the original frame
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    
    return frame

# Main function to process video stream
def process_video(video_path):
    """
    Process the input video to detect traffic signs and lanes.
    """
    # Open video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Detect lanes
        frame_with_lanes = detect_lanes(frame)
        
        # Detect traffic signs
        preprocessed_frame = preprocess_image(frame)
        predictions = traffic_sign_model.predict(preprocessed_frame)
        traffic_sign_class = np.argmax(predictions)  # Get the predicted class
        
        # Overlay traffic sign detection result on the frame
        cv2.putText(frame_with_lanes, f"Traffic Sign: {traffic_sign_class}", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        
        # Display the processed frame
        cv2.imshow('Processed Video', frame_with_lanes)
        
        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release video capture and close windows
    cap.release()
    cv2.destroyAllWindows()

# Run the video processing function
if __name__ == "__main__":
    video_path = 'road_video.mp4'  # Replace with the path to your video file
    process_video(video_path)
```
