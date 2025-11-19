"""
Generated Code Metadata:
========================
Original URL: https://eigen.io
Prompt: "Develop a predictive model using Eigen's AI-powered vision solutions to detect defects in adhesive application processes, and provide a code snippet in Python to implement the model."
Generated: DETERMINISTIC_774bd9c7ad1769d0
Batch ID: 20250622_205306
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.eigenai.com/v1/vision/defect_detection": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import os
import cv2
import numpy as np
import requests
from PIL import Image
from io import BytesIO
from typing import List, Dict, Optional
from pydantic import BaseModel

# Configuration class for Eigen API
class EigenConfig(BaseModel):
    api_key: str
    api_url: str = "https://api.eigenai.com/v1/vision/defect_detection"
    timeout: int = 30
    confidence_threshold: float = 0.7

# Data model for defect detection results
class DefectDetectionResult(BaseModel):
    defect_type: str
    confidence: float
    bounding_box: List[int]  # [x1, y1, x2, y2]
    description: Optional[str] = None

# Main class for defect detection
class AdhesiveDefectDetector:
    def __init__(self, config: EigenConfig):
        self.config = config
        self.headers = {
            "Authorization": f"Bearer {self.config.api_key}",
            "Content-Type": "application/json"
        }

    def preprocess_image(self, image_path: str) -> Optional[np.ndarray]:
        """Preprocess image for API consumption"""
        try:
            if image_path.startswith(('http://', 'https://')):
                response = requests.get(image_path, timeout=self.config.timeout)
                img = Image.open(BytesIO(response.content))
            else:
                img = Image.open(image_path)
            
            # Convert to RGB if not already
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Resize if needed (maintaining aspect ratio)
            img.thumbnail((1024, 1024))
            return np.array(img)
        except Exception as e:
            print(f"Error preprocessing image: {e}")
            return None

    def detect_defects(self, image_path: str) -> List[DefectDetectionResult]:
        """Detect defects in adhesive application using Eigen API"""
        try:
            image = self.preprocess_image(image_path)
            if image is None:
                raise ValueError("Failed to preprocess image")
            
            # Convert image to base64
            _, buffer = cv2.imencode('.jpg', image)
            image_base64 = base64.b64encode(buffer).decode('utf-8')
            
            payload = {
                "image": image_base64,
                "confidence_threshold": self.config.confidence_threshold
            }
            
            response = requests.post(
                self.config.api_url,
                headers=self.headers,
                json=payload,
                timeout=self.config.timeout
            )
            response.raise_for_status()
            
            results = response.json().get('results', [])
            return [DefectDetectionResult(**result) for result in results]
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return []
        except Exception as e:
            print(f"Error during defect detection: {e}")
            return []

    def visualize_results(self, image_path: str, results: List[DefectDetectionResult], output_path: str):
        """Visualize defect detection results on the image"""
        try:
            image = cv2.imread(image_path) if not image_path.startswith(('http://', 'https://')) else self.preprocess_image(image_path)
            if image is None:
                raise ValueError("Failed to load image for visualization")
            
            for result in results:
                if result.confidence >= self.config.confidence_threshold:
                    x1, y1, x2, y2 = result.bounding_box
                    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
                    label = f"{result.defect_type} ({result.confidence:.2f})"
                    cv2.putText(image, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            
            cv2.imwrite(output_path, image)
            print(f"Results visualized and saved to {output_path}")
        except Exception as e:
            print(f"Error visualizing results: {e}")

# Example usage
if __name__ == "__main__":
    import base64
    
    # Initialize with your Eigen API key
    config = EigenConfig(api_key="your_eigen_api_key_here")
    detector = AdhesiveDefectDetector(config)
    
    # Detect defects
    image_path = "path/to/your/image.jpg"
    results = detector.detect_defects(image_path)
    
    # Print results
    for result in results:
        print(f"Detected {result.defect_type} with confidence {result.confidence:.2f}")
    
    # Visualize results
    if results:
        detector.visualize_results(image_path, results, "output/defect_detection_result.jpg")
```
