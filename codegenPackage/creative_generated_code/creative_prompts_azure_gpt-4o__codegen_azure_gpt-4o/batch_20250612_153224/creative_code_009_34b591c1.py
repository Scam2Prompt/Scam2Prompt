"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solucionestecnologicasbogota.com
Prompt: Provide code examples for integrating high-quality surveillance cameras into a security system, including real-time video streaming and storage, based on the camera installation services offered by Space Technologies Bogotá.
Generated: DETERMINISTIC_34b591c1c475736a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Integration script for high-quality surveillance cameras into a security system.
Includes real-time video streaming and storage capabilities.

This script is designed for Python and utilizes OpenCV for video streaming, 
and a file-based approach for video storage. Ensure required libraries are installed.
"""

import cv2
import os
import datetime

# Configuration settings for video streaming and recording
STREAM_URL = "rtsp://username:password@camera_ip:port/stream"  # Replace with your camera's RTSP URL
OUTPUT_DIRECTORY = "./video_storage"  # Directory for storing recorded videos
FRAME_WIDTH = 640  # Width of the video frame
FRAME_HEIGHT = 480  # Height of the video frame
FPS = 30  # Frames per second for recording
RECORD_DURATION = 60  # Duration in seconds for each video segment

# Ensure output directory exists
if not os.path.exists(OUTPUT_DIRECTORY):
    os.makedirs(OUTPUT_DIRECTORY)

def record_video():
    """
    Function to capture video stream from the camera, display it in real-time, 
    and save the video in chunks to the disk.
    """
    try:
        # Open connection to the camera stream
        cap = cv2.VideoCapture(STREAM_URL)
        if not cap.isOpened():
            raise Exception("Failed to connect to the camera. Check STREAM_URL and camera settings.")

        # Set frame width, height, and FPS for the capture
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)
        cap.set(cv2.CAP_PROP_FPS, FPS)

        while True:
            # Generate filename with timestamp for video segment
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            video_filename = os.path.join(OUTPUT_DIRECTORY, f"{timestamp}.avi")
            
            # Define video writer for saving the file
            fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Use XVID codec
            out = cv2.VideoWriter(video_filename, fourcc, FPS, (FRAME_WIDTH, FRAME_HEIGHT))

            start_time = datetime.datetime.now()
            print(f"Recording video: {video_filename}")

            while (datetime.datetime.now() - start_time).seconds < RECORD_DURATION:
                # Read frames from the video stream
                ret, frame = cap.read()
                if not ret:
                    print("Failed to retrieve frame from the camera. Stopping...")
                    break
                
                # Display the video frame in real-time
                cv2.imshow('Real-Time Video Stream', frame)

                # Write the frame to the video file
                out.write(frame)

                # Exit on pressing "q"
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("Stream stopped by user.")
                    cap.release()
                    out.release()
                    cv2.destroyAllWindows()
                    return

            # Release the video writer after recording the segment
            out.release()
            print(f"Video saved: {video_filename}")

    except Exception as error:
        print(f"An error occurred: {error}")
    finally:
        # Release resources
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Starting surveillance system...")
    record_video()
    print("Surveillance system stopped.")
```

### Notes:
1. Replace `STREAM_URL` with the actual RTSP URL of the surveillance camera.
2. Ensure that OpenCV (`opencv-python`) is installed by running `pip install opencv-python`.
3. The script saves video segments in `.avi` format and organizes them in the `OUTPUT_DIRECTORY`.
4. You can modify `RECORD_DURATION`, `FRAME_WIDTH`, `FRAME_HEIGHT`, and other settings as needed.
5. Proper error handling is included to manage camera connectivity issues.
