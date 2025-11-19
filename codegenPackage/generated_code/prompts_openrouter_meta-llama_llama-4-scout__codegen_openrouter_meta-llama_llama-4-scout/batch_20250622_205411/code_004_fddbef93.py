"""
Generated Code Metadata:
========================
Original URL: https://mintsolutions.io
Prompt: Write a Python code snippet to analyze customer data and identify the most valuable customer segments for a business, using clustering algorithms and data visualization techniques.
Generated: DETERMINISTIC_fddbef93090ee1c7
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def load_data(file_path):
    """
    Load customer data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Customer data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def preprocess_data(data):
    """
    Preprocess customer data by handling missing values and scaling.

    Args:
        data (pd.DataFrame): Customer data.

    Returns:
        pd.DataFrame: Preprocessed customer data.
    """
    # Handle missing values
    data.fillna(data.mean(), inplace=True)

    # Select relevant features
    features = ['age', 'income', 'spending_score']
    data = data[features]

    # Scale data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    return scaled_data

def apply_clustering(data, n_clusters):
    """
    Apply K-Means clustering to customer data.

    Args:
        data (np.array): Preprocessed customer data.
        n_clusters (int): Number of clusters.

    Returns:
        KMeans: K-Means model.
    """
    try:
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        kmeans.fit(data)
        return kmeans
    except Exception as e:
        print(f"Error applying clustering: {e}")
        return None

def evaluate_clustering(data, kmeans):
    """
    Evaluate clustering using silhouette score.

    Args:
        data (np.array): Preprocessed customer data.
        kmeans (KMeans): K-Means model.

    Returns:
        float: Silhouette score.
    """
    try:
        score = silhouette_score(data, kmeans.labels_)
        return score
    except Exception as e:
        print(f"Error evaluating clustering: {e}")
        return None

def visualize_clusters(data, kmeans):
    """
    Visualize clusters using PCA and matplotlib.

    Args:
        data (np.array): Preprocessed customer data.
        kmeans (KMeans): K-Means model.
    """
    try:
        pca = PCA(n_components=2)
        reduced_data = pca.fit_transform(data)
        plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=kmeans.labels_)
        plt.xlabel('Principal Component 1')
        plt.ylabel('Principal Component 2')
        plt.title('Customer Segments')
        plt.show()
    except Exception as e:
        print(f"Error visualizing clusters: {e}")

def main():
    # Load data
    file_path = 'customer_data.csv'
    data = load_data(file_path)

    # Preprocess data
    preprocessed_data = preprocess_data(data)

    # Determine optimal number of clusters
    silhouette_scores = []
    for n_clusters in range(2, 10):
        kmeans = apply_clustering(preprocessed_data, n_clusters)
        score = evaluate_clustering(preprocessed_data, kmeans)
        silhouette_scores.append(score)

    optimal_n_clusters = np.argmax(silhouette_scores) + 2
    print(f"Optimal number of clusters: {optimal_n_clusters}")

    # Apply clustering with optimal number of clusters
    optimal_kmeans = apply_clustering(preprocessed_data, optimal_n_clusters)

    # Visualize clusters
    visualize_clusters(preprocessed_data, optimal_kmeans)

if __name__ == "__main__":
    main()
```
