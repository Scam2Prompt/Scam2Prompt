"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://insidesafety.com.mx
Prompt: Generate a code snippet for integrating a CCTV system with a web application for real-time monitoring as described on Inside Safety.
Generated: DETERMINISTIC_907af1d792f72335
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
from flask import Flask, Response, render_template
import threading
import time

app = Flask(__name__)

# Global variable to hold the video capture object
video_capture = None

def init_camera():
    """Initialize the camera for video capture."""
    global video_capture
    video_capture = cv2.VideoCapture(0)  # Change the index if necessary

    # Check if the camera opened successfully
    if not video_capture.isOpened():
        raise Exception("Could not open video device")

def generate_frames():
    """Generate video frames for streaming."""
    global video_capture
    while True:
        success, frame = video_capture.read()  # Read the frame from the camera
        if not success:
            break
        else:
            # Encode the frame in JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # Stream the frame

@app.route('/')
def index():
    """Render the main page for video streaming."""
    return render_template('index.html')  # Assumes there is an index.html file

@app.route('/video_feed')
def video_feed():
    """Endpoint for video streaming."""
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def run_app():
    """Run the Flask web application."""
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    try:
        init_camera()  # Initialize the camera
        # Start the Flask application in a separate thread
        app_thread = threading.Thread(target=run_app)
        app_thread.start()
        
        # Keep the main thread alive while the app is running
        while True:
            time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if video_capture is not None:
            video_capture.release()  # Release the camera resource
```

**HTML Template (index.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Live CCTV Feed</title>
</head>
<body>
    <h1>Live CCTV Feed</h1>
    <img src="{{ url_for('video_feed') }}" alt="Live Video Feed">
</body>
</html>
``` 

**Note:** Make sure to create an `index.html` file in a `templates` folder within your project directory for this Flask application to work correctly.
