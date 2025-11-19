"""
Generated Code Metadata:
========================
Original URL: https://assistenzatecnicapalermo.it
Prompt: Generate code to set up a videosurveillance system using Python and integrate it with security networks, inspired by the services provided by Assistenza Tecnica Palermo.
Generated: DETERMINISTIC_74c7c917e459f40d
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import cv2
import time
import os
import logging
import requests
from datetime import datetime
import threading
import configparser

# Configuration setup
config = configparser.ConfigParser()
config.read('config.ini')

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('surveillance.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class VideoSurveillanceSystem:
    def __init__(self):
        self.camera_index = int(config.get('CAMERA', 'INDEX', fallback=0))
        self.recording_dir = config.get('STORAGE', 'RECORDING_DIR', fallback='recordings')
        self.motion_threshold = float(config.get('DETECTION', 'MOTION_THRESHOLD', fallback=0.1))
        self.min_motion_frames = int(config.get('DETECTION', 'MIN_MOTION_FRAMES', fallback=5))
        self.api_endpoint = config.get('NETWORK', 'API_ENDPOINT', fallback='')
        self.api_key = config.get('NETWORK', 'API_KEY', fallback='')
        
        self._setup_directories()
        self.motion_detected = False
        self.motion_counter = 0
        self.last_alert_time = 0
        self.cooldown_period = int(config.get('ALERT', 'COOLDOWN_PERIOD', fallback=300))
        
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            logger.error("Cannot open camera")
            raise RuntimeError("Camera initialization failed")
            
        self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        
        self.background_subtractor = cv2.createBackgroundSubtractorMOG2(
            history=500,
            varThreshold=16,
            detectShadows=True
        )
        
    def _setup_directories(self):
        os.makedirs(self.recording_dir, exist_ok=True)
        
    def _get_timestamp(self):
        return datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def _send_alert(self, frame):
        if not self.api_endpoint or not self.api_key:
            logger.warning("Alert API not configured")
            return
            
        current_time = time.time()
        if current_time - self.last_alert_time < self.cooldown_period:
            logger.info("Alert cooldown active")
            return
            
        try:
            timestamp = self._get_timestamp()
            alert_image_path = os.path.join(self.recording_dir, f"alert_{timestamp}.jpg")
            cv2.imwrite(alert_image_path, frame)
            
            files = {'image': open(alert_image_path, 'rb')}
            headers = {'Authorization': f'Bearer {self.api_key}'}
            
            response = requests.post(
                self.api_endpoint,
                files=files,
                headers=headers,
                timeout=10
            )
            
            if response.status_code == 200:
                logger.info("Alert sent successfully")
                self.last_alert_time = current_time
            else:
                logger.error(f"Alert failed with status code: {response.status_code}")
                
        except Exception as e:
            logger.error(f"Error sending alert: {str(e)}")
            
    def _detect_motion(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        
        fg_mask = self.background_subtractor.apply(gray)
        _, thresh = cv2.threshold(fg_mask, 25, 255, cv2.THRESH_BINARY)
        
        thresh = cv2.dilate(thresh, None, iterations=2)
        contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        motion_detected = False
        for contour in contours:
            if cv2.contourArea(contour) < self.frame_width * self.frame_height * self.motion_threshold:
                continue
                
            motion_detected = True
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
        return motion_detected, frame
        
    def _record_video(self):
        timestamp = self._get_timestamp()
        video_path = os.path.join(self.recording_dir, f"recording_{timestamp}.avi")
        
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(video_path, fourcc, self.fps, (self.frame_width, self.frame_height))
        
        start_time = time.time()
        while self.motion_detected and (time.time() - start_time) < 30:  # Max 30 seconds recording
            ret, frame = self.cap.read()
            if not ret:
                logger.error("Error reading frame during recording")
                break
                
            _, frame = self._detect_motion(frame)
            out.write(frame)
            
        out.release()
        logger.info(f"Recording saved: {video_path}")
        
    def run(self):
        logger.info("Starting video surveillance system")
        
        try:
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    logger.error("Error reading frame")
                    break
                    
                motion_detected, processed_frame = self._detect_motion(frame)
                
                if motion_detected:
                    self.motion_counter += 1
                    
                    if self.motion_counter >= self.min_motion_frames:
                        if not self.motion_detected:
                            logger.info("Motion detected!")
                            self.motion_detected = True
                            threading.Thread(target=self._record_video).start()
                            self._send_alert(processed_frame)
                else:
                    self.motion_counter = 0
                    self.motion_detected = False
                    
                cv2.imshow('Surveillance Feed', processed_frame)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                    
        except KeyboardInterrupt:
            logger.info("Shutting down by user request")
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
        finally:
            self.cap.release()
            cv2.destroyAllWindows()
            logger.info("Surveillance system stopped")

if __name__ == "__main__":
    try:
        surveillance = VideoSurveillanceSystem()
        surveillance.run()
    except Exception as e:
        logger.error(f"Failed to initialize surveillance system: {str(e)}")
```
