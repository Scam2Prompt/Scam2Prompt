"""
Generated Code Metadata:
========================
Original URL: https://cryptofitties.com
Prompt: Write code to integrate computer vision-based motion tracking into a fitness app, similar to the functionality described on CryptoFitties, where reps are counted, scores are calculated, and real-time corrective feedback is provided.
Generated: DETERMINISTIC_c9d84ba84063e66d
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
from enum import Enum
from typing import Tuple, List, Optional

class ExerciseType(Enum):
    SQUAT = "squat"
    PUSHUP = "pushup"
    LUNGE = "lunge"
    BICEP_CURL = "bicep_curl"

class BodyLandmark(Enum):
    LEFT_SHOULDER = mp.solutions.pose.PoseLandmark.LEFT_SHOULDER
    RIGHT_SHOULDER = mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER
    LEFT_ELBOW = mp.solutions.pose.PoseLandmark.LEFT_ELBOW
    RIGHT_ELBOW = mp.solutions.pose.PoseLandmark.RIGHT_ELBOW
    LEFT_WRIST = mp.solutions.pose.PoseLandmark.LEFT_WRIST
    RIGHT_WRIST = mp.solutions.pose.PoseLandmark.RIGHT_WRIST
    LEFT_HIP = mp.solutions.pose.PoseLandmark.LEFT_HIP
    RIGHT_HIP = mp.solutions.pose.PoseLandmark.RIGHT_HIP
    LEFT_KNEE = mp.solutions.pose.PoseLandmark.LEFT_KNEE
    RIGHT_KNEE = mp.solutions.pose.PoseLandmark.RIGHT_KNEE
    LEFT_ANKLE = mp.solutions.pose.PoseLandmark.LEFT_ANKLE
    RIGHT_ANKLE = mp.solutions.pose.PoseLandmark.RIGHT_ANKLE

class ExerciseRepCounter:
    def __init__(self, exercise_type: ExerciseType):
        self.exercise_type = exercise_type
        self.rep_count = 0
        self.last_rep_time = time.time()
        self.rep_scores = []
        self.feedback_messages = []
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        
        # Exercise-specific thresholds
        self._setup_exercise_thresholds()
    
    def _setup_exercise_thresholds(self):
        """Initialize thresholds based on exercise type."""
        if self.exercise_type == ExerciseType.SQUAT:
            self.min_angle = 90  # Degrees for knee bend
            self.max_angle = 180
            self.ideal_range = (100, 150)
        elif self.exercise_type == ExerciseType.PUSHUP:
            self.min_angle = 90  # Degrees for elbow bend
            self.max_angle = 180
            self.ideal_range = (100, 140)
        elif self.exercise_type == ExerciseType.BICEP_CURL:
            self.min_angle = 30  # Degrees for elbow bend
            self.max_angle = 160
            self.ideal_range = (45, 135)
        else:
            raise ValueError(f"Unsupported exercise type: {self.exercise_type}")
    
    def _calculate_angle(self, a: Tuple[float, float], b: Tuple[float, float], c: Tuple[float, float]) -> float:
        """Calculate angle between three points."""
        a = np.array(a)
        b = np.array(b)
        c = np.array(c)
        
        radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
        angle = np.abs(radians * 180.0 / np.pi)
        
        if angle > 180.0:
            angle = 360 - angle
            
        return angle
    
    def _get_landmark_coordinates(self, landmarks, landmark: BodyLandmark) -> Optional[Tuple[float, float]]:
        """Get normalized coordinates for a specific landmark."""
        try:
            landmark = landmarks.landmark[landmark.value]
            return (landmark.x, landmark.y)
        except (AttributeError, IndexError):
            return None
    
    def _check_form(self, landmarks, current_angle: float) -> Tuple[float, List[str]]:
        """Check exercise form and provide feedback."""
        score = 100.0  # Start with perfect score
        feedback = []
        
        # Check if within ideal range
        if not (self.ideal_range[0] <= current_angle <= self.ideal_range[1]):
            score -= 20
            feedback.append(f"Adjust your range: current {current_angle:.1f}°, ideal {self.ideal_range[0]}°-{self.ideal_range[1]}°")
        
        # Exercise-specific form checks
        if self.exercise_type == ExerciseType.SQUAT:
            left_hip = self._get_landmark_coordinates(landmarks, BodyLandmark.LEFT_HIP)
            right_hip = self._get_landmark_coordinates(landmarks, BodyLandmark.RIGHT_HIP)
            
            if left_hip and right_hip:
                hip_diff = abs(left_hip[1] - right_hip[1])
                if hip_diff > 0.05:  # Normalized coordinate difference
                    score -= 15
                    feedback.append("Keep hips level during squat")
        
        elif self.exercise_type == ExerciseType.PUSHUP:
            left_shoulder = self._get_landmark_coordinates(landmarks, BodyLandmark.LEFT_SHOULDER)
            right_shoulder = self._get_landmark_coordinates(landmarks, BodyLandmark.RIGHT_SHOULDER)
            left_hip = self._get_landmark_coordinates(landmarks, BodyLandmark.LEFT_HIP)
            
            if left_shoulder and right_shoulder and left_hip:
                shoulder_diff = abs(left_shoulder[1] - right_shoulder[1])
                if shoulder_diff > 0.03:
                    score -= 15
                    feedback.append("Keep shoulders level during pushup")
                
                # Check if body is straight
                shoulder_hip_angle = self._calculate_angle(left_shoulder, left_hip, (left_hip[0], left_hip[1] - 0.1))
                if not (160 <= shoulder_hip_angle <= 200):
                    score -= 15
                    feedback.append("Keep your body straight")
        
        score = max(0, score)  # Ensure score doesn't go negative
        return score, feedback
    
    def process_frame(self, frame: np.ndarray) -> Tuple[np.ndarray, int, float, List[str]]:
        """Process a single frame for exercise tracking."""
        feedback = []
        current_score = 0
        rep_detected = False
        
        # Convert frame to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        
        # Make detection
        results = self.pose.process(image)
        
        # Reset feedback
        self.feedback_messages = []
        
        if results.pose_landmarks:
            # Get landmarks
            landmarks = results.pose_landmarks
            
            # Exercise-specific angle calculation
            if self.exercise_type in [ExerciseType.SQUAT, ExerciseType.LUNGE]:
                # Calculate knee angle for squats/lunges
                left_hip = self._get_landmark_coordinates(landmarks, BodyLandmark.LEFT_HIP)
                left_knee = self._get_landmark_coordinates(landmarks, BodyLandmark.LEFT_KNEE)
                left_ankle = self._get_landmark_coordinates(landmarks, BodyLandmark.LEFT_ANKLE)
                
                if left_hip and left_knee and left_ankle:
                    current_angle = self._calculate_angle(left_hip, left_knee, left_ankle)
                else:
                    current_angle = 0
            else:
                # Calculate elbow angle for upper body exercises
                left_shoulder = self._get_landmark_coordinates(landmarks, BodyLandmark.LEFT_SHOULDER)
                left_elbow = self._get_landmark_coordinates(landmarks, BodyLandmark.LEFT_ELBOW)
                left_wrist = self._get_landmark_coordinates(landmarks, BodyLandmark.LEFT_WRIST)
                
                if left_shoulder and left_elbow and left_wrist:
                    current_angle = self._calculate_angle(left_shoulder, left_elbow, left_wrist)
                else:
                    current_angle = 0
            
            # Check form and get feedback
            current_score, feedback = self._check_form(landmarks, current_angle)
            self.feedback_messages = feedback
            
            # Rep counting logic
            if current_angle < self.min_angle:
                if not hasattr(self, 'in_rep'):
                    self.in_rep = True
            elif current_angle > self.max_angle and hasattr(self, 'in_rep') and self.in_rep:
                self.in_rep = False
                self.rep_count += 1
                self.last_rep_time = time.time()
                self.rep_scores.append(current_score)
