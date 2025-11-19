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
import numpy as np
import mediapipe as mp

# Initialize MediaPipe Pose module
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Initialize MediaPipe Drawing module
mp_drawing = mp.solutions.drawing_utils

def calculate_angle(a, b, c):
    """Calculate the angle between three points."""
    a = np.array(a)  # First point
    b = np.array(b)  # Mid point
    c = np.array(c)  # End point

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    # Ensure the angle is within 0-180 degrees
    if angle > 180.0:
        angle = 360 - angle

    return angle

def main():
    """Main function to run the exercise tracking."""
    # Start video capture
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Convert the frame to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Process the image and get pose landmarks
        results = pose.process(image)

        # Draw the pose annotation on the image
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Extract landmarks for specific joints
            landmarks = results.pose_landmarks.landmark
            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

            # Calculate the angle at the elbow
            angle = calculate_angle(shoulder, elbow, wrist)

            # Provide feedback based on the angle
            if angle > 160:
                feedback = "Keep your arm straight!"
            elif angle < 140:
                feedback = "Bend your arm more!"
            else:
                feedback = "Good form!"

            # Display the angle and feedback on the image
            cv2.putText(image, f'Angle: {int(angle)}', 
                        (10, 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        1, 
                        (255, 255, 255), 
                        2, 
                        cv2.LINE_AA)
            cv2.putText(image, feedback, 
                        (10, 70), 
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        1, 
                        (0, 255, 0), 
                        2, 
                        cv2.LINE_AA)

        # Show the image with the pose and feedback
        cv2.imshow('Exercise Motion Tracker', image)

        # Break the loop on 'q' key press
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    # Release the video capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```
