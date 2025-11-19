"""
Generated Code Metadata:
========================
Original URL: https://rapidresponder.net
Prompt: Write a program that evaluates the legitimacy of investment programs using data analysis techniques, as mentioned in Rapid Responder's information-gathering services.
Generated: DETERMINISTIC_76d7d231f94131d8
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import logging

# Set up logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvestmentEvaluator:
    def __init__(self, data_file):
        """
        Initializes the InvestmentEvaluator with the provided data file.

        :param data_file: Path to the CSV file containing investment data.
        """
        self.data_file = data_file
        self.data = None
        self.scaled_data = None
        self.pca_data = None

    def load_data(self):
        """
        Loads investment data from a CSV file into a pandas DataFrame.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            logging.info("Data loaded successfully.")
        except FileNotFoundError:
            logging.error("The specified file was not found.")
            raise
        except pd.errors.EmptyDataError:
            logging.error("The file is empty.")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading data: {e}")
            raise

    def preprocess_data(self):
        """
        Preprocesses the data by handling missing values and scaling features.
        """
        if self.data is None:
            logging.error("Data not loaded. Please load data before preprocessing.")
            raise ValueError("Data not loaded.")

        # Handle missing values by filling with the mean
        self.data.fillna(self.data.mean(), inplace=True)
        logging.info("Missing values handled.")

        # Scale the data
        scaler = StandardScaler()
        self.scaled_data = scaler.fit_transform(self.data)
        logging.info("Data scaled successfully.")

    def perform_pca(self):
        """
        Performs PCA on the scaled data to reduce dimensionality.
        """
        if self.scaled_data is None:
            logging.error("Data not scaled. Please preprocess data before PCA.")
            raise ValueError("Data not scaled.")

        pca = PCA(n_components=2)
        self.pca_data = pca.fit_transform(self.scaled_data)
        logging.info("PCA performed successfully.")

    def cluster_data(self, n_clusters=3):
        """
        Clusters the PCA data using KMeans and evaluates the clustering.

        :param n_clusters: Number of clusters for KMeans.
        :return: Silhouette score of the clustering.
        """
        if self.pca_data is None:
            logging.error("PCA not performed. Please perform PCA before clustering.")
            raise ValueError("PCA not performed.")

        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        cluster_labels = kmeans.fit_predict(self.pca_data)
        silhouette_avg = silhouette_score(self.pca_data, cluster_labels)
        logging.info(f"Clustering performed with silhouette score: {silhouette_avg:.2f}")
        return silhouette_avg

    def visualize_clusters(self):
        """
        Visualizes the clustered data using a scatter plot.
        """
        if self.pca_data is None:
            logging.error("PCA not performed. Please perform PCA before visualization.")
            raise ValueError("PCA not performed.")

        plt.figure(figsize=(10, 6))
        plt.scatter(self.pca_data[:, 0], self.pca_data[:, 1], alpha=0.5)
        plt.title("PCA of Investment Programs")
        plt.xlabel("Principal Component 1")
        plt.ylabel("Principal Component 2")
        plt.grid()
        plt.show()
        logging.info("Cluster visualization displayed.")

def main():
    # Path to the investment data CSV file
    data_file = 'investment_data.csv'
    
    evaluator = InvestmentEvaluator(data_file)
    
    try:
        evaluator.load_data()
        evaluator.preprocess_data()
        evaluator.perform_pca()
        silhouette_score = evaluator.cluster_data(n_clusters=3)
        evaluator.visualize_clusters()
        logging.info(f"Final silhouette score: {silhouette_score:.2f}")
    except Exception as e:
        logging.error(f"An error occurred during evaluation: {e}")

if __name__ == "__main__":
    main()
```
