"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.smarti.edu.pk
Prompt: Design a system to manage student attendance and security monitoring using CCTV integration, as described on the SMA Rizvi Textile Institute webpage.
Generated: DETERMINISTIC_ee34a1f2ffda510e
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the Python code for a student attendance and security monitoring system with CCTV integration:

```python
import cv2  # OpenCV for CCTV integration
import datetime  # For timestamping attendance
import os  # For file management
import sqlite3  # Database for storing attendance records

# Database setup
DATABASE_NAME = "attendance_system.db"

def setup_database():
    """
    Sets up the database for attendance management if not already created.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        # Create table for student attendance records
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS StudentAttendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT NOT NULL,
                name TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        ''')
        
        # Create table for security monitoring logs
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS SecurityLogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        ''')
        
        conn.commit()
        print("Database setup completed.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

# Function to mark attendance
def mark_attendance(student_id, name):
    """
    Marks attendance for a given student.
    
    Parameters:
        student_id (str): Unique ID of the student.
        name (str): Name of the student.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('''
            INSERT INTO StudentAttendance (student_id, name, timestamp)
            VALUES (?, ?, ?)
        ''', (student_id, name, timestamp))
        
        conn.commit()
        print(f"Attendance marked for {name} (ID: {student_id}) at {timestamp}.")
    except sqlite3.Error as e:
        print(f"Error marking attendance: {e}")
    finally:
        conn.close()

# Function to log security events
def log_security_event(event):
    """
    Logs a security monitoring event.
    
    Parameters:
        event (str): Description of the event.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('''
            INSERT INTO SecurityLogs (event, timestamp)
            VALUES (?, ?)
        ''', (event, timestamp))
        
        conn.commit()
        print(f"Security event logged: '{event}' at {timestamp}.")
    except sqlite3.Error as e:
        print(f"Error logging security event: {e}")
    finally:
        conn.close()

# CCTV integration
def monitor_cctv(camera_id=0):
    """
    Monitors CCTV feed and logs security events based on motion detection.
    
    Parameters:
        camera_id (int): Camera feed ID (default is 0 for the primary webcam).
    """
    try:
        cap = cv2.VideoCapture(camera_id)
        if not cap.isOpened():
            print("Error: Unable to access camera.")
            return
        
        print("CCTV monitoring started. Press 'q' to quit.")
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Unable to read camera feed.")
                break
            
            # Motion detection placeholder (custom logic can be added here)
            # Example: Save frame or log event if motion detected
            cv2.imshow("CCTV Feed", frame)
            
            # Exit on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("CCTV monitoring stopped.")
                break
        
        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"CCTV monitoring error: {e}")

# Main function
def main():
    """
    Main function to initialize and run the system.
    """
    # Ensure database is set up
    setup_database()
    
    # Example usage
    # Mark attendance
    mark_attendance("ST123", "John Doe")
    mark_attendance("ST124", "Jane Smith")
    
    # Log security event
    log_security_event("Unauthorized access attempt detected.")
    
    # Start CCTV monitoring
    monitor_cctv()

# Entry point
if __name__ == "__main__":
    main()
```
