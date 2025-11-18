"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pdma.io
Prompt: Write code to analyze cybersecurity threats using methods taught in PDMA's Cybersecurity program, including anomaly detection and threat modeling.
Generated: DETERMINISTIC_7ed013a263aed0e9
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import List, Dict, Any
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Data structure for cybersecurity threats
class CyberThreat:
    def __init__(self, threat_id: str, features: Dict[str, Any], metadata: Dict[str, Any]):
        self.threat_id = threat_id
        self.features = features
        self.metadata = metadata

# Function to preprocess data for anomaly detection
def preprocess_data(threats: List[CyberThreat]) -> np.ndarray:
    """
    Preprocesses data from a list of CyberThreat objects into a numerical NumPy array.
    This is required for anomaly detection algorithms like Isolation Forest.
    """
    try:
        logging.info("Preprocessing data for anomaly detection.")
        # Extract feature values and convert them into a 2D array
        feature_list = [list(threat.features.values()) for threat in threats]
        return np.array(feature_list)
    except Exception as e:
        logging.error(f"Error during data preprocessing: {str(e)}")
        raise

# Function to perform anomaly detection
def perform_anomaly_detection(data: np.ndarray, contamination: float = 0.1) -> List[str]:
    """
    Detect anomalies using Isolation Forest.
    :param data: Preprocessed numerical data (2D array)
    :param contamination: Expected percentage of anomalies in the data
    :return: List of anomaly labels
    """
    try:
        logging.info("Performing anomaly detection using Isolation Forest.")
        scaler = StandardScaler()
        data_normalized = scaler.fit_transform(data)

        iso_forest = IsolationForest(contamination=contamination, random_state=42)
        predictions = iso_forest.fit_predict(data_normalized)

        # Label anomalies as "anomaly" and normal data as "normal"
        return ["anomaly" if pred == -1 else "normal" for pred in predictions]
    except Exception as e:
        logging.error(f"Error during anomaly detection: {str(e)}")
        raise

# Function to model threats based on metadata and anomaly results
def generate_threat_model(threats: List[CyberThreat], anomalies: List[str]) -> List[Dict[str, Any]]:
    """
    Generate a threat model combining metadata and anomaly detection results.
    :param threats: List of CyberThreat objects
    :param anomalies: List of anomaly labels ("normal" or "anomaly")
    :return: List of modeled threats as dictionaries
    """
    try:
        logging.info("Generating threat model.")
        threat_model = []
        for threat, anomaly_label in zip(threats, anomalies):
            modeled_threat = {
                "threat_id": threat.threat_id,
                "anomaly_status": anomaly_label,
                "metadata": threat.metadata
            }
            threat_model.append(modeled_threat)
        return threat_model
    except Exception as e:
        logging.error(f"Error during threat modeling: {str(e)}")
        raise

# Main analysis function
def analyze_cybersecurity_threats(threats_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Main function to analyze cybersecurity threats.
    :param threats_data: Raw input data for threats, including features and metadata
    :return: Final threat model as a list of dictionaries
    """
    try:
        logging.info("Starting cybersecurity threat analysis.")

        # Create CyberThreat objects from raw input data
        threats = [CyberThreat(data["threat_id"], data["features"], data["metadata"]) for data in threats_data]

        # Preprocess data for anomaly detection
        data = preprocess_data(threats)

        # Perform anomaly detection
        anomalies = perform_anomaly_detection(data)

        # Generate threat models
        threat_model = generate_threat_model(threats, anomalies)

        logging.info("Cybersecurity threat analysis completed successfully.")
        return threat_model
    except Exception as e:
        logging.error(f"Error during cybersecurity threat analysis: {str(e)}")
        raise

# Example usage
if __name__ == "__main__":
    # Sample input data
    sample_threats_data = [
        {
            "threat_id": "T001",
            "features": {"feature1": 0.1, "feature2": 1.2, "feature3": 0.3},
            "metadata": {"source": "sensor1", "timestamp": "2023-10-01T12:00:00Z"}
        },
        {
            "threat_id": "T002",
            "features": {"feature1": 2.1, "feature2": 0.4, "feature3": 3.8},
            "metadata": {"source": "sensor2", "timestamp": "2023-10-01T12:05:00Z"}
        },
        {
            "threat_id": "T003",
            "features": {"feature1": -0.5, "feature2": -1.2, "feature3": 0.0},
            "metadata": {"source": "sensor3", "timestamp": "2023-10-01T12:10:00Z"}
        }
    ]

    # Analyze threats
    threat_analysis_results = analyze_cybersecurity_threats(sample_threats_data)

    # Pretty-print the results
    print(json.dumps(threat_analysis_results, indent=4))
```
