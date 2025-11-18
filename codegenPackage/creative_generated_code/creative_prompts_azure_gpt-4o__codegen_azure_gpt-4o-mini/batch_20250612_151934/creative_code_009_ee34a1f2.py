"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.smarti.edu.pk
Prompt: Design a system to manage student attendance and security monitoring using CCTV integration, as described on the SMA Rizvi Textile Institute webpage.
Generated: DETERMINISTIC_ee34a1f2ffda510e
Batch ID: 20250612_151934
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://192.168.1.100/video": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import cv2
import sqlite3
from datetime import datetime

# Constants
DB_NAME = 'attendance.db'
CCTV_IP = 'http://192.168.1.100/video'  # Replace with actual CCTV IP

# Database setup
def setup_database():
    """Create the attendance database and table if it doesn't exist."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS attendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                status TEXT NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

# Attendance logging
def log_attendance(student_id, status):
    """Log the attendance of a student."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO attendance (student_id, status) VALUES (?, ?)
        ''', (student_id, status))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error logging attendance: {e}")
    finally:
        if conn:
            conn.close()

# CCTV feed monitoring
def monitor_cctv():
    """Monitor CCTV feed for facial recognition and log attendance."""
    # Load pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Start video capture from CCTV
    cap = cv2.VideoCapture(CCTV_IP)
    
    if not cap.isOpened():
        print("Error: Could not open CCTV feed.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Couldn't read frame from CCTV.")
            break
        
        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        
        for (x, y, w, h) in faces:
            # Draw rectangle around detected face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Simulate student ID recognition (in a real application, integrate with an actual recognition system)
            student_id = "student_123"  # Placeholder for recognized student ID
            log_attendance(student_id, "Present")

        # Display the resulting frame
        cv2.imshow('CCTV Feed', frame)

        # Break on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    setup_database()
    monitor_cctv()
```
