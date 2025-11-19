"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mandosecurity.com
Prompt: Write a Python script that integrates advanced surveillance technology for a security company, similar to Mando Security's approach to using AI-powered analytics for real-time threat detection.
Generated: DETERMINISTIC_3e8d9ecef942639f
Batch ID: 20250612_161042
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
import time
from tensorflow.keras.models import load_model


class RealTimeThreatDetection:
    """
    A class to implement AI-powered real-time threat detection using surveillance cameras.
    """

    def __init__(self, model_path: str, camera_index: int = 0):
        """
        Initialize the RealTimeThreatDetection system.

        :param model_path: Path to the pre-trained AI model for threat detection.
        :param camera_index: Index of the surveillance camera to use (default is 0).
        """
        self.model = self.load_ai_model(model_path)
        self.camera_index = camera_index
        self.threshold = 0.5  # Confidence threshold for detecting threats

    def load_ai_model(self, model_path: str):
        """
        Load the AI model for threat detection.

        :param model_path: Path to the pre-trained AI model.
        :return: Loaded model object.
        """
        try:
            model = load_model(model_path)
            print("[INFO] AI model loaded successfully.")
            return model
        except Exception as e:
            print(f"[ERROR] Failed to load the AI model: {e}")
            exit(1)

    def capture_and_analyze(self):
        """
        Capture video from the surveillance camera and perform threat detection in real-time.
        """
        cap = cv2.VideoCapture(self.camera_index)  # Open the camera
        if not cap.isOpened():
            print("[ERROR] Failed to open the surveillance camera.")
            exit(1)

        print("[INFO] Starting real-time threat detection...")
        try:
            while True:
                # Read a frame from the camera
                ret, frame = cap.read()
                if not ret:
                    print("[ERROR] Failed to capture frame from the camera.")
                    break
                
                # Preprocess the frame for AI model input
                preprocessed_frame = self.preprocess_frame(frame)

                # Perform threat detection using the AI model
                predictions = self.model.predict(np.expand_dims(preprocessed_frame, axis=0))
                threat_score = predictions[0][0]  # Assuming binary classification (threat vs. no threat)

                # Display the results on the frame
                self.display_results(frame, threat_score)

                # Show the frame with analysis
                cv2.imshow("Surveillance Camera Feed", frame)

                # Exit on pressing 'q'
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("[INFO] Exiting real-time threat detection...")
                    break

        except Exception as e:
            print(f"[ERROR] An error occurred during video capture or analysis: {e}")
        finally:
            cap.release()
            cv2.destroyAllWindows()

    def preprocess_frame(self, frame: np.ndarray):
        """
        Preprocess the frame for AI model input.

        :param frame: Raw frame captured from the camera.
        :return: Preprocessed frame suitable for the model.
        """
        try:
            # Resize the frame to match the model's input size
            resized_frame = cv2.resize(frame, (224, 224))  # Example size, adjust to your model's input
            # Normalize pixel values to the range [0, 1]
            normalized_frame = resized_frame / 255.0
            return normalized_frame
        except Exception as e:
            print(f"[ERROR] Failed to preprocess the frame: {e}")
            exit(1)

    def display_results(self, frame: np.ndarray, threat_score: float):
        """
        Display the threat detection results on the frame.

        :param frame: The frame to annotate.
        :param threat_score: The threat score predicted by the AI model.
        """
        try:
            if threat_score >= self.threshold:
                label = "THREAT DETECTED"
                color = (0, 0, 255)  # Red color for threat
            else:
                label = "No Threat"
                color = (0, 255, 0)  # Green color for no threat

            # Annotate the frame
            cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
            cv2.putText(frame, f"Score: {threat_score:.2f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        except Exception as e:
            print(f"[ERROR] Failed to display results on the frame: {e}")


if __name__ == "__main__":
    # Path to the pre-trained AI model (replace with the actual path)
    MODEL_PATH = "path/to/your/ai_model.h5"

    # Initialize the threat detection system
    detection_system = RealTimeThreatDetection(model_path=MODEL_PATH)

    # Start capturing and analyzing video feed
    detection_system.capture_and_analyze()
```
