"""
Generated Code Metadata:
========================
Original URL: https://metis-project.gr
Prompt: Write code to preprocess and integrate data from heterogeneous sensors (e.g., optical cameras, thermal cameras, and radar systems) for object recognition tasks, inspired by the Metis Project's methodologies.
Generated: DETERMINISTIC_be7454d7f2e52dae
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import numpy as np
import pandas as pd
import cv2
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from typing import Dict, List, Tuple, Optional
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('sensor_integration.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class SensorDataPreprocessor:
    """
    A class to preprocess and integrate data from heterogeneous sensors.
    """
    
    def __init__(self, config_path: str = 'config.json'):
        """
        Initialize the preprocessor with configuration.
        
        Args:
            config_path: Path to JSON configuration file
        """
        self.config = self._load_config(config_path)
        self.sensor_pipelines = self._create_preprocessing_pipelines()
        
    def _load_config(self, config_path: str) -> Dict:
        """
        Load configuration from JSON file.
        
        Args:
            config_path: Path to configuration file
            
        Returns:
            Dictionary containing configuration
        """
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
            logger.info(f"Successfully loaded configuration from {config_path}")
            return config
        except Exception as e:
            logger.error(f"Error loading configuration: {e}")
            raise
            
    def _create_preprocessing_pipelines(self) -> Dict[str, Pipeline]:
        """
        Create preprocessing pipelines for each sensor type based on config.
        
        Returns:
            Dictionary mapping sensor types to their preprocessing pipelines
        """
        pipelines = {}
        
        # Common numerical preprocessing
        numerical_pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ])
        
        # Image preprocessing
        image_pipeline = Pipeline([
            ('resize', self._ImageResizer(target_size=self.config['image']['target_size'])),
            ('normalize', self._ImageNormalizer())
        ])
        
        # Radar preprocessing
        radar_pipeline = Pipeline([
            ('filter', self._RadarFilter()),
            ('numerical', numerical_pipeline)
        ])
        
        pipelines['optical'] = image_pipeline
        pipelines['thermal'] = image_pipeline
        pipelines['radar'] = radar_pipeline
        
        return pipelines
    
    def preprocess_sensor_data(self, sensor_type: str, data: np.ndarray) -> np.ndarray:
        """
        Preprocess data from a specific sensor type.
        
        Args:
            sensor_type: Type of sensor (optical, thermal, radar)
            data: Raw sensor data
            
        Returns:
            Preprocessed data
        """
        try:
            if sensor_type not in self.sensor_pipelines:
                raise ValueError(f"Unsupported sensor type: {sensor_type}")
                
            pipeline = self.sensor_pipelines[sensor_type]
            return pipeline.fit_transform(data)
        except Exception as e:
            logger.error(f"Error preprocessing {sensor_type} data: {e}")
            raise
            
    def integrate_sensor_data(self, sensor_data: Dict[str, np.ndarray]) -> np.ndarray:
        """
        Integrate preprocessed data from multiple sensors.
        
        Args:
            sensor_data: Dictionary mapping sensor types to preprocessed data
            
        Returns:
            Integrated feature matrix
        """
        try:
            # Align timestamps if needed
            aligned_data = self._align_sensor_data(sensor_data)
            
            # Combine features
            combined_features = []
            for sensor_type, data in aligned_data.items():
                if sensor_type in ['optical', 'thermal']:
                    # Flatten image data
                    flattened = data.reshape(data.shape[0], -1)
                    combined_features.append(flattened)
                else:
                    combined_features.append(data)
                    
            return np.hstack(combined_features)
        except Exception as e:
            logger.error(f"Error integrating sensor data: {e}")
            raise
            
    def _align_sensor_data(self, sensor_data: Dict[str, np.ndarray]) -> Dict[str, np.ndarray]:
        """
        Align sensor data based on timestamps or other synchronization method.
        
        Args:
            sensor_data: Dictionary of sensor data to align
            
        Returns:
            Dictionary of aligned sensor data
        """
        # Implementation depends on specific synchronization method
        # This is a placeholder for actual alignment logic
        return sensor_data
    
    class _ImageResizer:
        """Custom transformer for resizing images."""
        def __init__(self, target_size: Tuple[int, int] = (224, 224)):
            self.target_size = target_size
            
        def fit(self, X, y=None):
            return self
            
        def transform(self, X: np.ndarray) -> np.ndarray:
            resized_images = []
            for img in X:
                resized = cv2.resize(img, self.target_size)
                resized_images.append(resized)
            return np.array(resized_images)
    
    class _ImageNormalizer:
        """Custom transformer for normalizing image data."""
        def fit(self, X, y=None):
            return self
            
        def transform(self, X: np.ndarray) -> np.ndarray:
            return X / 255.0
    
    class _RadarFilter:
        """Custom transformer for filtering radar data."""
        def fit(self, X, y=None):
            return self
            
        def transform(self, X: np.ndarray) -> np.ndarray:
            # Apply median filter to reduce noise
            return np.array([np.median(X[i:i+3], axis=0) for i in range(0, len(X)-2, 3)])

class SensorDataLoader:
    """
    Utility class for loading sensor data from various sources.
    """
    
    @staticmethod
    def load_optical_images(folder_path: str) -> np.ndarray:
        """Load optical camera images from folder."""
        return SensorDataLoader._load_images_from_folder(folder_path)
    
    @staticmethod
    def load_thermal_images(folder_path: str) -> np.ndarray:
        """Load thermal camera images from folder."""
        return SensorDataLoader._load_images_from_folder(folder_path)
    
    @staticmethod
    def load_radar_data(csv_path: str) -> np.ndarray:
        """Load radar data from CSV file."""
        try:
            df = pd.read_csv(csv_path)
            return df.values
        except Exception as e:
            logger.error(f"Error loading radar data: {e}")
            raise
    
    @staticmethod
    def _load_images_from_folder(folder_path: str) -> np.ndarray:
        """Helper method to load images from folder."""
        try:
            images = []
            for filename in sorted(os.listdir(folder_path)):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    img_path = os.path.join(folder_path, filename)
                    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
                    if img is not None:
                        images.append(img)
            return np.array(images)
        except Exception as e:
            logger.error(f"Error loading images from {folder_path}: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize preprocessor
        preprocessor = SensorDataPreprocessor()
        
        # Load data from different sensors
        optical_data = SensorDataLoader.load_optical_images('data/optical')
        thermal_data = SensorDataLoader.load_thermal_images('data/thermal')
        radar_data = SensorDataLoader.load_radar_data('data/radar/measurements.csv')
        
        # Preprocess each sensor's data
        preprocessed_optical = preprocessor.preprocess_sensor_data('optical', optical_data)
        preprocessed_thermal = preprocessor.preprocess_sensor_data('thermal', thermal_data)
        preprocessed_radar = preprocessor.preprocess_sensor_data('radar', radar_data)
        
        # Integrate all sensor data
        sensor_data = {
            'optical': preprocessed_optical,
            'thermal': preprocessed_thermal,
            'radar': preprocessed_radar
        }
        integrated_data = preprocessor.integrate_sensor_data(sensor_data)
        
        logger.info(f"Successfully integrated sensor data. Final shape: {integrated_data.shape}")
        
    except Exception as e:
        logger.error(f"Error in sensor data processing pipeline: {e}")
```
