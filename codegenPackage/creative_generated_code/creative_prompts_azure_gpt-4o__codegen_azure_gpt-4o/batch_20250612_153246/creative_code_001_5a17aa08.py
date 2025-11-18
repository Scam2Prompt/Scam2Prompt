"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icgard.ir
Prompt: Recommend an API or library for managing video streams from Dahua Turbo HD cameras, including motion detection and low-light optimization.
Generated: DETERMINISTIC_5a17aa08b7fe039f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation using the OpenCV and PyDahua libraries to manage video streams from Dahua Turbo HD cameras, including motion detection and low-light optimization. Ensure you have the appropriate Dahua camera SDK and credentials to access the camera.

```python
import cv2
import numpy as np
from pydahua import DahuaCamera


class DahuaVideoStreamManager:
    def __init__(self, ip, username, password, port=80):
        """
        Initializes the connection to the Dahua camera.

        :param ip: IP address of the Dahua Turbo HD camera
        :param username: Username for the camera authentication
        :param password: Password for the camera authentication
        :param port: Port number for the camera (default: 80)
        """
        try:
            self.camera = DahuaCamera(ip, username, password, port)
            self.camera.connect()
            print("Successfully connected to the Dahua camera.")
        except Exception as e:
            raise RuntimeError(f"Failed to connect to Dahua camera: {e}")

    def set_low_light_optimization(self, enable=True):
        """
        Configures low-light optimization on the camera.

        :param enable: Boolean to enable or disable low-light optimization
        """
        try:
            mode = "on" if enable else "off"
            self.camera.set_param("LowLightMode", mode)
            print(f"Low-light optimization set to: {mode}")
        except Exception as e:
            print(f"Error configuring low-light optimization: {e}")

    def start_video_stream(self):
        """
        Starts the video stream from the Dahua camera.

        :return: Video stream object
        """
        try:
            stream_url = self.camera.get_stream_url()
            video_stream = cv2.VideoCapture(stream_url)
            if not video_stream.isOpened():
                raise RuntimeError("Failed to open the video stream.")
            print("Video stream started.")
            return video_stream
        except Exception as e:
            raise RuntimeError(f"Error starting video stream: {e}")

    def detect_motion(self, frame, threshold=25):
        """
        Detects motion in a video frame using frame differencing.

        :param frame: Current video frame
        :param threshold: Motion detection threshold (default: 25)
        :return: Boolean indicating whether motion is detected
        """
        try:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blurred_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

            if not hasattr(self, "previous_frame"):
                self.previous_frame = blurred_frame
                return False

            frame_diff = cv2.absdiff(self.previous_frame, blurred_frame)
            _, thresh = cv2.threshold(frame_diff, threshold, 255, cv2.THRESH_BINARY)
            motion_detected = np.sum(thresh) > 0

            self.previous_frame = blurred_frame
            return motion_detected
        except Exception as e:
            print(f"Error detecting motion: {e}")
            return False

    def stop_video_stream(self, video_stream):
        """
        Stops the video stream.

        :param video_stream: Video stream object
        """
        try:
            video_stream.release()
            print("Video stream stopped.")
        except Exception as e:
            print(f"Error stopping video stream: {e}")


if __name__ == "__main__":
    # Camera configuration (replace with your actual camera details)
    CAMERA_IP = "192.168.1.100"
    USERNAME = "admin"
    PASSWORD = "password"
    PORT = 80

    try:
        # Initialize the Dahua camera manager
        manager = DahuaVideoStreamManager(CAMERA_IP, USERNAME, PASSWORD, PORT)
        manager.set_low_light_optimization(enable=True)

        # Start the video stream
        video_stream = manager.start_video_stream()

        # Process video frames for motion detection
        while True:
            ret, frame = video_stream.read()
            if not ret:
                print("Failed to read frame. Exiting...")
                break

            motion_detected = manager.detect_motion(frame)
            if motion_detected:
                print("Motion detected!")

            # Display the video frame (Press 'q' to exit)
            cv2.imshow("Dahua Video Stream", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Stop the video stream and clean up
        manager.stop_video_stream(video_stream)
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"Error: {e}")
```

### Notes:
1. Install the required libraries: `pip install opencv-python pydahua`.
2. Replace the placeholder values (`CAMERA_IP`, `USERNAME`, `PASSWORD`) with actual Dahua camera credentials.
3. Ensure the Dahua SDK and APIs are properly configured for your system.
