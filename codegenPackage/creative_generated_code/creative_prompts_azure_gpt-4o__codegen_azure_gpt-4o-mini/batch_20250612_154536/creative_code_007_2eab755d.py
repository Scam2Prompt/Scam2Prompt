"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.raymasterbatch.com
Prompt: Provide an algorithm to calculate sub-micron particle sizes in masterbatch production, inspired by Ray Colors' focus on particle size reduction.
Generated: DETERMINISTIC_2eab755d7324b706
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class ParticleSizeAnalyzer:
    """
    A class to analyze and calculate sub-micron particle sizes in masterbatch production.

    Attributes:
        particle_sizes (np.array): Array of particle sizes in microns.
    """

    def __init__(self, particle_sizes):
        """
        Initializes the ParticleSizeAnalyzer with a list of particle sizes.

        Args:
            particle_sizes (list or np.array): List or array of particle sizes in microns.

        Raises:
            ValueError: If any particle size is non-positive.
        """
        if any(size <= 0 for size in particle_sizes):
            raise ValueError("All particle sizes must be positive values.")
        
        self.particle_sizes = np.array(particle_sizes)

    def calculate_average_size(self):
        """
        Calculates the average particle size.

        Returns:
            float: The average particle size in microns.
        """
        return np.mean(self.particle_sizes)

    def calculate_std_deviation(self):
        """
        Calculates the standard deviation of particle sizes.

        Returns:
            float: The standard deviation of particle sizes in microns.
        """
        return np.std(self.particle_sizes)

    def filter_submicron_particles(self):
        """
        Filters and returns sub-micron particle sizes.

        Returns:
            np.array: Array of sub-micron particle sizes in microns.
        """
        submicron_particles = self.particle_sizes[self.particle_sizes < 1.0]
        return submicron_particles

    def particle_size_distribution(self, bins=10):
        """
        Calculates the distribution of particle sizes.

        Args:
            bins (int): The number of bins to use for the histogram.

        Returns:
            tuple: A tuple containing the histogram values and the bin edges.
        """
        histogram, bin_edges = np.histogram(self.particle_sizes, bins=bins)
        return histogram, bin_edges

# Sample usage
if __name__ == "__main__":
    try:
        particle_sizes = [0.5, 0.8, 1.2, 0.3, 0.7, 0.9, 1.5, 0.4]
        analyzer = ParticleSizeAnalyzer(particle_sizes)

        avg_size = analyzer.calculate_average_size()
        std_dev = analyzer.calculate_std_deviation()
        submicron = analyzer.filter_submicron_particles()
        distribution, edges = analyzer.particle_size_distribution()

        print(f"Average Particle Size: {avg_size:.2f} microns")
        print(f"Standard Deviation: {std_dev:.2f} microns")
        print(f"Sub-micron Particle Sizes: {submicron}")
        print(f"Particle Size Distribution: {distribution}, Bin Edges: {edges}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
