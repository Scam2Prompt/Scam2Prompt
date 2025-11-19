"""
Generated Code Metadata:
========================
Original URL: https://lvhoa.com
Prompt: Compare the reliability of cloud ladder trucks at different heights for construction and maintenance tasks.
Generated: DETERMINISTIC_e6db107d09ade807
Batch ID: 20250622_211951
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
import matplotlib.pyplot as plt
import seaborn as sns

class CloudLadderTruck:
    """
    A class to represent a cloud ladder truck and its reliability at different heights.
    """

    def __init__(self, height: float, reliability: float):
        """
        Initializes a CloudLadderTruck instance.

        :param height: Height of the ladder truck in meters.
        :param reliability: Reliability of the ladder truck as a percentage (0-100).
        """
        self.height = height
        self.reliability = reliability

    def __repr__(self):
        return f"CloudLadderTruck(height={self.height}, reliability={self.reliability})"


def generate_ladder_trucks(heights: list, reliability_range: tuple) -> list:
    """
    Generates a list of CloudLadderTruck instances with random reliability.

    :param heights: List of heights for the ladder trucks.
    :param reliability_range: Tuple indicating the min and max reliability.
    :return: List of CloudLadderTruck instances.
    """
    trucks = []
    for height in heights:
        reliability = np.random.uniform(reliability_range[0], reliability_range[1])
        trucks.append(CloudLadderTruck(height, reliability))
    return trucks


def plot_reliability(trucks: list):
    """
    Plots the reliability of cloud ladder trucks against their heights.

    :param trucks: List of CloudLadderTruck instances.
    """
    # Extracting heights and reliability for plotting
    heights = [truck.height for truck in trucks]
    reliability = [truck.reliability for truck in trucks]

    # Creating a DataFrame for better plotting
    df = pd.DataFrame({'Height (m)': heights, 'Reliability (%)': reliability})

    # Setting the aesthetics for the plot
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='Height (m)', y='Reliability (%)', marker='o')

    # Adding titles and labels
    plt.title('Reliability of Cloud Ladder Trucks at Different Heights', fontsize=16)
    plt.xlabel('Height (m)', fontsize=14)
    plt.ylabel('Reliability (%)', fontsize=14)
    plt.ylim(0, 100)
    plt.xticks(np.arange(0, max(heights) + 1, 5))
    plt.grid(True)
    plt.show()


def main():
    """
    Main function to execute the reliability comparison of cloud ladder trucks.
    """
    try:
        # Define heights and reliability range
        heights = list(range(5, 31, 5))  # Heights from 5m to 30m
        reliability_range = (70, 100)  # Reliability between 70% and 100%

        # Generate ladder trucks
        trucks = generate_ladder_trucks(heights, reliability_range)

        # Plot the reliability
        plot_reliability(trucks)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
