"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nvidiatechnologies.com
Prompt: Write Python code to implement real-time threat detection and motion alerts using AI-powered camera analytics, as described by Nvidia Technologies' AI Surveillance Systems.
Generated: DETERMINISTIC_234a568a6be0c8c3
Batch ID: 20250612_151100
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
from threading import Thread
from tensorflow.keras.models import load_model

class AIThreatDetection:
    def __init__(self, camera_source=0, model_path="threat_detection_model.h5"):
        """
        Initialize the AI-powered threat detection system.

        :param camera_source: The source of the camera feed (default is 0 for webcam).
        :param model_path: Path to the pre-trained AI model for threat detection.
        """
        self.camera_source = camera_source
        self.model_path = model_path
        self.model = None
        self.running = False

    def load_model(self):
        """
        Load the pre-trained AI model for threat detection.
        """
        try:
            self.model = load_model(self.model_path)
            print("[INFO] AI model loaded successfully.")
        except Exception as e:
            print(f"[ERROR] Failed to load model: {e}")
            exit(1)  # Exit if the model cannot be loaded.

    def start_camera_feed(self):
        """
        Start the camera feed and process frames for threat detection.
        """
        self.running = True
        video_capture = cv2.VideoCapture(self.camera_source)

        if not video_capture.isOpened():
            print("[ERROR] Unable to access camera.")
            self.running = False
            return

        print("[INFO] Camera feed started.")
        while self.running:
            ret, frame = video_capture.read()

            if not ret:
                print("[WARNING] Unable to fetch frame from camera.")
                continue

            # Preprocess the frame for AI model
            processed_frame = self.preprocess_frame(frame)

            # Perform threat detection using AI model
            detection_result = self.detect_threat(processed_frame)

            # Handle the detection result and display alerts
            self.handle_detection_result(frame, detection_result)

            # Display the processed frame
            cv2.imshow("AI Surveillance Feed", frame)

            # Exit when 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("[INFO] Stopping camera feed.")
                self.running = False

        video_capture.release()
        cv2.destroyAllWindows()

    def preprocess_frame(self, frame):
        """
        Preprocess the camera frame for AI model input.

        :param frame: Raw frame from the camera.
        :return: Preprocessed frame as a NumPy array.
        """
        try:
            resized_frame = cv2.resize(frame, (224, 224))  # Resize to model input size
            normalized_frame = resized_frame / 255.0  # Normalize pixel values
            return np.expand_dims(normalized_frame, axis=0)  # Add batch dimension
        except Exception as e:
            print(f"[ERROR] Frame preprocessing failed: {e}")
            return None

    def detect_threat(self, processed_frame):
        """
        Perform threat detection using the AI model.

        :param processed_frame: Preprocessed frame ready for model input.
        :return: Detection result as a dictionary.
        """
        try:
            if processed_frame is None:
                return {"error": "Invalid frame data"}

            predictions = self.model.predict(processed_frame)
            # Assuming the model outputs a probability score for threats
            threat_probability = predictions[0][0]  # Example: first class is "threat"
            return {"threat": threat_probability > 0.5, "confidence": threat_probability}
        except Exception as e:
            print(f"[ERROR] Threat detection failed: {e}")
            return {"error": "Model inference error"}

    def handle_detection_result(self, frame, detection_result):
        """
        Handle the threat detection result and display appropriate alerts.

        :param frame: Original camera frame.
        :param detection_result: Result from AI model.
        """
        try:
            if "error" in detection_result:
                return  # Skip processing if there was an error

            if detection_result["threat"]:
                confidence = detection_result["confidence"]
                alert_text = f"THREAT DETECTED! Confidence: {confidence:.2f}"
                print("[ALERT]", alert_text)
                cv2.putText(frame, alert_text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            else:
                cv2.putText(frame, "No Threat Detected", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        except Exception as e:
            print(f"[WARNING] Failed to handle detection result: {e}")

    def stop(self):
        """
        Stop the threat detection system gracefully.
        """
        self.running = False


if __name__ == "__main__":
    # Initialize and run the AI threat detection system
    threat_detection_system = AIThreatDetection(model_path="your_threat_detection_model.h5")
    threat_detection_system.load_model()

    # Start the camera feed in a separate thread
    camera_thread = Thread(target=threat_detection_system.start_camera_feed)
    camera_thread.start()

    # Allow manual stop using keyboard interrupt
    try:
        while camera_thread.is_alive():
            time.sleep(1)  # Keep the main thread alive
    except KeyboardInterrupt:
        print("[INFO] Keyboard interrupt received. Stopping the system...")
        threat_detection_system.stop()
        camera_thread.join()
```

Make sure to replace `"your_threat_detection_model.h5"` with the actual path to your pre-trained AI model. Also, ensure that the AI model accepts a 224x224x3 input if you're using the given preprocessing logic.
