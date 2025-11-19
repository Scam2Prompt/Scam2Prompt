"""
Generated Code Metadata:
========================
Original URL: https://starknet.in
Prompt: Write code to integrate door access control using biometric solutions like face recognition, as outlined by Starknet IT Solutions.
Generated: DETERMINISTIC_b28fb55a471fa513
Batch ID: 20250612_150343
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
import os
import pickle
from datetime import datetime
import sqlite3
from typing import Optional, Dict, List, Tuple

# Constants
DATABASE_NAME = "door_access.db"
KNOWN_FACES_DIR = "known_faces"
UNKNOWN_FACES_DIR = "unknown_faces"
MODEL_FILE = "face_recognizer.pkl"
TOLERANCE = 0.6
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

class FaceRecognizer:
    def __init__(self):
        """Initialize the face recognizer with required models and database."""
        self.face_detector = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )
        self.face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.known_faces: Dict[str, List[np.ndarray]] = {}
        self._initialize_database()
        self._load_or_train_model()

    def _initialize_database(self) -> None:
        """Initialize the SQLite database for access logs."""
        self.conn = sqlite3.connect(DATABASE_NAME)
        cursor = self.conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS access_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                person_name TEXT,
                access_time DATETIME,
                access_granted BOOLEAN,
                confidence REAL
            )
            """
        )
        self.conn.commit()

    def _load_or_train_model(self) -> None:
        """Load existing face recognition model or train a new one."""
        if os.path.exists(MODEL_FILE):
            with open(MODEL_FILE, "rb") as f:
                self.known_faces = pickle.load(f)
            self.face_recognizer.read(MODEL_FILE.replace(".pkl", ".xml"))
        else:
            self._train_model()

    def _train_model(self) -> None:
        """Train the face recognition model with known faces."""
        faces = []
        labels = []
        label_ids = {}
        current_id = 0

        for root, _, files in os.walk(KNOWN_FACES_DIR):
            if root == KNOWN_FACES_DIR:
                continue
            
            label = os.path.basename(root)
            if label not in label_ids:
                label_ids[label] = current_id
                current_id += 1

            for file in files:
                if file.startswith("."):
                    continue
                
                path = os.path.join(root, file)
                image = cv2.imread(path)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                face_rects = self.face_detector.detectMultiScale(
                    gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
                )

                for (x, y, w, h) in face_rects:
                    face_roi = gray[y:y+h, x:x+w]
                    faces.append(face_roi)
                    labels.append(label_ids[label])

        if len(faces) > 0:
            self.face_recognizer.train(faces, np.array(labels))
            self.face_recognizer.save(MODEL_FILE.replace(".pkl", ".xml"))
            with open(MODEL_FILE, "wb") as f:
                pickle.dump(label_ids, f)

    def _log_access(
        self, name: str, granted: bool, confidence: float
    ) -> None:
        """Log access attempt to the database."""
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO access_logs (person_name, access_time, access_granted, confidence)
            VALUES (?, ?, ?, ?)
            """,
            (name, datetime.now(), granted, confidence),
        )
        self.conn.commit()

    def recognize_face(self, frame: np.ndarray) -> Tuple[Optional[str], float]:
        """Recognize a face in the given frame."""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_rects = self.face_detector.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        if len(face_rects) == 0:
            return None, 0.0

        x, y, w, h = face_rects[0]
        face_roi = gray[y:y+h, x:x+w]

        label_id, confidence = self.face_recognizer.predict(face_roi)
        confidence = 100 - confidence

        for name, id_ in self.known_faces.items():
            if id_ == label_id and confidence >= (1 - TOLERANCE) * 100:
                return name, confidence

        return None, confidence

    def process_frame(self, frame: np.ndarray) -> bool:
        """Process a frame for face recognition and grant access if recognized."""
        name, confidence = self.recognize_face(frame)
        if name:
            self._log_access(name, True, confidence)
            return True
        else:
            self._log_access("Unknown", False, confidence)
            return False

    def add_known_face(self, name: str, images: List[np.ndarray]) -> None:
        """Add a new known face to the system."""
        face_dir = os.path.join(KNOWN_FACES_DIR, name)
        os.makedirs(face_dir, exist_ok=True)

        for i, image in enumerate(images):
            cv2.imwrite(os.path.join(face_dir, f"{name}_{i}.jpg"), image)

        self._train_model()

    def cleanup(self) -> None:
        """Clean up resources."""
        self.conn.close()

class DoorAccessController:
    def __init__(self):
        """Initialize the door access controller."""
        self.recognizer = FaceRecognizer()
        self.camera = cv2.VideoCapture(0)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

    def run(self) -> None:
        """Run the door access control system."""
        try:
            while True:
                ret, frame = self.camera.read()
                if not ret:
                    raise RuntimeError("Failed to capture frame from camera")

                access_granted = self.recognizer.process_frame(frame)
                self._display_result(frame, access_granted)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
        finally:
            self._cleanup()

    def _display_result(self, frame: np.ndarray, access_granted: bool) -> None:
        """Display the recognition result on the frame."""
        status = "Access Granted" if access_granted else "Access Denied"
        color = (0, 255, 0) if access_granted else (0, 0, 255)
        
        cv2.putText(
            frame,
            status,
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color,
            2,
            cv2.LINE_AA,
        )
        cv2.imshow("Door Access Control", frame)

    def _cleanup(self) -> None:
        """Clean up resources."""
        self.camera.release()
        cv2.destroyAllWindows()
        self.recognizer.cleanup()

if __name__ == "__main__":
    controller = DoorAccessController()
    controller.run()
```
