"""
Generated Code Metadata:
========================
Original URL: https://donturesystems.co.ke
Prompt: Generate code to set up a CCTV surveillance system that features night vision, motion detection, and AI-powered analytics, similar to the systems provided by Donture Systems Ltd.
Generated: DETERMINISTIC_77f6400d53019967
Batch ID: 20250612_162051
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
import time
from datetime import datetime
from tensorflow.keras.models import load_model

# Load pre-trained AI model for analytics (e.g., object detection, face recognition)
# Replace 'ai_model.h5' with the actual model file path
AI_MODEL_PATH = 'ai_model.h5'
ai_model = load_model(AI_MODEL_PATH)

# Initialize the video capture (0 for default camera, or replace with CCTV camera IP)
VIDEO_SOURCE = 0
cap = cv2.VideoCapture(VIDEO_SOURCE)

# Check if the video source is opened successfully
if not cap.isOpened():
    raise Exception("Error: Unable to access the video source.")

# Define parameters for motion detection
motion_threshold = 25  # Minimum pixel intensity difference to detect motion
min_contour_area = 500  # Minimum area of motion to consider
background_subtractor = cv2.createBackgroundSubtractorMOG2()

# Define parameters for night vision
IR_LIGHT_THRESHOLD = 50  # Threshold for low-light detection (adjust as needed)

# Define output video writer for recording
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_filename = f"surveillance_{datetime.now().strftime('%Y%m%d_%H%M%S')}.avi"
out = cv2.VideoWriter(output_filename, fourcc, 20.0, (640, 480))

# Main loop for surveillance
try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read frame from video source.")
            break

        # Convert frame to grayscale for night vision and motion detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Night vision: Enhance low-light frames
        if np.mean(gray_frame) < IR_LIGHT_THRESHOLD:
            frame = cv2.cvtColor(cv2.equalizeHist(gray_frame), cv2.COLOR_GRAY2BGR)

        # Motion detection
        fg_mask = background_subtractor.apply(gray_frame)
        _, thresh = cv2.threshold(fg_mask, motion_threshold, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        motion_detected = False
        for contour in contours:
            if cv2.contourArea(contour) > min_contour_area:
                motion_detected = True
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # AI-powered analytics (e.g., object detection)
        # Preprocess the frame for the AI model
        resized_frame = cv2.resize(frame, (224, 224))  # Adjust size based on model input
        normalized_frame = resized_frame / 255.0  # Normalize pixel values
        input_data = np.expand_dims(normalized_frame, axis=0)

        # Perform inference
        predictions = ai_model.predict(input_data)
        # Process predictions (this will depend on the specific AI model used)
        # Example: Display detected objects or events
        # (Assume the model outputs a list of detected objects with labels and confidence scores)
        for prediction in predictions:
            label, confidence = prediction['label'], prediction['confidence']
            if confidence > 0.5:  # Display only confident predictions
                cv2.putText(frame, f"{label}: {confidence:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        # Display the frame
        cv2.imshow('CCTV Surveillance', frame)

        # Record the frame to the output video file
        out.write(frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()
```
