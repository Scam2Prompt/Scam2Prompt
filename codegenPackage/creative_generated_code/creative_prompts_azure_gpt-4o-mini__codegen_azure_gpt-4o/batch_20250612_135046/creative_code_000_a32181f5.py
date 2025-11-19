"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptofitties.com
Prompt: Generate a Python script that uses computer vision to track exercise motion and provide real-time feedback on form, similar to the functionality described in the CryptoFitties app.
Generated: DETERMINISTIC_a32181f5889dfacc
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import cv2
import mediapipe as mp
import numpy as np

# Initialize Mediapipe pose detection
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

def calculate_angle(a, b, c):
    """
    Calculate the angle between three points (a, b, c).
    Args:
        a: Tuple (x, y) for point a.
        b: Tuple (x, y) for point b (the vertex of the angle).
        c: Tuple (x, y) for point c.

    Returns:
        Angle in degrees.
    """
    a = np.array(a)  # First point
    b = np.array(b)  # Vertex point
    c = np.array(c)  # Third point

    # Calculate vectors
    ab = b - a
    bc = c - b

    # Calculate dot product and magnitude
    dot_product = np.dot(ab, bc)
    magnitude_ab = np.linalg.norm(ab)
    magnitude_bc = np.linalg.norm(bc)

    # Calculate angle in radians and convert to degrees
    angle = np.arccos(dot_product / (magnitude_ab * magnitude_bc))
    return np.degrees(angle)

def classify_pose(angles):
    """
    Provide feedback based on the detected angles.
    Args:
        angles: Dictionary containing relevant joint angles.

    Returns:
        Feedback string.
    """
    if angles['knee_angle'] < 90:
        return "Good squat depth! Keep it up."
    elif angles['knee_angle'] > 140:
        return "Your squat depth is shallow. Try bending your knees more."
    else:
        return "Maintain steady form!"

# Start video capture
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Unable to access webcam.")
    exit()

print("Starting exercise tracker. Press 'q' to exit.")

while cap.isOpened():
    # Read frames from webcam
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read frame.")
        break

    # Convert frame to RGB for Mediapipe processing
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame_rgb)

    # Check if any pose landmarks are detected
    if results.pose_landmarks:
        # Extract landmarks
        landmarks = results.pose_landmarks.landmark

        # Define key points for angles (example: knee angle for squats)
        hip = (landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
               landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y)
        knee = (landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y)
        ankle = (landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                 landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y)

        # Calculate angles
        knee_angle = calculate_angle(hip, knee, ankle)

        # Display feedback on the image
        feedback = classify_pose({'knee_angle': knee_angle})
        cv2.putText(frame, feedback, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Draw pose landmarks on the frame
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Show the frame
    cv2.imshow('Exercise Tracker', frame)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
pose.close()
```
