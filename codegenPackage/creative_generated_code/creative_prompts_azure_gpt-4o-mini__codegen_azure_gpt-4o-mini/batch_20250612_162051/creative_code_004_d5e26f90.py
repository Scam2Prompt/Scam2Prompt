"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://farmboydrone.com
Prompt: Write a script that utilizes drone data to optimize field mapping in agriculture.
Generated: DETERMINISTIC_d5e26f9030d61320
Batch ID: 20250612_162051
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
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import logging

# Configure logging for debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FieldMapper:
    def __init__(self, drone_data: pd.DataFrame):
        """
        Initializes the FieldMapper with drone data.
        
        :param drone_data: A DataFrame containing drone data with columns ['latitude', 'longitude', 'crop_health']
        """
        self.drone_data = drone_data

    def preprocess_data(self):
        """
        Preprocesses the drone data by removing NaN values and scaling the features.
        
        :return: Scaled features and original clean data
        """
        try:
            # Drop rows with NaN values
            clean_data = self.drone_data.dropna(subset=['latitude', 'longitude', 'crop_health'])
            logging.info("Cleaned data: Removed NaN values.")

            # Scale the features for clustering
            scaler = StandardScaler()
            scaled_features = scaler.fit_transform(clean_data[['latitude', 'longitude', 'crop_health']])
            logging.info("Data scaling completed.")
            return scaled_features, clean_data
        except Exception as e:
            logging.error(f"Error in preprocessing data: {e}")
            raise

    def cluster_fields(self, scaled_features: np.ndarray, num_clusters: int = 3):
        """
        Clusters the fields based on drone data using KMeans clustering.
        
        :param scaled_features: Scaled feature data
        :param num_clusters: The number of clusters for KMeans
        :return: DataFrame with cluster labels
        """
        try:
            kmeans = KMeans(n_clusters=num_clusters, random_state=42)
            cluster_labels = kmeans.fit_predict(scaled_features)
            logging.info(f"KMeans clustering completed with {num_clusters} clusters.")
            return cluster_labels
        except Exception as e:
            logging.error(f"Error in clustering fields: {e}")
            raise

    def optimize_field_mapping(self, cluster_labels: np.ndarray, clean_data: pd.DataFrame):
        """
        Optimizes the field mapping by adding cluster labels to the original data.
        
        :param cluster_labels: Cluster labels from KMeans
        :param clean_data: The original cleaned DataFrame
        :return: DataFrame with cluster labels added
        """
        try:
            clean_data['cluster'] = cluster_labels
            logging.info("Field mapping optimization completed.")
            return clean_data
        except Exception as e:
            logging.error(f"Error in optimizing field mapping: {e}")
            raise

    def visualize_clusters(self, optimized_data: pd.DataFrame):
        """
        Visualizes the clusters on a scatter plot.
        
        :param optimized_data: DataFrame containing the optimized field mapping
        """
        try:
            plt.figure(figsize=(10, 8))
            scatter = plt.scatter(optimized_data['longitude'], optimized_data['latitude'], 
                                  c=optimized_data['cluster'], cmap='viridis', alpha=0.6)
            plt.title('Field Mapping Clusters')
            plt.xlabel('Longitude')
            plt.ylabel('Latitude')
            plt.colorbar(scatter, label='Cluster')
            plt.grid(True)
            plt.show()
            logging.info("Cluster visualization displayed.")
        except Exception as e:
            logging.error(f"Error in visualizing clusters: {e}")
            raise

def main():
    # Example usage of the FieldMapper class
    try:
        # Load drone data (for example purposes, a sample DataFrame is created)
        # In a real scenario, replace this with loading from a file or database
        data_dict = {
            'latitude': np.random.uniform(35.0, 36.0, 100),
            'longitude': np.random.uniform(-120.0, -119.0, 100),
            'crop_health': np.random.uniform(0, 100, 100)
        }
        drone_data = pd.DataFrame(data_dict)

        # Initialize the FieldMapper with the drone data
        field_mapper = FieldMapper(drone_data)

        # Preprocess data
        scaled_features, clean_data = field_mapper.preprocess_data()

        # Cluster fields
        cluster_labels = field_mapper.cluster_fields(scaled_features, num_clusters=5)

        # Optimize field mapping
        optimized_data = field_mapper.optimize_field_mapping(cluster_labels, clean_data)

        # Visualize clusters
        field_mapper.visualize_clusters(optimized_data)

    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
```
