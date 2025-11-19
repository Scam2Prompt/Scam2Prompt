"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solucionestecnologicasbogota.com
Prompt: Generate a code snippet for a system that integrates with CCTV camera installations in Bogotá, focusing on security and monitoring features as described by Space Technologies.
Generated: DETERMINISTIC_ec3ff85e0a8daf9a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import cv2
import time
import logging
import os

# Configure logging for monitoring and debugging
logging.basicConfig(
    filename="cctv_monitoring.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants for CCTV system
CAMERA_FEED_URL = "rtsp://192.168.1.100:554/live"  # Replace with your camera's RTSP URL
OUTPUT_VIDEO_DIR = "./recordings"  # Directory to store recorded videos
RECORDING_DURATION = 60  # Duration of each video segment in seconds
MONITORING_INTERVAL = 2  # Interval for motion detection checks in seconds

# Ensure the output directory exists
os.makedirs(OUTPUT_VIDEO_DIR, exist_ok=True)

def monitor_cctv():
    """
    Function to monitor a CCTV feed, detect motion, and save recordings.
    """
    try:
        # Initialize the video capture from the camera feed
        cap = cv2.VideoCapture(CAMERA_FEED_URL)
        if not cap.isOpened():
            logging.error("Unable to connect to the CCTV camera feed.")
            return

        logging.info("Successfully connected to the CCTV camera feed.")

        # Initialize background subtractor for motion detection
        background_subtractor = cv2.createBackgroundSubtractorMOG2()

        recording_start_time = time.time()
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = None

        while True:
            ret, frame = cap.read()
            if not ret:
                logging.warning("Failed to fetch frame from camera. Retrying...")
                time.sleep(1)
                continue

            # Apply motion detection
            fg_mask = background_subtractor.apply(frame)
            _, fg_thresh = cv2.threshold(fg_mask, 25, 255, cv2.THRESH_BINARY)
            motion_detected = cv2.countNonZero(fg_thresh) > 500  # Customize motion sensitivity threshold

            # Start recording if motion is detected
            if motion_detected:
                if out is None:
                    filename = os.path.join(
                        OUTPUT_VIDEO_DIR,
                        f"motion_{time.strftime('%Y%m%d_%H%M%S')}.avi"
                    )
                    out = cv2.VideoWriter(filename, fourcc, 20.0, (frame_width, frame_height))
                    logging.info(f"Motion detected. Started recording to {filename}")

                out.write(frame)

            # Stop recording after recording duration or if no motion
            if out is not None and (time.time() - recording_start_time > RECORDING_DURATION or not motion_detected):
                logging.info("Stopped recording due to timeout or no motion detected.")
                out.release()
                out = None
                recording_start_time = time.time()

            # Display the video feed (optional, can be disabled for headless systems)
            cv2.imshow("CCTV Feed", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
                logging.info("Exiting CCTV monitoring.")
                break

            time.sleep(MONITORING_INTERVAL)

    except Exception as e:
        logging.error(f"An error occurred during CCTV monitoring: {e}")
    finally:
        if cap.isOpened():
            cap.release()
        if out is not None:
            out.release()
        cv2.destroyAllWindows()
        logging.info("Released all resources and exited.")

if __name__ == "__main__":
    monitor_cctv()
```
