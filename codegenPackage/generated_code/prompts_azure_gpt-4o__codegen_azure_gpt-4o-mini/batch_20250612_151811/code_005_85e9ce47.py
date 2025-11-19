"""
Generated Code Metadata:
========================
Original URL: https://knoxvillebreastcenter.com
Prompt: Develop code to visualize breast MRI data in high resolution, ensuring sensitivity and comfort settings are adjustable for patient-specific needs.
Generated: DETERMINISTIC_85e9ce47528b0c67
Batch ID: 20250612_151811
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
import nibabel as nib
from skimage import exposure

class BreastMRIViz:
    """
    A class to visualize breast MRI data with adjustable sensitivity and comfort settings.
    """

    def __init__(self, file_path):
        """
        Initializes the BreastMRIViz with the MRI data from the specified file path.

        :param file_path: Path to the NIfTI file containing the MRI data.
        """
        self.file_path = file_path
        self.mri_data = self.load_mri_data()
        self.sensitivity = 1.0  # Default sensitivity setting
        self.comfort = 1.0       # Default comfort setting

    def load_mri_data(self):
        """
        Loads the MRI data from the specified NIfTI file.

        :return: 3D numpy array of MRI data.
        """
        try:
            img = nib.load(self.file_path)
            return img.get_fdata()
        except Exception as e:
            raise RuntimeError(f"Error loading MRI data: {e}")

    def adjust_settings(self, sensitivity=None, comfort=None):
        """
        Adjusts the sensitivity and comfort settings for visualization.

        :param sensitivity: Sensitivity adjustment factor (default is None).
        :param comfort: Comfort adjustment factor (default is None).
        """
        if sensitivity is not None:
            self.sensitivity = sensitivity
        if comfort is not None:
            self.comfort = comfort

    def visualize_slice(self, slice_index):
        """
        Visualizes a specific slice of the MRI data with the current settings.

        :param slice_index: Index of the slice to visualize.
        """
        if slice_index < 0 or slice_index >= self.mri_data.shape[2]:
            raise ValueError("Slice index out of bounds.")

        # Extract the specified slice
        slice_data = self.mri_data[:, :, slice_index]

        # Adjust the slice data based on sensitivity and comfort settings
        adjusted_data = exposure.rescale_intensity(slice_data, in_range=(0, self.sensitivity * np.max(slice_data)))

        # Display the slice
        plt.figure(figsize=(10, 10))
        plt.imshow(adjusted_data, cmap='gray', vmin=0, vmax=self.comfort * np.max(adjusted_data))
        plt.title(f'Breast MRI Slice {slice_index}')
        plt.axis('off')
        plt.show()

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the visualizer with the path to the MRI data file
        mri_viz = BreastMRIViz('path/to/breast_mri.nii')

        # Adjust settings as needed
        mri_viz.adjust_settings(sensitivity=1.5, comfort=1.2)

        # Visualize a specific slice
        mri_viz.visualize_slice(slice_index=10)

    except Exception as e:
        print(f"An error occurred: {e}")
```
