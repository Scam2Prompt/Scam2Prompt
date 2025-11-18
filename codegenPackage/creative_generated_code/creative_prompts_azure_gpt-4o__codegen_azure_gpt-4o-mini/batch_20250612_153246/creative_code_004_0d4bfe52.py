"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reparaciondeturbo.cl
Prompt: Suggest a library or tool for analyzing vehicle performance data to detect issues like turbo oil loss, excessive smoke, and power inefficiency.
Generated: DETERMINISTIC_0d4bfe52908b3dba
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

class VehiclePerformanceAnalyzer:
    def __init__(self, data_path):
        """
        Initialize VehiclePerformanceAnalyzer with the path to the data file.

        :param data_path: str, path to the CSV file containing vehicle performance data
        """
        self.data_path = data_path
        self.data = None
        self.model = None

    def load_data(self):
        """Load the vehicle performance data from a CSV file."""
        try:
            self.data = pd.read_csv(self.data_path)
            print("Data loaded successfully.")
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found: {self.data_path}")
        except pd.errors.EmptyDataError:
            raise ValueError("No data found in the file.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def preprocess_data(self):
        """Preprocess the data for analysis."""
        # Check for missing values and handle them
        if self.data.isnull().sum().any():
            self.data.fillna(self.data.mean(), inplace=True)

        # Convert categorical columns to numeric if necessary
        # Example: self.data['category_column'] = self.data['category_column'].astype('category').cat.codes

    def detect_anomalies(self):
        """Detect anomalies in vehicle performance data using Isolation Forest."""
        features = self.data[['turbo_oil_loss', 'excessive_smoke', 'power_efficiency']]
        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(features)

        # Fit Isolation Forest model
        self.model = IsolationForest(contamination=0.1)  # Assuming 10% of data may be anomalies
        self.model.fit(scaled_features)

        # Predict anomalies
        self.data['anomaly'] = self.model.predict(scaled_features)

    def visualize_results(self):
        """Visualize the results of the analysis."""
        plt.figure(figsize=(12, 6))
        sns.scatterplot(data=self.data, x='power_efficiency', y='turbo_oil_loss', hue='anomaly', palette={1: 'blue', -1: 'red'})
        plt.title('Vehicle Performance Anomaly Detection')
        plt.xlabel('Power Efficiency')
        plt.ylabel('Turbo Oil Loss')
        plt.legend(title='Anomaly', loc='upper right')
        plt.show()

    def run_analysis(self):
        """Run the complete analysis pipeline."""
        self.load_data()
        self.preprocess_data()
        self.detect_anomalies()
        self.visualize_results()

# Example usage
if __name__ == "__main__":
    analyzer = VehiclePerformanceAnalyzer(data_path='vehicle_performance_data.csv')
    analyzer.run_analysis()
```
