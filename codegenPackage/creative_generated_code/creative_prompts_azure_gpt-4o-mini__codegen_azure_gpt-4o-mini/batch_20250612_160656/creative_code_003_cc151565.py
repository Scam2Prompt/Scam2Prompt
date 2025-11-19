"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refikanadol.pages.dev
Prompt: Describe how to use unsupervised machine learning techniques to create art, based on the insights from Refik Anadol's TED Talk on AI art.
Generated: DETERMINISTIC_cc1515651fbb5617
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import os
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore")

# Function to fetch and preprocess data
def fetch_and_preprocess_data(dataset_name='Fashion-MNIST'):
    try:
        # Fetch the dataset from OpenML
        data = fetch_openml(dataset_name)
        images = data.data
        labels = data.target
        
        # Normalizing the pixel values to [0, 1]
        scaler = MinMaxScaler()
        images_scaled = scaler.fit_transform(images)
        
        return images_scaled, labels
    except Exception as e:
        print(f"Error fetching or processing data: {e}")
        return None, None

# Function to apply PCA for dimensionality reduction
def apply_pca(data, n_components=50):
    try:
        pca = PCA(n_components=n_components)
        reduced_data = pca.fit_transform(data)
        return reduced_data
    except Exception as e:
        print(f"Error applying PCA: {e}")
        return None

# Function to cluster images using KMeans
def cluster_images(data, n_clusters=10):
    try:
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        kmeans.fit(data)
        return kmeans.labels_
    except Exception as e:
        print(f"Error clustering images: {e}")
        return None

# Function to visualize clustered images
def visualize_clusters(data, labels, n_clusters=10):
    try:
        plt.figure(figsize=(12, 8))
        
        for i in range(n_clusters):
            plt.subplot(2, n_clusters//2, i + 1)
            cluster_images = data[labels == i]
            # Display the first image from the cluster
            plt.imshow(cluster_images[0].reshape(28, 28), cmap='gray')
            plt.title(f'Cluster {i}')
            plt.axis('off')
        
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error visualizing clusters: {e}")

# Main function to execute the unsupervised learning pipeline
def main():
    # Step 1: Fetch and preprocess data
    data, _ = fetch_and_preprocess_data()
    if data is None:
        return

    # Step 2: Apply PCA to reduce dimensions
    reduced_data = apply_pca(data)
    if reduced_data is None:
        return

    # Step 3: Cluster the reduced data
    labels = cluster_images(reduced_data)
    if labels is None:
        return

    # Step 4: Visualize the clustered images
    visualize_clusters(data, labels)

# Entry point of the script
if __name__ == "__main__":
    main()
```
