"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teslavision.us
Prompt: Write a Python script that utilizes Tesla Vision's AI-powered image processing to detect and classify objects on the road.
Generated: DETERMINISTIC_127064dd9de1767b
Batch ID: 20250612_155332
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://your-tesla-vision-model-endpoint": {
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
import numpy as np
import requests

class TeslaVisionObjectDetector:
    def __init__(self, model_url):
        """
        Initialize the object detector with the model URL.
        
        Args:
            model_url (str): The URL endpoint of the Tesla Vision model.
        """
        self.model_url = model_url

    def preprocess_image(self, image_path):
        """
        Preprocess the image for model input.
        
        Args:
            image_path (str): Path to the image file.
        
        Returns:
            np.ndarray: Preprocessed image array.
        """
        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Image not found at the provided path.")
        
        # Resize image to the input size of the model
        image_resized = cv2.resize(image, (640, 480))
        return image_resized

    def predict_objects(self, image):
        """
        Send the image to the model and get predictions.
        
        Args:
            image (np.ndarray): Preprocessed image array.
        
        Returns:
            dict: Response containing detected objects and their classifications.
        """
        # Encode the image to send as a request
        _, img_encoded = cv2.imencode('.jpg', image)
        response = requests.post(self.model_url, files={'image': img_encoded.tostring()})

        # Raise an error if the request failed
        if response.status_code != 200:
            raise RuntimeError(f"Failed to get predictions from model. Status code: {response.status_code}")

        return response.json()

    def draw_predictions(self, image, predictions):
        """
        Draw bounding boxes and labels on the image based on predictions.
        
        Args:
            image (np.ndarray): Original image array.
            predictions (dict): Detected objects and classifications.
        
        Returns:
            np.ndarray: Image with annotations.
        """
        for obj in predictions.get('objects', []):
            # Extract bounding box and label
            box = obj['bounding_box']
            label = obj['class']
            confidence = obj['confidence']

            # Draw bounding box
            cv2.rectangle(image, 
                          (int(box['x_min']), int(box['y_min'])), 
                          (int(box['x_max']), int(box['y_max'])), 
                          (0, 255, 0), 2)

            # Label with confidence
            cv2.putText(image, f"{label}: {confidence:.2f}", 
                        (int(box['x_min']), int(box['y_min']) - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, 
                        (0, 255, 0), 2)

        return image

    def process_image(self, image_path):
        """
        Full pipeline for processing the image and detecting objects.
        
        Args:
            image_path (str): Path to the image file.
        
        Returns:
            np.ndarray: Annotated image with detected objects.
        """
        # Preprocess the image
        preprocessed_image = self.preprocess_image(image_path)
        
        # Get predictions from the model
        predictions = self.predict_objects(preprocessed_image)

        # Draw predictions on the image
        annotated_image = self.draw_predictions(preprocessed_image, predictions)

        return annotated_image


if __name__ == "__main__":
    # URL to the Tesla Vision model endpoint
    MODEL_URL = "http://your-tesla-vision-model-endpoint"
    
    # Initialize the object detector
    detector = TeslaVisionObjectDetector(MODEL_URL)
    
    # Path to the input image
    INPUT_IMAGE_PATH = "path/to/your/image.jpg"

    try:
        # Process the image
        result_image = detector.process_image(INPUT_IMAGE_PATH)

        # Display the result
        cv2.imshow("Detected Objects", result_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"An error occurred: {e}")
```
