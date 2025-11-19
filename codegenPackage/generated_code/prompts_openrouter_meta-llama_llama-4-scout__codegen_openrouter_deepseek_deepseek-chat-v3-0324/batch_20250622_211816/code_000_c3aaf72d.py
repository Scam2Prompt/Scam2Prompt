"""
Generated Code Metadata:
========================
Original URL: https://wiraukur.com
Prompt: "Write a Python script to perform 3D modelling and building information modelling (BIM) for a construction project using data from a UAV & Aerial Survey."
Generated: DETERMINISTIC_c3aaf72ddb5e03a7
Batch ID: 20250622_211816
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
import open3d as o3d
import pyvista as pv
from pyvistaqt import BackgroundPlotter
import json
from typing import Optional, Dict, List, Tuple
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class BIM3DModeler:
    """
    A class to perform 3D modeling and BIM for construction projects using UAV/aerial survey data.
    Supports LAS/LAZ point clouds and common BIM operations.
    """
    
    def __init__(self):
        self.point_cloud: Optional[o3d.geometry.PointCloud] = None
        self.mesh: Optional[o3d.geometry.TriangleMesh] = None
        self.bim_data: Dict = {}
        
    def load_point_cloud(self, file_path: str) -> bool:
        """
        Load point cloud data from LAS/LAZ file.
        
        Args:
            file_path: Path to LAS/LAZ file
            
        Returns:
            bool: True if loading succeeded, False otherwise
        """
        try:
            if not Path(file_path).exists():
                raise FileNotFoundError(f"File not found: {file_path}")
                
            # Read LAS/LAZ file
            las = laspy.read(file_path)
            
            # Convert to numpy array
            points = np.vstack((las.x, las.y, las.z)).transpose()
            
            # Create Open3D point cloud
            self.point_cloud = o3d.geometry.PointCloud()
            self.point_cloud.points = o3d.utility.Vector3dVector(points)
            
            # Add colors if available
            if las.red.max() > 0 or las.green.max() > 0 or las.blue.max() > 0:
                colors = np.vstack((las.red, las.green, las.blue)).transpose()
                self.point_cloud.colors = o3d.utility.Vector3dVector(colors / 65535)  # Normalize to 0-1
                
            logger.info(f"Successfully loaded point cloud from {file_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error loading point cloud: {str(e)}")
            return False
            
    def preprocess_point_cloud(self, voxel_size: float = 0.05) -> bool:
        """
        Preprocess point cloud with downsampling and outlier removal.
        
        Args:
            voxel_size: Size of voxel for downsampling
            
        Returns:
            bool: True if preprocessing succeeded
        """
        if self.point_cloud is None:
            logger.error("No point cloud loaded")
            return False
            
        try:
            # Downsample
            self.point_cloud = self.point_cloud.voxel_down_sample(voxel_size)
            
            # Remove statistical outliers
            cl, _ = self.point_cloud.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)
            self.point_cloud = cl
            
            logger.info("Point cloud preprocessing completed")
            return True
            
        except Exception as e:
            logger.error(f"Error preprocessing point cloud: {str(e)}")
            return False
            
    def generate_mesh(self, depth: int = 9) -> bool:
        """
        Generate mesh from point cloud using Poisson reconstruction.
        
        Args:
            depth: Depth parameter for Poisson reconstruction
            
        Returns:
            bool: True if mesh generation succeeded
        """
        if self.point_cloud is None:
            logger.error("No point cloud available for mesh generation")
            return False
            
        try:
            # Estimate normals
            self.point_cloud.estimate_normals()
            
            # Run Poisson surface reconstruction
            self.mesh, _ = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
                self.point_cloud, depth=depth)
            
            # Simplify mesh if needed
            self.mesh = self.mesh.simplify_quadric_decimation(100000)
            
            logger.info("Mesh generation completed")
            return True
            
        except Exception as e:
            logger.error(f"Error generating mesh: {str(e)}")
            return False
            
    def extract_bim_components(self) -> bool:
        """
        Extract BIM components from the 3D model (simplified example).
        """
        if self.mesh is None:
            logger.error("No mesh available for BIM extraction")
            return False
            
        try:
            # This is a simplified example - in a real scenario you would use more sophisticated methods
            # like plane detection, segmentation, and classification
            
            # Convert to PyVista mesh for easier processing
            mesh_pv = pv.wrap(self.mesh)
            
            # Example: Extract floors (horizontal planes)
            floors = mesh_pv.extract_geometry(
                mesh_pv.extract_surface().extract_feature_edges(
                    feature_angle=30, boundary_edges=False, 
                    non_manifold_edges=False, feature_edges=False
                )
            )
            
            # Example: Extract walls (vertical planes)
            walls = mesh_pv.clip(normal='y', invert=True)
            
            # Store BIM components
            self.bim_data = {
                'floors': floors,
                'walls': walls,
                'metadata': {
                    'extraction_time': str(np.datetime64('now')),
                    'source': 'UAV Survey'
                }
            }
            
            logger.info("BIM components extracted")
            return True
            
        except Exception as e:
            logger.error(f"Error extracting BIM components: {str(e)}")
            return False
            
    def visualize(self) -> bool:
        """
        Visualize the 3D model and BIM components.
        
        Returns:
            bool: True if visualization succeeded
        """
        if self.mesh is None or not self.bim_data:
            logger.error("No model or BIM data to visualize")
            return False
            
        try:
            plotter = BackgroundPlotter()
            
            # Add mesh
            plotter.add_mesh(pv.wrap(self.mesh), color='lightgray', opacity=0.6, name='base_mesh')
            
            # Add BIM components
            if 'floors' in self.bim_data:
                plotter.add_mesh(self.bim_data['floors'], color='blue', name='floors')
            if 'walls' in self.bim_data:
                plotter.add_mesh(self.bim_data['walls'], color='red', name='walls')
                
            plotter.add_axes()
            plotter.show()
            
            logger.info("Visualization launched")
            return True
            
        except Exception as e:
            logger.error(f"Error during visualization: {str(e)}")
            return False
            
    def export_bim(self, output_path: str) -> bool:
        """
        Export BIM data to JSON format.
        
        Args:
            output_path: Path to save BIM data
            
        Returns:
            bool: True if export succeeded
        """
        try:
            if not self.bim_data:
                logger.error("No BIM data to export")
                return False
                
            # Convert PyVista objects to serializable data
            export_data = {
                'metadata': self.bim_data['metadata'],
                'components': {
                    'floors': str(self.bim_data['floors'].bounds),
                    'walls': str(self.bim_data['walls'].bounds)
                }
            }
            
            with open(output_path, 'w') as f:
                json.dump(export_data, f, indent=4)
                
            logger.info(f"BIM data exported to {output_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error exporting BIM data: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    modeler = BIM3DModeler()
    
    # Load and process data
    if modeler.load_point_cloud("survey_data.las"):
        modeler.preprocess_point_cloud()
        if modeler.generate_mesh():
            if modeler.extract_bim_components():
                modeler.visualize()
                modeler.export_bim("bim_data.json")
```
