"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigen.io
Prompt: Provide code to integrate Eigen's thermal imaging AI solution for real-time anomaly detection in metal welding applications.
Generated: DETERMINISTIC_b086b432693f1b33
Batch ID: 20250612_151610
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

class ThermalAnomalyDetector:
    """
    A class to implement real-time anomaly detection in metal welding applications using thermal imaging.
    """

    def __init__(self, model_path):
        """
        Initializes the ThermalAnomalyDetector with the provided AI model path.

        :param model_path: str - Path to the pretrained AI model for anomaly detection.
        """
        self.model_path = model_path
        self.model = self.load_model()

    def load_model(self):
        """
        Loads the AI model for anomaly detection.

        :return: model - Loaded AI model.
        """
        try:
            model = cv2.dnn.readNetFromONNX(self.model_path)
            return model
        except Exception as e:
            raise RuntimeError(f"Failed to load model from {self.model_path}: {e}")

    def preprocess_frame(self, frame):
        """
        Preprocesses the input frame for the AI model.

        :param frame: np.ndarray - The input thermal image frame.
        :return: np.ndarray - Preprocessed frame ready for model inference.
        """
        # Resize and normalize the frame
        blob = cv2.dnn.blobFromImage(frame, 1/255.0, (224, 224), (0, 0, 0), swapRB=True, crop=False)
        return blob

    def detect_anomalies(self, frame):
        """
        Detects anomalies in the provided thermal image frame.

        :param frame: np.ndarray - The input thermal image frame.
        :return: str - Anomaly detection result.
        """
        try:
            blob = self.preprocess_frame(frame)

            # Set the input to the model
            self.model.setInput(blob)
            output = self.model.forward()

            # Check model output for anomalies
            if output[0][1] > 0.5:  # Assuming index 1 indicates anomaly probability
                return "Anomaly Detected"
            else:
                return "No Anomaly Detected"
        except Exception as e:
            raise RuntimeError(f"Error during anomaly detection: {e}")

    def start_detection(self, video_source=0):
        """
        Starts the real-time anomaly detection process from the specified video source.

        :param video_source: int or str - Index of the camera or path to the video file.
        """
        cap = cv2.VideoCapture(video_source)

        if not cap.isOpened():
            raise RuntimeError(f"Failed to open video source: {video_source}")

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Perform anomaly detection
            result = self.detect_anomalies(frame)
            
            # Display the result on the frame
            cv2.putText(frame, result, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Show the frame with result
            cv2.imshow("Thermal Anomaly Detection", frame)

            # Exit on pressing 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release resources
        cap.release()
        cv2.destroyAllWindows()

# Example usage:
if __name__ == "__main__":
    try:
        # Replace 'path_to_model.onnx' with the actual model file path
        detector = ThermalAnomalyDetector(model_path='path_to_model.onnx')
        detector.start_detection(video_source=0)  # Use 0 for webcam or provide video file path
    except Exception as e:
        print(f"An error occurred: {e}")
```
