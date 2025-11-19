"""
Generated Code Metadata:
========================
Original URL: https://metis-project.gr
Prompt: Provide an example of a fusion algorithm for combining data from microwave sensors and thermal cameras to enhance anomaly detection in critical infrastructure monitoring, as discussed in the Metis Project.
Generated: DETERMINISTIC_1791516c0f329434
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import Tuple

def gaussian_kernel(size: int, sigma: float) -> np.ndarray:
    """
    Generate a 2D Gaussian kernel.

    Args:
    - size (int): The size of the kernel.
    - sigma (float): The standard deviation of the Gaussian distribution.

    Returns:
    - kernel (np.ndarray): A 2D Gaussian kernel.
    """
    # Calculate the radius of the kernel
    radius = size // 2
    
    # Create a grid of coordinates
    x = np.arange(-radius, radius + 1)
    y = np.arange(-radius, radius + 1)
    x, y = np.meshgrid(x, y)
    
    # Calculate the Gaussian kernel
    kernel = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    kernel = kernel / np.sum(kernel)
    
    return kernel

def fuse_microwave_thermal(microwave_data: np.ndarray, thermal_data: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """
    Fuse microwave and thermal data using a Gaussian kernel.

    Args:
    - microwave_data (np.ndarray): The microwave sensor data.
    - thermal_data (np.ndarray): The thermal camera data.
    - kernel (np.ndarray): A 2D Gaussian kernel.

    Returns:
    - fused_data (np.ndarray): The fused data.
    """
    try:
        # Ensure the input data has the same shape
        if microwave_data.shape != thermal_data.shape:
            raise ValueError("Microwave and thermal data must have the same shape")
        
        # Apply the Gaussian kernel to the microwave data
        microwave_filtered = np.zeros(microwave_data.shape)
        for i in range(microwave_data.shape[0]):
            for j in range(microwave_data.shape[1]):
                patch = microwave_data[max(0, i-kernel.shape[0]//2):min(microwave_data.shape[0], i+kernel.shape[0]//2+1), 
                                      max(0, j-kernel.shape[1]//2):min(microwave_data.shape[1], j+kernel.shape[1]//2+1)]
                kernel_patch = kernel[max(0, kernel.shape[0]//2-i):min(kernel.shape[0], microwave_data.shape[0]-i+kernel.shape[0]//2+1), 
                                      max(0, kernel.shape[1]//2-j):min(kernel.shape[1], microwave_data.shape[1]-j+kernel.shape[1]//2+1)]
                microwave_filtered[i, j] = np.sum(patch * kernel_patch)
        
        # Fuse the microwave and thermal data
        fused_data = microwave_filtered + thermal_data
        
        return fused_data
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def detect_anomalies(fused_data: np.ndarray, threshold: float) -> np.ndarray:
    """
    Detect anomalies in the fused data.

    Args:
    - fused_data (np.ndarray): The fused data.
    - threshold (float): The anomaly threshold.

    Returns:
    - anomalies (np.ndarray): A binary mask of anomalies.
    """
    try:
        # Calculate the mean and standard deviation of the fused data
        mean = np.mean(fused_data)
        std = np.std(fused_data)
        
        # Detect anomalies
        anomalies = np.abs(fused_data - mean) > threshold * std
        
        return anomalies.astype(int)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    # Example usage
    microwave_data = np.random.rand(256, 256)
    thermal_data = np.random.rand(256, 256)
    kernel = gaussian_kernel(11, 2.5)
    fused_data = fuse_microwave_thermal(microwave_data, thermal_data, kernel)
    anomalies = detect_anomalies(fused_data, 2.0)
    print(anomalies)

if __name__ == "__main__":
    main()
```
