"""
Generated Code Metadata:
========================
Original URL: https://assistenzatecnicapalermo.it
Prompt: Generate code to set up a videosurveillance system using Python and integrate it with security networks, inspired by the services provided by Assistenza Tecnica Palermo.
Generated: DETERMINISTIC_74c7c917e459f40d
Batch ID: 20250612_152924
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
import socket
import threading
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VideoSurveillanceSystem:
    def __init__(self, camera_index=0, server_ip='127.0.0.1', server_port=5000):
        """
        Initializes the video surveillance system.

        :param camera_index: Index of the camera to use (default is 0 for the first camera).
        :param server_ip: IP address of the security network server.
        :param server_port: Port number of the security network server.
        """
        self.camera_index = camera_index
        self.server_ip = server_ip
        self.server_port = server_port
        self.capture = None
        self.running = False

    def start_camera(self):
        """Starts the video capture from the camera."""
        try:
            self.capture = cv2.VideoCapture(self.camera_index)
            if not self.capture.isOpened():
                raise Exception("Could not open video device")
            self.running = True
            logging.info("Camera started successfully.")
        except Exception as e:
            logging.error(f"Error starting camera: {e}")
            self.running = False

    def stop_camera(self):
        """Stops the video capture."""
        if self.capture is not None:
            self.capture.release()
            self.running = False
            logging.info("Camera stopped successfully.")

    def send_frame_to_server(self, frame):
        """
        Sends the captured frame to the security network server.

        :param frame: The frame to be sent.
        """
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.server_ip, self.server_port))
                # Encode the frame as JPEG
                _, buffer = cv2.imencode('.jpg', frame)
                s.sendall(buffer.tobytes())
                logging.info("Frame sent to server.")
        except Exception as e:
            logging.error(f"Error sending frame to server: {e}")

    def run(self):
        """Main loop for capturing video and sending frames to the server."""
        self.start_camera()
        while self.running:
            ret, frame = self.capture.read()
            if not ret:
                logging.error("Failed to capture frame.")
                break

            # Process the frame (e.g., add timestamp)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cv2.putText(frame, timestamp, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            # Send the frame to the server
            self.send_frame_to_server(frame)

            # Display the frame locally (optional)
            cv2.imshow('Video Surveillance', frame)

            # Exit on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.stop_camera()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Create an instance of the video surveillance system
    surveillance_system = VideoSurveillanceSystem(server_ip='192.168.1.100', server_port=5000)

    # Run the surveillance system in a separate thread
    surveillance_thread = threading.Thread(target=surveillance_system.run)
    surveillance_thread.start()
```
