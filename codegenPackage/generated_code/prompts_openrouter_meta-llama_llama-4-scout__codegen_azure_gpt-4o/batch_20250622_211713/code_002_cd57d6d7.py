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

# Constants
BUILDING_WIDTH = 50  # Width of the building in meters
BUILDING_HEIGHT = 50  # Height of the building in meters
TRANSMITTER_POWER = 10  # Transmitter power in dBm
FREQUENCY = 800  # Frequency in MHz (typical for ERRCS systems)
PATH_LOSS_EXPONENT = 3.5  # Path loss exponent (depends on building materials)
MIN_SIGNAL_THRESHOLD = -95  # Minimum signal strength in dBm for coverage

# Function to calculate path loss using the Log-Distance Path Loss Model
def calculate_path_loss(distance, frequency, path_loss_exponent):
    """
    Calculate path loss based on the log-distance path loss model.

    Parameters:
        distance (float): Distance from the transmitter in meters.
        frequency (float): Frequency in MHz.
        path_loss_exponent (float): Path loss exponent.

    Returns:
        float: Path loss in dB.
    """
    if distance == 0:
        return 0  # No path loss at zero distance
    # Free-space path loss formula
    path_loss = 20 * np.log10(distance) + 20 * np.log10(frequency) + 20 * np.log10(4 * np.pi / 3e8)
    # Adjust for path loss exponent
    return path_loss * path_loss_exponent / 2

# Function to calculate signal strength at a given point
def calculate_signal_strength(tx_power, distance, frequency, path_loss_exponent):
    """
    Calculate signal strength at a given point.

    Parameters:
        tx_power (float): Transmitter power in dBm.
        distance (float): Distance from the transmitter in meters.
        frequency (float): Frequency in MHz.
        path_loss_exponent (float): Path loss exponent.

    Returns:
        float: Signal strength in dBm.
    """
    path_loss = calculate_path_loss(distance, frequency, path_loss_exponent)
    return tx_power - path_loss

# Simulate building coverage
def simulate_coverage(building_width, building_height, tx_power, frequency, path_loss_exponent, min_signal_threshold):
    """
    Simulate the coverage of a Public Safety ERRCS system in a building.

    Parameters:
        building_width (int): Width of the building in meters.
        building_height (int): Height of the building in meters.
        tx_power (float): Transmitter power in dBm.
        frequency (float): Frequency in MHz.
        path_loss_exponent (float): Path loss exponent.
        min_signal_threshold (float): Minimum signal strength in dBm for coverage.

    Returns:
        np.ndarray: 2D array representing signal strength at each point in the building.
    """
    # Create a grid representing the building
    x = np.linspace(0, building_width, building_width)
    y = np.linspace(0, building_height, building_height)
    signal_strength_grid = np.zeros((building_width, building_height))

    # Assume transmitter is at the center of the building
    tx_x, tx_y = building_width / 2, building_height / 2

    # Calculate signal strength at each point in the building
    for i in range(building_width):
        for j in range(building_height):
            distance = np.sqrt((tx_x - x[i])**2 + (tx_y - y[j])**2)
            signal_strength = calculate_signal_strength(tx_power, distance, frequency, path_loss_exponent)
            signal_strength_grid[i, j] = signal_strength

    return signal_strength_grid

# Plot coverage map
def plot_coverage(signal_strength_grid, min_signal_threshold):
    """
    Plot the coverage map of the building.

    Parameters:
        signal_strength_grid (np.ndarray): 2D array representing signal strength at each point in the building.
        min_signal_threshold (float): Minimum signal strength in dBm for coverage.
    """
    plt.figure(figsize=(10, 8))
    plt.imshow(signal_strength_grid, extent=(0, BUILDING_WIDTH, 0, BUILDING_HEIGHT), origin='lower', cmap='coolwarm')
    plt.colorbar(label='Signal Strength (dBm)')
    plt.contour(signal_strength_grid, levels=[min_signal_threshold], colors='black', linestyles='dashed', linewidths=1)
    plt.title('ERRCS Coverage Map')
    plt.xlabel('Width (m)')
    plt.ylabel('Height (m)')
    plt.show()

# Main function
def main():
    """
    Main function to simulate and plot the ERRCS coverage in a building.
    """
    try:
        # Simulate coverage
        signal_strength_grid = simulate_coverage(
            BUILDING_WIDTH, BUILDING_HEIGHT, TRANSMITTER_POWER, FREQUENCY, PATH_LOSS_EXPONENT, MIN_SIGNAL_THRESHOLD
        )

        # Plot coverage map
        plot_coverage(signal_strength_grid, MIN_SIGNAL_THRESHOLD)
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
