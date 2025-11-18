"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itab.com
Prompt: Generate code to analyze consumer buying behavior in a grocery store setting, referencing ITAB's sector experience and focus on increasing conversions and sales.
Generated: DETERMINISTIC_e9c53aa1864f281c
Batch ID: 20250612_154621
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
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Set the style for seaborn
sns.set(style="whitegrid")

class GroceryStoreAnalysis:
    """
    A class to analyze consumer buying behavior in a grocery store.
    This class focuses on data loading, preprocessing, clustering, 
    and visualizing customer segments to improve conversions and sales.
    """

    def __init__(self, data_path):
        """
        Initializes the GroceryStoreAnalysis with the given data path.
        
        Args:
            data_path (str): Path to the CSV data file containing purchase data.
        """
        self.data_path = data_path
        self.data = None
        self.scaled_data = None
        self.kmeans_model = None
        self.silhouette_avg = None

    def load_data(self):
        """Load data from the CSV file."""
        try:
            self.data = pd.read_csv(self.data_path)
            print(f"Data loaded successfully from {self.data_path}.")
        except FileNotFoundError:
            print(f"Error: The file {self.data_path} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            raise

    def preprocess_data(self):
        """Preprocess the data for analysis."""
        # Example preprocessing steps: Handling missing values and scaling
        try:
            # Drop rows with missing values
            self.data.dropna(inplace=True)
            
            # Select relevant features for clustering (example features)
            features = self.data[['Age', 'Annual_Income', 'Spending_Score']]
            self.scaled_data = StandardScaler().fit_transform(features)

            print("Data preprocessing completed successfully.")
        except KeyError as e:
            print(f"Error: Missing expected column in data: {e}")
            raise
        except Exception as e:
            print(f"An error occurred during preprocessing: {e}")
            raise

    def cluster_data(self, n_clusters=3):
        """
        Cluster the data using KMeans.

        Args:
            n_clusters (int): The number of clusters to form.
        """
        try:
            self.kmeans_model = KMeans(n_clusters=n_clusters, random_state=0)
            self.kmeans_model.fit(self.scaled_data)
            self.data['Cluster'] = self.kmeans_model.labels_

            # Calculate silhouette score
            self.silhouette_avg = silhouette_score(self.scaled_data, self.kmeans_model.labels_)
            print(f"KMeans clustering completed with silhouette score: {self.silhouette_avg:.2f}.")
        except Exception as e:
            print(f"An error occurred during clustering: {e}")
            raise

    def visualize_clusters(self):
        """Visualize the clustered data."""
        try:
            plt.figure(figsize=(10, 6))
            sns.scatterplot(x=self.data['Annual_Income'], y=self.data['Spending_Score'],
                            hue=self.data['Cluster'], palette='viridis', s=100)
            plt.title('Customer Segments Based on Income and Spending Score')
            plt.xlabel('Annual Income')
            plt.ylabel('Spending Score')
            plt.legend(title='Cluster')
            plt.grid()
            plt.show()
        except Exception as e:
            print(f"An error occurred during visualization: {e}")
            raise

if __name__ == "__main__":
    # Define the path to the data file
    data_file_path = 'grocery_store_data.csv'

    # Create an instance of the analysis class
    grocery_analysis = GroceryStoreAnalysis(data_file_path)

    # Load, preprocess, cluster, and visualize the data
    grocery_analysis.load_data()
    grocery_analysis.preprocess_data()
    grocery_analysis.cluster_data(n_clusters=4)  # Example with 4 clusters
    grocery_analysis.visualize_clusters()
```
