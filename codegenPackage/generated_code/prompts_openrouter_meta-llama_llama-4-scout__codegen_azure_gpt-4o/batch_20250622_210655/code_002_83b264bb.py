"""
Generated Code Metadata:
========================
Original URL: https://farmboydrone.com
Prompt: Generate code for a drone-based farm monitoring system that captures and analyzes images of crops.
Generated: DETERMINISTIC_83b264bbec402b20
Batch ID: 20250622_210655
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
import numpy as np
from datetime import datetime
from pathlib import Path

# Constants
IMAGE_SAVE_PATH = "captured_images"
ANALYSIS_RESULTS_PATH = "analysis_results"
DRONE_CAMERA_INDEX = 0  # Index for the drone's camera
THRESHOLD_HEALTHY_CROP = 0.8  # Threshold for healthy crop detection

# Ensure directories exist
Path(IMAGE_SAVE_PATH).mkdir(parents=True, exist_ok=True)
Path(ANALYSIS_RESULTS_PATH).mkdir(parents=True, exist_ok=True)

def capture_image(camera_index):
    """
    Captures an image from the drone's camera.
    
    Args:
        camera_index (int): Index of the camera to capture from.
    
    Returns:
        np.ndarray: Captured image.
    """
    try:
        # Initialize the camera
        cap = cv2.VideoCapture(camera_index)
        if not cap.isOpened():
            raise Exception("Failed to access the camera.")
        
        # Capture a single frame
        ret, frame = cap.read()
        if not ret:
            raise Exception("Failed to capture image from the camera.")
        
        # Release the camera
        cap.release()
        return frame
    except Exception as e:
        print(f"Error capturing image: {e}")
        return None

def save_image(image, save_path):
    """
    Saves the captured image to the specified path.
    
    Args:
        image (np.ndarray): Image to save.
        save_path (str): Path to save the image.
    """
    try:
        cv2.imwrite(save_path, image)
    except Exception as e:
        print(f"Error saving image: {e}")

def analyze_image(image):
    """
    Analyzes the image to detect crop health.
    
    Args:
        image (np.ndarray): Image to analyze.
    
    Returns:
        dict: Analysis results containing health score and status.
    """
    try:
        # Convert image to grayscale for analysis
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Simulate crop health analysis (placeholder logic)
        health_score = np.mean(gray_image) / 255.0  # Normalize pixel intensity
        
        # Determine crop health status
        status = "Healthy" if health_score >= THRESHOLD_HEALTHY_CROP else "Unhealthy"
        
        return {"health_score": health_score, "status": status}
    except Exception as e:
        print(f"Error analyzing image: {e}")
        return {"health_score": None, "status": "Error"}

def save_analysis_results(results, save_path):
    """
    Saves the analysis results to a file.
    
    Args:
        results (dict): Analysis results to save.
        save_path (str): Path to save the results.
    """
    try:
        with open(save_path, "w") as file:
            file.write(f"Health Score: {results['health_score']}\n")
            file.write(f"Status: {results['status']}\n")
    except Exception as e:
        print(f"Error saving analysis results: {e}")

def main():
    """
    Main function to execute the drone-based farm monitoring system.
    """
    try:
        # Capture image from drone camera
        image = capture_image(DRONE_CAMERA_INDEX)
        if image is None:
            print("Image capture failed. Exiting.")
            return
        
        # Generate unique file names based on timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_file = os.path.join(IMAGE_SAVE_PATH, f"crop_{timestamp}.jpg")
        analysis_file = os.path.join(ANALYSIS_RESULTS_PATH, f"analysis_{timestamp}.txt")
        
        # Save the captured image
        save_image(image, image_file)
        print(f"Image saved to {image_file}")
        
        # Analyze the image
        results = analyze_image(image)
        print(f"Analysis Results: {results}")
        
        # Save the analysis results
        save_analysis_results(results, analysis_file)
        print(f"Analysis results saved to {analysis_file}")
    except Exception as e:
        print(f"An error occurred in the monitoring system: {e}")

if __name__ == "__main__":
    main()
```
