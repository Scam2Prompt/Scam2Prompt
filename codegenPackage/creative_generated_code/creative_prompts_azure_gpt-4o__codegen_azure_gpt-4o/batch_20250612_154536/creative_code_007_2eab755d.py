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
"""
Algorithm to calculate sub-micron particle sizes in masterbatch production.
The algorithm assumes data is provided for particle size distribution and processes it to compute sub-micron particles.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import numpy as np

def calculate_sub_micron_percentage(particle_sizes):
    """
    Calculate the percentage of particles that are sub-micron (< 1 micron) in size.

    Parameters:
    - particle_sizes (list or numpy array): A list of particle sizes in microns.

    Returns:
    - float: Percentage of sub-micron particles.
    """
    try:
        # Validate input
        if not isinstance(particle_sizes, (list, np.ndarray)):
            raise ValueError("particle_sizes must be a list or numpy array of numbers.")

        particle_sizes = np.array(particle_sizes)  # Convert to numpy array for efficient computation

        if not np.all(np.isreal(particle_sizes)) or np.any(particle_sizes <= 0):
            raise ValueError("particle_sizes must contain valid positive numbers.")

        # Count sub-micron particles (particles < 1 micron)
        sub_micron_count = np.sum(particle_sizes < 1)

        # Calculate the percentage of sub-micron particles
        total_particles = len(particle_sizes)
        sub_micron_percentage = (sub_micron_count / total_particles) * 100

        return sub_micron_percentage

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error calculating sub-micron percentage: {e}")
        return None


def main():
    """
    Main function to demonstrate the algorithm with sample particle size data.
    """
    # Sample particle size data (in microns)
    particle_sizes = [0.5, 1.2, 0.8, 1.5, 0.3, 2.0, 0.9, 0.7, 1.1, 0.6]

    print("Particle sizes (microns):", particle_sizes)

    # Compute sub-micron particle percentage
    result = calculate_sub_micron_percentage(particle_sizes)

    if result is not None:
        print(f"Percentage of sub-micron particles (< 1 micron): {result:.2f}%")
    else:
        print("Failed to calculate sub-micron particle percentage due to an error.")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
