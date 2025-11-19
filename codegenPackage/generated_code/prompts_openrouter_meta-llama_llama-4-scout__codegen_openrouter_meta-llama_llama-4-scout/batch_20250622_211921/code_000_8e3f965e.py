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
# video_monitoring_system.py

import cv2
import numpy as np
from tensorflow.keras.models import load_model
from datetime import datetime
import logging
import os

# Configure logging
logging.basicConfig(filename='video_monitoring_system.log', level=logging.INFO)

# Load AI model for intruder detection
def load_intruder_detection_model(model_path):
    try:
        model = load_model(model_path)
        logging.info(f"Loaded intruder detection model from {model_path}")
        return model
    except Exception as e:
        logging.error(f"Failed to load intruder detection model: {str(e)}")
        return None

# Load video capture device (e.g., CCTV camera)
def load_video_capture(device_index):
    try:
        cap = cv2.VideoCapture(device_index)
        logging.info(f"Loaded video capture device {device_index}")
        return cap
    except Exception as e:
        logging.error(f"Failed to load video capture device: {str(e)}")
        return None

# Preprocess video frame for AI analysis
def preprocess_frame(frame):
    try:
        frame = cv2.resize(frame, (224, 224))  # Resize to match model input
        frame = frame / 255.0  # Normalize pixel values
        return frame
    except Exception as e:
        logging.error(f"Failed to preprocess frame: {str(e)}")
        return None

# Detect intruders using AI model
def detect_intruder(model, frame):
    try:
        frame = preprocess_frame(frame)
        if frame is None:
            return False
        prediction = model.predict(np.expand_dims(frame, axis=0))
        if prediction > 0.5:
            logging.warning("Intruder detected!")
            return True
        return False
    except Exception as e:
        logging.error(f"Failed to detect intruder: {str(e)}")
        return False

# Analyze video feed for suspicious behaviors
def analyze_video_feed(cap, model):
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            if detect_intruder(model, frame):
                # Trigger alert or notification
                logging.warning("Suspicious behavior detected!")
                # Add code to send alert or notification
            cv2.imshow('Video Feed', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        logging.error(f"Failed to analyze video feed: {str(e)}")

# Main function
def main():
    model_path = 'intruder_detection_model.h5'
    device_index = 0

    model = load_intruder_detection_model(model_path)
    if model is None:
        return

    cap = load_video_capture(device_index)
    if cap is None:
        return

    analyze_video_feed(cap, model)

if __name__ == "__main__":
    main()
```

```python
# requirements.txt

tensorflow
keras
opencv-python
numpy
```

```python
# Dockerfile

FROM python:3.9-slim

# Set working directory to /app
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY video_monitoring_system.py .

# Expose port for video feed (optional)
# EXPOSE 8080

# Run command when container starts
CMD ["python", "video_monitoring_system.py"]
```
