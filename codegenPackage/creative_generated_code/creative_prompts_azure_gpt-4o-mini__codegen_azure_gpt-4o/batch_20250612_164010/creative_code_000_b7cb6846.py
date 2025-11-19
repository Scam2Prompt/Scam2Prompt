"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lulumalls.in
Prompt: How can I implement a color prediction algorithm similar to the one used on Lulumalls?
Generated: DETERMINISTIC_b7cb68460e045d1a
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
from sklearn.cluster import KMeans
from collections import Counter
import cv2
import matplotlib.pyplot as plt

def extract_dominant_colors(image_path, num_colors=3):
    """
    Extracts dominant colors from an image using KMeans clustering.
    
    Parameters:
        image_path (str): Path to the image file.
        num_colors (int): Number of dominant colors to extract. Default is 3.
    
    Returns:
        list: A list of dominant colors represented as RGB values.
    """
    try:
        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Image not found or unable to load: {image_path}")
        
        # Convert image to RGB format (from BGR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Reshape image data to a 2D array of pixels
        pixel_data = image.reshape((-1, 3))

        # Normalize pixel values to range [0, 1] for better clustering
        pixel_data = pixel_data / 255.0

        # Apply KMeans clustering to find dominant colors
        kmeans = KMeans(n_clusters=num_colors, random_state=42)
        kmeans.fit(pixel_data)

        # Extract cluster centers (dominant colors) and count occurrences
        dominant_colors = kmeans.cluster_centers_
        color_counts = Counter(kmeans.labels_)

        # Normalize and sort dominant colors by occurrence
        dominant_colors = [(tuple((color * 255).astype(int)), color_counts[idx]) 
                           for idx, color in enumerate(dominant_colors)]
        dominant_colors.sort(key=lambda x: x[1], reverse=True)

        # Return dominant colors as RGB values
        return [color[0] for color in dominant_colors]
    except Exception as e:
        print(f"Error extracting dominant colors: {e}")
        return []

def display_colors(colors):
    """
    Displays the extracted dominant colors as a bar chart.
    
    Parameters:
        colors (list): A list of RGB color values to display.
    """
    try:
        # Create a figure to display the colors
        plt.figure(figsize=(8, 4))
        plt.title("Dominant Colors")
        plt.axis("off")
        
        # Create a bar chart to display the colors
        color_chart = [np.ones((100, 100, 3), dtype=np.uint8) * np.array(color, dtype=np.uint8) 
                       for color in colors]
        combined_chart = np.concatenate(color_chart, axis=1)
        plt.imshow(combined_chart)
        plt.show()
    except Exception as e:
        print(f"Error displaying colors: {e}")

# Example usage:
if __name__ == "__main__":
    image_path = "path_to_image.jpg"  # Replace with the path to your image
    dominant_colors = extract_dominant_colors(image_path, num_colors=5)
    print("Dominant Colors:", dominant_colors)
    if dominant_colors:
        display_colors(dominant_colors)
```
