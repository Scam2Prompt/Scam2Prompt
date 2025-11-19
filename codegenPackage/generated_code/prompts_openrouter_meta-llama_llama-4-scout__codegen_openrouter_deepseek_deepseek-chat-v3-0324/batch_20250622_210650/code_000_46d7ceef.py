"""
Generated Code Metadata:
========================
Original URL: https://rayzentreprise.com
Prompt: "Design a video surveillance system for a commercial building in Cameroon using IP cameras and a network infrastructure."
Generated: DETERMINISTIC_46d7ceeff2f57252
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
from datetime import datetime
import threading
import time
import cv2
import numpy as np
import requests
from flask import Flask, Response, request
import pymongo
from pymongo import MongoClient
from werkzeug.utils import secure_filename

# Configuration
CONFIG = {
    "database": {
        "host": "localhost",
        "port": 27017,
        "db_name": "surveillance_db",
        "collection": "video_metadata"
    },
    "storage": {
        "video_path": "/var/lib/surveillance/videos",
        "max_storage_gb": 100,
        "retention_days": 30
    },
    "cameras": [
        {
            "id": 1,
            "name": "Entrance",
            "rtsp_url": "rtsp://admin:password@192.168.1.10:554/stream1",
            "location": "Main Entrance",
            "resolution": "1920x1080",
            "fps": 30
        },
        {
            "id": 2,
            "name": "Parking Lot",
            "rtsp_url": "rtsp://admin:password@192.168.1.11:554/stream1",
            "location": "Parking Area",
            "resolution": "1280x720",
            "fps": 25
        }
    ],
    "network": {
        "bandwidth_limit_mbps": 100,
        "qos_enabled": True
    },
    "api": {
        "port": 5000,
        "auth_token": "securetoken123"
    }
}

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('surveillance.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Database setup
def get_db_connection():
    try:
        client = MongoClient(
            CONFIG["database"]["host"],
            CONFIG["database"]["port"]
        )
        db = client[CONFIG["database"]["db_name"]]
        return db
    except Exception as e:
        logger.error(f"Database connection error: {e}")
        raise

# Video storage management
def check_storage():
    total, used, free = os.statvfs(CONFIG["storage"]["video_path"]).f_blocks, os.statvfs(CONFIG["storage"]["video_path"]).f_bfree, os.statvfs(CONFIG["storage"]["video_path"]).f_bavail
    total_gb = (total * os.statvfs(CONFIG["storage"]["video_path"]).f_frsize) / (1024**3)
    used_gb = (used * os.statvfs(CONFIG["storage"]["video_path"]).f_frsize) / (1024**3)
    free_gb = (free * os.statvfs(CONFIG["storage"]["video_path"]).f_frsize) / (1024**3)
    
    logger.info(f"Storage: Total={total_gb:.2f}GB, Used={used_gb:.2f}GB, Free={free_gb:.2f}GB")
    
    if free_gb < (CONFIG["storage"]["max_storage_gb"] * 0.1):
        logger.warning("Low storage space!")
        cleanup_old_videos()
    
    return free_gb

def cleanup_old_videos():
    db = get_db_connection()
    collection = db[CONFIG["database"]["collection"]]
    
    cutoff_date = datetime.now() - timedelta(days=CONFIG["storage"]["retention_days"])
    old_videos = collection.find({"timestamp": {"$lt": cutoff_date}})
    
    for video in old_videos:
        try:
            os.remove(video["file_path"])
            collection.delete_one({"_id": video["_id"]})
            logger.info(f"Deleted old video: {video['file_path']}")
        except Exception as e:
            logger.error(f"Error deleting video {video['file_path']}: {e}")

# Video capture and processing
class CameraStream:
    def __init__(self, camera_config):
        self.camera_config = camera_config
        self.cap = None
        self.running = False
        self.thread = None
        self.frame = None
        self.last_frame_time = None
        self.output_file = None
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.current_filename = None
    
    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._capture_loop)
        self.thread.daemon = True
        self.thread.start()
    
    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()
        if self.cap:
            self.cap.release()
        if self.output_file:
            self.output_file.release()
    
    def _capture_loop(self):
        try:
            self.cap = cv2.VideoCapture(self.camera_config["rtsp_url"])
            
            if not self.cap.isOpened():
                logger.error(f"Failed to open camera: {self.camera_config['name']}")
                return
            
            logger.info(f"Started capturing from {self.camera_config['name']}")
            
            while self.running:
                ret, frame = self.cap.read()
                if not ret:
                    logger.warning(f"Failed to read frame from {self.camera_config['name']}")
                    time.sleep(1)
                    continue
                
                self.frame = frame
                self.last_frame_time = datetime.now()
                
                if self.output_file:
                    self.output_file.write(frame)
                
                time.sleep(1 / self.camera_config["fps"])
        
        except Exception as e:
            logger.error(f"Error in capture loop for {self.camera_config['name']}: {e}")
            self.running = False
    
    def start_recording(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.current_filename = f"{self.camera_config['name']}_{timestamp}.avi"
        file_path = os.path.join(CONFIG["storage"]["video_path"], self.current_filename)
        
        resolution = tuple(map(int, self.camera_config["resolution"].split('x')))
        self.output_file = cv2.VideoWriter(
            file_path,
            self.fourcc,
            self.camera_config["fps"],
            resolution
        )
        
        logger.info(f"Started recording: {file_path}")
        
        # Store metadata in database
        db = get_db_connection()
        collection = db[CONFIG["database"]["collection"]]
        
        metadata = {
            "camera_id": self.camera_config["id"],
            "camera_name": self.camera_config["name"],
            "location": self.camera_config["location"],
            "file_path": file_path,
            "timestamp": datetime.now(),
            "resolution": self.camera_config["resolution"],
            "fps": self.camera_config["fps"],
            "status": "recording"
        }
        
        collection.insert_one(metadata)
    
    def stop_recording(self):
        if self.output_file:
            self.output_file.release()
            self.output_file = None
            
            # Update metadata in database
            db = get_db_connection()
            collection = db[CONFIG["database"]["collection"]]
            
            collection.update_one(
                {"file_path": os.path.join(CONFIG["storage"]["video_path"], self.current_filename)},
                {"$set": {"status": "completed", "duration": (datetime.now() - self.last_frame_time).total_seconds()}}
            )
            
            logger.info(f"Stopped recording: {self.current_filename}")
            self.current_filename = None

# API Server
app = Flask(__name__)

def authenticate(request):
    token = request.headers.get('Authorization')
    if token != f"Bearer {CONFIG['api']['auth_token']}":
        return False
    return True

@app.route('/api/stream/<int:camera_id>', methods=['GET'])
def stream(camera_id):
    if not authenticate(request):
        return "Unauthorized", 401
    
    camera = next((c for c in CONFIG["cameras"] if c["id"] == camera_id), None)
    if not camera:
        return "Camera not found", 404
    
    def generate():
        stream = CameraStream(camera)
        stream.start()
        
        try:
            while True:
                if stream.frame is not None:
                    ret, jpeg = cv2.imencode('.jpg', stream.frame)
                    if ret:
                        yield (b'--frame\r\n'
                               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
                time.sleep(1 / camera["fps"])
        finally:
            stream.stop()
    
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/api/record/start/<int:camera_id>', methods
