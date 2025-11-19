"""
Generated Code Metadata:
========================
Original URL: https://mandosecurity.com
Prompt: Generate code for setting up a real-time monitoring system with high-definition surveillance cameras and access control features, inspired by Mando Security's protective services.
Generated: DETERMINISTIC_782bb58d84cabf36
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import cv2
import threading
import time
import logging
from flask import Flask, Response, jsonify, request

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# Global variable to store camera feed
camera_feed = None

# Function to capture video from the camera
def capture_video(camera_index=0):
    global camera_feed
    camera = cv2.VideoCapture(camera_index)

    if not camera.isOpened():
        logging.error("Could not open video device")
        return

    while True:
        ret, frame = camera.read()
        if not ret:
            logging.error("Failed to capture frame")
            break
        camera_feed = frame

    camera.release()

# Route to stream video feed
@app.route('/video_feed')
def video_feed():
    """Stream video feed from the camera."""
    def generate():
        global camera_feed
        while True:
            if camera_feed is not None:
                # Encode frame to JPEG
                _, buffer = cv2.imencode('.jpg', camera_feed)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            time.sleep(0.1)  # Reduce CPU usage
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Route to handle access control
@app.route('/access_control', methods=['POST'])
def access_control():
    """Handle access control requests."""
    data = request.json
    if not data or 'action' not in data:
        return jsonify({"error": "Invalid request"}), 400

    action = data['action']
    if action == 'grant':
        logging.info("Access granted")
        return jsonify({"message": "Access granted"}), 200
    elif action == 'deny':
        logging.info("Access denied")
        return jsonify({"message": "Access denied"}), 200
    else:
        return jsonify({"error": "Unknown action"}), 400

if __name__ == '__main__':
    # Start video capture in a separate thread
    video_thread = threading.Thread(target=capture_video)
    video_thread.daemon = True
    video_thread.start()

    # Start Flask app
    try:
        app.run(host='0.0.0.0', port=5000, threaded=True)
    except Exception as e:
        logging.error(f"Error starting the server: {e}")
```

### Requirements:
- Ensure you have the necessary libraries installed:
  ```bash
  pip install opencv-python flask
  ```
- Run the script and access the video feed at `http://<your_ip>:5000/video_feed`.
- Use a tool like Postman to send POST requests to `http://<your_ip>:5000/access_control` with JSON body `{"action": "grant"}` or `{"action": "deny"}` for access control.
