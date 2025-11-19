"""
Generated Code Metadata:
========================
Original URL: https://refikanadol.pages.dev
Prompt: Create a digital art piece using unsupervised machine learning, inspired by Refik Anadol's MoMA project, and describe the process in detail.
Generated: DETERMINISTIC_6e880adc9e1781a9
Batch ID: 20250622_205623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_sample_image
from PIL import Image

def load_and_preprocess_image(image_path):
    """
    Load and preprocess an image for clustering.
    
    Args:
        image_path (str): Path to the image file.
        
    Returns:
        numpy.ndarray: Flattened and scaled image array.
    """
    try:
        # Load image
        img = Image.open(image_path)
        img_array = np.array(img)
        
        # Normalize pixel values to [0, 1]
        img_array = img_array / 255.0
        
        # Flatten the image to 2D array (pixels x RGB)
        h, w, d = img_array.shape
        img_flat = img_array.reshape(h * w, d)
        
        return img_flat
    except Exception as e:
        print(f"Error loading/preprocessing image: {e}")
        return None

def apply_kmeans(data, n_clusters=8):
    """
    Apply K-means clustering to the image data.
    
    Args:
        data (numpy.ndarray): Input data for clustering.
        n_clusters (int): Number of clusters to form.
        
    Returns:
        sklearn.cluster.KMeans: Fitted KMeans model.
    """
    try:
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        kmeans.fit(data)
        return kmeans
    except Exception as e:
        print(f"Error applying K-means: {e}")
        return None

def reduce_dimensions(data, n_components=2):
    """
    Reduce dimensions using PCA for visualization.
    
    Args:
        data (numpy.ndarray): Input data.
        n_components (int): Number of components to keep.
        
    Returns:
        numpy.ndarray: Transformed data.
    """
    try:
        pca = PCA(n_components=n_components)
        reduced_data = pca.fit_transform(data)
        return reduced_data
    except Exception as e:
        print(f"Error reducing dimensions: {e}")
        return None

def generate_art_piece(original_img, kmeans_model, output_path):
    """
    Generate and save the digital art piece.
    
    Args:
        original_img (numpy.ndarray): Original image array.
        kmeans_model (sklearn.cluster.KMeans): Trained KMeans model.
        output_path (str): Path to save the output image.
    """
    try:
        # Get cluster centers and labels
        cluster_centers = kmeans_model.cluster_centers_
        labels = kmeans_model.labels_
        
        # Reconstruct image using cluster centers
        h, w, d = original_img.shape
        reconstructed = np.zeros((h, w, d))
        label_idx = 0
        
        for i in range(h):
            for j in range(w):
                reconstructed[i][j] = cluster_centers[labels[label_idx]]
                label_idx += 1
        
        # Save the art piece
        plt.figure(figsize=(10, 10))
        plt.imshow(reconstructed)
        plt.axis('off')
        plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
        plt.close()
    except Exception as e:
        print(f"Error generating art piece: {e}")

def visualize_clusters(reduced_data, labels, output_path):
    """
    Visualize the clusters in 2D space.
    
    Args:
        reduced_data (numpy.ndarray): PCA-reduced data.
        labels (numpy.ndarray): Cluster labels.
        output_path (str): Path to save the visualization.
    """
    try:
        plt.figure(figsize=(10, 8))
        plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=labels, cmap='viridis', s=5)
        plt.colorbar()
        plt.title('Cluster Visualization in 2D Space')
        plt.savefig(output_path)
        plt.close()
    except Exception as e:
        print(f"Error visualizing clusters: {e}")

def main():
    # Configuration
    input_image_path = "sample_image.jpg"
    cluster_viz_path = "cluster_visualization.png"
    art_piece_path = "digital_art_piece.png"
    n_clusters = 10
    
    # Load and preprocess image
    img_flat = load_and_preprocess_image(input_image_path)
    if img_flat is None:
        return
    
    # Apply K-means clustering
    kmeans = apply_kmeans(img_flat, n_clusters=n_clusters)
    if kmeans is None:
        return
    
    # Reduce dimensions for visualization
    reduced_data = reduce_dimensions(img_flat)
    if reduced_data is None:
        return
    
    # Visualize clusters
    visualize_clusters(reduced_data, kmeans.labels_, cluster_viz_path)
    
    # Generate and save art piece
    original_img = np.array(Image.open(input_image_path)) / 255.0
    generate_art_piece(original_img, kmeans, art_piece_path)

if __name__ == "__main__":
    main()
```
