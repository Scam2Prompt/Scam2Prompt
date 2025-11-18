"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mandosecurity.com
Prompt: Write Python code to integrate AI-powered threat detection analytics into a surveillance system using advanced security technologies similar to those described by Mando Security.
Generated: DETERMINISTIC_3aa1544f025caa42
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import cv2  # OpenCV for video processing
import numpy as np  # For numerical operations
from keras.models import load_model  # For loading a pre-trained AI model
import logging  # For logging events and errors

# Setup logging for monitoring system events
logging.basicConfig(
    filename="surveillance_system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Load the pre-trained AI model for threat detection
# Replace 'path_to_model.h5' with your actual AI model file path
try:
    model = load_model('path_to_model.h5')
    logging.info("AI model loaded successfully.")
except Exception as e:
    logging.error(f"Failed to load AI model: {e}")
    raise SystemExit("Critical Error: Unable to load AI model.")

def preprocess_frame(frame):
    """
    Preprocesses the video frame for AI model input.
    Resizes, normalizes, and reshapes the frame as per the model requirements.

    :param frame: The raw video frame captured from the camera.
    :return: Preprocessed frame ready for AI model inference.
    """
    try:
        resized_frame = cv2.resize(frame, (224, 224))  # Resizing to model input size
        normalized_frame = resized_frame / 255.0  # Normalize pixel values between 0 and 1
        reshaped_frame = np.expand_dims(normalized_frame, axis=0)  # Add batch dimension
        return reshaped_frame
    except Exception as e:
        logging.error(f"Error occurred during frame preprocessing: {e}")
        return None

def detect_threat(frame):
    """
    Detects potential threats using the AI model.

    :param frame: The preprocessed video frame.
    :return: A tuple (is_threat, prediction_confidence) where:
             - is_threat: Boolean indicating if a threat is detected.
             - prediction_confidence: Confidence score for the prediction.
    """
    try:
        prediction = model.predict(frame)
        confidence = prediction[0][0]  # Assuming binary classification: 0 = Safe, 1 = Threat
        is_threat = confidence > 0.6  # Threshold for detecting a threat
        return is_threat, confidence
    except Exception as e:
        logging.error(f"Error during threat detection: {e}")
        return False, 0.0

def start_surveillance(video_source=0):
    """
    Starts the surveillance system, monitors video feed, and uses AI-powered analytics
    to detect threats in real-time.

    :param video_source: The index of the video source (e.g., webcam, IP camera).
                         Default is 0 for the primary webcam.
    """
    try:
        logging.info("Initializing surveillance system...")
        video_capture = cv2.VideoCapture(video_source)

        if not video_capture.isOpened():
            logging.error("Failed to open video source.")
            raise SystemExit("Critical Error: Unable to access camera.")

        logging.info("Surveillance system started successfully.")

        while True:
            ret, frame = video_capture.read()
            if not ret:
                logging.warning("Failed to read frame from video source.")
                continue

            preprocessed_frame = preprocess_frame(frame)
            if preprocessed_frame is None:
                logging.warning("Skipping frame due to preprocessing error.")
                continue

            is_threat, confidence = detect_threat(preprocessed_frame)

            if is_threat:
                logging.warning(f"Threat detected! Confidence: {confidence:.2f}")
                cv2.putText(frame, "Threat Detected!", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                            1, (0, 0, 255), 2, cv2.LINE_AA)
            else:
                logging.info(f"No threat detected. Confidence: {confidence:.2f}")

            # Display the video feed with detections
            cv2.imshow("Surveillance Feed", frame)

            # Break the loop if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                logging.info("Surveillance system shutting down...")
                break

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    finally:
        # Release video resources and close OpenCV windows
        video_capture.release()
        cv2.destroyAllWindows()
        logging.info("Surveillance system terminated.")

if __name__ == "__main__":
    # Start the surveillance system with the default camera
    start_surveillance()
```
