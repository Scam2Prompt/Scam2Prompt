"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.prointegrationfuture.asia
Prompt: Generate code to create a real-time AV system that integrates immersive technologies, similar to the solutions demonstrated at Pro Integration Future Asia.
Generated: DETERMINISTIC_e472fd79c85e33df
Batch ID: 20250612_145234
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
import socket
import threading

# Define constants for the server
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

class AVSystem:
    def __init__(self):
        """Initialize the AV system with parameters for video capture and networking."""
        self.capture = cv2.VideoCapture(0)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Check if the camera opened successfully
        if not self.capture.isOpened():
            raise Exception("Could not open video device")

        # Set video frame width and height
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def start_video_stream(self):
        """Start streaming video frames in a separate thread."""
        threading.Thread(target=self.stream_video, daemon=True).start()

    def stream_video(self):
        """Capture video frames and send them over UDP."""
        while True:
            ret, frame = self.capture.read()
            if not ret:
                print("Failed to capture frame")
                break
            
            # Encode the frame to JPEG format
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
            result, frame_encoded = cv2.imencode('.jpg', frame, encode_param)

            if not result:
                print("Failed to encode frame")
                continue
            
            # Send the encoded frame via UDP
            try:
                self.sock.sendto(frame_encoded.tobytes(), (UDP_IP, UDP_PORT))
            except Exception as e:
                print(f"Error sending frame: {e}")

    def stop(self):
        """Release the video capture and close the socket."""
        self.capture.release()
        self.sock.close()

def main():
    """Main function to run the AV system."""
    av_system = AVSystem()
    try:
        av_system.start_video_stream()
        print("Streaming video. Press Ctrl+C to stop...")
        while True:
            pass  # Keep the main thread alive
    except KeyboardInterrupt:
        print("Stopping the AV system...")
    finally:
        av_system.stop()
        print("AV system stopped.")

if __name__ == "__main__":
    main()
```
