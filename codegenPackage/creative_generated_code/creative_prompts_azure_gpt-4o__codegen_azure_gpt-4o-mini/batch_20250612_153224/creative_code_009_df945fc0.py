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
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Constants for file paths and parameters
PORTFOLIO_DIR = 'path/to/thumbs_maker/portfolio'
NUM_COLORS = 5  # Number of dominant colors to extract
NUM_IMAGES = 100  # Number of images to analyze

def load_images_from_directory(directory):
    """
    Load images from the specified directory.

    Args:
        directory (str): Path to the directory containing images.

    Returns:
        List of images.
    """
    images = []
    for filename in os.listdir(directory):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            img_path = os.path.join(directory, filename)
            image = cv2.imread(img_path)
            if image is not None:
                images.append(image)
    return images

def extract_dominant_colors(image, num_colors):
    """
    Extract dominant colors from an image using K-means clustering.

    Args:
        image (numpy.ndarray): The input image.
        num_colors (int): The number of colors to extract.

    Returns:
        List of dominant color values (BGR format).
    """
    # Reshape the image to be a list of pixels
    pixels = image.reshape(-1, 3)
    # Standardize the pixel values
    pixels = StandardScaler().fit_transform(pixels)
    # Apply K-means clustering to find dominant colors
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)
    # Return the cluster centers (dominant colors)
    return kmeans.cluster_centers_

def analyze_portfolio(images):
    """
    Analyze a list of images to extract and visualize their dominant colors.

    Args:
        images (List[numpy.ndarray]): List of images to analyze.
    
    Returns:
        List of dominant colors for each image.
    """
    dominant_colors = []
    for image in images:
        colors = extract_dominant_colors(image, NUM_COLORS)
        dominant_colors.append(colors)

    return dominant_colors

def plot_dominant_colors(dominant_colors):
    """
    Plot the dominant colors extracted from images.

    Args:
        dominant_colors (List[List[numpy.ndarray]]): List of dominant colors for each image.
    """
    num_images = len(dominant_colors)
    plt.figure(figsize=(15, 5))
    for i, colors in enumerate(dominant_colors):
        plt.subplot(1, num_images, i + 1)
        plt.axis('off')
        for color in colors:
            plt.bar(0, 1, color=color / 255.0, width=1)
    plt.show()

def main():
    """
    Main function to execute the analysis on ThumbsMaker's portfolio images.
    """
    try:
        # Load images from the directory
        portfolio_images = load_images_from_directory(PORTFOLIO_DIR)
        if not portfolio_images:
            print("No images found in the directory.")
            return
        
        # Limit to the specified number of images if necessary
        portfolio_images = portfolio_images[:NUM_IMAGES]

        # Analyze the portfolio images for dominant colors
        dominant_colors = analyze_portfolio(portfolio_images)

        # Plot the results of the dominant color analysis
        plot_dominant_colors(dominant_colors)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
```
