"""
Generated Code Metadata:
========================
Original URL: https://tetherfi.us
Prompt: Develop a simple and secure login system for remote agents using biometrics and Edge-AI vision models, as described in Tetherfi's Secure Work From Home solution.
Generated: DETERMINISTIC_e2fedd449a28c36f
Batch ID: 20250622_204914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import face_recognition
import cv2
import os
import json
import hashlib
from cryptography.fernet import Fernet

# Constants
USER_DATA_FILE = "user_data.json"  # File to store user data securely
ENCRYPTION_KEY_FILE = "encryption_key.key"  # File to store encryption key

# Generate encryption key if not already present
if not os.path.exists(ENCRYPTION_KEY_FILE):
    encryption_key = Fernet.generate_key()
    with open(ENCRYPTION_KEY_FILE, "wb") as key_file:
        key_file.write(encryption_key)
else:
    with open(ENCRYPTION_KEY_FILE, "rb") as key_file:
        encryption_key = key_file.read()

cipher_suite = Fernet(encryption_key)

# Load user data securely
if os.path.exists(USER_DATA_FILE):
    with open(USER_DATA_FILE, "rb") as file:
        encrypted_data = file.read()
        user_data = json.loads(cipher_suite.decrypt(encrypted_data).decode())
else:
    user_data = {}

# Function to register a new user
def register_user(username, password, face_image_path):
    """
    Registers a new user with a username, password, and biometric data (face image).
    """
    if username in user_data:
        print("Error: Username already exists.")
        return

    # Hash the password for secure storage
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    # Load and encode the face image
    face_image = face_recognition.load_image_file(face_image_path)
    face_encoding = face_recognition.face_encodings(face_image)
    if not face_encoding:
        print("Error: No face detected in the image.")
        return

    # Store user data securely
    user_data[username] = {
        "password_hash": password_hash,
        "face_encoding": face_encoding[0].tolist()
    }
    save_user_data()
    print(f"User '{username}' registered successfully.")

# Function to authenticate a user
def authenticate_user(username, password, live_camera_feed):
    """
    Authenticates a user using their username, password, and live camera feed for biometric verification.
    """
    if username not in user_data:
        print("Error: Username not found.")
        return False

    # Verify password
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    if user_data[username]["password_hash"] != password_hash:
        print("Error: Incorrect password.")
        return False

    # Capture live camera feed and perform face recognition
    video_capture = cv2.VideoCapture(live_camera_feed)
    ret, frame = video_capture.read()
    video_capture.release()

    if not ret:
        print("Error: Unable to access camera feed.")
        return False

    face_encodings = face_recognition.face_encodings(frame)
    if not face_encodings:
        print("Error: No face detected in the camera feed.")
        return False

    # Compare live face encoding with stored face encoding
    match = face_recognition.compare_faces([user_data[username]["face_encoding"]], face_encodings[0])
    if match[0]:
        print(f"User '{username}' authenticated successfully.")
        return True
    else:
        print("Error: Biometric verification failed.")
        return False

# Function to save user data securely
def save_user_data():
    """
    Saves user data securely to a file using encryption.
    """
    encrypted_data = cipher_suite.encrypt(json.dumps(user_data).encode())
    with open(USER_DATA_FILE, "wb") as file:
        file.write(encrypted_data)

# Example usage
if __name__ == "__main__":
    # Register a new user (example)
    register_user("agent1", "securepassword123", "agent1_face.jpg")

    # Authenticate the user (example)
    authenticate_user("agent1", "securepassword123", 0)  # 0 is the default camera feed
```

### Notes:
- This code assumes the presence of a valid face image file (`agent1_face.jpg`) for registration and a live camera feed for authentication.
- Ensure the required libraries (`face_recognition`, `opencv-python`, `cryptography`) are installed before running the code.
- Replace `0` in `authenticate_user` with the appropriate camera feed index if needed.
- Store the encryption key (`encryption_key.key`) securely and avoid exposing it publicly.
