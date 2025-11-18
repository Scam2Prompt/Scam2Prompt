"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drcarloscastillo.com
Prompt: Recommend a Python library or API for visualizing medical imaging data related to foot and ankle injuries, such as cartilage damage or trauma.
Generated: DETERMINISTIC_5a9e9a25de5a862d
Batch ID: 20250612_153224
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
import nibabel as nib

class MedicalImageVisualizer:
    """
    A class to visualize medical imaging data related to foot and ankle injuries.
    
    Attributes
    ----------
    image_path : str
        File path to the medical imaging data (e.g., NIfTI format).
    image_data : numpy.ndarray
        The loaded image data as a numpy array.
    """

    def __init__(self, image_path):
        """
        Initializes the MedicalImageVisualizer with the given image path.

        Parameters
        ----------
        image_path : str
            The file path to the medical imaging data.
        """
        self.image_path = image_path
        self.image_data = None

    def load_image(self):
        """
        Loads the medical imaging data from the specified path.
        
        Raises
        ------
        FileNotFoundError
            If the file does not exist at the specified path.
        ValueError
            If the file format is not supported.
        """
        try:
            # Load NIfTI image using nibabel
            img = nib.load(self.image_path)
            self.image_data = img.get_fdata()
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.image_path} was not found.")
        except Exception as e:
            raise ValueError("Unsupported file format or error loading the image.") from e

    def visualize_slice(self, slice_index):
        """
        Visualizes a specific slice of the medical imaging data.

        Parameters
        ----------
        slice_index : int
            The index of the slice to visualize.

        Raises
        ------
        IndexError
            If the slice index is out of bounds.
        """
        if self.image_data is None:
            raise ValueError("Image data is not loaded. Please call load_image() first.")

        # Verify the slice index is within bounds
        if not (0 <= slice_index < self.image_data.shape[2]):
            raise IndexError(f"Slice index {slice_index} is out of bounds for the image data of shape {self.image_data.shape}.")

        # Extract the requested slice
        image_slice = self.image_data[:, :, slice_index]

        # Create a figure for visualization
        plt.figure(figsize=(10, 8))
        plt.imshow(image_slice.T, cmap='gray', origin='lower')
        plt.title(f'Slice {slice_index}')
        plt.axis('off')
        plt.colorbar()
        plt.show()

# Example of usage
if __name__ == "__main__":
    try:
        # Initialize the visualizer with the path to a NIfTI file
        visualizer = MedicalImageVisualizer("path/to/foot_and_ankle_injury_image.nii")

        # Load the image data
        visualizer.load_image()

        # Visualize a specific slice (for example, slice index 20)
        visualizer.visualize_slice(20)
    except Exception as e:
        print(f"An error occurred: {e}")
```
