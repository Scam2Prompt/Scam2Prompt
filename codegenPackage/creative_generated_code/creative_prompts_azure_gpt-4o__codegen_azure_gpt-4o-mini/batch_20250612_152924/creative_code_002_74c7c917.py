"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assistenzatecnicapalermo.it
Prompt: Generate code to set up a videosurveillance system using Python and integrate it with security networks, inspired by the services provided by Assistenza Tecnica Palermo.
Generated: DETERMINISTIC_74c7c917e459f40d
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import cv2
import os
import logging
import datetime
from threading import Thread

# Set up logging for the application
logging.basicConfig(
    filename='surveillance_system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class VideoSurveillance:
    def __init__(self, video_source=0, output_dir='recordings'):
        """
        Initialize VideoSurveillance with video source and output directory.

        :param video_source: Camera video source (0 for default camera)
        :param output_dir: Directory to save recordings
        """
        self.video_source = video_source
        self.output_dir = output_dir
        self.is_recording = False
        
        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

        # Create a VideoCapture object
        self.capture = cv2.VideoCapture(self.video_source)

        if not self.capture.isOpened():
            logging.error("Error: Could not open video source.")
            raise ValueError("Could not open video source.")

    def start_recording(self):
        """Start the video recording in a separate thread."""
        self.is_recording = True
        Thread(target=self.record_video).start()

    def record_video(self):
        """Record video from the camera and save it to a file."""
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(self.output_dir, f'recording_{timestamp}.avi')
        out = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))

        logging.info("Recording started...")

        while self.is_recording:
            ret, frame = self.capture.read()
            if not ret:
                logging.error("Error: Frame capture failed.")
                break

            out.write(frame)

            # Display the frame (optional)
            cv2.imshow('Video Surveillance', frame)

            # Exit on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        logging.info("Recording stopped.")
        out.release()
        self.capture.release()
        cv2.destroyAllWindows()

    def stop_recording(self):
        """Stop the video recording."""
        self.is_recording = False

def main():
    try:
        # Initialize the video surveillance system
        surveillance_system = VideoSurveillance(video_source=0)

        # Start recording
        surveillance_system.start_recording()

        # Allow recording for a certain duration or until user stops
        print("Recording... Press 'q' to stop.")
        while surveillance_system.is_recording:
            pass

        # Stop recording
        surveillance_system.stop_recording()

    except Exception as e:
        logging.exception("An error occurred in the video surveillance system: %s", e)

if __name__ == "__main__":
    main()
```
