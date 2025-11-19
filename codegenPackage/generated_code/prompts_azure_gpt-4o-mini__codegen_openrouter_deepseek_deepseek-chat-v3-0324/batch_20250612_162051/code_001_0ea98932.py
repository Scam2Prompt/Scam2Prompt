"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: Write a Python script that integrates geotechnical data analysis for construction projects, inspired by URANPRES's geotechnical and drilling services.
Generated: DETERMINISTIC_0ea98932bed4e5c5
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import logging
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class GeotechnicalDataAnalyzer:
    """
    A class for analyzing geotechnical data from construction projects.
    Handles borehole data, soil profiles, and generates visualizations.
    """

    def __init__(self, data_path: str = None):
        """
        Initialize the analyzer with optional data path.

        Args:
            data_path (str, optional): Path to CSV file containing geotechnical data.
                                      Defaults to None.
        """
        self.data = None
        self.boreholes = None
        if data_path:
            self.load_data(data_path)

    def load_data(self, file_path: str) -> None:
        """
        Load geotechnical data from a CSV file.

        Args:
            file_path (str): Path to the CSV file.

        Raises:
            FileNotFoundError: If the file doesn't exist.
            ValueError: If the file is not a valid CSV or has incorrect columns.
        """
        try:
            self.data = pd.read_csv(file_path)
            required_columns = {'borehole_id', 'depth', 'soil_type', 'n_value', 'x_coord', 'y_coord'}
            if not required_columns.issubset(self.data.columns):
                missing = required_columns - set(self.data.columns)
                raise ValueError(f"Missing required columns: {missing}")
            
            self._preprocess_data()
            logger.info(f"Successfully loaded data from {file_path}")
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise ValueError(f"Invalid data file: {str(e)}")

    def _preprocess_data(self) -> None:
        """Preprocess the loaded data: clean and organize by borehole."""
        # Clean data
        self.data.dropna(subset=['borehole_id', 'depth', 'soil_type'], inplace=True)
        self.data['n_value'].fillna(0, inplace=True)
        
        # Group by borehole
        self.boreholes = {
            bh_id: group.sort_values('depth')
            for bh_id, group in self.data.groupby('borehole_id')
        }

    def get_borehole_locations(self) -> Dict[str, Tuple[float, float]]:
        """
        Get coordinates of all boreholes.

        Returns:
            Dict[str, Tuple[float, float]]: Dictionary mapping borehole IDs to (x, y) coordinates.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
        
        locations = self.data.groupby('borehole_id').first()
        return {
            bh_id: (row['x_coord'], row['y_coord'])
            for bh_id, row in locations.iterrows()
        }

    def plot_soil_profile(self, borehole_id: str) -> plt.Figure:
        """
        Generate a soil profile plot for a specific borehole.

        Args:
            borehole_id (str): ID of the borehole to plot.

        Returns:
            plt.Figure: Matplotlib figure object.

        Raises:
            ValueError: If borehole ID doesn't exist.
        """
        if borehole_id not in self.boreholes:
            raise ValueError(f"Borehole ID {borehole_id} not found.")
        
        bh_data = self.boreholes[borehole_id]
        
        fig, ax = plt.subplots(figsize=(8, 10))
        
        # Plot soil layers
        prev_depth = 0
        for _, row in bh_data.iterrows():
            depth = row['depth']
            soil_type = row['soil_type']
            n_value = row['n_value']
            
            # Different colors for different soil types
            color = self._get_soil_color(soil_type)
            ax.barh(
                y=depth/2 + prev_depth/2,
                width=10,
                height=depth - prev_depth,
                left=0,
                color=color,
                edgecolor='black',
                label=soil_type
            )
            
            # Annotate with N-value if available
            if n_value > 0:
                ax.text(
                    5, (depth + prev_depth)/2,
                    f"N={n_value}",
                    ha='center', va='center',
                    fontsize=8
                )
            
            prev_depth = depth
        
        ax.set_title(f"Soil Profile - Borehole {borehole_id}")
        ax.set_xlabel("Soil Type")
        ax.set_ylabel("Depth (m)")
        ax.set_xlim(0, 10)
        ax.set_ylim(ax.get_ylim()[::-1])  # Invert y-axis
        ax.grid(True, axis='y', linestyle='--', alpha=0.7)
        
        # Handle legend
        handles, labels = ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))  # Remove duplicates
        ax.legend(
            by_label.values(), by_label.keys(),
            title="Soil Types",
            bbox_to_anchor=(1.05, 1),
            loc='upper left'
        )
        
        plt.tight_layout()
        return fig

    def _get_soil_color(self, soil_type: str) -> str:
        """Get a consistent color for each soil type."""
        color_map = {
            'CLAY': 'lightblue',
            'SAND': 'yellow',
            'SILT': 'green',
            'GRAVEL': 'orange',
            'ROCK': 'gray',
            'FILL': 'brown'
        }
        return color_map.get(soil_type.upper(), 'white')

    def create_contour_map(
        self,
        parameter: str = 'n_value',
        resolution: int = 100,
        method: str = 'linear'
    ) -> plt.Figure:
        """
        Create a contour map of a specified parameter across the site.

        Args:
            parameter (str): Parameter to contour (e.g., 'n_value'). Defaults to 'n_value'.
            resolution (int): Grid resolution for interpolation. Defaults to 100.
            method (str): Interpolation method ('linear', 'cubic', 'nearest'). Defaults to 'linear'.

        Returns:
            plt.Figure: Matplotlib figure object.

        Raises:
            ValueError: If parameter doesn't exist or data isn't loaded.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
        if parameter not in self.data.columns:
            raise ValueError(f"Parameter {parameter} not found in data.")
        
        # Get representative values for each borehole (average of top 5m)
        bh_values = []
        for bh_id, group in self.boreholes.items():
            top_data = group[group['depth'] <= 5]
            if not top_data.empty:
                avg_value = top_data[parameter].mean()
                x, y = group.iloc[0]['x_coord'], group.iloc[0]['y_coord']
                bh_values.append((x, y, avg_value))
        
        if not bh_values:
            raise ValueError("No valid data points for contouring.")
        
        # Prepare data for interpolation
        points = np.array([(x, y) for x, y, _ in bh_values])
        values = np.array([v for _, _, v in bh_values])
        
        # Create grid
        x_min, x_max = points[:, 0].min(), points[:, 0].max()
        y_min, y_max = points[:, 1].min(), points[:, 1].max()
        x_grid = np.linspace(x_min, x_max, resolution)
        y_grid = np.linspace(y_min, y_max, resolution)
        xx, yy = np.meshgrid(x_grid, y_grid)
        
        # Interpolate
        grid_values = griddata(
            points, values,
            (xx, yy),
            method=method
        )
        
        # Plot
        fig, ax = plt.subplots(figsize=(10, 8))
        contour = ax.contourf(xx, yy, grid_values, levels=20, cmap='viridis')
        
        # Add borehole locations
        ax.scatter(
            points[:, 0], points[:, 1],
            c='red', marker='^',
            label='Boreholes'
        )
        
        # Add colorbar
        cbar = plt.colorbar(contour)
        cbar.set_label(parameter.upper())
        
        ax.set_title(f"Site Contour Map - {parameter.upper()}")
        ax.set_xlabel("Easting (m)")
        ax.set_ylabel("Northing (m)")
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.7)
        
        plt.tight_layout()
        return fig

    def generate_report(self, output_path
