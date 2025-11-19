"""
Generated Code Metadata:
========================
Original URL: https://wilsonelectronics.co
Prompt: Write a Python script to simulate the coverage of a Public Safety ERRCS system in a small building, taking into account the requirements for emergency responder radio communication systems.
Generated: DETERMINISTIC_cd57d6d7133f0b72
Batch ID: 20250622_211713
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
from matplotlib.patches import Rectangle
import random
import math

class Building:
    """
    Represents a building with floors and areas to simulate ERRCS coverage.
    """
    def __init__(self, length, width, floors):
        """
        Initialize the building dimensions and floors.
        
        Args:
            length (float): Length of the building in meters.
            width (float): Width of the building in meters.
            floors (int): Number of floors in the building.
        """
        self.length = length
        self.width = width
        self.floors = floors
        self.floor_height = 3.0  # Standard floor height in meters

    def get_dimensions(self):
        """
        Returns the building dimensions.
        
        Returns:
            tuple: (length, width, floors)
        """
        return (self.length, self.width, self.floors)

class ERRCS:
    """
    Simulates the Public Safety ERRCS coverage in a building.
    """
    def __init__(self, building, antenna_locations, antenna_power=10.0, frequency=800.0):
        """
        Initialize the ERRCS system with building and antenna parameters.
        
        Args:
            building (Building): The building object.
            antenna_locations (list): List of tuples (x, y, floor) for antenna positions.
            antenna_power (float): Transmit power in watts (default: 10W).
            frequency (float): Frequency in MHz (default: 800MHz).
        """
        self.building = building
        self.antenna_locations = antenna_locations
        self.antenna_power = antenna_power
        self.frequency = frequency
        self.coverage_map = None

    def calculate_coverage(self, resolution=1.0):
        """
        Calculate the coverage map for the building.
        
        Args:
            resolution (float): Resolution in meters for coverage grid (default: 1m).
            
        Returns:
            numpy.ndarray: 3D array representing coverage strength per floor.
        """
        length, width, floors = self.building.get_dimensions()
        x_points = int(length / resolution)
        y_points = int(width / resolution)
        
        # Initialize coverage map (floors x y_points x x_points)
        self.coverage_map = np.zeros((floors, y_points, x_points))
        
        for floor in range(floors):
            for y in range(y_points):
                for x in range(x_points):
                    # Convert grid coordinates to real-world coordinates
                    real_x = x * resolution
                    real_y = y * resolution
                    
                    # Calculate signal strength from all antennas on this floor
                    total_strength = 0.0
                    for ant_x, ant_y, ant_floor in self.antenna_locations:
                        if ant_floor != floor + 1:  # Floors are 1-indexed
                            continue
                        
                        # Calculate distance to antenna
                        distance = math.sqrt((real_x - ant_x)**2 + (real_y - ant_y)**2)
                        
                        # Free-space path loss model (simplified)
                        if distance == 0:
                            strength = self.antenna_power
                        else:
                            # FSPL formula: (4πd/λ)^2
                            wavelength = 300 / self.frequency  # λ = c/f (c in m/s, f in MHz)
                            fspl = (4 * math.pi * distance / wavelength)**2
                            strength = self.antenna_power / fspl
                        
                        total_strength += strength
                    
                    self.coverage_map[floor, y, x] = total_strength
        
        return self.coverage_map

    def visualize_coverage(self, floor=1, threshold=0.01):
        """
        Visualize the coverage for a specific floor.
        
        Args:
            floor (int): Floor number to visualize (1-indexed).
            threshold (float): Minimum signal strength to consider as covered.
        """
        if self.coverage_map is None:
            raise ValueError("Coverage map not calculated. Run calculate_coverage() first.")
        
        if floor < 1 or floor > self.building.floors:
            raise ValueError(f"Floor must be between 1 and {self.building.floors}.")
        
        floor_idx = floor - 1
        coverage = self.coverage_map[floor_idx]
        
        plt.figure(figsize=(10, 8))
        
        # Plot coverage heatmap
        plt.imshow(coverage, cmap='viridis', origin='lower',
                   extent=[0, self.building.length, 0, self.building.width])
        plt.colorbar(label='Signal Strength (arbitrary units)')
        
        # Mark antenna locations on this floor
        for x, y, f in self.antenna_locations:
            if f == floor:
                plt.scatter(x, y, c='red', marker='x', s=100, label='Antenna')
        
        # Draw building outline
        plt.gca().add_patch(Rectangle((0, 0), self.building.length, self.building.width,
                                     fill=False, edgecolor='black', linewidth=2))
        
        # Threshold line
        plt.contour(coverage, levels=[threshold], colors='white', linestyles='dashed')
        
        plt.title(f'ERRCS Coverage - Floor {floor}')
        plt.xlabel('Length (m)')
        plt.ylabel('Width (m)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()

    def check_compliance(self, threshold=0.01):
        """
        Check if the coverage meets compliance requirements (95% coverage).
        
        Args:
            threshold (float): Minimum signal strength to consider as covered.
            
        Returns:
            tuple: (bool, dict) where bool is True if compliant, and dict contains floor-wise coverage percentages.
        """
        if self.coverage_map is None:
            raise ValueError("Coverage map not calculated. Run calculate_coverage() first.")
        
        compliance_results = {}
        overall_compliant = True
        
        for floor in range(1, self.building.floors + 1):
            floor_idx = floor - 1
            coverage = self.coverage_map[floor_idx]
            
            # Count points above threshold
            covered_points = np.sum(coverage >= threshold)
            total_points = coverage.size
            coverage_pct = (covered_points / total_points) * 100
            
            compliance_results[floor] = coverage_pct
            
            if coverage_pct < 95.0:
                overall_compliant = False
        
        return (overall_compliant, compliance_results)

def main():
    """Main function to demonstrate ERRCS simulation."""
    # Create a building: 50m long, 30m wide, 3 floors
    building = Building(50, 30, 3)
    
    # Define antenna locations (x, y, floor)
    antenna_locations = [
        (10, 15, 1),
        (40, 15, 1),
        (25, 5, 2),
        (25, 25, 2),
        (15, 15, 3),
        (35, 15, 3)
    ]
    
    # Create ERRCS system
    errcs = ERRCS(building, antenna_locations)
    
    # Calculate coverage
    errcs.calculate_coverage(resolution=0.5)
    
    # Visualize coverage for each floor
    for floor in range(1, building.floors + 1):
        errcs.visualize_coverage(floor=floor)
    
    # Check compliance
    compliant, results = errcs.check_compliance()
    print("\nCompliance Results:")
    for floor, pct in results.items():
        print(f"Floor {floor}: {pct:.2f}% coverage")
    
    if compliant:
        print("\nThe system meets the 95% coverage requirement on all floors.")
    else:
        print("\nWARNING: The system does NOT meet the 95% coverage requirement on all floors.")

if __name__ == "__main__":
    main()
```
