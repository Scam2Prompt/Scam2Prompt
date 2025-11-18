"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://calmartransport.ca
Prompt: Suggest a tool or library to model and streamline supply chain operations, inspired by the logistics services offered by Calmar Transport.
Generated: DETERMINISTIC_30632c25ad252406
Batch ID: 20250612_152405
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
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

class SupplyChainOptimizer:
    """
    A class to model and streamline supply chain operations using KMeans clustering.

    Attributes:
        data (pd.DataFrame): The input data for supply chain operations.
        scaler (StandardScaler): Standard scaler for normalizing data.
        model (KMeans): KMeans clustering model.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the SupplyChainOptimizer with the given data.

        Args:
            data (pd.DataFrame): Data containing supply chain metrics.
        """
        self.data = data
        self.scaler = StandardScaler()
        self.model = None

    def preprocess_data(self) -> pd.DataFrame:
        """
        Preprocess the data by normalizing it.

        Returns:
            pd.DataFrame: The normalized data.
        """
        try:
            normalized_data = self.scaler.fit_transform(self.data)
            return pd.DataFrame(normalized_data, columns=self.data.columns)
        except Exception as e:
            raise ValueError("Error preprocessing data: " + str(e))

    def fit_model(self, n_clusters: int) -> None:
        """
        Fit the KMeans clustering model to the data.

        Args:
            n_clusters (int): The number of clusters to form.
        """
        try:
            normalized_data = self.preprocess_data()
            self.model = KMeans(n_clusters=n_clusters, random_state=42)
            self.model.fit(normalized_data)
        except Exception as e:
            raise RuntimeError("Error fitting the model: " + str(e))

    def predict_clusters(self) -> np.ndarray:
        """
        Predict the clusters for the data.

        Returns:
            np.ndarray: Cluster labels for each data point.

        Raises:
            RuntimeError: If the model has not been fitted yet.
        """
        if self.model is None:
            raise RuntimeError("Model has not been fitted yet. Please run fit_model() first.")
        
        try:
            normalized_data = self.preprocess_data()
            return self.model.predict(normalized_data)
        except Exception as e:
            raise RuntimeError("Error predicting clusters: " + str(e))

    def visualize_clusters(self) -> None:
        """
        Visualize the clusters using a scatter plot.

        Raises:
            RuntimeError: If the model has not been fitted yet.
        """
        if self.model is None:
            raise RuntimeError("Model has not been fitted yet. Please run fit_model() first.")

        try:
            normalized_data = self.preprocess_data()
            plt.scatter(normalized_data.iloc[:, 0], normalized_data.iloc[:, 1], c=self.model.labels_, cmap='viridis')
            plt.title('Supply Chain Clusters')
            plt.xlabel('Feature 1')
            plt.ylabel('Feature 2')
            plt.colorbar(label='Cluster Label')
            plt.show()
        except Exception as e:
            raise RuntimeError("Error visualizing clusters: " + str(e))

# Example usage
if __name__ == "__main__":
    # Sample DataFrame representing supply chain metrics
    data = pd.DataFrame({
        'Demand': [100, 150, 200, 250, 300],
        'Supply': [80, 120, 190, 240, 290],
        'LeadTime': [2, 3, 1, 4, 2]
    })

    try:
        optimizer = SupplyChainOptimizer(data)
        optimizer.fit_model(n_clusters=2)
        clusters = optimizer.predict_clusters()
        print("Cluster labels:", clusters)
        optimizer.visualize_clusters()
    except Exception as e:
        print("An error occurred:", e)
```
