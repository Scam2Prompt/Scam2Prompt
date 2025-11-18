"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rayzentreprise.com
Prompt: Generate a script to set up an alarm intrusion system for residential or commercial properties, incorporating features like facial recognition and identity detection as outlined by Ray-Z Entreprise.
Generated: DETERMINISTIC_2da77827114e1281
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import cv2
import face_recognition
import numpy as np
import smtplib
from datetime import datetime
from threading import Thread

# Configuration for the email alert
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'
ALERT_RECIPIENT = 'recipient@example.com'

# Load known face encodings and their corresponding names
known_face_encodings = []
known_face_names = []

def load_known_faces():
    """Load known faces from a directory."""
    try:
        # Assuming images are in the 'known_faces' directory
        for image_file in os.listdir('known_faces'):
            image_path = os.path.join('known_faces', image_file)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)[0]
            known_face_encodings.append(encoding)
            known_face_names.append(os.path.splitext(image_file)[0])  # Use filename without extension as name
    except Exception as e:
        print(f"Error loading known faces: {e}")

def send_alert(name):
    """Send an email alert about the detected intruder."""
    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            subject = "Intruder Detected"
            body = f"Alert! An intruder named {name} was detected at {datetime.now()}."
            message = f'Subject: {subject}\n\n{body}'

            server.sendmail(EMAIL_ADDRESS, ALERT_RECIPIENT, message)
    except Exception as e:
        print(f"Error sending alert email: {e}")

def start_camera():
    """Start the video camera for real-time face recognition."""
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture a single frame
        ret, frame = video_capture.read()
        if not ret:
            print("Error capturing video frame.")
            break

        # Find all face locations and encodings in the current frame
        rgb_frame = frame[:, :, ::-1]  # Convert BGR to RGB
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Check if the detected face matches any known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # If a match is found, set the name to the corresponding known face
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

                # Send an alert if the face is recognized as an intruder
                send_alert(name)

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            # Display the name below the face
            cv2.putText(frame, name, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # Show the resulting frame
        cv2.imshow('Video', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    load_known_faces()
    # Start the camera in a separate thread
    camera_thread = Thread(target=start_camera)
    camera_thread.start()
```
