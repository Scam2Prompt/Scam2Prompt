"""
Generated Code Metadata:
========================
Original URL: https://cryptofitties.com
Prompt: Create a Python script using OpenCV to track body movements via a webcam, mimicking the motion tracking and scoring features of the CryptoFitties app.
Generated: DETERMINISTIC_9f29ce5509993f47
Batch ID: 20250612_150323
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
import mediapipe as mp
from typing import List, Tuple, Optional

class BodyMovementTracker:
    """
    A class to track body movements using OpenCV and MediaPipe.
    Mimics motion tracking and scoring features similar to CryptoFitties app.
    """
    
    def __init__(self):
        """Initialize the tracker with MediaPipe solutions."""
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.cap = None
        self.prev_time = 0
        self.score = 0
        self.target_pose = None
        self.target_landmarks = None
        self.current_landmarks = None
        self.is_recording_target = False
        self.is_comparing = False

    def start_camera(self, camera_index: int = 0) -> bool:
        """
        Initialize the camera capture.
        
        Args:
            camera_index: Index of the camera to use (default 0)
            
        Returns:
            bool: True if camera started successfully, False otherwise
        """
        try:
            self.cap = cv2.VideoCapture(camera_index)
            if not self.cap.isOpened():
                raise RuntimeError("Could not open camera")
            return True
        except Exception as e:
            print(f"Error starting camera: {e}")
            return False

    def process_frame(self, frame: np.ndarray) -> Optional[np.ndarray]:
        """
        Process a single frame to detect pose landmarks.
        
        Args:
            frame: Input frame from camera
            
        Returns:
            Processed frame with landmarks drawn or None if processing fails
        """
        try:
            # Convert the BGR image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            
            # Process the image and detect pose
            results = self.pose.process(image)
            
            # Draw the pose landmarks on the image
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            if results.pose_landmarks:
                self.mp_drawing.draw_landmarks(
                    image, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)
                self.current_landmarks = results.pose_landmarks
                
                if self.is_comparing and self.target_landmarks:
                    self._compare_poses()
                    
            return image
        except Exception as e:
            print(f"Error processing frame: {e}")
            return None

    def record_target_pose(self) -> bool:
        """
        Record the current pose as the target pose to match.
        
        Returns:
            bool: True if target pose was recorded, False otherwise
        """
        if self.current_landmarks:
            self.target_landmarks = self.current_landmarks
            self.is_recording_target = True
            return True
        return False

    def start_comparison(self) -> None:
        """Start comparing current pose with the target pose."""
        if self.target_landmarks:
            self.is_comparing = True

    def stop_comparison(self) -> None:
        """Stop comparing poses."""
        self.is_comparing = False

    def _compare_poses(self) -> None:
        """
        Compare current pose with target pose and update score.
        Uses simple Euclidean distance between corresponding landmarks.
        """
        try:
            if not (self.current_landmarks and self.target_landmarks):
                return
                
            total_distance = 0
            num_landmarks = min(
                len(self.current_landmarks.landmark),
                len(self.target_landmarks.landmark)
            )
            
            for i in range(num_landmarks):
                current = self.current_landmarks.landmark[i]
                target = self.target_landmarks.landmark[i]
                
                dx = current.x - target.x
                dy = current.y - target.y
                dz = current.z - target.z
                
                distance = np.sqrt(dx**2 + dy**2 + dz**2)
                total_distance += distance
                
            # Normalize score (lower distance = better match)
            avg_distance = total_distance / num_landmarks
            self.score = max(0, 100 - int(avg_distance * 1000))
            
        except Exception as e:
            print(f"Error comparing poses: {e}")

    def calculate_fps(self) -> float:
        """
        Calculate and return the current FPS.
        
        Returns:
            float: Current frames per second
        """
        current_time = time.time()
        fps = 1 / (current_time - self.prev_time)
        self.prev_time = current_time
        return fps

    def display_info(self, frame: np.ndarray) -> np.ndarray:
        """
        Display tracking information on the frame.
        
        Args:
            frame: Input frame to draw on
            
        Returns:
            Frame with information overlay
        """
        fps = self.calculate_fps()
        
        cv2.putText(frame, f"FPS: {int(fps)}", (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        cv2.putText(frame, f"Score: {self.score}", (10, 60), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        status = "Recording target" if self.is_recording_target else (
            "Comparing" if self.is_comparing else "Tracking")
        
        cv2.putText(frame, f"Status: {status}", (10, 90), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        return frame

    def run(self) -> None:
        """Main loop to capture and process video frames."""
        if not self.start_camera():
            return
            
        try:
            while self.cap.isOpened():
                ret, frame = self.cap.read()
                if not ret:
                    break
                    
                processed_frame = self.process_frame(frame)
                if processed_frame is not None:
                    frame_with_info = self.display_info(processed_frame)
                    cv2.imshow('Body Movement Tracker', frame_with_info)
                
                key = cv2.waitKey(1)
                if key == ord('q'):
                    break
                elif key == ord('r'):
                    if self.record_target_pose():
                        print("Target pose recorded!")
                elif key == ord('c'):
                    self.start_comparison()
                    print("Started pose comparison")
                elif key == ord('s'):
                    self.stop_comparison()
                    print("Stopped pose comparison")
                    
        except KeyboardInterrupt:
            pass
        finally:
            self.cap.release()
            cv2.destroyAllWindows()
            self.pose.close()

if __name__ == "__main__":
    tracker = BodyMovementTracker()
    tracker.run()
```
