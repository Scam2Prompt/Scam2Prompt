"""
Generated Code Metadata:
========================
Original URL: https://wiraukur.com
Prompt: Write Python code to process UAV aerial survey data and generate a 3D model using Building Information Modelling (BIM) techniques, referencing methodologies used by Wira Survey Consultants.
Generated: DETERMINISTIC_49a27400130f9005
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import numpy as np
import open3d as o3d
import laspy
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from pyntcloud import PyntCloud
import pandas as pd
from scipy.spatial import Delaunay
import logging
from typing import Optional, Tuple, List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class UAVDataProcessor:
    """
    Class to process UAV aerial survey data and generate 3D BIM models.
    Methodology inspired by Wira Survey Consultants' approaches.
    """
    
    def __init__(self, input_path: str, output_dir: str = "output"):
        """
        Initialize the UAV data processor.
        
        Args:
            input_path: Path to input data (LAS/LAZ file or point cloud data)
            output_dir: Directory to save output files
        """
        self.input_path = input_path
        self.output_dir = output_dir
        self.point_cloud = None
        self.processed_data = None
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
        
    def load_point_cloud(self) -> bool:
        """
        Load point cloud data from input file.
        
        Returns:
            bool: True if loading was successful, False otherwise
        """
        try:
            if self.input_path.endswith(('.las', '.laz')):
                # Read LAS/LAZ file
                las = laspy.read(self.input_path)
                points = np.vstack((las.x, las.y, las.z)).transpose()
                
                # Create Open3D point cloud
                self.point_cloud = o3d.geometry.PointCloud()
                self.point_cloud.points = o3d.utility.Vector3dVector(points)
                
                # Add colors if available
                if hasattr(las, 'red') and hasattr(las, 'green') and hasattr(las, 'blue'):
                    colors = np.vstack((las.red, las.green, las.blue)).transpose()
                    colors = colors / 65535.0  # Normalize to [0,1]
                    self.point_cloud.colors = o3d.utility.Vector3dVector(colors)
                    
            elif self.input_path.endswith(('.ply', '.pcd', '.xyz', '.pts')):
                # Read other point cloud formats
                self.point_cloud = o3d.io.read_point_cloud(self.input_path)
            else:
                logger.error("Unsupported file format")
                return False
                
            if not self.point_cloud.has_points():
                logger.error("No points found in the point cloud")
                return False
                
            logger.info(f"Successfully loaded point cloud with {len(self.point_cloud.points)} points")
            return True
            
        except Exception as e:
            logger.error(f"Error loading point cloud: {str(e)}")
            return False
    
    def preprocess_point_cloud(self, voxel_size: float = 0.05) -> bool:
        """
        Preprocess point cloud by downsampling and removing outliers.
        
        Args:
            voxel_size: Size of voxel for downsampling
            
        Returns:
            bool: True if preprocessing was successful, False otherwise
        """
        try:
            if self.point_cloud is None:
                logger.error("Point cloud not loaded")
                return False
                
            # Downsample the point cloud
            logger.info("Downsampling point cloud...")
            downsampled = self.point_cloud.voxel_down_sample(voxel_size=voxel_size)
            
            # Remove statistical outliers
            logger.info("Removing outliers...")
            cl, _ = downsampled.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)
            
            self.point_cloud = cl
            logger.info(f"Preprocessed point cloud now has {len(self.point_cloud.points)} points")
            return True
            
        except Exception as e:
            logger.error(f"Error preprocessing point cloud: {str(e)}")
            return False
    
    def segment_building_points(self, eps: float = 0.5, min_samples: int = 10) -> Optional[np.ndarray]:
        """
        Segment building points from the point cloud using DBSCAN clustering.
        
        Args:
            eps: DBSCAN parameter - maximum distance between two samples
            min_samples: DBSCAN parameter - number of samples in a neighborhood
            
        Returns:
            Optional[np.ndarray]: Array of labels for each point, or None if failed
        """
        try:
            if self.point_cloud is None:
                logger.error("Point cloud not loaded")
                return None
                
            points = np.asarray(self.point_cloud.points)
            
            # Standardize the data
            scaler = StandardScaler()
            points_scaled = scaler.fit_transform(points)
            
            # Apply DBSCAN clustering
            logger.info("Segmenting building points using DBSCAN...")
            dbscan = DBSCAN(eps=eps, min_samples=min_samples)
            labels = dbscan.fit_predict(points_scaled)
            
            # Find the largest cluster (likely the building)
            unique_labels, counts = np.unique(labels[labels != -1], return_counts=True)
            if len(unique_labels) == 0:
                logger.warning("No clusters found")
                return None
                
            building_label = unique_labels[np.argmax(counts)]
            building_mask = (labels == building_label)
            
            # Extract building points
            building_points = points[building_mask]
            
            # Create new point cloud with just building points
            building_pcd = o3d.geometry.PointCloud()
            building_pcd.points = o3d.utility.Vector3dVector(building_points)
            
            if self.point_cloud.has_colors():
                colors = np.asarray(self.point_cloud.colors)[building_mask]
                building_pcd.colors = o3d.utility.Vector3dVector(colors)
            
            self.point_cloud = building_pcd
            logger.info(f"Building segmentation complete. {len(building_pcd.points)} points identified as building.")
            
            return labels
            
        except Exception as e:
            logger.error(f"Error segmenting building points: {str(e)}")
            return None
    
    def reconstruct_surface(self, depth: int = 9) -> Optional[o3d.geometry.TriangleMesh]:
        """
        Reconstruct surface mesh using Poisson surface reconstruction.
        
        Args:
            depth: Depth of the octree used for reconstruction
            
        Returns:
            Optional[o3d.geometry.TriangleMesh]: Reconstructed mesh or None if failed
        """
        try:
            if self.point_cloud is None or len(self.point_cloud.points) < 100:
                logger.error("Not enough points for surface reconstruction")
                return None
                
            logger.info("Reconstructing surface using Poisson reconstruction...")
            
            # Estimate normals if not present
            if not self.point_cloud.has_normals():
                self.point_cloud.estimate_normals(
                    search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
            
            # Perform Poisson surface reconstruction
            mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
                self.point_cloud, depth=depth)
            
            # Remove low density vertices
            vertices_to_remove = densities < np.quantile(densities, 0.01)
            mesh.remove_vertices_by_mask(vertices_to_remove)
            
            logger.info("Surface reconstruction complete")
            return mesh
            
        except Exception as e:
            logger.error(f"Error reconstructing surface: {str(e)}")
            return None
    
    def generate_bim_model(self, mesh: o3d.geometry.TriangleMesh) -> bool:
        """
        Generate BIM model from the reconstructed mesh.
        
        Args:
            mesh: Reconstructed mesh to convert to BIM model
            
        Returns:
            bool: True if BIM generation was successful, False otherwise
        """
        try:
            if mesh is None:
                logger.error("No mesh provided for BIM generation")
                return False
                
            logger.info("Generating BIM model...")
            
            # Simplify the mesh for BIM
            simplified_mesh = mesh.simplify_quadric_decimation(target_number_of_triangles=10000)
            
            # Save the BIM model
            output_path = os.path.join(self.output_dir, "bim_model.obj")
            o3d.io.write_triangle_mesh(output_path, simplified_mesh)
            
            logger.info(f"BIM model saved to {output_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error generating BIM model: {str(e)}")
            return False
    
    def process_pipeline(self) -> bool:
        """
        Run the complete processing pipeline.
        
        Returns:
            bool: True if pipeline completed successfully, False otherwise
        """
        try:
            # Step 1: Load point cloud
