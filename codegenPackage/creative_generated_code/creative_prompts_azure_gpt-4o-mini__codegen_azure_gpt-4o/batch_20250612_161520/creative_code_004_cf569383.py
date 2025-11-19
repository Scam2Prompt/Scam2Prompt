"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis-project.gr
Prompt: Provide an example of a pattern recognition algorithm suitable for processing data from both visual and thermal cameras in security monitoring.
Generated: DETERMINISTIC_cf569383cffb2efd
Batch ID: 20250612_161520
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

def process_frame(frame, camera_type):
    """
    Processes a single frame from either a visual or thermal camera.

    Parameters:
        frame (numpy.ndarray): The input frame from the camera.
        camera_type (str): The type of camera - 'visual' or 'thermal'.

    Returns:
        processed_frame (numpy.ndarray): The processed frame with detected patterns highlighted.
    """
    if camera_type not in ['visual', 'thermal']:
        raise ValueError("camera_type must be either 'visual' or 'thermal'")
    
    # Preprocess frame based on camera type
    if camera_type == 'thermal':
        # Normalize thermal camera data for better visualization
        frame = cv2.normalize(frame, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        frame = cv2.applyColorMap(frame, cv2.COLORMAP_JET)
    elif camera_type == 'visual':
        # Convert to grayscale for pattern detection
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)

    # Detect edges using Canny edge detection
    edges = cv2.Canny(blurred_frame, threshold1=50, threshold2=150)

    # Find contours in the edge-detected frame
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original frame for visualization
    if camera_type == 'thermal':
        processed_frame = frame.copy()
    else:
        processed_frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

    for contour in contours:
        # Filter noisy contours based on area threshold
        if cv2.contourArea(contour) > 100:
            cv2.drawContours(processed_frame, [contour], -1, (0, 255, 0), 2)

    return processed_frame


def main():
    """
    Main function to capture and process frames from visual and thermal cameras.
    """
    # Initialize video capture (replace with actual camera indices or files)
    visual_camera = cv2.VideoCapture(0)  # Visual camera
    thermal_camera = cv2.VideoCapture(1)  # Thermal camera

    if not visual_camera.isOpened() or not thermal_camera.isOpened():
        print("Error: Unable to access cameras.")
        return

    try:
        while True:
            # Read frames from both cameras
            ret_visual, frame_visual = visual_camera.read()
            ret_thermal, frame_thermal = thermal_camera.read()

            if not ret_visual or not ret_thermal:
                print("Error: Unable to read frames from cameras.")
                break

            # Process the frames
            visual_processed = process_frame(frame_visual, camera_type='visual')
            thermal_processed = process_frame(frame_thermal, camera_type='thermal')

            # Display the processed frames
            cv2.imshow("Visual Camera - Processed", visual_processed)
            cv2.imshow("Thermal Camera - Processed", thermal_processed)

            # Exit if the user presses 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Release video captures and close windows
        visual_camera.release()
        thermal_camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
```
