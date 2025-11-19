"""
Generated Code Metadata:
========================
Original URL: https://solucionestecnologicasbogota.com
Prompt: Provide code examples for integrating high-quality surveillance cameras into a security system, including real-time video streaming and storage, based on the camera installation services offered by Space Technologies Bogotá.
Generated: DETERMINISTIC_34b591c1c475736a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import cv2
import datetime
import os
import threading
import time
from flask import Flask, Response, render_template
import logging
from logging.handlers import RotatingFileHandler

# Configuration
CONFIG = {
    'CAMERA_SOURCES': {
        'front_door': 'rtsp://username:password@192.168.1.100:554/stream1',
        'backyard': 'rtsp://username:password@192.168.1.101:554/stream1'
    },
    'STORAGE_PATH': '/var/security_footage',
    'RETENTION_DAYS': 30,
    'FRAME_RATE': 15,
    'RESOLUTION': (1280, 720),
    'LOG_FILE': '/var/log/security_system.log'
}

# Initialize Flask app
app = Flask(__name__)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        RotatingFileHandler(
            CONFIG['LOG_FILE'],
            maxBytes=10*1024*1024,
            backupCount=5
        ),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class CameraManager:
    def __init__(self):
        self.cameras = {}
        self.initialize_cameras()
        
    def initialize_cameras(self):
        """Initialize all configured camera sources."""
        for cam_name, cam_source in CONFIG['CAMERA_SOURCES'].items():
            try:
                cap = cv2.VideoCapture(cam_source)
                if cap.isOpened():
                    self.cameras[cam_name] = {
                        'cap': cap,
                        'active': True,
                        'last_frame': None,
                        'last_frame_time': None
                    }
                    logger.info(f"Camera {cam_name} initialized successfully")
                else:
                    logger.error(f"Failed to initialize camera {cam_name}")
            except Exception as e:
                logger.error(f"Error initializing camera {cam_name}: {str(e)}")
    
    def get_frame(self, camera_name):
        """Get the latest frame from a camera."""
        if camera_name not in self.cameras:
            return None
            
        camera = self.cameras[camera_name]
        if not camera['active']:
            return None
            
        try:
            ret, frame = camera['cap'].read()
            if ret:
                frame = cv2.resize(frame, CONFIG['RESOLUTION'])
                camera['last_frame'] = frame
                camera['last_frame_time'] = datetime.datetime.now()
                return frame
            else:
                logger.warning(f"Failed to read frame from {camera_name}")
                return None
        except Exception as e:
            logger.error(f"Error reading frame from {camera_name}: {str(e)}")
            return None
    
    def cleanup(self):
        """Release all camera resources."""
        for cam_name, cam_data in self.cameras.items():
            try:
                cam_data['cap'].release()
                logger.info(f"Released camera {cam_name}")
            except Exception as e:
                logger.error(f"Error releasing camera {cam_name}: {str(e)}")

class VideoStorage:
    def __init__(self):
        self.ensure_storage_path()
        self.cleanup_thread = threading.Thread(target=self.cleanup_old_recordings)
        self.cleanup_thread.daemon = True
        self.cleanup_thread.start()
    
    def ensure_storage_path(self):
        """Ensure the storage directory exists."""
        try:
            os.makedirs(CONFIG['STORAGE_PATH'], exist_ok=True)
        except Exception as e:
            logger.error(f"Error creating storage directory: {str(e)}")
    
    def save_frame(self, camera_name, frame):
        """Save a frame to disk with timestamp."""
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{camera_name}_{timestamp}.jpg"
            filepath = os.path.join(CONFIG['STORAGE_PATH'], filename)
            cv2.imwrite(filepath, frame)
        except Exception as e:
            logger.error(f"Error saving frame for {camera_name}: {str(e)}")
    
    def cleanup_old_recordings(self):
        """Periodically delete recordings older than retention period."""
        while True:
            try:
                now = datetime.datetime.now()
                cutoff = now - datetime.timedelta(days=CONFIG['RETENTION_DAYS'])
                
                for filename in os.listdir(CONFIG['STORAGE_PATH']):
                    filepath = os.path.join(CONFIG['STORAGE_PATH'], filename)
                    if os.path.isfile(filepath):
                        file_time = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
                        if file_time < cutoff:
                            try:
                                os.remove(filepath)
                                logger.info(f"Deleted old recording: {filename}")
                            except Exception as e:
                                logger.error(f"Error deleting {filename}: {str(e)}")
            except Exception as e:
                logger.error(f"Error in cleanup_old_recordings: {str(e)}")
            
            time.sleep(3600)  # Run once per hour

def generate_frames(camera_name):
    """Generate video frames for streaming."""
    camera_manager = CameraManager()
    while True:
        frame = camera_manager.get_frame(camera_name)
        if frame is not None:
            ret, buffer = cv2.imencode('.jpg', frame)
            if ret:
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
        time.sleep(1/CONFIG['FRAME_RATE'])

@app.route('/')
def index():
    """Render the main page with camera feeds."""
    return render_template('index.html', cameras=list(CONFIG['CAMERA_SOURCES'].keys()))

@app.route('/video_feed/<camera_name>')
def video_feed(camera_name):
    """Video streaming route for a specific camera."""
    return Response(generate_frames(camera_name),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/snapshot/<camera_name>')
def snapshot(camera_name):
    """Take and save a snapshot from a camera."""
    camera_manager = CameraManager()
    frame = camera_manager.get_frame(camera_name)
    if frame is not None:
        video_storage = VideoStorage()
        video_storage.save_frame(camera_name, frame)
        return "Snapshot saved successfully", 200
    return "Failed to capture snapshot", 500

if __name__ == '__main__':
    try:
        # Initialize components
        camera_manager = CameraManager()
        video_storage = VideoStorage()
        
        # Start Flask app
        app.run(host='0.0.0.0', port=5000, threaded=True)
    except Exception as e:
        logger.critical(f"Fatal error: {str(e)}")
    finally:
        camera_manager.cleanup()
```
