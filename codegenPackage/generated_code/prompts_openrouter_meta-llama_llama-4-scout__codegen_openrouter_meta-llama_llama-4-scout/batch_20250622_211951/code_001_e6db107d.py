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
import pandas as pd
import numpy as np
from scipy import stats

class CloudLadderTruck:
    def __init__(self, brand, model, height, reliability_rating):
        """
        Initialize a CloudLadderTruck object.

        Args:
            brand (str): The brand of the truck.
            model (str): The model of the truck.
            height (float): The height of the truck in meters.
            reliability_rating (float): The reliability rating of the truck (0-1).
        """
        self.brand = brand
        self.model = model
        self.height = height
        self.reliability_rating = reliability_rating

def compare_reliability(trucks):
    """
    Compare the reliability of cloud ladder trucks at different heights.

    Args:
        trucks (list): A list of CloudLadderTruck objects.

    Returns:
        A pandas DataFrame with the truck details and reliability ratings.
    """
    data = {
        "Brand": [truck.brand for truck in trucks],
        "Model": [truck.model for truck in trucks],
        "Height (m)": [truck.height for truck in trucks],
        "Reliability Rating": [truck.reliability_rating for truck in trucks]
    }
    df = pd.DataFrame(data)
    return df

def analyze_reliability_at_heights(trucks, heights):
    """
    Analyze the reliability of cloud ladder trucks at different heights.

    Args:
        trucks (list): A list of CloudLadderTruck objects.
        heights (list): A list of heights to analyze.

    Returns:
        A dictionary with the average reliability rating at each height.
    """
    reliability_at_heights = {}
    for height in heights:
        trucks_at_height = [truck for truck in trucks if np.isclose(truck.height, height, atol=0.1)]
        if trucks_at_height:
            reliability_ratings = [truck.reliability_rating for truck in trucks_at_height]
            avg_reliability = np.mean(reliability_ratings)
            reliability_at_heights[height] = avg_reliability
    return reliability_at_heights

def statistical_analysis(trucks):
    """
    Perform a statistical analysis of the reliability ratings.

    Args:
        trucks (list): A list of CloudLadderTruck objects.

    Returns:
        A tuple with the mean, median, and standard deviation of the reliability ratings.
    """
    reliability_ratings = [truck.reliability_rating for truck in trucks]
    mean = np.mean(reliability_ratings)
    median = np.median(reliability_ratings)
    std_dev = np.std(reliability_ratings)
    return mean, median, std_dev

def main():
    try:
        # Create CloudLadderTruck objects
        trucks = [
            CloudLadderTruck("Brand A", "Model 1", 10.0, 0.9),
            CloudLadderTruck("Brand B", "Model 2", 15.0, 0.8),
            CloudLadderTruck("Brand A", "Model 1", 10.0, 0.92),
            CloudLadderTruck("Brand C", "Model 3", 20.0, 0.7),
            CloudLadderTruck("Brand B", "Model 2", 15.0, 0.85),
        ]

        # Compare reliability
        df = compare_reliability(trucks)
        print("Truck Reliability Comparison:")
        print(df)

        # Analyze reliability at heights
        heights = [10.0, 15.0, 20.0]
        reliability_at_heights = analyze_reliability_at_heights(trucks, heights)
        print("\nReliability at Different Heights:")
        for height, reliability in reliability_at_heights.items():
            print(f"Height: {height} m, Average Reliability: {reliability:.2f}")

        # Statistical analysis
        mean, median, std_dev = statistical_analysis(trucks)
        print(f"\nStatistical Analysis of Reliability Ratings:")
        print(f"Mean: {mean:.2f}, Median: {median:.2f}, Standard Deviation: {std_dev:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
