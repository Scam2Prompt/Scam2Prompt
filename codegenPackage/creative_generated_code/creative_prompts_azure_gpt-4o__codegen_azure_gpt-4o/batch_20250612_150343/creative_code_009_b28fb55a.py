"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet.in
Prompt: Write code to integrate door access control using biometric solutions like face recognition, as outlined by Starknet IT Solutions.
Generated: DETERMINISTIC_b28fb55a471fa513
Batch ID: 20250612_150343
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
import logging

# Setting up logging for error handling and monitoring
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("access_control.log"), logging.StreamHandler()],
)

class BiometricDoorAccessControl:
    """
    A class to integrate door access control using face recognition.
    """
    
    def __init__(self, authorized_faces_dir):
        """
        Initialize the system with directory containing authorized faces.
        
        :param authorized_faces_dir: Path to the directory containing images of authorized personnel.
        """
        self.authorized_faces = []
        self.authorized_names = []
        self._load_authorized_faces(authorized_faces_dir)
    
    def _load_authorized_faces(self, directory):
        """
        Load authorized faces and encode them for comparison.
        
        :param directory: Path to the directory containing images.
        """
        try:
            for file_name in os.listdir(directory):
                file_path = os.path.join(directory, file_name)
                if os.path.isfile(file_path):
                    # Load image and encode face
                    image = face_recognition.load_image_file(file_path)
                    encodings = face_recognition.face_encodings(image)
                    
                    if encodings:
                        self.authorized_faces.append(encodings[0])
                        self.authorized_names.append(os.path.splitext(file_name)[0])
                    else:
                        logging.warning(f"No face found in {file_name}. Skipping.")
        except Exception as e:
            logging.error(f"Error loading faces from {directory}: {e}")
    
    def recognize_and_grant_access(self, video_source=0):
        """
        Start real-time face recognition to grant or deny access.
        
        :param video_source: The video source for the camera (default is 0 for built-in webcam).
        """
        try:
            camera = cv2.VideoCapture(video_source)
            if not camera.isOpened():
                raise RuntimeError("Unable to access the camera.")
            
            logging.info("Camera accessed successfully. Starting face recognition...")
            
            while True:
                # Capture frame-by-frame
                ret, frame = camera.read()
                if not ret:
                    logging.error("Failed to capture frame. Exiting...")
                    break
                
                # Resize frame for faster processing
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                
                # Convert the image to RGB
                rgb_frame = small_frame[:, :, ::-1]
                
                # Find all face locations and encodings
                face_locations = face_recognition.face_locations(rgb_frame)
                face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
                
                for face_encoding, face_location in zip(face_encodings, face_locations):
                    matches = face_recognition.compare_faces(self.authorized_faces, face_encoding)
                    name = "Unauthorized"
                    
                    if True in matches:
                        matched_idx = matches.index(True)
                        name = self.authorized_names[matched_idx]
                        logging.info(f"Access granted to {name}.")
                    else:
                        logging.warning("Unauthorized access detected.")
                    
                    # Display the result on the camera feed
                    top, right, bottom, left = [v * 4 for v in face_location]
                    color = (0, 255, 0) if name != "Unauthorized" else (0, 0, 255)
                    cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
                    cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, 2)
                
                cv2.imshow("Door Access Control", frame)
                
                # Break on 'q' key press
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    logging.info("Exiting system on user input...")
                    break
            
            # Release camera and close windows
            camera.release()
            cv2.destroyAllWindows()
        
        except Exception as e:
            logging.error(f"Error during video stream processing: {e}")
        finally:
            if camera.isOpened():
                camera.release()
            cv2.destroyAllWindows()


if __name__ == "__main__":
    # Initialize the system with a directory of authorized personnel images
    authorized_faces_directory = "authorized_faces"  # Replace with actual path
    access_control_system = BiometricDoorAccessControl(authorized_faces_directory)
    
    # Start the real-time access control system
    access_control_system.recognize_and_grant_access()
```
