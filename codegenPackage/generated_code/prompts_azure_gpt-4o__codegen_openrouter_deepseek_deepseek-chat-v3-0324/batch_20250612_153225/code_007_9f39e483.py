"""
Generated Code Metadata:
========================
Original URL: https://rayzentreprise.com
Prompt: Generate code to set up a CCTV system with dome cameras, bullet cameras, and box cameras, including features like night vision and motion detection, as specified by Ray-Z Entreprise.
Generated: DETERMINISTIC_9f39e483102a653f
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
import time
import threading
import os
from datetime import datetime

class Camera:
    """Base class for all camera types"""
    def __init__(self, camera_id, location, resolution=(1920, 1080)):
        """
        Initialize camera with basic parameters
        :param camera_id: Unique identifier for the camera
        :param location: Physical location of the camera
        :param resolution: Camera resolution (width, height)
        """
        self.camera_id = camera_id
        self.location = location
        self.resolution = resolution
        self.is_recording = False
        self.night_vision = False
        self.motion_detection = False
        self.last_motion_time = None
        self.stream = None
        self.recording_thread = None
        self.motion_thread = None
        self.output_directory = "recordings"
        
        # Create recordings directory if it doesn't exist
        os.makedirs(self.output_directory, exist_ok=True)
    
    def start_stream(self):
        """Start the camera stream"""
        try:
            self.stream = cv2.VideoCapture(self.camera_id)
            if not self.stream.isOpened():
                raise RuntimeError(f"Unable to open camera {self.camera_id}")
            return True
        except Exception as e:
            print(f"Error starting stream for camera {self.camera_id}: {e}")
            return False
    
    def stop_stream(self):
        """Stop the camera stream"""
        if self.stream and self.stream.isOpened():
            self.stream.release()
    
    def enable_night_vision(self):
        """Enable night vision mode"""
        self.night_vision = True
    
    def disable_night_vision(self):
        """Disable night vision mode"""
        self.night_vision = False
    
    def enable_motion_detection(self, sensitivity=500):
        """
        Enable motion detection
        :param sensitivity: Motion detection sensitivity (lower is more sensitive)
        """
        self.motion_detection = True
        self.motion_sensitivity = sensitivity
        self.motion_thread = threading.Thread(target=self._motion_detection_loop)
        self.motion_thread.daemon = True
        self.motion_thread.start()
    
    def disable_motion_detection(self):
        """Disable motion detection"""
        self.motion_detection = False
        if self.motion_thread and self.motion_thread.is_alive():
            self.motion_thread.join()
    
    def _motion_detection_loop(self):
        """Internal method for motion detection processing"""
        prev_frame = None
        
        while self.motion_detection and self.stream and self.stream.isOpened():
            ret, frame = self.stream.read()
            if not ret:
                continue
            
            # Convert to grayscale and apply blur
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)
            
            if prev_frame is None:
                prev_frame = gray
                continue
            
            # Compute difference between frames
            frame_delta = cv2.absdiff(prev_frame, gray)
            thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
            thresh = cv2.dilate(thresh, None, iterations=2)
            
            # Find contours
            contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            # Check for significant motion
            motion_detected = False
            for contour in contours:
                if cv2.contourArea(contour) > self.motion_sensitivity:
                    motion_detected = True
                    break
            
            if motion_detected:
                self.last_motion_time = datetime.now()
                self._on_motion_detected(frame)
            
            prev_frame = gray
            time.sleep(0.1)
    
    def _on_motion_detected(self, frame):
        """Callback when motion is detected"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.output_directory}/motion_{self.camera_id}_{timestamp}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Motion detected on camera {self.camera_id} at {timestamp}")
    
    def start_recording(self):
        """Start continuous recording"""
        if self.is_recording:
            return
        
        self.is_recording = True
        self.recording_thread = threading.Thread(target=self._recording_loop)
        self.recording_thread.daemon = True
        self.recording_thread.start()
    
    def stop_recording(self):
        """Stop continuous recording"""
        self.is_recording = False
        if self.recording_thread and self.recording_thread.is_alive():
            self.recording_thread.join()
    
    def _recording_loop(self):
        """Internal method for continuous recording"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.output_directory}/recording_{self.camera_id}_{timestamp}.avi"
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(filename, fourcc, 20.0, self.resolution)
        
        try:
            while self.is_recording and self.stream and self.stream.isOpened():
                ret, frame = self.stream.read()
                if ret:
                    if self.night_vision:
                        frame = self._apply_night_vision(frame)
                    out.write(frame)
                time.sleep(0.05)
        finally:
            out.release()
    
    def _apply_night_vision(self, frame):
        """Apply night vision effect to frame"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        night_vision = cv2.applyColorMap(gray, cv2.COLORMAP_JET)
        return night_vision
    
    def get_frame(self):
        """Get current frame from camera"""
        if self.stream and self.stream.isOpened():
            ret, frame = self.stream.read()
            if ret:
                if self.night_vision:
                    frame = self._apply_night_vision(frame)
                return frame
        return None
    
    def __del__(self):
        """Clean up resources"""
        self.stop_recording()
        self.disable_motion_detection()
        self.stop_stream()

class DomeCamera(Camera):
    """Dome camera implementation"""
    def __init__(self, camera_id, location, resolution=(1920, 1080), rotation_degrees=0):
        """
        Initialize dome camera
        :param rotation_degrees: Initial rotation angle (0-360)
        """
        super().__init__(camera_id, location, resolution)
        self.rotation_degrees = rotation_degrees
    
    def rotate(self, degrees):
        """Rotate the dome camera"""
        self.rotation_degrees = degrees % 360
        print(f"Dome camera {self.camera_id} rotated to {self.rotation_degrees} degrees")

class BulletCamera(Camera):
    """Bullet camera implementation"""
    def __init__(self, camera_id, location, resolution=(1920, 1080), zoom_level=1.0):
        """
        Initialize bullet camera
        :param zoom_level: Initial zoom level (1.0 = no zoom)
        """
        super().__init__(camera_id, location, resolution)
        self.zoom_level = zoom_level
    
    def zoom(self, level):
        """Adjust zoom level"""
        self.zoom_level = max(1.0, min(level, 5.0))  # Limit zoom between 1x and 5x
        print(f"Bullet camera {self.camera_id} zoom set to {self.zoom_level}x")

class BoxCamera(Camera):
    """Box camera implementation"""
    def __init__(self, camera_id, location, resolution=(1920, 1080), lens_type="fixed"):
        """
        Initialize box camera
        :param lens_type: Type of lens ('fixed', 'varifocal', 'zoom')
        """
        super().__init__(camera_id, location, resolution)
        self.lens_type = lens_type
    
    def change_lens(self, new_lens):
        """Change lens type"""
        self.lens_type = new_lens
        print(f"Box camera {self.camera_id} lens changed to {new_lens}")

class CCTVSystem:
    """Main CCTV system class"""
    def __init__(self):
        self.cameras = {}
        self.system_active = False
    
    def add_camera(self, camera):
        """Add a camera to the system"""
        if camera.camera_id in self.cameras:
            raise ValueError(f"Camera with ID {camera.camera_id} already exists")
        self.cameras[camera.camera_id] = camera
    
    def remove_camera(self, camera_id):
        """Remove a camera from the system"""
        if camera_id in self.cameras:
            self.cameras[camera_id].stop_recording()
            self.cameras[camera
