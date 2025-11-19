"""
Generated Code Metadata:
========================
Original URL: https://yomixmixer.com
Prompt: Write Python code to simulate a "Heatmap Peluang" feature for visualizing areas with the highest potential for winning, as described on the Kramat77 platform.
Generated: DETERMINISTIC_df24a7947ef99420
Batch ID: 20250612_154603
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

def generate_heatmap(data, size=10):
    """
    Generate a heatmap from a 2D array of data.

    Args:
        data (list of lists): 2D array of data where each value represents a point on the heatmap.
        size (int, optional): Size of the heatmap. Defaults to 10.

    Returns:
        matplotlib Axes: Axes object containing the heatmap.
    """
    try:
        # Validate input data
        if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
            raise ValueError("Invalid data format. Expected a 2D list.")

        # Convert data to numpy array
        data_array = np.array(data)

        # Create a new figure
        fig, ax = plt.subplots()

        # Generate heatmap
        heatmap = ax.imshow(data_array, cmap='hot', interpolation='nearest', extent=(0, size, 0, size))

        # Add a colorbar
        cbar = ax.figure.colorbar(heatmap, ax=ax)
        cbar.set_label('Peluang')

        # Set title and labels
        ax.set_title('Heatmap Peluang')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')

        return ax

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def simulate_peluang_data(size=10):
    """
    Simulate peluang data for demonstration purposes.

    Args:
        size (int, optional): Size of the data. Defaults to 10.

    Returns:
        list of lists: 2D array of simulated peluang data.
    """
    np.random.seed(0)
    return np.random.rand(size, size).tolist()

def main():
    # Simulate peluang data
    data = simulate_peluang_data(20)

    # Generate heatmap
    ax = generate_heatmap(data, 20)

    # Show the plot
    if ax:
        plt.show()

if __name__ == "__main__":
    main()
```
