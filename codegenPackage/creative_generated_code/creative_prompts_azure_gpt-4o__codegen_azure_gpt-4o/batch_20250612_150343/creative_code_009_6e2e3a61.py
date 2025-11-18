"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starkware.in
Prompt: Create a data analytics pipeline in Python to elevate customer experience and develop new products, inspired by Starkware's IT services.
Generated: DETERMINISTIC_6e2e3a61e897a3d8
Batch ID: 20250612_150343
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
import logging
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

class DataAnalyticsPipeline:
    """
    Data Analytics Pipeline to process customer data,
    derive insights, and propose actionable outcomes to 
    elevate customer experience and develop new products.
    """

    def __init__(self, input_data_path: str):
        """
        Initialize the pipeline with the input data path.
        """
        self.input_data_path = input_data_path
        self.data = None
        self.processed_data = None
        self.cluster_model = None

    def load_data(self):
        """
        Load data from a CSV file.
        """
        try:
            logging.info("Loading data from file: %s", self.input_data_path)
            self.data = pd.read_csv(self.input_data_path)
            logging.info("Data loaded successfully.")
        except Exception as e:
            logging.error("Failed to load data: %s", str(e))
            raise

    def preprocess_data(self):
        """
        Preprocess the data: handle missing values, normalize numerical columns,
        and prepare the data for analysis.
        """
        try:
            logging.info("Starting data preprocessing...")
            
            # Drop rows with missing values
            self.data.dropna(inplace=True)
            
            # Select only numerical columns for clustering
            numerical_columns = self.data.select_dtypes(include=np.number).columns
            
            # Normalize numerical data
            scaler = StandardScaler()
            self.processed_data = scaler.fit_transform(self.data[numerical_columns])

            logging.info("Data preprocessing completed.")
        except Exception as e:
            logging.error("Data preprocessing failed: %s", str(e))
            raise

    def perform_clustering(self, num_clusters: int = 3):
        """
        Perform K-Means clustering on the processed data.
        :param num_clusters: Number of clusters to create.
        """
        try:
            logging.info("Starting K-Means clustering with %d clusters...", num_clusters)
            self.cluster_model = KMeans(n_clusters=num_clusters, random_state=42)
            cluster_labels = self.cluster_model.fit_predict(self.processed_data)
            self.data['Cluster'] = cluster_labels
            silhouette_avg = silhouette_score(self.processed_data, cluster_labels)
            logging.info("Clustering completed. Silhouette Score: %.2f", silhouette_avg)
        except Exception as e:
            logging.error("Clustering failed: %s", str(e))
            raise

    def visualize_clusters(self):
        """
        Visualize the clustering results for the first two features (for simplicity).
        """
        try:
            if self.cluster_model is None:
                raise ValueError("Clustering model has not been initialized.")
            
            logging.info("Visualizing cluster results...")

            plt.figure(figsize=(10, 6))
            plt.scatter(
                self.processed_data[:, 0], 
                self.processed_data[:, 1], 
                c=self.data['Cluster'], 
                cmap='viridis', 
                s=50
            )
            plt.title('Cluster Visualization')
            plt.xlabel('Feature 1')
            plt.ylabel('Feature 2')
            plt.colorbar(label='Cluster')
            plt.show()

            logging.info("Cluster visualization completed.")
        except Exception as e:
            logging.error("Cluster visualization failed: %s", str(e))
            raise

    def save_results(self, output_path: str):
        """
        Save the clustered data to a CSV file.
        :param output_path: File path to save the results.
        """
        try:
            logging.info("Saving clustered data to file: %s", output_path)
            self.data.to_csv(output_path, index=False)
            logging.info("Clustered data saved successfully.")
        except Exception as e:
            logging.error("Failed to save results: %s", str(e))
            raise

# Main pipeline execution
if __name__ == "__main__":
    # File paths
    input_file = "customer_data.csv"  # Replace with your input file path
    output_file = "clustered_data.csv"  # Replace with your output file path

    # Initialize and execute the pipeline
    pipeline = DataAnalyticsPipeline(input_file)
    
    try:
        pipeline.load_data()
        pipeline.preprocess_data()
        pipeline.perform_clustering(num_clusters=4)  # Choose appropriate number of clusters
        pipeline.visualize_clusters()
        pipeline.save_results(output_file)
    except Exception as ex:
        logging.error("Pipeline execution failed: %s", str(ex))
```
