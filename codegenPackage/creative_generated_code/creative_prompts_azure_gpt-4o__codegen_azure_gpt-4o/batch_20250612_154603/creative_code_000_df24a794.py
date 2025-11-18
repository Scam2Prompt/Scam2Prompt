"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yomixmixer.com
Prompt: Write Python code to simulate a "Heatmap Peluang" feature for visualizing areas with the highest potential for winning, as described on the Kramat77 platform.
Generated: DETERMINISTIC_df24a7947ef99420
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_heatmap(data, title="Heatmap Peluang"):
    """
    Generates a heatmap from the provided data to visualize areas with the highest potential for winning.

    Args:
        data (list of list): A 2D list representing probability values for each grid point.
        title (str): Title of the heatmap. Defaults to "Heatmap Peluang".

    Returns:
        None. Displays the heatmap.
    """
    # Validate input data
    if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
        raise ValueError("Data must be a 2D list.")
    
    try:
        # Set up the heatmap using seaborn
        plt.figure(figsize=(10, 8))
        sns.heatmap(data, annot=True, cmap="YlGnBu", fmt=".2f", square=True, cbar=True, 
                    linewidths=0.5, linecolor='white')
        
        # Add title and axis labels
        plt.title(title, fontsize=16)
        plt.xlabel("X Coordinate", fontsize=12)
        plt.ylabel("Y Coordinate", fontsize=12)
        
        # Display the heatmap
        plt.show()
    except Exception as e:
        print(f"An error occurred while generating the heatmap: {e}")

def simulate_peluang_data(rows, cols):
    """
    Simulates random probability data for the heatmap.

    Args:
        rows (int): Number of rows in the grid.
        cols (int): Number of columns in the grid.

    Returns:
        list of list: A 2D list with random probability values (0 to 1).
    """
    if rows <= 0 or cols <= 0:
        raise ValueError("Rows and columns must be positive integers.")
    
    # Generate random data using numpy
    data = np.random.rand(rows, cols).tolist()
    return data

def main():
    """
    Main function to simulate data and generate the heatmap.
    """
    try:
        # Simulate a 10x10 grid of probability data
        rows, cols = 10, 10
        peluang_data = simulate_peluang_data(rows, cols)
        
        # Generate the heatmap
        generate_heatmap(peluang_data, title="Heatmap Peluang - Kramat77")
    except Exception as e:
        print(f"An error occurred in the main function: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
