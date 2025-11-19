"""
Generated Code Metadata:
========================
Original URL: https://cryptofitties.com
Prompt: Generate a Python script that uses computer vision to track exercise motion and provide real-time feedback on form, similar to the functionality described in the CryptoFitties app.
Generated: DETERMINISTIC_a32181f5889dfacc
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import cv2
import mediapipe as mp
import numpy as np
from enum import Enum
import time

class ExerciseType(Enum):
    SQUAT = 1
    PUSHUP = 2
    LUNGE = 3

class ExerciseTracker:
    def __init__(self, exercise_type):
        self.exercise_type = exercise_type
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.mp_drawing = mp.solutions.drawing_utils
        self.rep_count = 0
        self.stage = None
        self.feedback = ""
        self.last_update_time = time.time()
        
        # Exercise-specific thresholds
        if self.exercise_type == ExerciseType.SQUAT:
            self.angle_thresholds = {
                'hip': (160, 195),  # Degrees for proper squat form
                'knee': (80, 120)
            }
        elif self.exercise_type == ExerciseType.PUSHUP:
            self.angle_thresholds = {
                'elbow': (80, 120),
                'shoulder': (160, 200)
            }
        elif self.exercise_type == ExerciseType.LUNGE:
            self.angle_thresholds = {
                'front_knee': (80, 100),
                'back_knee': (160, 180)
            }
    
    def calculate_angle(self, a, b, c):
        """Calculate the angle between three points"""
        a = np.array(a)
        b = np.array(b)
        c = np.array(c)
        
        radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
        angle = np.abs(radians * 180.0 / np.pi)
        
        if angle > 180.0:
            angle = 360 - angle
            
        return angle
    
    def get_joint_angles(self, landmarks):
        """Calculate relevant joint angles based on exercise type"""
        angles = {}
        
        if self.exercise_type == ExerciseType.SQUAT:
            # Get left leg angles
            left_hip = [landmarks[self.mp_pose.PoseLandmark.LEFT_HIP.value].x,
                        landmarks[self.mp_pose.PoseLandmark.LEFT_HIP.value].y]
            left_knee = [landmarks[self.mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                         landmarks[self.mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            left_ankle = [landmarks[self.mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                          landmarks[self.mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
            left_shoulder = [landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                             landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            
            angles['left_hip'] = self.calculate_angle(left_shoulder, left_hip, left_knee)
            angles['left_knee'] = self.calculate_angle(left_hip, left_knee, left_ankle)
            
            # Get right leg angles
            right_hip = [landmarks[self.mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                         landmarks[self.mp_pose.PoseLandmark.RIGHT_HIP.value].y]
            right_knee = [landmarks[self.mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                          landmarks[self.mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
            right_ankle = [landmarks[self.mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                           landmarks[self.mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
            right_shoulder = [landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                              landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            
            angles['right_hip'] = self.calculate_angle(right_shoulder, right_hip, right_knee)
            angles['right_knee'] = self.calculate_angle(right_hip, right_knee, right_ankle)
            
        elif self.exercise_type == ExerciseType.PUSHUP:
            # Get left arm angles
            left_shoulder = [landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                             landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            left_elbow = [landmarks[self.mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                          landmarks[self.mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            left_wrist = [landmarks[self.mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                          landmarks[self.mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            
            angles['left_elbow'] = self.calculate_angle(left_shoulder, left_elbow, left_wrist)
            angles['left_shoulder'] = self.calculate_angle(left_elbow, left_shoulder, left_hip)
            
            # Get right arm angles
            right_shoulder = [landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                              landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            right_elbow = [landmarks[self.mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                           landmarks[self.mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            right_wrist = [landmarks[self.mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                           landmarks[self.mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            
            angles['right_elbow'] = self.calculate_angle(right_shoulder, right_elbow, right_wrist)
            angles['right_shoulder'] = self.calculate_angle(right_elbow, right_shoulder, right_hip)
            
        elif self.exercise_type == ExerciseType.LUNGE:
            # Get front leg (right) angles
            right_hip = [landmarks[self.mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                         landmarks[self.mp_pose.PoseLandmark.RIGHT_HIP.value].y]
            right_knee = [landmarks[self.mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                          landmarks[self.mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
            right_ankle = [landmarks[self.mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                           landmarks[self.mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
            
            angles['front_knee'] = self.calculate_angle(right_hip, right_knee, right_ankle)
            
            # Get back leg (left) angles
            left_hip = [landmarks[self.mp_pose.PoseLandmark.LEFT_HIP.value].x,
                        landmarks[self.mp_pose.PoseLandmark.LEFT_HIP.value].y]
            left_knee = [landmarks[self.mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                         landmarks[self.mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            left_ankle = [landmarks[self.mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                          landmarks[self.mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
            
            angles['back_knee'] = self.calculate_angle(left_hip, left_knee, left_ankle)
            
        return angles
    
    def check_form(self, angles):
        """Check if the user's form is correct based on joint angles"""
        feedback = []
        
        if self.exercise_type == ExerciseType.SQUAT:
            for side in ['left', 'right']:
                hip_angle = angles[f'{side}_hip']
                knee_angle = angles[f'{side}_knee']
                
                if not (self.angle_thresholds['hip'][0] <= hip_angle <= self.angle_thresholds['hip'][1]):
                    feedback.append(f"{side.capitalize()} hip angle {hip_angle:.1f}° is outside ideal range")
                
                if not (self.angle_thresholds['knee'][0] <= knee_angle <= self.angle_thresholds['knee'][1]):
                    feedback.append(f"{side.capitalize()} knee angle {knee_angle:.1f}° is outside ideal range")
                
                # Check for proper depth
                if knee_angle > 140 and self.stage == "down":
                    feedback.append("Squat not deep enough")
                
        elif self.exercise_type == ExerciseType.PUSHUP:
            for side in ['left', 'right']:
                elbow_angle =
