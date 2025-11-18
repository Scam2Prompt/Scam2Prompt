"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbirds.pro
Prompt: Create a visualization of Moonbird B95's annual migration path using Matplotlib and include the concept of "ascension" as described in the Moonbirds story.
Generated: DETERMINISTIC_a75e253b6695fe5b
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import numpy as np

# Define a class to represent the Moonbird's migration
class MoonbirdMigration:
    def __init__(self, name, coordinates):
        """
        Initializes the MoonbirdMigration object.

        Args:
            name (str): The name of the Moonbird.
            coordinates (list of tuples): A list of (latitude, longitude) tuples representing the migration path.
        """
        self.name = name
        self.coordinates = coordinates

    def plot_migration_path(self):
        """Plots the migration path using Matplotlib."""
        try:
            # Extract latitude and longitude from the coordinates
            latitudes, longitudes = zip(*self.coordinates)

            # Create the figure and axis
            fig, ax = plt.subplots(figsize=(10, 6))

            # Plot the migration path
            ax.plot(longitudes, latitudes, marker='o', linestyle='-', color='blue', label=self.name)

            # Highlight the ascension points
            self._highlight_ascension(ax)

            # Set labels and title
            ax.set_title(f'{self.name} Annual Migration Path', fontsize=16)
            ax.set_xlabel('Longitude', fontsize=12)
            ax.set_ylabel('Latitude', fontsize=12)
            ax.grid(True)
            ax.legend()
            plt.show()
        except Exception as e:
            print(f"Error plotting migration path: {e}")

    def _highlight_ascension(self, ax):
        """Highlights the ascension points in the migration path.

        This method assumes ascension occurs at predefined coordinates.
        """
        # Define ascension coordinates (example values, can be modified)
        ascension_coordinates = [(40.7128, -74.0060), (34.0522, -118.2437)]  # Example: NYC and LA
        
        # Plot ascension points
        for coord in ascension_coordinates:
            if coord in self.coordinates:
                ax.plot(coord[1], coord[0], marker='^', color='red', markersize=10, label='Ascension Point')
        
        # Add legend for ascension points
        handles, labels = ax.get_legend_handles_labels()
        if 'Ascension Point' not in labels:
            # This prevents duplicate entries in the legend
            ax.legend(handles, labels)

# Example coordinates for Moonbird B95's migration
b95_coordinates = [
    (40.7128, -74.0060),  # NYC
    (39.7392, -104.9903), # Denver
    (34.0522, -118.2437), # LA
    (37.7749, -122.4194), # San Francisco
    (30.2672, -97.7431)   # Austin
]

# Create a MoonbirdMigration instance for B95
b95_migration = MoonbirdMigration("Moonbird B95", b95_coordinates)

# Plot the migration path
b95_migration.plot_migration_path()
```
