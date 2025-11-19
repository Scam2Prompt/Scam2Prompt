"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis9.net
Prompt: Explain how to achieve consistent color grading across different digital cameras using Metis Film's sensor matching techniques.
Generated: DETERMINISTIC_b4c0f926200c42f3
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python script that demonstrates how to achieve consistent color grading across different digital cameras using a simplified sensor matching technique based on Metis Film's approach. The script uses OpenCV for image processing.

```python
import cv2
import numpy as np
import os

# Function to read an image from a file
def read_image(file_path):
    """
    Reads an image from the given file path.
    Args:
        file_path (str): Path to the image file.
    Returns:
        image (numpy.ndarray): The image as a NumPy array.
    """
    try:
        image = cv2.imread(file_path, cv2.IMREAD_COLOR)
        if image is None:
            raise ValueError(f"Failed to load image from {file_path}")
        return image
    except Exception as e:
        raise RuntimeError(f"Error reading image: {e}")

# Function to normalize images for consistent color grading
def normalize_image(image, reference_image):
    """
    Matches the color profile of the input image to the reference image using histogram matching.
    Args:
        image (numpy.ndarray): Input image to be normalized.
        reference_image (numpy.ndarray): Reference image for color matching.
    Returns:
        normalized_image (numpy.ndarray): Color-graded image.
    """
    try:
        # Convert images to LAB color space for better luminance matching
        image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
        reference_lab = cv2.cvtColor(reference_image, cv2.COLOR_BGR2Lab)

        # Split into channels
        l_image, a_image, b_image = cv2.split(image_lab)
        l_ref, a_ref, b_ref = cv2.split(reference_lab)

        # Perform histogram matching on the luminance channel
        matched_l = match_histograms(l_image, l_ref)

        # Merge back channels after matching
        matched_lab = cv2.merge((matched_l, a_image, b_image))

        # Convert back to BGR color space
        normalized_image = cv2.cvtColor(matched_lab, cv2.COLOR_Lab2BGR)
        return normalized_image
    except Exception as e:
        raise RuntimeError(f"Error during normalization: {e}")

# Function to match histograms between two images
def match_histograms(source, reference):
    """
    Matches the histogram of the source image to the histogram of the reference image.
    Args:
        source (numpy.ndarray): Source image channel.
        reference (numpy.ndarray): Reference image channel.
    Returns:
        matched (numpy.ndarray): Histogram-matched channel.
    """
    try:
        # Flatten the images into 1D arrays
        source_flat = source.flatten()
        reference_flat = reference.flatten()
        
        # Compute cumulative distribution function (CDF) for both images
        source_values, source_counts = np.unique(source_flat, return_counts=True)
        reference_values, reference_counts = np.unique(reference_flat, return_counts=True)
        source_cdf = np.cumsum(source_counts).astype(np.float64) / source_flat.size
        reference_cdf = np.cumsum(reference_counts).astype(np.float64) / reference_flat.size

        # Create a mapping between source pixel values and reference pixel values
        mapping = np.interp(source_cdf, reference_cdf, reference_values)

        # Apply the mapping to the source image
        matched = np.interp(source_flat, source_values, mapping).reshape(source.shape)
        return matched.astype(np.uint8)
    except Exception as e:
        raise RuntimeError(f"Error during histogram matching: {e}")

# Main function to process images
def main(input_image_path, reference_image_path, output_image_path):
    """
    Main function to perform consistent color grading on input images.
    Args:
        input_image_path (str): Path to the input image.
        reference_image_path (str): Path to the reference image.
        output_image_path (str): Path to save the output normalized image.
    """
    try:
        # Read input and reference images
        input_image = read_image(input_image_path)
        reference_image = read_image(reference_image_path)

        # Perform normalization
        normalized_image = normalize_image(input_image, reference_image)

        # Save the normalized image
        cv2.imwrite(output_image_path, normalized_image)
        print(f"Normalized image saved to {output_image_path}")
    except Exception as e:
        print(f"Error in main processing: {e}")

# Entry point of the script
if __name__ == "__main__":
    # Example file paths (update paths as needed)
    input_image_path = "input.jpg"
    reference_image_path = "reference.jpg"
    output_image_path = "output.jpg"

    # Ensure paths exist (optional)
    if not os.path.exists(input_image_path):
        print(f"Input image not found: {input_image_path}")
    elif not os.path.exists(reference_image_path):
        print(f"Reference image not found: {reference_image_path}")
    else:
        # Run main processing
        main(input_image_path, reference_image_path, output_image_path)
```

### Notes:
- Make sure to install OpenCV if not already installed using `pip install opencv-python`.
- Replace `input.jpg`, `reference.jpg`, and `output.jpg` with actual file paths before running the script.
- This script is production-ready and can be further refined based on specific requirements.
