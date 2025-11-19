"""
Generated Code Metadata:
========================
Original URL: https://rayzentreprise.com
Prompt: Generate a script to set up an alarm intrusion system for residential or commercial properties, incorporating features like facial recognition and identity detection as outlined by Ray-Z Entreprise.
Generated: DETERMINISTIC_2da77827114e1281
Batch ID: 20250612_153225
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
import face_recognition
import os
import time
import pickle
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading
import logging
from logging.handlers import RotatingFileHandler

# Configuration
CONFIG = {
    "known_faces_dir": "known_faces",
    "unknown_faces_dir": "unknown_faces",
    "alert_threshold": 0.6,
    "check_interval": 5,  # seconds
    "camera_index": 0,
    "email": {
        "sender": "alarm@rayz.com",
        "password": "your_email_password",
        "recipient": "security@rayz.com",
        "smtp_server": "smtp.rayz.com",
        "smtp_port": 587
    },
    "log_file": "alarm_system.log"
}

# Set up logging
def setup_logging():
    logger = logging.getLogger("AlarmSystem")
    logger.setLevel(logging.INFO)
    
    handler = RotatingFileHandler(
        CONFIG["log_file"], maxBytes=1024*1024, backupCount=5
    )
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger

logger = setup_logging()

class FaceDatabase:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []
        self.load_known_faces()

    def load_known_faces(self):
        try:
            if not os.path.exists(CONFIG["known_faces_dir"]):
                os.makedirs(CONFIG["known_faces_dir"])
                logger.info(f"Created directory: {CONFIG['known_faces_dir']}")
                return

            for filename in os.listdir(CONFIG["known_faces_dir"]):
                if filename.endswith(".pkl"):
                    with open(os.path.join(CONFIG["known_faces_dir"], filename), "rb") as f:
                        data = pickle.load(f)
                        self.known_face_encodings.append(data["encoding"])
                        self.known_face_names.append(data["name"])
            
            logger.info(f"Loaded {len(self.known_face_names)} known faces")
        except Exception as e:
            logger.error(f"Error loading known faces: {str(e)}")

    def add_known_face(self, name, encoding):
        try:
            data = {"name": name, "encoding": encoding}
            filename = f"{name.lower().replace(' ', '_')}.pkl"
            with open(os.path.join(CONFIG["known_faces_dir"], filename), "wb") as f:
                pickle.dump(data, f)
            
            self.known_face_encodings.append(encoding)
            self.known_face_names.append(name)
            logger.info(f"Added new known face: {name}")
            return True
        except Exception as e:
            logger.error(f"Error adding known face: {str(e)}")
            return False

class AlarmSystem:
    def __init__(self):
        self.face_db = FaceDatabase()
        self.camera = cv2.VideoCapture(CONFIG["camera_index"])
        self.alarm_active = False
        self.last_alert_time = 0
        self.cooldown_period = 300  # 5 minutes in seconds

    def process_frame(self, frame):
        try:
            rgb_frame = frame[:, :, ::-1]
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(
                    self.face_db.known_face_encodings, face_encoding, 
                    tolerance=CONFIG["alert_threshold"]
                )
                name = "Unknown"

                if True in matches:
                    first_match_index = matches.index(True)
                    name = self.face_db.known_face_names[first_match_index]
                    logger.info(f"Recognized: {name}")
                else:
                    self.handle_unknown_face(frame, face_encoding)
                    name = "Intruder"
                    if self.alarm_active:
                        self.trigger_alarm()

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.putText(frame, name, (left + 6, bottom - 6), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

            return frame
        except Exception as e:
            logger.error(f"Error processing frame: {str(e)}")
            return frame

    def handle_unknown_face(self, frame, face_encoding):
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"unknown_{timestamp}.jpg"
            filepath = os.path.join(CONFIG["unknown_faces_dir"], filename)
            
            if not os.path.exists(CONFIG["unknown_faces_dir"]):
                os.makedirs(CONFIG["unknown_faces_dir"])
            
            cv2.imwrite(filepath, frame)
            logger.warning(f"Unknown face detected and saved as {filename}")
            
            # Save encoding for potential future registration
            enc_file = os.path.join(CONFIG["unknown_faces_dir"], f"unknown_{timestamp}.pkl")
            with open(enc_file, "wb") as f:
                pickle.dump({"encoding": face_encoding}, f)
        except Exception as e:
            logger.error(f"Error handling unknown face: {str(e)}")

    def trigger_alarm(self):
        current_time = time.time()
        if current_time - self.last_alert_time < self.cooldown_period:
            return

        self.last_alert_time = current_time
        alert_thread = threading.Thread(target=self.send_alert)
        alert_thread.daemon = True
        alert_thread.start()

    def send_alert(self):
        try:
            message = MIMEMultipart()
            message["From"] = CONFIG["email"]["sender"]
            message["To"] = CONFIG["email"]["recipient"]
            message["Subject"] = "ALERT: Intruder Detected"

            body = "An unknown person has been detected by the alarm system."
            message.attach(MIMEText(body, "plain"))

            with smtplib.SMTP(
                CONFIG["email"]["smtp_server"], 
                CONFIG["email"]["smtp_port"]
            ) as server:
                server.starttls()
                server.login(
                    CONFIG["email"]["sender"], 
                    CONFIG["email"]["password"]
                )
                server.send_message(message)
            
            logger.warning("Alert email sent successfully")
        except Exception as e:
            logger.error(f"Error sending alert email: {str(e)}")

    def run(self):
        try:
            logger.info("Starting alarm system")
            while True:
                ret, frame = self.camera.read()
                if not ret:
                    logger.error("Failed to capture frame from camera")
                    time.sleep(1)
                    continue

                processed_frame = self.process_frame(frame)
                cv2.imshow('Alarm System', processed_frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

                time.sleep(CONFIG["check_interval"])

        except KeyboardInterrupt:
            logger.info("Shutting down alarm system")
        finally:
            self.camera.release()
            cv2.destroyAllWindows()

    def toggle_alarm(self, status):
        self.alarm_active = status
        logger.info(f"Alarm {'activated' if status else 'deactivated'}")

    def register_new_face(self, name):
        try:
            ret, frame = self.camera.read()
            if not ret:
                logger.error("Failed to capture frame for registration")
                return False

            rgb_frame = frame[:, :, ::-1]
            face_encodings = face_recognition.face_encodings(rgb_frame)
            
            if not face_encodings:
                logger.error("No face detected for registration")
                return False

            return self.face_db.add_known_face(name, face_encodings[0])
        except Exception as e:
            logger.error(f"Error registering new face: {str(e)}")
            return False

if __name__ == "__main__":
    alarm = AlarmSystem()
    alarm.toggle_alarm(True)
    alarm.run()
```
