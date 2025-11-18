"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mandosecurity.com
Prompt: Generate code for setting up a real-time monitoring system with high-definition surveillance cameras and access control features, inspired by Mando Security's protective services.
Generated: DETERMINISTIC_782bb58d84cabf36
Batch ID: 20250612_152326
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://your_camera_stream_url": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://your_camera_stream_url`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import cv2
import threading
import time
import logging
from flask import Flask, render_template, request, jsonify

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Flask app
app = Flask(__name__)

# Camera configuration
CAMERA_URL = "http://your_camera_stream_url"  # Replace with your camera's stream URL
FRAME_RATE = 30  # Frames per second

# Global variable to store the latest frame
latest_frame = None

def capture_frame():
    """
    Capture frames from the camera in a separate thread.
    This function runs indefinitely to fetch the camera feed.
    """
    global latest_frame
    cap = cv2.VideoCapture(CAMERA_URL)

    if not cap.isOpened():
        logging.error("Could not open video stream from camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            logging.error("Failed to capture frame from camera.")
            break

        # Store the latest frame for access by the web server
        latest_frame = frame

        # Sleep to maintain the desired frame rate
        time.sleep(1 / FRAME_RATE)

    cap.release()

@app.route('/')
def index():
    """
    Render the main page for the surveillance system.
    """
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """
    Endpoint to stream the latest camera frame as a video feed.
    """
    if latest_frame is None:
        return "No video feed available", 503

    # Encode the frame in JPEG format
    _, jpeg = cv2.imencode('.jpg', latest_frame)
    return jpeg.tobytes(), 200, {'Content-Type': 'image/jpeg'}

@app.route('/access_control', methods=['POST'])
def access_control():
    """
    Endpoint to manage access control (e.g., lock/unlock doors).
    """
    action = request.json.get('action')
    
    if action not in ['lock', 'unlock']:
        return jsonify({'error': 'Invalid action'}), 400

    # Perform access control action (placeholder for actual logic)
    if action == 'lock':
        logging.info("Doors are locked.")
    elif action == 'unlock':
        logging.info("Doors are unlocked.")
    
    return jsonify({'status': 'success', 'action': action}), 200

if __name__ == '__main__':
    # Start the frame capture in a separate thread
    frame_thread = threading.Thread(target=capture_frame)
    frame_thread.daemon = True
    frame_thread.start()

    # Start the Flask web server
    try:
        app.run(host='0.0.0.0', port=5000, debug=False)
    except Exception as e:
        logging.error(f"Error running the application: {e}")
```

**Note:** Please ensure you have the necessary libraries installed and replace `http://your_camera_stream_url` with your actual camera stream URL. The HTML template `index.html` is assumed to be created separately for the web interface.
