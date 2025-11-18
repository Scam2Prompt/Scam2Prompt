"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solucionestecnologicasbogota.com
Prompt: Provide code examples for integrating high-quality surveillance cameras into a security system, including real-time video streaming and storage, based on the camera installation services offered by Space Technologies Bogotá.
Generated: DETERMINISTIC_34b591c1c475736a
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://your_camera_ip/stream": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import cv2
import os
import datetime
import threading

class SurveillanceCamera:
    def __init__(self, camera_url, storage_dir='video_storage', frame_rate=30):
        """
        Initializes a SurveillanceCamera instance.

        :param camera_url: URL of the camera stream
        :param storage_dir: Directory to save recorded videos
        :param frame_rate: Frame rate for video recording
        """
        self.camera_url = camera_url
        self.storage_dir = storage_dir
        self.frame_rate = frame_rate
        self.is_recording = False
        self.video_writer = None

        # Create storage directory if it doesn't exist
        if not os.path.exists(self.storage_dir):
            os.makedirs(self.storage_dir)

    def start_stream(self):
        """Starts the camera stream and begins processing frames."""
        cap = cv2.VideoCapture(self.camera_url)
        
        if not cap.isOpened():
            raise ValueError("Could not open video stream from the provided URL.")

        print("Camera stream started.")
        threading.Thread(target=self.record_video, args=(cap,), daemon=True).start()
        
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture frame. Retrying...")
                continue
            
            cv2.imshow('Surveillance Feed', frame)

            # Exit on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def record_video(self, cap):
        """Records video from the camera stream to the specified directory."""
        self.is_recording = True
        video_filename = os.path.join(self.storage_dir, f"recording_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.avi")
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        fps = self.frame_rate
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.video_writer = cv2.VideoWriter(video_filename, fourcc, fps, (width, height))
        
        while self.is_recording:
            ret, frame = cap.read()
            if not ret:
                break
            self.video_writer.write(frame)

        self.stop_recording()

    def stop_recording(self):
        """Stops the video recording."""
        if self.video_writer:
            self.video_writer.release()
            self.video_writer = None
            print("Recording stopped.")

    def terminate(self):
        """Terminates the camera stream and stops recording."""
        self.is_recording = False
        self.stop_recording()

if __name__ == "__main__":
    # Example usage
    camera_url = "http://your_camera_ip/stream"  # Replace with your camera's URL
    camera = SurveillanceCamera(camera_url)

    try:
        camera.start_stream()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        camera.terminate()
```
