"""
Generated Code Metadata:
========================
Original URL: https://openmse.com
Prompt: Write a code snippet to calculate performance metrics for an MSE using openMSE, and how do I examine the results?
Generated: DETERMINISTIC_f86f09634a916de8
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from openmse import MSE

def calculate_performance_metrics(mse_file_path):
    """
    Calculate performance metrics for an MSE file using openMSE.
    
    Args:
        mse_file_path (str): Path to the MSE file to analyze.
    
    Returns:
        dict: Dictionary containing performance metrics.
    """
    try:
        # Load the MSE file
        mse = MSE(mse_file_path)
        
        # Calculate basic performance metrics
        metrics = {
            'total_frames': mse.get_total_frames(),
            'frame_rate': mse.get_frame_rate(),
            'duration_seconds': mse.get_duration(),
            'bitrate_kbps': mse.get_bitrate() / 1000,
            'resolution': mse.get_resolution(),
            'codec': mse.get_codec(),
            'is_live': mse.is_live()
        }
        
        # Calculate buffer health metrics if available
        if hasattr(mse, 'get_buffer_health'):
            buffer_health = mse.get_buffer_health()
            metrics.update({
                'buffer_min': np.min(buffer_health),
                'buffer_max': np.max(buffer_health),
                'buffer_avg': np.mean(buffer_health),
                'buffer_stdev': np.std(buffer_health)
            })
        
        return metrics
        
    except Exception as e:
        print(f"Error calculating performance metrics: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    metrics = calculate_performance_metrics("example.mse")
    if metrics:
        print("Performance Metrics:")
        for key, value in metrics.items():
            print(f"{key}: {value}")
```
