"""
Generated Code Metadata:
========================
Original URL: https://wiraukur.com
Prompt: Write code to process cadastral survey data and visualize property boundaries, using techniques employed by Wira Survey Consultants.
Generated: DETERMINISTIC_b40c8f236d3b01c0
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import fiona
import os
import logging
from typing import Optional, List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CadastralDataProcessor:
    """
    A class to process and visualize cadastral survey data.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the CadastralDataProcessor with the path to the cadastral data.
        
        Args:
            data_path (str): Path to the cadastral data file (e.g., shapefile, GeoJSON).
        """
        self.data_path = data_path
        self.gdf = None
        self._validate_data_path()
        
    def _validate_data_path(self) -> None:
        """
        Validate that the data path exists and is a supported file format.
        
        Raises:
            FileNotFoundError: If the data path does not exist.
            ValueError: If the file format is not supported.
        """
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Data file not found at {self.data_path}")
        
        supported_drivers = fiona.supported_drivers.keys()
        file_ext = os.path.splitext(self.data_path)[1].lower()
        
        if file_ext not in ['.shp', '.geojson', '.gpkg']:
            raise ValueError(f"Unsupported file format: {file_ext}. Supported formats: {', '.join(supported_drivers)}")
    
    def load_data(self) -> None:
        """
        Load the cadastral data into a GeoDataFrame.
        
        Raises:
            Exception: If there is an error loading the data.
        """
        try:
            self.gdf = gpd.read_file(self.data_path)
            logger.info(f"Successfully loaded data with {len(self.gdf)} features")
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def validate_geometries(self) -> None:
        """
        Validate geometries in the GeoDataFrame and fix any issues.
        """
        if self.gdf is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        # Check for invalid geometries
        invalid_geoms = ~self.gdf.geometry.is_valid
        if invalid_geoms.any():
            logger.warning(f"Found {invalid_geoms.sum()} invalid geometries. Attempting to fix...")
            self.gdf.geometry = self.gdf.geometry.buffer(0)
            
            # Verify fixes
            if (~self.gdf.geometry.is_valid).any():
                logger.error("Could not fix all invalid geometries")
            else:
                logger.info("All geometries are now valid")
    
    def plot_property_boundaries(
        self,
        output_path: Optional[str] = None,
        title: str = "Property Boundaries",
        figsize: tuple = (10, 10),
        dpi: int = 300,
        color: str = 'blue',
        edgecolor: str = 'black',
        alpha: float = 0.5,
        show_plot: bool = True
    ) -> None:
        """
        Plot property boundaries from the cadastral data.
        
        Args:
            output_path (Optional[str]): Path to save the plot. If None, plot is not saved.
            title (str): Title for the plot.
            figsize (tuple): Figure size (width, height) in inches.
            dpi (int): Dots per inch for the output figure.
            color (str): Fill color for the properties.
            edgecolor (str): Edge color for the property boundaries.
            alpha (float): Transparency of the fill color.
            show_plot (bool): Whether to display the plot.
            
        Raises:
            ValueError: If data is not loaded or contains no valid geometries.
        """
        if self.gdf is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        if len(self.gdf) == 0:
            raise ValueError("No data to plot.")
            
        try:
            fig, ax = plt.subplots(figsize=figsize)
            
            # Plot the property boundaries
            self.gdf.plot(
                ax=ax,
                color=color,
                edgecolor=edgecolor,
                alpha=alpha,
                linewidth=0.5
            )
            
            # Set plot title and labels
            ax.set_title(title, fontsize=14)
            ax.set_xlabel("Longitude")
            ax.set_ylabel("Latitude")
            
            # Add grid and adjust layout
            ax.grid(True, linestyle='--', alpha=0.7)
            plt.tight_layout()
            
            # Save or show the plot
            if output_path:
                plt.savefig(output_path, dpi=dpi, bbox_inches='tight')
                logger.info(f"Plot saved to {output_path}")
            if show_plot:
                plt.show()
                
        except Exception as e:
            logger.error(f"Error plotting property boundaries: {str(e)}")
            raise
    
    def calculate_area_stats(self) -> Dict[str, Any]:
        """
        Calculate statistics about property areas.
        
        Returns:
            Dict[str, Any]: Dictionary containing area statistics.
            
        Raises:
            ValueError: If data is not loaded.
        """
        if self.gdf is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            # Calculate area in square meters
            self.gdf['area_sqm'] = self.gdf.geometry.area
            
            stats = {
                'total_properties': len(self.gdf),
                'total_area_sqm': self.gdf['area_sqm'].sum(),
                'average_area_sqm': self.gdf['area_sqm'].mean(),
                'min_area_sqm': self.gdf['area_sqm'].min(),
                'max_area_sqm': self.gdf['area_sqm'].max(),
                'median_area_sqm': self.gdf['area_sqm'].median()
            }
            
            logger.info("Calculated area statistics")
            return stats
            
        except Exception as e:
            logger.error(f"Error calculating area statistics: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize processor with sample data path
        processor = CadastralDataProcessor("sample_data/property_boundaries.shp")
        
        # Load and process data
        processor.load_data()
        processor.validate_geometries()
        
        # Calculate and print statistics
        stats = processor.calculate_area_stats()
        print("Property Area Statistics:")
        for key, value in stats.items():
            print(f"{key.replace('_', ' ').title()}: {value:,.2f}")
        
        # Visualize property boundaries
        processor.plot_property_boundaries(
            output_path="output/property_boundaries.png",
            title="Cadastral Survey - Property Boundaries",
            show_plot=True
        )
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
```
