"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://donturesystems.co.ke
Prompt: Generate code to set up a CCTV surveillance system that features night vision, motion detection, and AI-powered analytics, similar to the systems provided by Donture Systems Ltd.
Generated: DETERMINISTIC_77f6400d53019967
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python code example for setting up a CCTV surveillance system with night vision support, motion detection, and AI-powered analytics. This code uses libraries such as OpenCV, TensorFlow/Keras for AI analytics, and supports error handling. (Note: Actual implementation might vary based on hardware and software requirements).

```python
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import datetime
import os

# Constants
MODEL_PATH = 'ai_model.h5'  # Path to a pre-trained AI model for analytics
VIDEO_SOURCE = 0  # Use 0 for default webcam, or replace with actual CCTV camera source
OUTPUT_DIR = 'recordings'  # Directory to store recorded videos

# Ensure output directory exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Function to initialize AI model
def load_ai_model(model_path):
    try:
        model = load_model(model_path)
        return model
    except Exception as e:
        print(f"Error loading AI model: {e}")
        return None

# Function for motion detection
def detect_motion(frame, previous_frame):
    try:
        # Convert frames to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_previous = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)

        # Compute absolute difference between current and previous frame
        delta = cv2.absdiff(gray_previous, gray_frame)

        # Thresholding to highlight areas of motion
        _, thresh = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)

        # Dilate the threshold image to fill in holes
        dilated = cv2.dilate(thresh, None, iterations=2)

        # Find contours (areas of motion)
        contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Return True if motion detected
        return len(contours) > 0
    except Exception as e:
        print(f"Error in motion detection: {e}")
        return False

# Function for AI-powered analytics (e.g., detecting objects in a frame)
def perform_ai_analytics(frame, model):
    try:
        # Preprocess the frame for the AI model
        resized_frame = cv2.resize(frame, (224, 224))  # Resize to model's input size
        preprocessed_frame = np.expand_dims(resized_frame / 255.0, axis=0)  # Normalize and add batch dimension

        # Predict using the model
        predictions = model.predict(preprocessed_frame)

        # Return predictions (e.g., object classes and probabilities)
        return predictions
    except Exception as e:
        print(f"Error in AI analytics: {e}")
        return None

# Main function to start surveillance system
def start_surveillance(video_source, model):
    try:
        # Initialize video capture
        cap = cv2.VideoCapture(video_source)
        if not cap.isOpened():
            raise ValueError("Unable to access the camera/video source")

        # Initialize AI model
        ai_model = load_ai_model(model)

        # Previous frame for motion detection
        previous_frame = None

        # Video writer for recording
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = os.path.join(OUTPUT_DIR, f'cctv_{timestamp}.avi')
        out = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))

        print("CCTV Surveillance System is running. Press 'q' to exit.")

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error reading from the video source.")
                break

            # Night vision (convert to grayscale for low-light environments)
            night_vision_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            night_vision_frame = cv2.cvtColor(night_vision_frame, cv2.COLOR_GRAY2BGR)

            # Motion detection
            motion_detected = False
            if previous_frame is not None:
                motion_detected = detect_motion(frame, previous_frame)

            # AI-powered analytics
            if ai_model:
                predictions = perform_ai_analytics(frame, ai_model)
                # (Optional) Process predictions here (e.g., draw bounding boxes or labels)

            # Display frame with optional enhancements (e.g., night vision effects)
            cv2.imshow("CCTV Surveillance", night_vision_frame if motion_detected else frame)

            # Record video
            out.write(frame)

            # Update previous frame
            previous_frame = frame.copy()

            # Exit on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release resources
        cap.release()
        out.release()
        cv2.destroyAllWindows()
        print("Surveillance system stopped.")

    except Exception as e:
        print(f"An error occurred in the surveillance system: {e}")

# Run the surveillance system
if __name__ == '__main__':
    start_surveillance(VIDEO_SOURCE, MODEL_PATH)
```

### Notes:
1. **Night Vision:** Implemented as grayscale enhancement.
2. **Motion Detection:** Uses image difference technique.
3. **AI Analytics:** Assumes a pre-trained model is available for object detection or other analytics.
4. **Error Handling:** Errors are caught and logged.
5. **Recording:** Video frames are saved in the specified directory.

Make sure to install the required libraries (`opencv-python`, `tensorflow`, etc.) and have a compatible AI model (`ai_model.h5`) ready for analytics.
