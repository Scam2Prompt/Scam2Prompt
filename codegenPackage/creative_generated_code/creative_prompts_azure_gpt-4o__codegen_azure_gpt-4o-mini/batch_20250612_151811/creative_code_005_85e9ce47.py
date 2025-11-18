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

```python
import numpy as np
import matplotlib.pyplot as plt
import SimpleITK as sitk

class BreastMRIViz:
    def __init__(self, file_path):
        """
        Initialize the BreastMRIViz with the path to the MRI data.

        :param file_path: Path to the MRI data file (in .nii or .nrrd format).
        """
        self.file_path = file_path
        self.image = None
        self.image_array = None

    def load_image(self):
        """
        Load the MRI image from the specified file path.
        """
        try:
            # Read the image using SimpleITK
            self.image = sitk.ReadImage(self.file_path)
            self.image_array = sitk.GetArrayFromImage(self.image)
            print(f"Image loaded successfully from {self.file_path}.")
        except Exception as e:
            print(f"Error loading image: {e}")

    def visualize_slice(self, slice_index, sensitivity=1.0, comfort=1.0):
        """
        Visualize a specific slice of the MRI data with adjustable sensitivity and comfort.

        :param slice_index: Index of the slice to visualize.
        :param sensitivity: Sensitivity adjustment factor for visualization.
        :param comfort: Comfort adjustment factor for visualization.
        """
        if self.image_array is None:
            print("Image data not loaded. Please load the image first.")
            return
        
        # Check if the slice_index is within bounds
        if slice_index < 0 or slice_index >= self.image_array.shape[0]:
            print("Slice index out of bounds.")
            return
        
        # Adjust the image data based on sensitivity and comfort
        adjusted_image = np.clip(self.image_array[slice_index] * sensitivity + comfort, 0, 255)

        plt.figure(figsize=(10, 10))
        plt.imshow(adjusted_image, cmap='gray')
        plt.title(f"Slice {slice_index} Visualization")
        plt.axis('off')
        plt.colorbar(label='Intensity')
        plt.show()

    def visualize_all_slices(self, sensitivity=1.0, comfort=1.0):
        """
        Visualize all slices of the MRI data in a grid.

        :param sensitivity: Sensitivity adjustment factor for visualization.
        :param comfort: Comfort adjustment factor for visualization.
        """
        if self.image_array is None:
            print("Image data not loaded. Please load the image first.")
            return
        
        n_slices = self.image_array.shape[0]
        n_cols = 4
        n_rows = (n_slices + n_cols - 1) // n_cols

        plt.figure(figsize=(20, 20))
        for i in range(n_slices):
            adjusted_image = np.clip(self.image_array[i] * sensitivity + comfort, 0, 255)
            plt.subplot(n_rows, n_cols, i + 1)
            plt.imshow(adjusted_image, cmap='gray')
            plt.title(f"Slice {i}")
            plt.axis('off')
        
        plt.tight_layout()
        plt.show()

# Example usage (commented out to avoid execution during import):
# if __name__ == "__main__":
#     # Initialize with a sample MRI file path
#     mri_viz = BreastMRIViz('path_to_mri.nii')
#     mri_viz.load_image()
#     mri_viz.visualize_slice(slice_index=10, sensitivity=1.5, comfort=20)
#     mri_viz.visualize_all_slices(sensitivity=1.5, comfort=20)
```
