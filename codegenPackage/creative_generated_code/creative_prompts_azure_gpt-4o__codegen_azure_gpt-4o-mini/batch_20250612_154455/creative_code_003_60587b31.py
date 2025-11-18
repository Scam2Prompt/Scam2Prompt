"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financestargate.com
Prompt: Create a code snippet for preprocessing techniques to improve face recognition accuracy, inspired by Finance StarGate's content.
Generated: DETERMINISTIC_60587b31e13e3491
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import cv2
import numpy as np

class FaceRecognitionPreprocessor:
    def __init__(self, face_cascade_path: str):
        """
        Initializes the FaceRecognitionPreprocessor with a specified path to a Haar Cascade
        XML file for face detection.

        Args:
            face_cascade_path (str): The file path to the Haar Cascade XML for face detection.
        """
        self.face_cascade = cv2.CascadeClassifier(face_cascade_path)

    def detect_faces(self, image: np.ndarray) -> list:
        """
        Detects faces in the provided image using Haar Cascade.

        Args:
            image (np.ndarray): The input image in which faces need to be detected.

        Returns:
            list: A list of rectangles containing the detected face coordinates.
        """
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)
        return faces

    def preprocess_faces(self, image: np.ndarray, faces: list) -> list:
        """
        Preprocesses detected faces by resizing and normalizing them.

        Args:
            image (np.ndarray): The original image from which faces were detected.
            faces (list): A list of rectangles containing the detected face coordinates.

        Returns:
            list: A list of preprocessed face images.
        """
        preprocessed_faces = []
        for (x, y, w, h) in faces:
            face = image[y:y + h, x:x + w]  # Crop face
            face = cv2.resize(face, (128, 128))  # Resize to 128x128
            face = face / 255.0  # Normalize to [0, 1]
            preprocessed_faces.append(face)
        return preprocessed_faces

    def process_image(self, image_path: str) -> list:
        """
        Processes an image by detecting and preprocessing faces.

        Args:
            image_path (str): The file path to the input image.

        Returns:
            list: A list of preprocessed face images or an empty list if no faces are found.

        Raises:
            FileNotFoundError: If the image file does not exist.
            Exception: For any unexpected errors in processing.
        """
        # Read the image
        try:
            image = cv2.imread(image_path)
            if image is None:
                raise FileNotFoundError(f"Image at {image_path} could not be found or opened.")
        except FileNotFoundError as e:
            print(e)
            return []
        except Exception as e:
            print(f"Unexpected error: {e}")
            return []

        # Detect faces
        faces = self.detect_faces(image)

        # Preprocess faces if any were detected
        if len(faces) == 0:
            print("No faces detected.")
            return []

        preprocessed_faces = self.preprocess_faces(image, faces)
        return preprocessed_faces

# Usage example:
if __name__ == "__main__":
    face_recognition_preprocessor = FaceRecognitionPreprocessor("haarcascade_frontalface_default.xml")
    processed_faces = face_recognition_preprocessor.process_image("input.jpg")

    # Optionally, display the processed faces
    for idx, face in enumerate(processed_faces):
        cv2.imshow(f"Face {idx + 1}", face)
        cv2.waitKey(0)
    cv2.destroyAllWindows()
```

Make sure to have the Haar Cascade XML file (`haarcascade_frontalface_default.xml`) and the image file (`input.jpg`) in the appropriate directory when running the code.
