"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thumbsmaker.com
Prompt: Write code to extract and analyze ThumbsMaker’s portfolio images to identify common design patterns and features that boost engagement.
Generated: DETERMINISTIC_df945fc0ac6c6e03
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image
import numpy as np
from collections import Counter
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Constants
PORTFOLIO_PATH = "path/to/ThumbsMaker/portfolio/images"
IMAGE_SIZE = (128, 128)  # Resize all images to this size for analysis
NUM_CLUSTERS = 5         # Number of clusters for design pattern analysis

def load_images(directory):
    """
    Loads images from the given directory and preprocesses them.
    :param directory: Path to portfolio images directory.
    :return: List of preprocessed image data and filenames.
    """
    image_data = []
    filenames = []
    for file in os.listdir(directory):
        try:
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
                img_path = os.path.join(directory, file)
                img = Image.open(img_path).convert("RGB").resize(IMAGE_SIZE)
                image_data.append(np.array(img).flatten())  # Flatten image data
                filenames.append(file)
        except Exception as e:
            print(f"Error loading image {file}: {e}")
    return np.array(image_data), filenames

def analyze_design_patterns(image_data):
    """
    Perform clustering analysis on image data to identify common design patterns.
    :param image_data: Array of flattened image data.
    :return: Cluster labels and a KMeans model instance.
    """
    try:
        kmeans = KMeans(n_clusters=NUM_CLUSTERS, random_state=42)
        labels = kmeans.fit_predict(image_data)
        return labels, kmeans
    except Exception as e:
        print(f"Error during clustering analysis: {e}")
        return None, None

def visualize_clusters(image_data, labels, filenames, num_samples=5):
    """
    Visualize random samples from each cluster.
    :param image_data: Array of flattened image data.
    :param labels: Cluster labels for each image.
    :param filenames: Original image filenames.
    :param num_samples: Number of samples to display per cluster.
    """
    try:
        cluster_map = {i: [] for i in range(NUM_CLUSTERS)}
        for idx, label in enumerate(labels):
            cluster_map[label].append((image_data[idx], filenames[idx]))

        for cluster, items in cluster_map.items():
            print(f"\nCluster {cluster}:")
            samples = items[:num_samples]
            for sample, filename in samples:
                img = Image.fromarray(sample.reshape(IMAGE_SIZE[0], IMAGE_SIZE[1], 3))
                plt.imshow(img)
                plt.title(f"Cluster {cluster} - {filename}")
                plt.axis("off")
                plt.show()
    except Exception as e:
        print(f"Error during visualization: {e}")

def main():
    """
    Main function to execute the portfolio analysis workflow.
    """
    try:
        # Load and preprocess images
        image_data, filenames = load_images(PORTFOLIO_PATH)
        if len(image_data) == 0:
            print("No valid images found. Exiting.")
            return

        # Perform clustering analysis
        labels, kmeans_model = analyze_design_patterns(image_data)
        if labels is None or kmeans_model is None:
            print("Clustering analysis failed. Exiting.")
            return

        # Display cluster centers
        print("\nCluster Centers:")
        print(kmeans_model.cluster_centers_)

        # Visualize clusters
        visualize_clusters(image_data, labels, filenames)

    except Exception as e:
        print(f"Unhandled error: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
