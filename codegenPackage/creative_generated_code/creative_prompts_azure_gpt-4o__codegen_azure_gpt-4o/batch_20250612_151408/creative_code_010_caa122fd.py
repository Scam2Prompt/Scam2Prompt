"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Recommend libraries or APIs for visualizing Engel cooler temperature retention data, and write code to generate graphs comparing different cooler models.
Generated: DETERMINISTIC_caa122fd63c3696f
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Function to visualize Engel cooler temperature retention data
def visualize_cooler_data(cooler_data):
    """
    Generates comparison graphs for temperature retention data of different cooler models.

    Args:
        cooler_data (dict): Dictionary containing cooler names as keys and their temperature retention data as values.
                            Each value should be a list of temperatures recorded over time.
                            Example:
                            {
                                "Cooler A": [5, 4, 4, 3, 3],
                                "Cooler B": [6, 5, 5, 4, 4],
                                "Cooler C": [7, 6, 5, 4, 3]
                            }
    """
    try:
        # Validate input
        if not isinstance(cooler_data, dict):
            raise ValueError("cooler_data must be a dictionary with cooler names and their temperature retention data.")

        # Create a line plot to compare cooler models
        plt.figure(figsize=(10, 6))
        sns.set(style="whitegrid")  # Use Seaborn's white grid style for better visuals

        for cooler_name, temperature_data in cooler_data.items():
            if not isinstance(temperature_data, list):
                raise ValueError(f"Temperature data for {cooler_name} must be a list.")
            plt.plot(temperature_data, label=cooler_name, marker='o')  # Plot each cooler's data

        # Add labels, title, and legend
        plt.title("Temperature Retention Comparison of Engel Coolers", fontsize=16)
        plt.xlabel("Time (hours)", fontsize=12)
        plt.ylabel("Temperature (°C)", fontsize=12)
        plt.legend(title="Cooler Models", loc="upper right", fontsize=10)
        plt.tight_layout()

        # Display the graph
        plt.show()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage of the function with sample data
if __name__ == "__main__":
    # Sample data for Engel coolers
    sample_cooler_data = {
        "Cooler A": [5, 4, 3, 3, 2],
        "Cooler B": [6, 5, 4, 4, 3],
        "Cooler C": [7, 6, 5, 4, 4],
    }

    # Call the visualization function
    visualize_cooler_data(sample_cooler_data)
```
