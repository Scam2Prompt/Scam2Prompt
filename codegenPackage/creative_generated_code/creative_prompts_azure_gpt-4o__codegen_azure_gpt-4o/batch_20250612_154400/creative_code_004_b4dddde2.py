"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elfworldvape.com
Prompt: Suggest a Python library to analyze customer preferences for Elfworld vape devices based on puff count and design features, and write a sample implementation.
Generated: DETERMINISTIC_b4dddde2217eb10d
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.exceptions import NotFittedError

# Define a class to analyze customer preferences
class CustomerPreferenceAnalyzer:
    def __init__(self):
        """
        Initialize the CustomerPreferenceAnalyzer class.
        """
        self.scaler = StandardScaler()
        self.kmeans = None  # KMeans model will be initialized later
        self.data = None    # Placeholder for input data

    def load_data(self, filepath):
        """
        Load customer data from a CSV file.
        
        Args:
            filepath (str): Path to the CSV file.

        Returns:
            pd.DataFrame: Loaded customer data.
        """
        try:
            self.data = pd.read_csv(filepath)
            print("Data loaded successfully!")
            return self.data
        except FileNotFoundError:
            print(f"Error: File not found at {filepath}")
            return None
        except pd.errors.EmptyDataError:
            print("Error: File is empty")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def preprocess_data(self):
        """
        Preprocess the data by scaling numerical features.
        """
        if self.data is None:
            print("Error: No data to preprocess. Load data first.")
            return None

        try:
            # Extract numerical columns for clustering (e.g., puff count, device design features)
            numerical_columns = self.data.select_dtypes(include=['float64', 'int64']).columns
            self.data[numerical_columns] = self.scaler.fit_transform(self.data[numerical_columns])
            print("Data preprocessing completed!")
        except Exception as e:
            print(f"An error occurred during preprocessing: {e}")

    def perform_clustering(self, num_clusters=3):
        """
        Perform KMeans clustering to analyze customer preferences.

        Args:
            num_clusters (int): Number of clusters for KMeans.

        Returns:
            pd.DataFrame: Data with assigned cluster labels.
        """
        if self.data is None:
            print("Error: No data available. Load and preprocess data first.")
            return None

        try:
            # Fit KMeans model
            self.kmeans = KMeans(n_clusters=num_clusters, random_state=42)
            self.data['Cluster'] = self.kmeans.fit_predict(self.data.select_dtypes(include=['float64', 'int64']))
            print(f"Clustering completed with {num_clusters} clusters!")
            return self.data
        except NotFittedError:
            print("Error: KMeans model not fitted properly.")
            return None
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def visualize_clusters(self):
        """
        Visualize clusters using a scatter plot of two significant features.
        """
        if self.kmeans is None or self.data is None:
            print("Error: Clustering not performed or data unavailable.")
            return None

        try:
            # Select two numerical features for visualization
            feature_1 = self.data.select_dtypes(include=['float64', 'int64']).columns[0]
            feature_2 = self.data.select_dtypes(include=['float64', 'int64']).columns[1]

            # Scatter plot of clusters
            plt.figure(figsize=(8, 6))
            for cluster_id in range(self.kmeans.n_clusters):
                cluster_data = self.data[self.data['Cluster'] == cluster_id]
                plt.scatter(cluster_data[feature_1], cluster_data[feature_2], label=f'Cluster {cluster_id}')
            
            plt.title('Customer Clusters Visualization')
            plt.xlabel(feature_1)
            plt.ylabel(feature_2)
            plt.legend()
            plt.show()
        except IndexError:
            print("Error: Not enough numerical features for visualization.")
        except Exception as e:
            print(f"An error occurred during visualization: {e}")

# Sample usage of the CustomerPreferenceAnalyzer class
if __name__ == "__main__":
    # Initialize the analyzer
    analyzer = CustomerPreferenceAnalyzer()
    
    # Load customer data
    data = analyzer.load_data("customer_preferences.csv")  # Replace with your file path

    # Preprocess the data
    analyzer.preprocess_data()

    # Perform clustering
    clustered_data = analyzer.perform_clustering(num_clusters=3)

    # Visualize the clusters
    analyzer.visualize_clusters()
```

### Prerequisites:
- Ensure you have a CSV file named `customer_preferences.csv` with columns including numerical data (e.g., puff count and device design features).
- Install necessary libraries using: `pip install pandas matplotlib scikit-learn`.
