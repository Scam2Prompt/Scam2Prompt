"""
Generated Code Metadata:
========================
Original URL: https://liveonlinetv.org
Prompt: Write a code snippet to implement live TV streaming on a tablet or mobile device using 2G or 3G networks, similar to LiveOnlineTv.org's functionality.
Generated: DETERMINISTIC_b224a595bbd9e4f2
Batch ID: 20250622_212335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import threading
import time
from flask import Flask, Response, render_template
import cv2
import numpy as np
from urllib.parse import urlparse
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
BUFFER_SIZE = 1024 * 1024  # 1MB buffer
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds
STREAM_TIMEOUT = 10  # seconds
ALLOWED_EXTENSIONS = {'m3u', 'm3u8', 'ts'}

class StreamBuffer:
    def __init__(self):
        self.buffer = b''
        self.lock = threading.Lock()
        self.last_update = time.time()

    def write(self, data):
        with self.lock:
            self.buffer += data
            self.last_update = time.time()
            # Keep buffer size manageable
            if len(self.buffer) > BUFFER_SIZE:
                self.buffer = self.buffer[-BUFFER_SIZE:]

    def read(self):
        with self.lock:
            return self.buffer

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def fetch_stream(url, buffer):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36'
    }
    
    retries = 0
    while retries < MAX_RETRIES:
        try:
            response = requests.get(url, stream=True, headers=headers, timeout=STREAM_TIMEOUT)
            if response.status_code == 200:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        buffer.write(chunk)
                break
            else:
                raise Exception(f"HTTP Error: {response.status_code}")
        except Exception as e:
            print(f"Stream error: {str(e)}")
            retries += 1
            time.sleep(RETRY_DELAY)
    else:
        print("Max retries reached. Could not establish stream.")

def generate_frames(buffer):
    while True:
        data = buffer.read()
        if not data:
            time.sleep(0.1)
            continue
        
        try:
            # Convert bytes to numpy array
            nparr = np.frombuffer(data, np.uint8)
            # Decode image
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            if frame is not None:
                # Encode frame as JPEG
                ret, jpeg = cv2.imencode('.jpg', frame)
                if ret:
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + 
                           jpeg.tobytes() + b'\r\n')
        except Exception as e:
            print(f"Frame generation error: {str(e)}")
            time.sleep(0.1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream')
def stream():
    stream_url = request.args.get('url', '')
    if not stream_url:
        return "Stream URL not provided", 400
    
    buffer = StreamBuffer()
    threading.Thread(target=fetch_stream, args=(stream_url, buffer)).start()
    
    return Response(generate_frames(buffer),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return f"File uploaded successfully: {filename}", 200
    
    return "Invalid file type", 400

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = 'uploads'
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(host='0.0.0.0', port=5000, threaded=True)
```
