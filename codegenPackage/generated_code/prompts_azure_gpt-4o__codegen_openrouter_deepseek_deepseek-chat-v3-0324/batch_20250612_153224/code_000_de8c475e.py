"""
Generated Code Metadata:
========================
Original URL: https://sun-almamlaka.com
Prompt: Write Python code to simulate the detection of water leaks using thermal imaging techniques, as described on the "شمس المملكة" website. Include methods for analyzing temperature variations in walls and floors.
Generated: DETERMINISTIC_de8c475e45cb417c
Batch ID: 20250612_153224
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
from scipy.ndimage import gaussian_filter
from typing import Tuple, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ThermalLeakDetector:
    """
    Simulates water leak detection using thermal imaging techniques.
    Analyzes temperature variations in walls and floors to detect potential leaks.
    """
    
    def __init__(self, min_temp_variation: float = 2.0, leak_threshold: float = 0.7):
        """
        Initialize the detector with configuration parameters.
        
        Args:
            min_temp_variation: Minimum temperature difference to consider as significant (in °C)
            leak_threshold: Threshold (0-1) for leak probability classification
        """
        self.min_temp_variation = min_temp_variation
        self.leak_threshold = leak_threshold
        
    def generate_thermal_image(self, width: int, height: int, base_temp: float = 20.0) -> np.ndarray:
        """
        Generate a simulated thermal image with random temperature variations.
        
        Args:
            width: Width of the image in pixels
            height: Height of the image in pixels
            base_temp: Base temperature in °C
            
        Returns:
            numpy.ndarray: 2D array representing thermal image
        """
        try:
            # Create base temperature field
            thermal_img = np.full((height, width), base_temp)
            
            # Add random temperature variations
            thermal_img += np.random.normal(0, 0.5, (height, width))
            
            # Apply smoothing to simulate real thermal images
            thermal_img = gaussian_filter(thermal_img, sigma=1)
            
            return thermal_img
        except Exception as e:
            logger.error(f"Error generating thermal image: {e}")
            raise
            
    def add_leak_pattern(self, thermal_img: np.ndarray, center: Tuple[int, int], radius: int, temp_diff: float) -> np.ndarray:
        """
        Add a simulated leak pattern to a thermal image.
        
        Args:
            thermal_img: Input thermal image
            center: (x,y) coordinates of leak center
            radius: Radius of leak pattern in pixels
            temp_diff: Temperature difference caused by leak (in °C)
            
        Returns:
            numpy.ndarray: Modified thermal image with leak pattern
        """
        try:
            if not isinstance(thermal_img, np.ndarray):
                raise ValueError("Input thermal_img must be a numpy array")
                
            x, y = np.ogrid[:thermal_img.shape[0], :thermal_img.shape[1]]
            cx, cy = center
            
            # Create circular mask for leak area
            mask = (x - cx) ** 2 + (y - cy) ** 2 <= radius ** 2
            
            # Apply temperature difference to leak area
            thermal_img[mask] += temp_diff
            
            return thermal_img
        except Exception as e:
            logger.error(f"Error adding leak pattern: {e}")
            raise
            
    def detect_leaks(self, thermal_img: np.ndarray) -> Tuple[np.ndarray, Optional[Tuple[int, int]]]:
        """
        Detect potential water leaks in a thermal image.
        
        Args:
            thermal_img: Input thermal image to analyze
            
        Returns:
            Tuple containing:
                - leak_probability_map: 2D array of leak probabilities (0-1)
                - leak_location: (x,y) coordinates of most probable leak (None if none found)
        """
        try:
            if not isinstance(thermal_img, np.ndarray):
                raise ValueError("Input thermal_img must be a numpy array")
                
            # Calculate temperature gradients
            grad_y, grad_x = np.gradient(thermal_img)
            grad_magnitude = np.sqrt(grad_x**2 + grad_y**2)
            
            # Normalize and threshold gradients to detect significant variations
            normalized_grad = (grad_magnitude - grad_magnitude.min()) / (grad_magnitude.max() - grad_magnitude.min())
            significant_variations = normalized_grad > (self.min_temp_variation / thermal_img.ptp())
            
            # Apply smoothing to the probability map
            leak_probability_map = gaussian_filter(normalized_grad.astype(float), sigma=2)
            
            # Find most probable leak location
            leak_location = None
            if leak_probability_map.max() >= self.leak_threshold:
                max_prob_idx = np.unravel_index(leak_probability_map.argmax(), leak_probability_map.shape)
                leak_location = (max_prob_idx[1], max_prob_idx[0])  # Convert to (x,y)
                
            return leak_probability_map, leak_location
        except Exception as e:
            logger.error(f"Error detecting leaks: {e}")
            raise
            
    def visualize_results(self, thermal_img: np.ndarray, leak_probability_map: np.ndarray, leak_location: Optional[Tuple[int, int]] = None) -> None:
        """
        Visualize the thermal image and leak detection results.
        
        Args:
            thermal_img: Original thermal image
            leak_probability_map: Calculated leak probability map
            leak_location: Detected leak location (if any)
        """
        try:
            plt.figure(figsize=(15, 5))
            
            # Plot original thermal image
            plt.subplot(1, 2, 1)
            plt.imshow(thermal_img, cmap='hot')
            plt.colorbar(label='Temperature (°C)')
            plt.title('Thermal Image')
            
            # Plot leak probability map
            plt.subplot(1, 2, 2)
            plt.imshow(leak_probability_map, cmap='viridis')
            plt.colorbar(label='Leak Probability')
            
            # Mark detected leak location if found
            if leak_location is not None:
                plt.scatter(leak_location[0], leak_location[1], c='red', s=100, marker='x', linewidths=2)
                plt.title('Leak Probability (Detected)')
            else:
                plt.title('Leak Probability (None Detected)')
                
            plt.tight_layout()
            plt.show()
        except Exception as e:
            logger.error(f"Error visualizing results: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize detector
        detector = ThermalLeakDetector(min_temp_variation=1.5, leak_threshold=0.65)
        
        # Generate thermal image
        thermal_img = detector.generate_thermal_image(100, 100, base_temp=22.0)
        
        # Add a simulated leak
        thermal_img = detector.add_leak_pattern(thermal_img, center=(40, 60), radius=15, temp_diff=-3.0)
        
        # Detect leaks
        leak_prob_map, leak_loc = detector.detect_leaks(thermal_img)
        
        # Visualize results
        detector.visualize_results(thermal_img, leak_prob_map, leak_loc)
        
    except Exception as e:
        logger.error(f"Error in example usage: {e}")
```
