"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet.in
Prompt: Write a script to set up a surveillance system using CCTV and IP cameras, as outlined by Starknet IT Solutions.
Generated: DETERMINISTIC_202b20a1e0d4ba49
Batch ID: 20250612_135324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Surveillance System Setup Script

This script sets up a surveillance system using CCTV and IP cameras. It connects to the cameras,
configures them, and starts recording feeds for monitoring purposes.

Requirements:
- The `opencv-python` library for handling video feeds.
- Proper network and port configuration for IP cameras.

Ensure the cameras are connected to the network and accessible before running this script.
"""

import cv2
import os
import datetime
import logging

# Configure logging for debugging and error tracking
logging.basicConfig(
    filename='surveillance_system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define constants
OUTPUT_DIR = 'surveillance_feeds'  # Directory to store recorded feeds
CAMERA_URLS = [
    # Replace these placeholders with your actual IP camera URLs
    'rtsp://username:password@192.168.1.101:554/stream1',  # Camera 1
    'rtsp://username:password@192.168.1.102:554/stream1',  # Camera 2
]
RECORD_DURATION = 10  # Duration to record each feed (in minutes)
FPS = 30  # Default frames per second for video recording

def create_output_directory(directory):
    """
    Create the output directory if it doesn't exist.
    """
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            logging.info(f"Created output directory: {directory}")
    except Exception as e:
        logging.error(f"Failed to create output directory: {e}")
        raise

def start_camera_feed(camera_url, output_path):
    """
    Starts capturing feed from a camera, writing it to an output file.

    :param camera_url: URL of the camera (RTSP or local path)
    :param output_path: Path to save the recorded video
    """
    try:
        cap = cv2.VideoCapture(camera_url)

        if not cap.isOpened():
            logging.error(f"Unable to connect to camera: {camera_url}")
            return

        # Get video specifications
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for output file

        # Initialize video writer
        out = cv2.VideoWriter(output_path, fourcc, FPS, (frame_width, frame_height))
        logging.info(f"Recording started for: {camera_url}")

        start_time = datetime.datetime.now()

        while (datetime.datetime.now() - start_time).seconds < RECORD_DURATION * 60:
            ret, frame = cap.read()
            if ret:
                out.write(frame)
                cv2.imshow(camera_url, frame)  # Optional: Display the feed in a window
                # Break loop if 'q' is pressed (for manual termination during testing)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                logging.warning(f"Frame failed to capture from: {camera_url}")
                break

        # Release resources
        cap.release()
        out.release()
        cv2.destroyAllWindows()
        logging.info(f"Recording finished for: {camera_url}")

    except Exception as e:
        logging.error(f"Error during recording for {camera_url}: {e}")

def setup_surveillance_system():
    """
    Main function to set up the surveillance system.
    """
    create_output_directory(OUTPUT_DIR)

    for index, camera_url in enumerate(CAMERA_URLS):
        try:
            # Generate output file name based on timestamp
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = os.path.join(OUTPUT_DIR, f'camera_{index + 1}_{timestamp}.avi')

            logging.info(f"Starting setup for Camera {index + 1}...")
            start_camera_feed(camera_url, output_file)

        except Exception as e:
            logging.error(f"Failed to set up Camera {index + 1}: {e}")

if __name__ == '__main__':
    logging.info("Surveillance system setup started.")
    setup_surveillance_system()
    logging.info("Surveillance system setup completed.")
```
