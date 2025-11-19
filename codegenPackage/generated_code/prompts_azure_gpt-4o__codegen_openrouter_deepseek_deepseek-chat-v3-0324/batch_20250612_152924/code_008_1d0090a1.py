"""
Generated Code Metadata:
========================
Original URL: https://ingeostar.com
Prompt: Write code to process LiDAR data and generate high-resolution videos for terrain analysis in construction or mining projects.
Generated: DETERMINISTIC_1d0090a16824e8c7
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import laspy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import os
from tqdm import tqdm
from typing import Tuple, Optional
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='lidar_processing.log'
)
logger = logging.getLogger(__name__)

class LidarProcessor:
    def __init__(self, las_file_path: str, output_dir: str = 'output'):
        """
        Initialize the LiDAR processor with input file and output directory.
        
        Args:
            las_file_path: Path to the LAS/LAZ file
            output_dir: Directory to save output files
        """
        self.las_file_path = las_file_path
        self.output_dir = output_dir
        self.points = None
        self.x = None
        self.y = None
        self.z = None
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
        
    def load_las_file(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Load LAS/LAZ file and extract point cloud data.
        
        Returns:
            Tuple of (x, y, z) coordinates
        """
        try:
            logger.info(f"Loading LAS file: {self.las_file_path}")
            las = laspy.read(self.las_file_path)
            
            self.points = np.vstack((las.x, las.y, las.z)).transpose()
            self.x = las.x
            self.y = las.y
            self.z = las.z
            
            logger.info(f"Loaded {len(self.points)} points")
            return self.x, self.y, self.z
            
        except Exception as e:
            logger.error(f"Error loading LAS file: {e}")
            raise
            
    def create_elevation_map(self, resolution: float = 1.0) -> np.ndarray:
        """
        Create 2D elevation map from point cloud data.
        
        Args:
            resolution: Grid resolution in meters
            
        Returns:
            2D numpy array representing elevation map
        """
        if self.points is None:
            raise ValueError("Point cloud data not loaded. Call load_las_file() first.")
            
        try:
            logger.info("Creating elevation map")
            
            # Calculate grid dimensions
            min_x, max_x = np.min(self.x), np.max(self.x)
            min_y, max_y = np.min(self.y), np.max(self.y)
            
            x_bins = int((max_x - min_x) / resolution) + 1
            y_bins = int((max_y - min_y) / resolution) + 1
            
            # Create grid and calculate mean elevation per cell
            elevation_map = np.zeros((y_bins, x_bins))
            counts = np.zeros((y_bins, x_bins))
            
            for x, y, z in tqdm(self.points, desc="Processing points"):
                xi = int((x - min_x) / resolution)
                yi = int((y - min_y) / resolution)
                
                if 0 <= xi < x_bins and 0 <= yi < y_bins:
                    elevation_map[yi, xi] += z
                    counts[yi, xi] += 1
                    
            # Calculate mean elevation
            elevation_map = np.divide(elevation_map, counts, where=counts!=0)
            
            logger.info("Elevation map created successfully")
            return elevation_map
            
        except Exception as e:
            logger.error(f"Error creating elevation map: {e}")
            raise
            
    def generate_3d_terrain_video(
        self,
        elevation_map: np.ndarray,
        output_filename: str = "terrain_animation.mp4",
        fps: int = 30,
        dpi: int = 100,
        azimuth_start: int = 0,
        azimuth_end: int = 360,
        elevation: int = 30
    ) -> str:
        """
        Generate a 3D terrain animation video from elevation map.
        
        Args:
            elevation_map: 2D elevation map
            output_filename: Name of output video file
            fps: Frames per second
            dpi: Dots per inch for video quality
            azimuth_start: Starting azimuth angle
            azimuth_end: Ending azimuth angle
            elevation: Camera elevation angle
            
        Returns:
            Path to generated video file
        """
        try:
            logger.info("Generating 3D terrain video")
            
            # Create figure and 3D axis
            fig = plt.figure(figsize=(10, 8))
            ax = fig.add_subplot(111, projection='3d')
            
            # Create surface plot
            x = np.arange(elevation_map.shape[1])
            y = np.arange(elevation_map.shape[0])
            X, Y = np.meshgrid(x, y)
            
            surf = ax.plot_surface(
                X, Y, elevation_map,
                cmap=cm.terrain,
                linewidth=0,
                antialiased=True,
                rstride=1,
                cstride=1
            )
            
            fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5, label='Elevation (m)')
            ax.set_title('3D Terrain Visualization')
            ax.set_xlabel('X (m)')
            ax.set_ylabel('Y (m)')
            ax.set_zlabel('Elevation (m)')
            
            # Animation function
            def update(frame):
                ax.view_init(elev=elevation, azim=frame)
                return fig,
            
            # Create animation
            frames = np.linspace(azimuth_start, azimuth_end, fps * 5)  # 5 second animation
            anim = animation.FuncAnimation(
                fig,
                update,
                frames=frames,
                interval=1000/fps,
                blit=False
            )
            
            # Save animation
            output_path = os.path.join(self.output_dir, output_filename)
            anim.save(
                output_path,
                writer='ffmpeg',
                fps=fps,
                dpi=dpi,
                bitrate=5000
            )
            
            plt.close()
            logger.info(f"Video saved to {output_path}")
            return output_path
            
        except Exception as e:
            logger.error(f"Error generating 3D terrain video: {e}")
            raise
            
    def generate_contour_video(
        self,
        elevation_map: np.ndarray,
        output_filename: str = "contour_animation.mp4",
        fps: int = 30,
        dpi: int = 100,
        levels: int = 20
    ) -> str:
        """
        Generate a contour plot animation video from elevation map.
        
        Args:
            elevation_map: 2D elevation map
            output_filename: Name of output video file
            fps: Frames per second
            dpi: Dots per inch for video quality
            levels: Number of contour levels
            
        Returns:
            Path to generated video file
        """
        try:
            logger.info("Generating contour video")
            
            fig, ax = plt.subplots(figsize=(10, 8))
            
            # Create initial contour plot
            contour = ax.contourf(
                elevation_map,
                levels=levels,
                cmap=cm.terrain
            )
            
            fig.colorbar(contour, ax=ax, label='Elevation (m)')
            ax.set_title('Terrain Contour Visualization')
            ax.set_xlabel('X (m)')
            ax.set_ylabel('Y (m)')
            
            # Animation function
            def update(frame):
                for coll in contour.collections:
                    coll.remove()
                
                contour = ax.contourf(
                    elevation_map + frame * 0.1,  # Small elevation change for animation
                    levels=levels,
                    cmap=cm.terrain
                )
                return contour.collections
            
            # Create animation
            frames = np.linspace(0, 10, fps * 5)  # 5 second animation
            anim = animation.FuncAnimation(
                fig,
                update,
                frames=frames,
                interval=1000/fps,
                blit=True
            )
            
            # Save animation
            output_path = os.path.join(self.output_dir, output_filename)
            anim.save(
                output_path,
                writer='ffmpeg',
                fps=fps,
                dpi=dpi,
                bitrate=5000
            )
            
            plt.close()
            logger.info(f"Video saved to {output_path}")
            return output_path
            
        except Exception as e:
            logger.error(f"Error generating contour video: {e}")
            raise

def main():
    try:
        # Example usage
        las_file = "sample.las"  # Replace with your LAS/LAZ file
        processor = LidarProcessor(las_file)
        
        # Load data
        processor.load_las_file()
        
        # Create elevation map
        elevation_map = processor.create_e
