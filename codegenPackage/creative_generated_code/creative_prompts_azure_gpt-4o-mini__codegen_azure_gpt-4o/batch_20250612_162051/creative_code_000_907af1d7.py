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
# Import necessary libraries
from flask import Flask, Response, render_template
import cv2

# Initialize Flask app
app = Flask(__name__)

# Initialize video capture (replace '0' with the CCTV camera's feed URL/IP if needed)
camera = cv2.VideoCapture(0)

# Function to generate video frames
def generate_frames():
    while True:
        try:
            # Capture frame-by-frame
            success, frame = camera.read()
            if not success:
                break
            else:
                # Encode the frame to JPEG format
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()

                # Yield frame as a byte stream
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        except Exception as e:
            print(f"Error generating frames: {e}")
            break

@app.route('/')
def index():
    """
    Render the HTML template for the home page.
    This template should contain an HTML video tag to display the CCTV feed.
    """
    return render_template('index.html')  # Ensure you have an 'index.html' file with a video tag.

@app.route('/video_feed')
def video_feed():
    """
    Route to provide the video feed.
    This is streamed as MJPEG content suitable for real-time monitoring.
    """
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    try:
        # Run the Flask app
        app.run(host='0.0.0.0', port=5000, debug=False)
    except Exception as e:
        print(f"An error occurred while starting the server: {e}")
    finally:
        # Release the camera when the application is terminated
        camera.release()
        print("Camera released.")
```

**HTML Template (`templates/index.html`) Example:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Real-Time CCTV Monitoring</title>
</head>
<body>
    <h1>Live CCTV Feed</h1>
    <div>
        <img src="/video_feed" alt="CCTV Feed" style="width: 100%; max-width: 720px;">
    </div>
</body>
</html>
```
