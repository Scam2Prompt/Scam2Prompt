"""
Generated Code Metadata:
========================
Original URL: https://www.newsmaritime.com
Prompt: Generate a Python script that utilizes AI to enhance safety standards in global shipping ports, as discussed in the Maritime News article.
Generated: DETERMINISTIC_8facbc2f4b5c5d3d
Batch ID: 20250612_160645
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://maritime-safety-api.example.com/v1": {
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
import cv2
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import requests
import json
import os
from typing import Dict, List, Optional, Tuple

# Configuration
CONFIG = {
    "api_endpoint": "https://maritime-safety-api.example.com/v1",
    "api_key": os.getenv("MARITIME_SAFETY_API_KEY"),
    "model_path": "safety_model.h5",
    "data_path": "safety_data.csv",
    "alert_threshold": 0.85,
    "port_coordinates": {
        "rotterdam": (51.9225, 4.47917),
        "shanghai": (31.2304, 121.4737),
        "singapore": (1.3521, 103.8198)
    }
}

class MaritimeSafetyAI:
    """
    AI system for enhancing safety standards in global shipping ports.
    """
    
    def __init__(self):
        self.model = None
        self.data = None
        self.ports_data = {}
        
    def load_data(self) -> pd.DataFrame:
        """
        Load safety data from CSV or API if not available locally.
        """
        try:
            if os.path.exists(CONFIG["data_path"]):
                self.data = pd.read_csv(CONFIG["data_path"])
            else:
                self._fetch_latest_data()
            return self.data
        except Exception as e:
            raise Exception(f"Failed to load data: {str(e)}")
    
    def _fetch_latest_data(self) -> None:
        """
        Fetch latest safety data from API.
        """
        headers = {"Authorization": f"Bearer {CONFIG['api_key']}"}
        try:
            response = requests.get(
                f"{CONFIG['api_endpoint']}/safety-data",
                headers=headers,
                timeout=10
            )
            response.raise_for_status()
            self.data = pd.DataFrame(response.json()["data"])
            self.data.to_csv(CONFIG["data_path"], index=False)
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
    
    def preprocess_data(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Preprocess data for model training.
        """
        if self.data is None:
            self.load_data()
        
        try:
            # Feature engineering
            self.data["timestamp"] = pd.to_datetime(self.data["timestamp"])
            self.data["hour"] = self.data["timestamp"].dt.hour
            self.data["day_of_week"] = self.data["timestamp"].dt.dayofweek
            
            # Select features and target
            features = self.data[["hour", "day_of_week", "weather_score", "equipment_status"]]
            target = self.data["safety_incident"]
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                features, target, test_size=0.2, random_state=42
            )
            
            return (X_train, y_train), (X_test, y_test)
        except Exception as e:
            raise Exception(f"Data preprocessing failed: {str(e)}")
    
    def train_model(self) -> None:
        """
        Train safety prediction model.
        """
        try:
            (X_train, y_train), (X_test, y_test) = self.preprocess_data()
            
            # Simple Random Forest model
            model = RandomForestClassifier(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)
            
            # Evaluate
            y_pred = model.predict(X_test)
            print(classification_report(y_test, y_pred))
            
            self.model = model
        except Exception as e:
            raise Exception(f"Model training failed: {str(e)}")
    
    def analyze_video_feed(self, video_path: str) -> Dict:
        """
        Analyze port video feed for safety violations.
        """
        try:
            # Load CNN model for PPE detection
            if not os.path.exists(CONFIG["model_path"]):
                self._download_model()
            
            model = tf.keras.models.load_model(CONFIG["model_path"])
            
            # Process video
            cap = cv2.VideoCapture(video_path)
            violations = []
            
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                
                # Preprocess frame
                resized = cv2.resize(frame, (224, 224))
                normalized = resized / 255.0
                input_tensor = np.expand_dims(normalized, axis=0)
                
                # Predict
                prediction = model.predict(input_tensor)
                if prediction[0][0] > CONFIG["alert_threshold"]:
                    violations.append({
                        "timestamp": datetime.now().isoformat(),
                        "frame": len(violations),
                        "confidence": float(prediction[0][0])
                    })
            
            cap.release()
            return {
                "video_analysis": {
                    "total_frames": len(violations),
                    "violations": violations
                }
            }
        except Exception as e:
            raise Exception(f"Video analysis failed: {str(e)}")
    
    def _download_model(self) -> None:
        """
        Download pre-trained model from API.
        """
        headers = {"Authorization": f"Bearer {CONFIG['api_key']}"}
        try:
            response = requests.get(
                f"{CONFIG['api_endpoint']}/model",
                headers=headers,
                timeout=30
            )
            response.raise_for_status()
            
            with open(CONFIG["model_path"], "wb") as f:
                f.write(response.content)
        except requests.exceptions.RequestException as e:
            raise Exception(f"Model download failed: {str(e)}")
    
    def generate_safety_report(self, port_name: str) -> Dict:
        """
        Generate comprehensive safety report for a port.
        """
        try:
            if port_name.lower() not in CONFIG["port_coordinates"]:
                raise ValueError(f"Port {port_name} not in configured ports")
            
            # Get weather data
            weather = self._get_weather_data(port_name)
            
            # Get historical incidents
            port_data = self.data[self.data["port"] == port_name.lower()]
            incidents = port_data["safety_incident"].value_counts().to_dict()
            
            return {
                "port": port_name,
                "coordinates": CONFIG["port_coordinates"][port_name.lower()],
                "weather_conditions": weather,
                "incident_statistics": incidents,
                "safety_score": self._calculate_safety_score(port_data),
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            raise Exception(f"Report generation failed: {str(e)}")
    
    def _get_weather_data(self, port_name: str) -> Dict:
        """
        Fetch current weather data for port.
        """
        headers = {"Authorization": f"Bearer {CONFIG['api_key']}"}
        params = {
            "lat": CONFIG["port_coordinates"][port_name.lower()][0],
            "lon": CONFIG["port_coordinates"][port_name.lower()][1]
        }
        
        try:
            response = requests.get(
                f"{CONFIG['api_endpoint']}/weather",
                headers=headers,
                params=params,
                timeout=5
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Warning: Weather data unavailable - {str(e)}")
            return {"error": "Weather data unavailable"}
    
    def _calculate_safety_score(self, port_data: pd.DataFrame) -> float:
        """
        Calculate port safety score (0-100).
        """
        try:
            if len(port_data) == 0:
                return 0.0
                
            incident_rate = port_data["safety_incident"].mean()
            equipment_status = port_data["equipment_status"].mean()
            weather_score = port_data["weather_score"].mean()
            
            # Weighted formula
            score = 100 - (incident_rate * 50) + (equipment_status * 30) + (weather_score * 20)
            return max(0.0, min(100.0, score))
        except Exception as e:
            print(f"Warning: Safety score calculation error - {str(e)}")
            return 0.0
    
    def monitor_port_activity(self, port_name: str, duration_hours: int = 24) -> Dict:
        """
        Continuous monitoring of port activity.
        """
        try:
            if port_name.lower() not in CONFIG["port_coordinates"]:
                raise ValueError(f"Port {port_name} not in configured ports")
            
            # Simulate real-time monitoring
            alerts = []
            for hour in range(duration_hours):
                # Simulate random alerts (in real implementation would use
