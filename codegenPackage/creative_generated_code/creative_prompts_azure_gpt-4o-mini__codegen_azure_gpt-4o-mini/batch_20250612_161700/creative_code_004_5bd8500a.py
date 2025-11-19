"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mydrones.gr
Prompt: Suggest an API that allows for real-time video streaming from drones during aerial photography sessions, emphasizing user experience.
Generated: DETERMINISTIC_5bd8500ac88828c9
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, Response, stream_with_context
import cv2
import threading

app = Flask(__name__)

# Global variable to hold the camera capture object
camera = None
camera_lock = threading.Lock()

def initialize_camera():
    """Initializes the camera for video streaming."""
    global camera
    if camera is None:
        # Replace '0' with the index of your camera, or a video file path
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            raise RuntimeError("Could not open camera.")

def generate_frames():
    """Generator function to yield video frames for streaming."""
    global camera
    while True:
        with camera_lock:
            success, frame = camera.read()  # Read the frame from the camera
            if not success:
                break
            # Encode the frame in JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                break
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Route to stream video feed."""
    # Initialize the camera if not already done
    initialize_camera()
    return Response(stream_with_context(generate_frames()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    """Home route to display video stream on a simple HTML page."""
    return """
    <!doctype html>
    <html>
        <head>
            <title>Drone Video Stream</title>
        </head>
        <body>
            <h1>Real-Time Video Stream from Drone</h1>
            <img src="/video_feed" width="640" height="480">
        </body>
    </html>
    """

def cleanup():
    """Releases the camera resource on shutdown."""
    global camera
    if camera is not None:
        camera.release()

if __name__ == "__main__":
    try:
        # Run the Flask app
        app.run(host='0.0.0.0', port=5000, debug=False)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cleanup()
```
