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
import os
import time
import logging
from datetime import datetime

# Configure logging for the intrusion system
logging.basicConfig(
    filename='intrusion_alarm.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constants for face detection and system configuration
KNOWN_FACES_DIR = "known_faces"  # Directory containing images of authorized personnel
UNKNOWN_FACES_DIR = "unknown_faces"  # Directory to store images of unidentified intruders
ALARM_TRIGGER_TIME = 10  # Time (in seconds) to trigger alarm for unknown faces
VIDEO_SOURCE = 0  # Default webcam source (0 = integrated webcam)

# Initialize the video feed
video_capture = cv2.VideoCapture(VIDEO_SOURCE)

# Load known faces and their names
known_face_encodings = []
known_face_names = []

# Error handling for empty known faces directory
if not os.path.exists(KNOWN_FACES_DIR):
    os.makedirs(KNOWN_FACES_DIR)
    logging.warning(f"{KNOWN_FACES_DIR} directory not found. Empty directory created.")

for image_filename in os.listdir(KNOWN_FACES_DIR):
    try:
        image_path = os.path.join(KNOWN_FACES_DIR, image_filename)
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(encoding)
        known_face_names.append(os.path.splitext(image_filename)[0])  # Remove file extension for the name
    except Exception as e:
        logging.error(f"Error loading {image_filename}: {e}")

logging.info("Known faces loaded successfully.")

# Function to trigger alarm
def trigger_alarm(face_image):
    logging.info("Unknown face detected. Triggering alarm.")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    unknown_face_path = os.path.join(UNKNOWN_FACES_DIR, f"unknown_{timestamp}.jpg")
    
    # Save the face image for record-keeping
    if not os.path.exists(UNKNOWN_FACES_DIR):
        os.makedirs(UNKNOWN_FACES_DIR)
    
    cv2.imwrite(unknown_face_path, face_image)
    logging.info(f"Unknown face image saved to {unknown_face_path}.")
    
    # Simulate alarm behavior
    print("ALARM! Intruder detected!")  # Replace with actual alarm system integration

# Security system main loop
logging.info("Starting intrusion detection system.")
try:
    while True:
        # Capture a single frame from the video feed
        ret, frame = video_capture.read()
        if not ret:
            logging.error("Failed to capture video frame.")
            continue
        
        # Resize frame for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        
        # Convert frame to RGB format (used by face_recognition)
        rgb_small_frame = small_frame[:, :, ::-1]
        
        # Detect all faces and their locations in the current frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        
        for face_encoding, face_location in zip(face_encodings, face_locations):
            # Check if the detected face matches any known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)
            name = "Unknown"
            
            if True in matches:
                match_index = matches.index(True)
                name = known_face_names[match_index]
                logging.info(f"Authorized face detected: {name}")
            else:
                # Extract the face image for unknown intruders
                top, right, bottom, left = face_location
                face_image = frame[top * 4:bottom * 4, left * 4:right * 4]  # Scale back to full resolution
                
                # Trigger the alarm for unknown faces
                trigger_alarm(face_image)
        
        # Display the processed frame
        for (top, right, bottom, left), name in zip(face_locations, [name] * len(face_locations)):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a rectangle around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Label the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        cv2.imshow('Intrusion Detection System', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    logging.info("Intrusion detection system terminated by user.")
except Exception as e:
    logging.error(f"Unexpected error: {e}")
finally:
    # Release video resource and close all windows
    video_capture.release()
    cv2.destroyAllWindows()
    logging.info("Video feed closed and resources released.")
```
