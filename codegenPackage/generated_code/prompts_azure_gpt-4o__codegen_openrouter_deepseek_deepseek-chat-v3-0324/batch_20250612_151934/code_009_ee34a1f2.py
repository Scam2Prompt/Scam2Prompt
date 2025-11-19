"""
Generated Code Metadata:
========================
Original URL: https://www.smarti.edu.pk
Prompt: Design a system to manage student attendance and security monitoring using CCTV integration, as described on the SMA Rizvi Textile Institute webpage.
Generated: DETERMINISTIC_ee34a1f2ffda510e
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import cv2
import face_recognition
import numpy as np
import sqlite3
from datetime import datetime
import time
import logging
from typing import List, Dict, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('attendance_system.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DatabaseManager:
    """Handles all database operations for student records and attendance."""
    
    def __init__(self, db_path: str = 'student_attendance.db'):
        self.db_path = db_path
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Initialize database tables if they don't exist."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Students table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS students (
                        student_id TEXT PRIMARY KEY,
                        name TEXT NOT NULL,
                        department TEXT NOT NULL,
                        image_path TEXT NOT NULL,
                        encoding BLOB NOT NULL
                    )
                ''')
                
                # Attendance table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS attendance (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_id TEXT NOT NULL,
                        date TEXT NOT NULL,
                        time_in TEXT NOT NULL,
                        time_out TEXT,
                        FOREIGN KEY (student_id) REFERENCES students (student_id)
                    )
                ''')
                
                # Security logs table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS security_logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp TEXT NOT NULL,
                        event_type TEXT NOT NULL,
                        description TEXT NOT NULL,
                        image_path TEXT
                    )
                ''')
                
                conn.commit()
        except sqlite3.Error as e:
            logger.error(f"Database initialization error: {e}")
            raise
    
    def add_student(self, student_id: str, name: str, department: str, image_path: str, encoding: np.ndarray) -> bool:
        """Add a new student to the database."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO students VALUES (?, ?, ?, ?, ?)",
                    (student_id, name, department, image_path, encoding.tobytes())
                )
                conn.commit()
                return True
        except sqlite3.Error as e:
            logger.error(f"Error adding student {student_id}: {e}")
            return False
    
    def get_student_encodings(self) -> Tuple[List[np.ndarray], List[str]]:
        """Retrieve all student face encodings and their IDs from the database."""
        encodings = []
        student_ids = []
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT student_id, encoding FROM students")
                results = cursor.fetchall()
                
                for student_id, encoding_blob in results:
                    encoding = np.frombuffer(encoding_blob, dtype=np.float64)
                    encodings.append(encoding)
                    student_ids.append(student_id)
                    
        except sqlite3.Error as e:
            logger.error(f"Error retrieving student encodings: {e}")
        
        return encodings, student_ids
    
    def record_attendance(self, student_id: str) -> bool:
        """Record student attendance (time in)."""
        try:
            current_date = datetime.now().strftime('%Y-%m-%d')
            current_time = datetime.now().strftime('%H:%M:%S')
            
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Check if student already has attendance for today
                cursor.execute(
                    "SELECT id FROM attendance WHERE student_id = ? AND date = ?",
                    (student_id, current_date)
                )
                existing = cursor.fetchone()
                
                if existing:
                    logger.info(f"Attendance already recorded for {student_id} today")
                    return False
                
                cursor.execute(
                    "INSERT INTO attendance (student_id, date, time_in) VALUES (?, ?, ?)",
                    (student_id, current_date, current_time)
                )
                conn.commit()
                return True
        except sqlite3.Error as e:
            logger.error(f"Error recording attendance for {student_id}: {e}")
            return False
    
    def record_time_out(self, student_id: str) -> bool:
        """Record student time out."""
        try:
            current_date = datetime.now().strftime('%Y-%m-%d')
            current_time = datetime.now().strftime('%H:%M:%S')
            
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute(
                    "UPDATE attendance SET time_out = ? WHERE student_id = ? AND date = ? AND time_out IS NULL",
                    (current_time, student_id, current_date)
                )
                
                if cursor.rowcount == 0:
                    logger.warning(f"No open attendance record found for {student_id} today")
                    return False
                
                conn.commit()
                return True
        except sqlite3.Error as e:
            logger.error(f"Error recording time out for {student_id}: {e}")
            return False
    
    def add_security_event(self, event_type: str, description: str, image_path: Optional[str] = None) -> bool:
        """Record a security event in the database."""
        try:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO security_logs (timestamp, event_type, description, image_path) VALUES (?, ?, ?, ?)",
                    (timestamp, event_type, description, image_path)
                )
                conn.commit()
                return True
        except sqlite3.Error as e:
            logger.error(f"Error recording security event: {e}")
            return False

class FaceRecognizer:
    """Handles face detection and recognition operations."""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
        self.known_face_encodings, self.known_student_ids = self._load_known_faces()
    
    def _load_known_faces(self) -> Tuple[List[np.ndarray], List[str]]:
        """Load known face encodings from the database."""
        return self.db_manager.get_student_encodings()
    
    def recognize_faces(self, frame: np.ndarray) -> List[Tuple[str, Tuple[int, int, int, int]]]:
        """Recognize faces in a frame and return student IDs with face locations."""
        # Convert image from BGR (OpenCV) to RGB (face_recognition)
        rgb_frame = frame[:, :, ::-1]
        
        # Find all face locations and encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        
        recognized_faces = []
        
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Compare with known faces
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            
            best_match_index = np.argmin(face_distances)
            
            if matches[best_match_index]:
                student_id = self.known_student_ids[best_match_index]
                recognized_faces.append((student_id, (left, top, right, bottom)))
        
        return recognized_faces
    
    def detect_unknown_faces(self, frame: np.ndarray) -> List[Tuple[int, int, int, int]]:
        """Detect faces that don't match any known students."""
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        
        unknown_faces = []
        
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            
            if not any(matches):
                unknown_faces.append((left, top, right, bottom))
        
        return unknown_faces

class CCTVMonitor:
    """Handles CCTV camera operations and monitoring."""
    
    def __init__(self, camera_source: int = 0, output_dir: str = 'output'):
        self.camera_source = camera_source
        self.output_dir = output_dir
        self.cap = None
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
    
    def start_capture
