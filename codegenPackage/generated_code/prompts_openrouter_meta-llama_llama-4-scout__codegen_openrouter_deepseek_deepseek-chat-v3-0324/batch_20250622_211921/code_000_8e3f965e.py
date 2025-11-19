"""
Generated Code Metadata:
========================
Original URL: https://www.vatio.cl
Prompt: "Write a Python script to implement a 24/7 video monitoring system with AI-powered analytics for detecting intruders and suspicious behaviors, as described in VATIO's Vigilancia Inteligente stage."
Generated: DETERMINISTIC_8e3f965e96199a82
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import cv2
import numpy as np
import time
import os
from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler
from threading import Thread
import queue
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# Configuration
CONFIG = {
    "video_source": 0,  # 0 for default camera, or path to video file
    "output_dir": "monitoring_output",
    "model_path": "intruder_detection_model.h5",  # Pretrained model path
    "confidence_threshold": 0.7,
    "frame_skip": 5,  # Process every 5th frame to reduce computation
    "log_file": "monitoring.log",
    "max_log_size": 10 * 1024 * 1024,  # 10MB
    "backup_count": 5,
    "alert_cooldown": 30,  # Seconds between alerts for the same event
}

# Initialize logging
def setup_logging():
    os.makedirs(CONFIG["output_dir"], exist_ok=True)
    logger = logging.getLogger("VideoMonitoring")
    logger.setLevel(logging.INFO)
    
    handler = RotatingFileHandler(
        os.path.join(CONFIG["output_dir"], CONFIG["log_file"]),
        maxBytes=CONFIG["max_log_size"],
        backupCount=CONFIG["backup_count"]
    )
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger

logger = setup_logging()

# Load AI model
def load_ai_model():
    try:
        model = load_model(CONFIG["model_path"])
        logger.info("AI model loaded successfully")
        return model
    except Exception as e:
        logger.error(f"Failed to load AI model: {str(e)}")
        raise

# Video processing class
class VideoProcessor:
    def __init__(self, model):
        self.model = model
        self.cap = None
        self.frame_queue = queue.Queue(maxsize=10)
        self.last_alert_time = 0
        self.running = False
        self.process_thread = None
        self.capture_thread = None

    def preprocess_frame(self, frame):
        try:
            resized = cv2.resize(frame, (224, 224))
            normalized = preprocess_input(resized)
            expanded = np.expand_dims(normalized, axis=0)
            return expanded
        except Exception as e:
            logger.error(f"Frame preprocessing failed: {str(e)}")
            return None

    def process_frame(self, frame):
        try:
            processed_frame = self.preprocess_frame(frame)
            if processed_frame is None:
                return False, frame
            
            predictions = self.model.predict(processed_frame)
            confidence = predictions[0][0]
            
            if confidence > CONFIG["confidence_threshold"]:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_path = os.path.join(CONFIG["output_dir"], f"alert_{timestamp}.jpg")
                cv2.imwrite(output_path, frame)
                logger.info(f"Intruder detected with confidence {confidence:.2f}")
                return True, frame
            return False, frame
        except Exception as e:
            logger.error(f"Frame processing failed: {str(e)}")
            return False, frame

    def capture_frames(self):
        try:
            self.cap = cv2.VideoCapture(CONFIG["video_source"])
            if not self.cap.isOpened():
                raise RuntimeError("Could not open video source")
            
            frame_count = 0
            while self.running:
                ret, frame = self.cap.read()
                if not ret:
                    logger.warning("Failed to capture frame")
                    continue
                
                frame_count += 1
                if frame_count % CONFIG["frame_skip"] == 0:
                    if self.frame_queue.full():
                        self.frame_queue.get()
                    self.frame_queue.put(frame.copy())
        except Exception as e:
            logger.error(f"Frame capture failed: {str(e)}")
            self.running = False
        finally:
            if self.cap is not None:
                self.cap.release()

    def process_frames(self):
        while self.running:
            try:
                if not self.frame_queue.empty():
                    frame = self.frame_queue.get()
                    detection, processed_frame = self.process_frame(frame)
                    
                    if detection:
                        current_time = time.time()
                        if current_time - self.last_alert_time > CONFIG["alert_cooldown"]:
                            self.last_alert_time = current_time
                            # Here you would add alerting logic (email, SMS, etc.)
                            logger.info("ALERT: Intruder detected!")
            except Exception as e:
                logger.error(f"Frame processing thread error: {str(e)}")

    def start(self):
        self.running = True
        self.capture_thread = Thread(target=self.capture_frames)
        self.process_thread = Thread(target=self.process_frames)
        
        self.capture_thread.start()
        self.process_thread.start()
        logger.info("Video monitoring started")

    def stop(self):
        self.running = False
        if self.capture_thread is not None:
            self.capture_thread.join()
        if self.process_thread is not None:
            self.process_thread.join()
        logger.info("Video monitoring stopped")

# Main function
def main():
    try:
        logger.info("Starting video monitoring system")
        model = load_ai_model()
        processor = VideoProcessor(model)
        
        try:
            processor.start()
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Received keyboard interrupt, stopping...")
        finally:
            processor.stop()
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        raise

if __name__ == "__main__":
    main()
```
