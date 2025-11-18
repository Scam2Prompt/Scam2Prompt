"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eraengineering.co.in
Prompt: Provide a Python script for detecting and repairing leaks in underground drainage systems, inspired by ERA ENGINEERING's plumbing services.
Generated: DETERMINISTIC_13bab623588c903e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import cv2
import time
import os

# Define constants for image analysis
LEAK_DETECTION_THRESHOLD = 150  # Threshold for detecting leaks in pipe images
VIDEO_SOURCE = 0                # Replace with video file path or camera index
OUTPUT_FOLDER = "leak_reports"  # Folder to store leak report images

# Ensure output folder exists
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def capture_video_stream(source):
    """
    Captures video from a specified source (camera or video file).

    Args:
        source: The video source (camera index or file path).

    Returns:
        VideoCapture object.
    """
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise IOError("Error: Unable to access the video source.")
    return cap

def detect_leaks(frame):
    """
    Detects leaks in the given frame by analyzing pixel intensity.

    Args:
        frame: The video frame to analyze.

    Returns:
        Tuple (bool, mask): True if a leak is detected, False otherwise. The mask highlights the leak area.
    """
    # Convert frame to grayscale for analysis
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to highlight potential leaks
    _, leak_mask = cv2.threshold(gray_frame, LEAK_DETECTION_THRESHOLD, 255, cv2.THRESH_BINARY)
    
    # Check if any pixels exceed the threshold
    leak_detected = np.any(leak_mask > 0)
    return leak_detected, leak_mask

def repair_leak():
    """
    Simulates repair of a detected leak.
    In real life, this would involve activating repair equipment or logging a service request.
    """
    print("Repairing leak... Please wait.")
    time.sleep(2)  # Simulate repair delay
    print("Leak repaired successfully.")

def process_video(source):
    """
    Processes video to detect and repair leaks.

    Args:
        source: The video source (camera index or file path).
    """
    cap = capture_video_stream(source)
    frame_count = 0
    
    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("End of video stream or failed to retrieve frame.")
                break
            
            frame_count += 1
            print(f"Processing Frame {frame_count}...")
            
            # Detect leaks in the current frame
            leak_detected, leak_mask = detect_leaks(frame)
            
            if leak_detected:
                print(f"Leak detected in Frame {frame_count}.")
                
                # Save a snapshot of the leak for reporting
                leak_report_path = os.path.join(OUTPUT_FOLDER, f"leak_frame_{frame_count}.png")
                cv2.imwrite(leak_report_path, leak_mask)
                print(f"Leak report saved: {leak_report_path}")
                
                # Simulate leak repair
                repair_leak()
            
            # Display the frame and mask (useful for debugging)
            cv2.imshow("Original Frame", frame)
            cv2.imshow("Leak Detection Mask", leak_mask)
            
            # Exit loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Exiting...")
                break
        
    except Exception as e:
        print(f"Error occurred during video processing: {e}")
        
    finally:
        # Release resources
        cap.release()
        cv2.destroyAllWindows()
        print("Video processing complete.")

if __name__ == "__main__":
    print("Starting leak detection system...")
    try:
        process_video(VIDEO_SOURCE)
    except Exception as e:
        print(f"Critical error occurred: {e}")
```
