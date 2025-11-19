"""
Generated Code Metadata:
========================
Original URL: https://owainpritchard.co.uk
Prompt: Recommend a suitable API for integrating CCTV system monitoring and control features into a web application, considering factors like real-time video streaming and motion detection.
Generated: DETERMINISTIC_f1ec925ac67e15aa
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates how to integrate a CCTV system monitoring and control feature into a web application
using the Flask framework and the OpenCV library for video streaming and motion detection.

Dependencies:
- Flask: For building the web application
- OpenCV (cv2): For video processing and motion detection
- Camera API (e.g., RTSP stream): For accessing CCTV camera feeds

Ensure you have installed the required libraries:
pip install flask opencv-python
"""

from flask import Flask, Response, render_template
import cv2

app = Flask(__name__)

# Replace with your CCTV camera's RTSP URL or local camera index (e.g., 0 for the default webcam)
CAMERA_STREAM_URL = "rtsp://username:password@camera_ip_address:port/stream"

# Initialize the video capture object
try:
    camera = cv2.VideoCapture(CAMERA_STREAM_URL)
    if not camera.isOpened():
        raise Exception("Unable to connect to the camera stream. Check the URL or camera settings.")
except Exception as e:
    print(f"Error initializing camera: {e}")
    exit(1)

def generate_frames():
    """
    Generator function to yield video frames for streaming.
    Includes basic motion detection logic.
    """
    previous_frame = None

    while True:
        # Read the current frame from the camera
        success, frame = camera.read()
        if not success:
            break

        # Convert the frame to grayscale for motion detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

        # Perform motion detection by comparing the current frame with the previous frame
        if previous_frame is not None:
            frame_diff = cv2.absdiff(previous_frame, gray_frame)
            _, threshold_frame = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)
            motion_detected = cv2.countNonZero(threshold_frame) > 5000  # Adjust sensitivity as needed

            if motion_detected:
                cv2.putText(frame, "Motion Detected!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Update the previous frame
        previous_frame = gray_frame

        # Encode the frame as JPEG
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # Yield the frame in a format suitable for streaming
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    """
    Render the main page of the web application.
    """
    return render_template('index.html')  # Ensure you have an 'index.html' template in the 'templates' folder

@app.route('/video_feed')
def video_feed():
    """
    Route to stream video frames to the web application.
    """
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    try:
        # Run the Flask application
        app.run(host='0.0.0.0', port=5000, debug=False)
    except Exception as e:
        print(f"Error running the application: {e}")
    finally:
        # Release the camera resource when the application exits
        camera.release()
```

**Note:** 
1. Replace `CAMERA_STREAM_URL` with the actual RTSP URL or camera index.
2. Create an `index.html` file in the `templates` folder to display the video feed. Example content:
```html
<!DOCTYPE html>
<html>
<head>
    <title>CCTV Monitoring</title>
</head>
<body>
    <h1>CCTV Monitoring</h1>
    <img src="/video_feed" width="800" height="450">
</body>
</html>
```
