"""
Generated Code Metadata:
========================
Original URL: https://www.vatio.cl
Prompt: "Write a Python script to implement a 24/7 video monitoring system with AI-powered analytics for detecting intruders and suspicious behaviors, as described in VATIO's Vigilancia Inteligente stage."
Generated: DETERMINISTIC_8e3f965e96199a82
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import cv2
import time
import threading
import numpy as np
from datetime import datetime
from tensorflow.keras.models import load_model

# Load pre-trained AI model for intruder detection
# Replace 'model_path' with the actual path to your trained model
MODEL_PATH = 'model_path'
try:
    model = load_model(MODEL_PATH)
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)

# Define constants
VIDEO_SOURCE = 0  # Default to webcam; replace with video file path or IP camera URL if needed
OUTPUT_DIR = 'output_videos'  # Directory to save recorded videos
ALERT_THRESHOLD = 0.8  # Confidence threshold for detecting intruders
RECORD_DURATION = 10  # Duration (in seconds) to record after detecting an intruder

# Ensure output directory exists
import os
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def analyze_frame(frame):
    """
    Analyze a single video frame using the AI model.
    :param frame: The video frame to analyze.
    :return: Tuple (is_intruder_detected, confidence_score)
    """
    try:
        # Preprocess the frame for the AI model
        resized_frame = cv2.resize(frame, (224, 224))  # Resize to model input size
        normalized_frame = resized_frame / 255.0  # Normalize pixel values
        input_data = np.expand_dims(normalized_frame, axis=0)  # Add batch dimension

        # Predict using the AI model
        predictions = model.predict(input_data)
        confidence_score = predictions[0][0]  # Assuming binary classification (0: no intruder, 1: intruder)

        return confidence_score >= ALERT_THRESHOLD, confidence_score
    except Exception as e:
        print(f"Error analyzing frame: {e}")
        return False, 0.0

def record_video(video_writer, duration):
    """
    Record video for a specified duration.
    :param video_writer: OpenCV VideoWriter object.
    :param duration: Duration in seconds to record.
    """
    start_time = time.time()
    while time.time() - start_time < duration:
        ret, frame = cap.read()
        if not ret:
            print("Error reading video frame during recording.")
            break
        video_writer.write(frame)

# Initialize video capture
cap = cv2.VideoCapture(VIDEO_SOURCE)
if not cap.isOpened():
    print("Error: Unable to open video source.")
    exit(1)

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS)) if cap.get(cv2.CAP_PROP_FPS) > 0 else 30

print("Video monitoring system started. Press 'q' to exit.")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error reading video frame.")
            break

        # Analyze the current frame
        is_intruder, confidence = analyze_frame(frame)

        if is_intruder:
            print(f"Intruder detected! Confidence: {confidence:.2f}")

            # Generate a unique filename for the recorded video
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            video_filename = os.path.join(OUTPUT_DIR, f"intruder_{timestamp}.avi")

            # Initialize video writer
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            video_writer = cv2.VideoWriter(video_filename, fourcc, fps, (frame_width, frame_height))

            # Record video
            record_thread = threading.Thread(target=record_video, args=(video_writer, RECORD_DURATION))
            record_thread.start()

        # Display the video feed
        cv2.imshow('Video Monitoring', frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    print("Video monitoring system interrupted by user.")
finally:
    # Release resources
    cap.release()
    cv2.destroyAllWindows()
    print("Video monitoring system stopped.")
```
