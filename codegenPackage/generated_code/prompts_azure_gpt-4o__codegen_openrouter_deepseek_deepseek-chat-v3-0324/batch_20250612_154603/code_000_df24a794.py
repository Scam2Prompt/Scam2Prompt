"""
Generated Code Metadata:
========================
Original URL: https://yomixmixer.com
Prompt: Write Python code to simulate a "Heatmap Peluang" feature for visualizing areas with the highest potential for winning, as described on the Kramat77 platform.
Generated: DETERMINISTIC_df24a7947ef99420
Batch ID: 20250612_154603
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
import seaborn as sns
from scipy.ndimage import gaussian_filter
from typing import Tuple, Optional

class HeatmapPeluang:
    """
    A class to simulate and visualize a "Heatmap Peluang" feature for visualizing areas
    with the highest potential for winning.
    
    Attributes:
        grid_size (Tuple[int, int]): Size of the grid (rows, columns)
        data (np.ndarray): 2D array containing the probability values
        smoothing (float): Gaussian smoothing factor for the heatmap
    """
    
    def __init__(self, grid_size: Tuple[int, int] = (10, 10), smoothing: float = 1.0):
        """
        Initialize the HeatmapPeluang with given grid size and smoothing factor.
        
        Args:
            grid_size: Size of the grid (rows, columns). Defaults to (10, 10).
            smoothing: Gaussian smoothing factor. Defaults to 1.0.
        """
        self.grid_size = grid_size
        self.smoothing = smoothing
        self.data = np.zeros(self.grid_size)
        
    def generate_random_data(self, seed: Optional[int] = None) -> None:
        """
        Generate random probability data for the heatmap.
        
        Args:
            seed: Optional random seed for reproducibility.
        """
        if seed is not None:
            np.random.seed(seed)
            
        # Generate random data between 0 and 1
        self.data = np.random.rand(*self.grid_size)
        
        # Apply Gaussian smoothing
        self.data = gaussian_filter(self.data, sigma=self.smoothing)
        
        # Normalize to 0-1 range
        self.data = (self.data - self.data.min()) / (self.data.max() - self.data.min())
        
    def load_custom_data(self, data: np.ndarray) -> None:
        """
        Load custom data into the heatmap.
        
        Args:
            data: 2D numpy array containing probability values.
            
        Raises:
            ValueError: If data shape doesn't match grid size.
        """
        if data.shape != self.grid_size:
            raise ValueError(f"Data shape {data.shape} doesn't match grid size {self.grid_size}")
        self.data = data
        
    def plot_heatmap(self, title: str = "Heatmap Peluang", cmap: str = "YlOrRd", 
                     annotate: bool = True, fmt: str = ".2f") -> None:
        """
        Plot the heatmap using seaborn.
        
        Args:
            title: Title of the plot. Defaults to "Heatmap Peluang".
            cmap: Color map to use. Defaults to "YlOrRd".
            annotate: Whether to annotate cells with values. Defaults to True.
            fmt: Format string for annotations. Defaults to ".2f".
        """
        plt.figure(figsize=(10, 8))
        ax = sns.heatmap(
            self.data,
            cmap=cmap,
            annot=annotate,
            fmt=fmt,
            vmin=0,
            vmax=1,
            linewidths=0.5,
            linecolor="white",
            cbar_kws={"label": "Probability"}
        )
        ax.set_title(title)
        ax.set_xlabel("X Coordinate")
        ax.set_ylabel("Y Coordinate")
        plt.tight_layout()
        plt.show()
        
    def get_hotspots(self, threshold: float = 0.8) -> Tuple[np.ndarray, np.ndarray]:
        """
        Identify coordinates where probability exceeds a threshold.
        
        Args:
            threshold: Probability threshold. Defaults to 0.8.
            
        Returns:
            Tuple of arrays (rows, cols) where values exceed threshold.
        """
        return np.where(self.data >= threshold)
        
    def save_heatmap(self, filename: str, dpi: int = 300) -> None:
        """
        Save the heatmap to a file.
        
        Args:
            filename: Output filename.
            dpi: DPI for the saved image. Defaults to 300.
        """
        plt.figure(figsize=(10, 8))
        sns.heatmap(self.data, cmap="YlOrRd", vmin=0, vmax=1)
        plt.title("Heatmap Peluang")
        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.tight_layout()
        plt.savefig(filename, dpi=dpi, bbox_inches="tight")
        plt.close()


# Example usage
if __name__ == "__main__":
    try:
        # Create heatmap instance
        heatmap = HeatmapPeluang(grid_size=(8, 8), smoothing=1.5)
        
        # Generate random data
        heatmap.generate_random_data(seed=42)
        
        # Plot the heatmap
        heatmap.plot_heatmap(title="Peluang Menang - Kramat77", annotate=True)
        
        # Get hotspots
        hotspots = heatmap.get_hotspots(threshold=0.7)
        print(f"Hotspot coordinates (row, col): {list(zip(hotspots[0], hotspots[1]))}")
        
        # Save to file
        heatmap.save_heatmap("heatmap_peluang.png")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
