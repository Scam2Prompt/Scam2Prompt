"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: Write Python code to simulate geotechnical tasks using numerical modeling techniques, specifically for evaluating the influence of new construction on surrounding structures, as described by the services of the Научно-образовательный центр «Геотехника».
Generated: DETERMINISTIC_7c856cb749a853d0
Batch ID: 20250612_151752
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
from scipy.interpolate import griddata
from scipy.spatial import Delaunay

class GeotechnicalSimulation:
    """
    A class to simulate geotechnical tasks using numerical modeling techniques.
    Specifically evaluates the influence of new construction on surrounding structures.
    """
    
    def __init__(self, grid_size=(100, 100), young_modulus=1e6, poisson_ratio=0.3):
        """
        Initialize the simulation with grid size and material properties.
        
        Args:
            grid_size (tuple): Dimensions of the simulation grid (x, y)
            young_modulus (float): Young's modulus of the soil (Pa)
            poisson_ratio (float): Poisson's ratio of the soil
        """
        self.grid_size = grid_size
        self.young_modulus = young_modulus
        self.poisson_ratio = poisson_ratio
        self.grid_x, self.grid_y = np.meshgrid(
            np.linspace(0, 1, grid_size[0]),
            np.linspace(0, 1, grid_size[1])
        )
        self.displacements = None
        self.stresses = None
        self.strains = None
        
    def apply_load(self, load_points, load_values):
        """
        Apply loads to specific points in the grid.
        
        Args:
            load_points (np.array): Array of (x,y) coordinates where loads are applied
            load_values (np.array): Array of load values at each point
        """
        try:
            if len(load_points) != len(load_values):
                raise ValueError("Number of load points and values must match")
                
            # Interpolate loads onto the grid
            self.load_grid = griddata(
                load_points,
                load_values,
                (self.grid_x, self.grid_y),
                method='linear',
                fill_value=0
            )
            
        except Exception as e:
            print(f"Error applying loads: {str(e)}")
            raise
            
    def calculate_displacements(self):
        """
        Calculate displacements using simplified elastic solution.
        """
        try:
            # Simplified elastic solution (for demonstration)
            # In practice, this would use FEM or other numerical methods
            self.displacements = np.zeros_like(self.grid_x)
            
            # Calculate influence of each load point
            for i in range(self.grid_size[0]):
                for j in range(self.grid_size[1]):
                    if self.load_grid[i,j] > 0:
                        # Simplified displacement calculation
                        r = np.sqrt((self.grid_x - self.grid_x[i,j])**2 + 
                                   (self.grid_y - self.grid_y[i,j])**2)
                        mask = r > 0
                        self.displacements[mask] += (self.load_grid[i,j] * 
                                                    np.log(r[mask]) / 
                                                    (2 * np.pi * self.young_modulus))
            
        except Exception as e:
            print(f"Error calculating displacements: {str(e)}")
            raise
            
    def calculate_stresses(self):
        """
        Calculate stresses from displacements.
        """
        try:
            if self.displacements is None:
                raise ValueError("Displacements must be calculated first")
                
            # Simplified stress calculation (for demonstration)
            # In practice, this would use proper constitutive relationships
            grad_x, grad_y = np.gradient(self.displacements)
            self.stresses = {
                'xx': self.young_modulus * grad_x,
                'yy': self.young_modulus * grad_y,
                'xy': 0.5 * self.young_modulus * (grad_x + grad_y)
            }
            
        except Exception as e:
            print(f"Error calculating stresses: {str(e)}")
            raise
            
    def calculate_strains(self):
        """
        Calculate strains from displacements.
        """
        try:
            if self.displacements is None:
                raise ValueError("Displacements must be calculated first")
                
            # Simplified strain calculation
            grad_x, grad_y = np.gradient(self.displacements)
            self.strains = {
                'xx': grad_x,
                'yy': grad_y,
                'xy': 0.5 * (grad_x + grad_y)
            }
            
        except Exception as e:
            print(f"Error calculating strains: {str(e)}")
            raise
            
    def plot_results(self, field='displacements'):
        """
        Plot simulation results.
        
        Args:
            field (str): Field to plot ('displacements', 'stresses', or 'strains')
        """
        try:
            plt.figure(figsize=(10, 8))
            
            if field == 'displacements' and self.displacements is not None:
                plt.contourf(self.grid_x, self.grid_y, self.displacements, levels=20)
                plt.title('Displacement Field')
                plt.colorbar(label='Displacement (m)')
                
            elif field == 'stresses' and self.stresses is not None:
                plt.contourf(self.grid_x, self.grid_y, self.stresses['xx'], levels=20)
                plt.title('Stress Field (xx component)')
                plt.colorbar(label='Stress (Pa)')
                
            elif field == 'strains' and self.strains is not None:
                plt.contourf(self.grid_x, self.grid_y, self.strains['xx'], levels=20)
                plt.title('Strain Field (xx component)')
                plt.colorbar(label='Strain')
                
            else:
                raise ValueError(f"Invalid field or field not calculated: {field}")
                
            plt.xlabel('X position')
            plt.ylabel('Y position')
            plt.grid(True)
            plt.show()
            
        except Exception as e:
            print(f"Error plotting results: {str(e)}")
            raise
            
    def evaluate_influence(self, structure_points):
        """
        Evaluate influence on specific structure points.
        
        Args:
            structure_points (np.array): Array of (x,y) coordinates of structure points
            
        Returns:
            dict: Dictionary containing displacements, stresses, and strains at structure points
        """
        try:
            if self.displacements is None:
                raise ValueError("Simulation must be run first")
                
            # Interpolate results at structure points
            results = {}
            points = np.column_stack((self.grid_x.flatten(), self.grid_y.flatten()))
            
            results['displacements'] = griddata(
                points,
                self.displacements.flatten(),
                structure_points,
                method='linear'
            )
            
            if self.stresses is not None:
                results['stresses_xx'] = griddata(
                    points,
                    self.stresses['xx'].flatten(),
                    structure_points,
                    method='linear'
                )
                
            if self.strains is not None:
                results['strains_xx'] = griddata(
                    points,
                    self.strains['xx'].flatten(),
                    structure_points,
                    method='linear'
                )
                
            return results
            
        except Exception as e:
            print(f"Error evaluating influence: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Create simulation
        sim = GeotechnicalSimulation(grid_size=(50, 50))
        
        # Define load points (simulating new construction)
        load_points = np.array([[0.5, 0.5], [0.6, 0.5], [0.5, 0.6], [0.6, 0.6]])
        load_values = np.array([1e5, 1e5, 1e5, 1e5])  # 100 kPa at each point
        
        # Apply loads
        sim.apply_load(load_points, load_values)
        
        # Run simulations
        sim.calculate_displacements()
        sim.calculate_stresses()
        sim.calculate_strains()
        
        # Plot results
        sim.plot_results('displacements')
        sim.plot_results('stresses')
        
        # Evaluate influence on surrounding structure
        structure_points = np.array([[0.3, 0.3], [0.7, 0.3], [0.3, 0.7], [0.7, 0.7]])
        influence = sim.evaluate_influence(structure_points)
        print("Influence on structure points:", influence)
        
    except Exception as e:
        print(f"Simulation error: {str(e)}")
```
