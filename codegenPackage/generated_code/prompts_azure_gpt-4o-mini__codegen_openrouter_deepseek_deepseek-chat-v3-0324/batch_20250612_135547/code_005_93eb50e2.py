"""
Generated Code Metadata:
========================
Original URL: https://eigen.io
Prompt: Create a function that generates prediction heatmaps based on image data processed by Eigen's AI solutions.
Generated: DETERMINISTIC_93eb50e22434eaa0
Batch ID: 20250612_135547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import cv2
import matplotlib.pyplot as plt
from typing import Optional, Tuple

def generate_prediction_heatmap(
    image: np.ndarray,
    predictions: np.ndarray,
    colormap: int = cv2.COLORMAP_JET,
    alpha: float = 0.5,
    normalize: bool = True,
    output_size: Optional[Tuple[int, int]] = None
) -> np.ndarray:
    """
    Generate a prediction heatmap overlay for an input image.
    
    Args:
        image: Input image (BGR or RGB format)
        predictions: 2D numpy array of prediction values (same height/width as image)
        colormap: OpenCV colormap to use (default: COLORMAP_JET)
        alpha: Transparency of heatmap overlay (0-1)
        normalize: Whether to normalize prediction values (0-1)
        output_size: Optional tuple (width, height) to resize output
        
    Returns:
        Heatmap overlay image (BGR format)
        
    Raises:
        ValueError: If inputs are invalid or dimensions don't match
    """
    # Validate inputs
    if len(image.shape) != 3 or image.shape[2] not in (3, 4):
        raise ValueError("Input image must be 3-channel (BGR/RGB) or 4-channel (BGRA/RGBA)")
    
    if len(predictions.shape) != 2:
        raise ValueError("Predictions must be a 2D array")
    
    if image.shape[0] != predictions.shape[0] or image.shape[1] != predictions.shape[1]:
        raise ValueError("Image and predictions must have the same dimensions")
    
    if not 0 <= alpha <= 1:
        raise ValueError("Alpha must be between 0 and 1")
    
    # Convert image to BGR if needed
    if image.shape[2] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
    elif image.shape[2] == 3 and np.mean(image[:, :, 0]) > np.mean(image[:, :, 2]):
        # Check if likely RGB (red channel brighter than blue)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    # Normalize predictions if requested
    if normalize:
        predictions = (predictions - predictions.min()) / (predictions.max() - predictions.min() + 1e-10)
    
    # Convert predictions to uint8 and apply colormap
    predictions_uint8 = (predictions * 255).astype(np.uint8)
    heatmap = cv2.applyColorMap(predictions_uint8, colormap)
    
    # Blend with original image
    overlay = cv2.addWeighted(image, 1 - alpha, heatmap, alpha, 0)
    
    # Resize if requested
    if output_size is not None:
        overlay = cv2.resize(overlay, output_size, interpolation=cv2.INTER_LINEAR)
    
    return overlay

def save_heatmap(
    output_path: str,
    heatmap: np.ndarray,
    dpi: int = 300,
    show_original: bool = False,
    original_image: Optional[np.ndarray] = None
) -> None:
    """
    Save heatmap visualization to file.
    
    Args:
        output_path: Path to save the image
        heatmap: Heatmap image (BGR format)
        dpi: DPI for saved image
        show_original: Whether to show original image side by side
        original_image: Original image (required if show_original=True)
        
    Raises:
        ValueError: If show_original is True but original_image is not provided
        IOError: If file cannot be saved
    """
    if show_original and original_image is None:
        raise ValueError("Original image must be provided when show_original=True")
    
    try:
        plt.figure(dpi=dpi)
        
        if show_original:
            plt.subplot(1, 2, 1)
            plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
            plt.title('Original Image')
            plt.axis('off')
            
            plt.subplot(1, 2, 2)
            plt.imshow(cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB))
            plt.title('Prediction Heatmap')
            plt.axis('off')
        else:
            plt.imshow(cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB))
            plt.axis('off')
        
        plt.tight_layout()
        plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
        plt.close()
    except Exception as e:
        raise IOError(f"Failed to save heatmap: {str(e)}")
```
