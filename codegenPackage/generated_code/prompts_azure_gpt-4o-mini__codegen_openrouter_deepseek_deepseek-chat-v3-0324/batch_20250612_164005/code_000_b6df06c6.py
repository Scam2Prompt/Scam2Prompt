"""
Generated Code Metadata:
========================
Original URL: https://wilsonelectronics.co
Prompt: Generate code to assess cellular signal coverage using a Distributed Antenna System (DAS) for a large building.
Generated: DETERMINISTIC_b6df06c6f358a771
Batch ID: 20250612_164005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from typing import Tuple, List, Dict, Optional

class DASCoverageAnalyzer:
    """
    A class to analyze cellular signal coverage in a building using Distributed Antenna System (DAS).
    It processes signal measurements, interpolates coverage, and generates visualizations.
    """

    def __init__(self, measurement_points: pd.DataFrame):
        """
        Initialize the analyzer with measurement data.
        
        Args:
            measurement_points: DataFrame containing columns 'x', 'y', 'z' (coordinates), 
                               and 'signal_strength' (in dBm).
        """
        self.measurement_points = measurement_points
        self.coverage_grid = None
        self.grid_resolution = 1.0  # Default grid resolution in meters

    def validate_measurements(self) -> bool:
        """
        Validates the measurement data for required columns and non-NaN values.
        
        Returns:
            bool: True if data is valid, raises ValueError otherwise.
        """
        required_columns = {'x', 'y', 'z', 'signal_strength'}
        if not required_columns.issubset(self.measurement_points.columns):
            raise ValueError(f"Missing required columns. Expected: {required_columns}")
        
        if self.measurement_points.isna().any().any():
            raise ValueError("Measurement data contains NaN values.")
            
        return True

    def interpolate_coverage(self, resolution: Optional[float] = None) -> None:
        """
        Interpolates signal coverage over a 3D grid using nearest-neighbor interpolation.
        
        Args:
            resolution: Grid spacing in meters. Uses instance default if None.
        """
        if resolution is not None:
            self.grid_resolution = resolution
            
        self.validate_measurements()
        
        # Extract coordinates and signal strengths
        points = self.measurement_points[['x', 'y', 'z']].values
        values = self.measurement_points['signal_strength'].values
        
        # Create grid for interpolation
        x_min, y_min, z_min = points.min(axis=0)
        x_max, y_max, z_max = points.max(axis=0)
        
        x_grid = np.arange(x_min, x_max + self.grid_resolution, self.grid_resolution)
        y_grid = np.arange(y_min, y_max + self.grid_resolution, self.grid_resolution)
        z_grid = np.arange(z_min, z_max + self.grid_resolution, self.grid_resolution)
        
        xx, yy, zz = np.meshgrid(x_grid, y_grid, z_grid, indexing='ij')
        
        # Perform interpolation
        self.coverage_grid = griddata(
            points, 
            values, 
            (xx, yy, zz), 
            method='nearest'
        )

    def get_coverage_stats(self) -> Dict[str, float]:
        """
        Calculates basic statistics for the interpolated coverage.
        
        Returns:
            Dict: Contains 'min', 'max', 'mean', 'median' signal strengths in dBm,
                  or empty dict if no interpolation.
        """
        if self.coverage_grid is None:
            return {}
            
        return {
            'min': np.nanmin(self.coverage_grid),
            'max': np.nanmax(self.coverage_grid),
            'mean': np.nanmean(self.coverage_grid),
            'median': np.nanmedian(self.coverage_grid)
        }

    def visualize_floor_coverage(self, floor_z: float, threshold: float = -85.0) -> plt.Figure:
        """
        Generates a 2D coverage map for a specific building floor.
        
        Args:
            floor_z: Z-coordinate of the floor to visualize.
            threshold: Signal strength threshold for coverage (dBm).
            
        Returns:
            plt.Figure: Matplotlib figure showing floor coverage.
        """
        if self.coverage_grid is None:
            raise ValueError("No coverage data available. Run interpolate_coverage() first.")
            
        # Find closest Z-index
        z_grid = np.arange(
            self.measurement_points['z'].min(),
            self.measurement_points['z'].max() + self.grid_resolution,
            self.grid_resolution
        )
        z_idx = np.argmin(np.abs(z_grid - floor_z))
        
        # Create figure
        fig, ax = plt.subplots(figsize=(10, 8))
        coverage_slice = self.coverage_grid[:, :, z_idx]
        
        # Plot coverage
        im = ax.imshow(
            coverage_slice.T, 
            extent=[
                self.measurement_points['x'].min(),
                self.measurement_points['x'].max(),
                self.measurement_points['y'].min(),
                self.measurement_points['y'].max()
            ],
            origin='lower',
            cmap='RdYlGn',
            vmin=-120,
            vmax=-50
        )
        
        # Add threshold contour
        ax.contour(
            coverage_slice.T, 
            levels=[threshold],
            colors=['black'],
            linestyles='dashed',
            extent=[
                self.measurement_points['x'].min(),
                self.measurement_points['x'].max(),
                self.measurement_points['y'].min(),
                self.measurement_points['y'].max()
            ]
        )
        
        # Formatting
        ax.set_title(f'Coverage at Z={floor_z:.1f}m')
        ax.set_xlabel('X Position (m)')
        ax.set_ylabel('Y Position (m)')
        plt.colorbar(im, label='Signal Strength (dBm)')
        
        return fig

    def save_coverage_report(self, filename: str) -> None:
        """
        Saves coverage statistics and visualizations to a file.
        
        Args:
            filename: Output file path (should end with .html).
        """
        if not filename.endswith('.html'):
            raise ValueError("Filename must end with .html")
            
        stats = self.get_coverage_stats()
        visualizations = []
        
        # Generate visualizations for each unique floor
        unique_floors = np.unique(np.round(self.measurement_points['z'], 1))
        for floor_z in unique_floors:
            fig = self.visualize_floor_coverage(floor_z)
            fig.savefig(f"temp_floor_{floor_z}.png")
            plt.close(fig)
            visualizations.append((floor_z, f"temp_floor_{floor_z}.png"))
        
        # Create HTML report
        html_content = f"""
        <html>
            <head>
                <title>DAS Coverage Report</title>
            </head>
            <body>
                <h1>DAS Coverage Report</h1>
                <h2>Statistics</h2>
                <ul>
                    <li>Min Signal: {stats['min']:.1f} dBm</li>
                    <li>Max Signal: {stats['max']:.1f} dBm</li>
                    <li>Mean Signal: {stats['mean']:.1f} dBm</li>
                    <li>Median Signal: {stats['median']:.1f} dBm</li>
                </ul>
                <h2>Floor Coverage</h2>
        """
        
        for floor_z, img_path in visualizations:
            html_content += f"""
                <h3>Floor Z={floor_z:.1f}m</h3>
                <img src="{img_path}" width="800">
            """
        
        html_content += """
            </body>
        </html>
        """
        
        with open(filename, 'w') as f:
            f.write(html_content)

# Example usage
if __name__ == "__main__":
    # Sample data generation
    np.random.seed(42)
    measurements = pd.DataFrame({
        'x': np.random.uniform(0, 100, 200),
        'y': np.random.uniform(0, 50, 200),
        'z': np.random.choice([0.0, 3.0, 6.0], 200),
        'signal_strength': np.random.uniform(-100, -60, 200)
    })
    
    analyzer = DASCoverageAnalyzer(measurements)
    analyzer.interpolate_coverage(resolution=2.0)
    
    # Generate and save report
    analyzer.save_coverage_report("das_coverage_report.html")
```
