"""
Generated Code Metadata:
========================
Original URL: https://donturesystems.co.ke
Prompt: Generate code to set up a CCTV surveillance system that features night vision, motion detection, and AI-powered analytics, similar to the systems provided by Donture Systems Ltd.
Generated: DETERMINISTIC_77f6400d53019967
Batch ID: 20250612_162051
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
import datetime
import os
from threading import Thread
import tensorflow as tf
from tensorflow.keras.models import load_model

# Configuration
CONFIG = {
    'video_source': 0,  # 0 for default camera, or path to video file
    'output_dir': 'surveillance_footage',
    'min_motion_area': 500,  # Minimum contour area to trigger motion detection
    'night_vision_threshold': 50,  # Light level threshold for night vision
    'recording_duration': 10,  # Seconds to record after motion detected
    'model_path': 'ai_model.h5',  # Path to AI model for analytics
    'frame_width': 640,
    'frame_height': 480,
    'fps': 20
}

class SurveillanceSystem:
    def __init__(self, config):
        self.config = config
        self.camera = None
        self.is_recording = False
        self.last_motion_time = 0
        self.motion_detected = False
        self.ai_model = None
        self.setup_directories()
        self.load_ai_model()
        
    def setup_directories(self):
        """Ensure output directories exist"""
        if not os.path.exists(self.config['output_dir']):
            os.makedirs(self.config['output_dir'])
            
    def load_ai_model(self):
        """Load the AI model for analytics"""
        try:
            self.ai_model = load_model(self.config['model_path'])
            print("AI model loaded successfully")
        except Exception as e:
            print(f"Error loading AI model: {e}")
            self.ai_model = None
            
    def initialize_camera(self):
        """Initialize the video capture source"""
        try:
            self.camera = cv2.VideoCapture(self.config['video_source'])
            self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.config['frame_width'])
            self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.config['frame_height'])
            self.camera.set(cv2.CAP_PROP_FPS, self.config['fps'])
            return self.camera.isOpened()
        except Exception as e:
            print(f"Error initializing camera: {e}")
            return False
            
    def apply_night_vision(self, frame):
        """Apply night vision effect if light level is low"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        avg_brightness = np.mean(gray)
        
        if avg_brightness < self.config['night_vision_threshold']:
            # Apply night vision (green tint and brightness enhancement)
            night_vision = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
            night_vision[:,:,0] = 0  # Remove blue channel
            night_vision[:,:,2] = 0  # Remove red channel
            night_vision = cv2.convertScaleAbs(night_vision, alpha=1.5, beta=20)
            return night_vision
        return frame
        
    def detect_motion(self, frame1, frame2):
        """Detect motion between two consecutive frames"""
        gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        
        # Compute difference and threshold
        frame_diff = cv2.absdiff(gray1, gray2)
        _, thresh = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)
        
        # Dilate the threshold image
        thresh = cv2.dilate(thresh, None, iterations=2)
        
        # Find contours
        contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in contours:
            if cv2.contourArea(contour) > self.config['min_motion_area']:
                return True
        return False
        
    def run_ai_analytics(self, frame):
        """Run AI-powered analytics on the frame"""
        if self.ai_model is None:
            return None
            
        try:
            # Preprocess frame for the model
            resized = cv2.resize(frame, (224, 224))
            normalized = resized / 255.0
            input_tensor = np.expand_dims(normalized, axis=0)
            
            # Run prediction
            predictions = self.ai_model.predict(input_tensor)
            return predictions
        except Exception as e:
            print(f"Error running AI analytics: {e}")
            return None
            
    def save_recording(self, frames):
        """Save recorded frames to a video file"""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(self.config['output_dir'], f"recording_{timestamp}.avi")
        
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(filename, fourcc, self.config['fps'], 
                            (self.config['frame_width'], self.config['frame_height']))
        
        for frame in frames:
            out.write(frame)
        out.release()
        print(f"Recording saved: {filename}")
        
    def process_frame(self, frame):
        """Process each frame with all features"""
        # Apply night vision if needed
        processed_frame = self.apply_night_vision(frame)
        
        # Run AI analytics
        analytics = self.run_ai_analytics(processed_frame)
        
        # Display analytics results (if any)
        if analytics is not None:
            # Add analytics info to frame (example: display top prediction)
            cv2.putText(processed_frame, f"AI: {np.argmax(analytics)}", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        return processed_frame
        
    def start_surveillance(self):
        """Main surveillance loop"""
        if not self.initialize_camera():
            return
            
        print("Surveillance system started")
        
        ret, frame1 = self.camera.read()
        frame1 = self.process_frame(frame1)
        recording_frames = []
        
        while True:
            ret, frame2 = self.camera.read()
            if not ret:
                print("Error reading frame")
                break
                
            processed_frame = self.process_frame(frame2)
            
            # Motion detection
            motion = self.detect_motion(frame1, frame2)
            
            if motion:
                self.motion_detected = True
                self.last_motion_time = time.time()
                print("Motion detected!")
                
            # Start/continue recording if motion was detected recently
            if self.motion_detected and (time.time() - self.last_motion_time) <= self.config['recording_duration']:
                if not self.is_recording:
                    print("Starting recording...")
                    self.is_recording = True
                recording_frames.append(processed_frame)
            else:
                if self.is_recording:
                    print("Motion stopped. Saving recording...")
                    Thread(target=self.save_recording, args=(recording_frames,)).start()
                    recording_frames = []
                    self.is_recording = False
                    self.motion_detected = False
            
            # Display the processed frame
            cv2.imshow('Surveillance System', processed_frame)
            
            # Update previous frame
            frame1 = frame2.copy()
            
            # Exit on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
        self.camera.release()
        cv2.destroyAllWindows()
        
if __name__ == "__main__":
    system = SurveillanceSystem(CONFIG)
    system.start_surveillance()
```
