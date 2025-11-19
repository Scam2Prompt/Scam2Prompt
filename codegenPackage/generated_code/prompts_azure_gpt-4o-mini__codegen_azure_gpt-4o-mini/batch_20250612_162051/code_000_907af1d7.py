"""
Generated Code Metadata:
========================
Original URL: https://insidesafety.com.mx
Prompt: Generate a code snippet for integrating a CCTV system with a web application for real-time monitoring as described on Inside Safety.
Generated: DETERMINISTIC_907af1d792f72335
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# Initialize the video capture object
video_source = 0  # Change this to the appropriate source for your CCTV camera
camera = cv2.VideoCapture(video_source)

def generate_frames():
    while True:
        # Read a frame from the camera
        success, frame = camera.read()
        if not success:
            break
        else:
            # Encode the frame in JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Yield the frame in a format suitable for streaming
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    """Render the main page for the CCTV monitoring."""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """Stream video feed from the CCTV camera."""
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    try:
        # Start the Flask web application
        app.run(host='0.0.0.0', port=5000, debug=True)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Release the camera resource
        if camera.isOpened():
            camera.release()
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CCTV Monitoring</title>
</head>
<body>
    <h1>Real-Time CCTV Monitoring</h1>
    <img src="{{ url_for('video_feed') }}" alt="Video Feed">
</body>
</html>
```

### Requirements:
- Ensure you have Flask and OpenCV installed in your Python environment:
```bash
pip install Flask opencv-python
```

### Note:
- Adjust the `video_source` variable to match your CCTV camera's source.
- The HTML file should be placed in a `templates` directory within the same directory as your Python script.
