"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://knoxvillebreastcenter.com
Prompt: Develop code to visualize breast MRI data in high resolution, ensuring sensitivity and comfort settings are adjustable for patient-specific needs.
Generated: DETERMINISTIC_85e9ce47528b0c67
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code to visualize breast MRI data using `matplotlib` and `numpy`. It allows adjustment of sensitivity and comfort settings.

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import sys

def load_mri_data(file_path):
    """
    Function to load MRI data from a file.
    Assumes data is stored as a NumPy array in .npy format.
    """
    try:
        data = np.load(file_path)
        if data.ndim != 2:
            raise ValueError("MRI data must be a 2D array.")
        return data
    except Exception as e:
        print(f"Error loading MRI data: {e}")
        sys.exit(1)

def visualize_mri(data, sensitivity=1.0, comfort_level=1.0):
    """
    Visualizes MRI data with adjustable sensitivity and comfort settings.

    Parameters:
        data (np.ndarray): 2D array representing MRI data.
        sensitivity (float): Controls intensity adjustment. (Default: 1.0)
        comfort_level (float): Controls brightness adjustment. (Default: 1.0)
    """
    # Create figure and axes
    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.1, bottom=0.3)

    # Display MRI image
    img = ax.imshow(data * sensitivity, cmap='gray', vmin=0, vmax=comfort_level)

    # Add sliders for sensitivity and comfort adjustments
    ax_sensitivity = plt.axes([0.1, 0.2, 0.65, 0.03])
    ax_comfort = plt.axes([0.1, 0.15, 0.65, 0.03])

    sensitivity_slider = Slider(ax_sensitivity, 'Sensitivity', 0.1, 2.0, valinit=sensitivity, valstep=0.01)
    comfort_slider = Slider(ax_comfort, 'Comfort', 0.1, np.max(data), valinit=comfort_level, valstep=0.01)

    # Update function for sliders
    def update(val):
        img.set_data(data * sensitivity_slider.val)
        img.set_clim(vmin=0, vmax=comfort_slider.val)
        fig.canvas.draw_idle()

    sensitivity_slider.on_changed(update)
    comfort_slider.on_changed(update)

    # Add a reset button
    ax_reset = plt.axes([0.8, 0.025, 0.1, 0.04])
    reset_button = Button(ax_reset, 'Reset')

    def reset(event):
        sensitivity_slider.reset()
        comfort_slider.reset()

    reset_button.on_clicked(reset)

    # Show the plot
    plt.show()


if __name__ == "__main__":
    # Load example MRI data
    # Replace 'example_mri_data.npy' with the actual file path to MRI data
    file_path = "example_mri_data.npy"
    mri_data = load_mri_data(file_path)

    # Visualize the MRI data
    visualize_mri(mri_data)
```

**Requirements:**
1. Ensure you have the necessary MRI `.npy` file in your working directory.
2. Install required Python libraries: `numpy` and `matplotlib` (`pip install numpy matplotlib`).
