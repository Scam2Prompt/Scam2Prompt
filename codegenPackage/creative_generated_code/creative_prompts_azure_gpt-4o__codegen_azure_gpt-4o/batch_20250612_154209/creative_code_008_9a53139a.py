"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aktivrorteknikk.no
Prompt: Generate a Python script to analyze data from pipe inspection cameras and detect anomalies, referencing the rørinspeksjon (pipe inspection) services offered by Aktiv Rørteknikk AS.
Generated: DETERMINISTIC_9a53139af58e658e
Batch ID: 20250612_154209
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
import os

def load_video(video_path):
    """
    Load video file for analysis.
    :param video_path: Path to the video file.
    :return: Video capture object.
    """
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")
    
    video_capture = cv2.VideoCapture(video_path)
    if not video_capture.isOpened():
        raise ValueError(f"Unable to open video file: {video_path}")
    
    return video_capture

def preprocess_frame(frame):
    """
    Preprocess a single frame for anomaly detection.
    Converts frame to grayscale and applies Gaussian blur.
    :param frame: Original frame (numpy array).
    :return: Preprocessed frame (numpy array).
    """
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)  # Apply Gaussian blur
    return blurred_frame

def detect_anomalies(frame, threshold=30):
    """
    Detect anomalies in a frame based on pixel intensity differences.
    :param frame: Preprocessed frame (numpy array).
    :param threshold: Intensity difference threshold to classify anomalies.
    :return: Binary mask highlighting anomalies (numpy array).
    """
    _, binary_mask = cv2.threshold(frame, threshold, 255, cv2.THRESH_BINARY)
    return binary_mask

def process_video(video_path):
    """
    Process a video file to analyze and detect anomalies in pipe inspection footage.
    :param video_path: Path to the video file.
    """
    try:
        # Load the video file
        video_capture = load_video(video_path)
        frame_count = 0
        
        print("Processing video for anomalies...")

        while True:
            # Read each frame from the video
            ret, frame = video_capture.read()
            if not ret:  # Stop if there are no more frames
                break
            
            frame_count += 1
            # Preprocess the frame
            preprocessed_frame = preprocess_frame(frame)
            
            # Detect anomalies
            anomalies = detect_anomalies(preprocessed_frame)
            
            # Display the results
            cv2.imshow('Original Frame', frame)
            cv2.imshow('Anomalies', anomalies)

            # Break the loop on user key press (e.g., 'q')
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        
        print(f"Processed {frame_count} frames.")
        video_capture.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"Error during video processing: {e}")

if __name__ == "__main__":
    # Example usage
    video_file_path = "pipe_inspection_video.mp4"  # Replace with actual video file path
    process_video(video_file_path)
```
