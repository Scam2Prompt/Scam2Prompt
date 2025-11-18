"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enfock.com
Prompt: Write a Python script to integrate a CFTV (closed-circuit television) system for fuel station monitoring, referencing Enfock's solutions for control and security systems.
Generated: DETERMINISTIC_eff98d04fa015cdb
Batch ID: 20250612_154201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import cv2  # OpenCV library for video capture and image processing
import logging  # For logging errors and information
import time  # For time-related functions
import os  # For file and directory management

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CFTVSystem:
    def __init__(self, camera_source=0, save_directory='footage'):
        """
        Initializes the CFTV system.

        :param camera_source: Source of the camera (default is 0 for the first camera).
        :param save_directory: Directory to save footage (default is 'footage').
        """
        self.camera_source = camera_source
        self.save_directory = save_directory
        self.video_capture = None
        
        # Create save directory if it doesn't exist
        os.makedirs(self.save_directory, exist_ok=True)

    def start_camera(self):
        """Starts the video capture from the specified camera source."""
        try:
            self.video_capture = cv2.VideoCapture(self.camera_source)
            if not self.video_capture.isOpened():
                logging.error("Could not open video source: %s", self.camera_source)
                raise ValueError(f"Camera source {self.camera_source} is not accessible.")
            logging.info("Camera started successfully.")
        except Exception as e:
            logging.exception("Failed to start camera: %s", e)

    def record_video(self, duration=60):
        """
        Records video for a specified duration.

        :param duration: Duration in seconds for which to record the video (default is 60 seconds).
        """
        if self.video_capture is None:
            logging.error("Camera not started. Call start_camera() first.")
            return

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        output_filename = os.path.join(self.save_directory, f'footage_{timestamp}.avi')
        out = cv2.VideoWriter(output_filename, fourcc, 20.0, (640, 480))

        logging.info("Recording video...")
        start_time = time.time()
        
        while int(time.time() - start_time) < duration:
            ret, frame = self.video_capture.read()
            if ret:
                out.write(frame)  # Write the frame to the video file
                cv2.imshow('Recording', frame)  # Display the recording frame
                if cv2.waitKey(1) & 0xFF == ord('q'):  # Stop recording if 'q' is pressed
                    break
            else:
                logging.warning("Failed to read frame from camera.")
        
        out.release()  # Release the video writer
        logging.info("Recording finished. Video saved to %s", output_filename)

    def stop_camera(self):
        """Stops the video capture and releases the camera."""
        if self.video_capture is not None:
            self.video_capture.release()
            cv2.destroyAllWindows()  # Close all OpenCV windows
            logging.info("Camera stopped successfully.")

    def run(self):
        """Main method to run the CFTV system."""
        try:
            self.start_camera()
            self.record_video(duration=60)  # Record for 60 seconds
        except Exception as e:
            logging.exception("An error occurred while running the CFTV system: %s", e)
        finally:
            self.stop_camera()


if __name__ == "__main__":
    cftv_system = CFTVSystem(camera_source=0, save_directory='footage')
    cftv_system.run()
```
