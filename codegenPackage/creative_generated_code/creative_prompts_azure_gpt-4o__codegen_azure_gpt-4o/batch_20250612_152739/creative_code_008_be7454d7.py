"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis-project.gr
Prompt: Write code to preprocess and integrate data from heterogeneous sensors (e.g., optical cameras, thermal cameras, and radar systems) for object recognition tasks, inspired by the Metis Project's methodologies.
Generated: DETERMINISTIC_be7454d7f2e52dae
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import cv2
import json
import logging
from typing import Dict, Any

# Configure logging for debugging and error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SensorDataPreprocessor:
    """
    A class to preprocess and integrate data from heterogeneous sensors
    (optical cameras, thermal cameras, and radar systems) for object recognition tasks.
    """

    def __init__(self):
        self.scaler = StandardScaler()

    def preprocess_optical_data(self, image_path: str) -> np.ndarray:
        """
        Preprocess data from optical cameras.

        :param image_path: Path to the optical camera image file.
        :return: Preprocessed image as a numpy array.
        """
        try:
            # Read image
            image = cv2.imread(image_path)
            if image is None:
                raise ValueError(f"Optical image not found at path: {image_path}")
            
            # Convert image to grayscale
            grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Normalize pixel values to range [0, 1]
            normalized_image = grayscale_image / 255.0
            
            logging.info("Optical data preprocessing completed.")
            return normalized_image
        except Exception as e:
            logging.error(f"Error processing optical data: {e}")
            raise

    def preprocess_thermal_data(self, thermal_data_path: str) -> np.ndarray:
        """
        Preprocess data from thermal cameras.

        :param thermal_data_path: Path to the thermal camera data file (JSON format).
        :return: Preprocessed thermal data as a numpy array.
        """
        try:
            # Load thermal data from JSON file
            with open(thermal_data_path, "r") as file:
                thermal_data = json.load(file)
            
            # Convert temperature readings to a numpy array
            thermal_array = np.array(thermal_data["temperature_readings"])
            
            # Normalize temperature readings using z-score normalization
            thermal_array = self.scaler.fit_transform(thermal_array.reshape(-1, 1)).flatten()
            
            logging.info("Thermal data preprocessing completed.")
            return thermal_array
        except Exception as e:
            logging.error(f"Error processing thermal data: {e}")
            raise

    def preprocess_radar_data(self, radar_data_path: str) -> pd.DataFrame:
        """
        Preprocess data from radar systems.

        :param radar_data_path: Path to the radar data file (CSV format).
        :return: Preprocessed radar data as a Pandas DataFrame.
        """
        try:
            # Load radar data from CSV file
            radar_data = pd.read_csv(radar_data_path)
            
            # Fill missing values with the column mean
            radar_data.fillna(radar_data.mean(), inplace=True)
            
            # Normalize radar data using z-score normalization
            radar_data_normalized = pd.DataFrame(self.scaler.fit_transform(radar_data), columns=radar_data.columns)
            
            logging.info("Radar data preprocessing completed.")
            return radar_data_normalized
        except Exception as e:
            logging.error(f"Error processing radar data: {e}")
            raise

    def integrate_sensor_data(self, optical_data: np.ndarray, thermal_data: np.ndarray, radar_data: pd.DataFrame) -> pd.DataFrame:
        """
        Integrate preprocessed data from all sensors into a unified format.

        :param optical_data: Preprocessed optical camera data (numpy array).
        :param thermal_data: Preprocessed thermal camera data (numpy array).
        :param radar_data: Preprocessed radar system data (Pandas DataFrame).
        :return: Integrated sensor data as a Pandas DataFrame.
        """
        try:
            # Combine all data into a Pandas DataFrame
            integrated_data = pd.DataFrame({
                "Optical": optical_data.flatten(),
                "Thermal": thermal_data.flatten(),
            })
            
            # Append radar data columns
            for col in radar_data.columns:
                integrated_data[col] = radar_data[col]
            
            logging.info("Sensor data integration completed.")
            return integrated_data
        except Exception as e:
            logging.error(f"Error integrating sensor data: {e}")
            raise

# Example usage (paths should be updated to actual file locations)
if __name__ == "__main__":
    try:
        preprocessor = SensorDataPreprocessor()

        optical_data = preprocessor.preprocess_optical_data("path_to_optical_image.jpg")
        thermal_data = preprocessor.preprocess_thermal_data("path_to_thermal_data.json")
        radar_data = preprocessor.preprocess_radar_data("path_to_radar_data.csv")

        integrated_data = preprocessor.integrate_sensor_data(optical_data, thermal_data, radar_data)
        print("Integrated Sensor Data:")
        print(integrated_data.head())
    except Exception as e:
        logging.error(f"Error in sensor data processing workflow: {e}")
```
