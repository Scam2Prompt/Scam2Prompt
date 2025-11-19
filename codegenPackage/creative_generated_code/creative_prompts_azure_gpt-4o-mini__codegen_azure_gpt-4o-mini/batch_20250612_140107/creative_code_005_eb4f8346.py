"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://generate-digital.com
Prompt: Suggest a method for assessing the optimal potential of digital inventory to identify new commercial opportunities in sports and entertainment.
Generated: DETERMINISTIC_eb4f8346bff1ff7a
Batch ID: 20250612_140107
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

class DigitalInventoryAssessment:
    def __init__(self, data_file):
        """
        Initializes the DigitalInventoryAssessment class with the provided data file.

        Args:
            data_file (str): The path to the CSV file containing digital inventory data.
        """
        self.data_file = data_file
        self.data = self.load_data()
        self.processed_data = None

    def load_data(self):
        """
        Loads the digital inventory data from a CSV file.

        Returns:
            pd.DataFrame: The loaded data as a pandas DataFrame.
        """
        try:
            data = pd.read_csv(self.data_file)
            return data
        except FileNotFoundError:
            raise FileNotFoundError("The specified data file was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The data file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading the data: {e}")

    def preprocess_data(self):
        """
        Preprocesses the data by handling missing values and standardizing features.
        """
        # Dropping rows with missing values
        self.data.dropna(inplace=True)

        # Selecting relevant features for clustering
        features = self.data[['engagement', 'reach', 'conversion_rate']]
        
        # Standardizing the features
        scaler = StandardScaler()
        self.processed_data = scaler.fit_transform(features)

    def identify_opportunities(self, n_clusters=3):
        """
        Identifies potential commercial opportunities using K-means clustering.

        Args:
            n_clusters (int): The number of clusters to form. Default is 3.

        Returns:
            pd.DataFrame: Data with cluster labels added.
        """
        if self.processed_data is None:
            raise ValueError("Data has not been preprocessed. Call preprocess_data() before this method.")

        # Applying K-means clustering
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        cluster_labels = kmeans.fit_predict(self.processed_data)

        # Adding cluster labels to the original data
        self.data['cluster'] = cluster_labels
        return self.data

    def plot_clusters(self):
        """
        Plots the identified clusters for visual assessment.
        """
        if self.processed_data is None or 'cluster' not in self.data.columns:
            raise ValueError("Clusters have not been identified. Call identify_opportunities() before this method.")

        plt.figure(figsize=(10, 6))
        plt.scatter(self.processed_data[:, 0], self.processed_data[:, 1], c=self.data['cluster'], cmap='viridis')
        plt.title('Clusters of Digital Inventory Opportunities')
        plt.xlabel('Engagement')
        plt.ylabel('Reach')
        plt.colorbar(label='Cluster')
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        assessment = DigitalInventoryAssessment('digital_inventory.csv')
        assessment.preprocess_data()
        opportunities = assessment.identify_opportunities(n_clusters=4)
        print(opportunities)
        assessment.plot_clusters()
    except Exception as e:
        print(f"An error occurred: {e}")
```
