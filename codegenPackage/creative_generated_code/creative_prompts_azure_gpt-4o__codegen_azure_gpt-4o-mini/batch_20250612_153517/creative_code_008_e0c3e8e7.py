"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tidhholding.com
Prompt: Develop a program to track and visualize the progress of desertification control schemes, referencing TIDH Holding's initiatives in this area.
Generated: DETERMINISTIC_e0c3e8e7b28687fa
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json

class DesertificationControlTracker:
    """
    A class to track and visualize the progress of desertification control schemes.

    Attributes:
        data (pd.DataFrame): A DataFrame containing the initiatives data.
    """

    def __init__(self, json_file):
        """
        Initializes the tracker with data from a JSON file.

        Args:
            json_file (str): Path to the JSON file containing initiatives data.

        Raises:
            FileNotFoundError: If the JSON file does not exist.
            ValueError: If the JSON file does not contain valid data.
        """
        try:
            with open(json_file, 'r') as file:
                self.data = pd.DataFrame(json.load(file))
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Error: The file {json_file} was not found.") from e
        except json.JSONDecodeError as e:
            raise ValueError("Error: The file does not contain valid JSON.") from e
        except Exception as e:
            raise RuntimeError("An unexpected error occurred while loading data.") from e

    def visualize_progress(self):
        """
        Visualizes the progress of desertification control initiatives using a bar chart.
        """

        # Check if data is empty
        if self.data.empty:
            print("No data available to visualize.")
            return

        # Ensure required columns exist
        required_columns = ['initiative', 'progress']
        if not all(col in self.data.columns for col in required_columns):
            raise ValueError(f"Data must contain the following columns: {required_columns}")

        # Prepare data for visualization
        initiatives = self.data['initiative']
        progress = self.data['progress']

        # Create a bar chart
        plt.figure(figsize=(10, 6))
        plt.barh(initiatives, progress, color='skyblue')
        plt.xlabel('Progress (%)')
        plt.title('Progress of Desertification Control Schemes')
        plt.xlim(0, 100)
        plt.grid(axis='x')

        # Show plot
        plt.tight_layout()
        plt.show()

def main():
    """
    Main function to execute the desertification control tracker.
    """
    try:
        # Instantiate the tracker with the path to the JSON data file
        tracker = DesertificationControlTracker('desertification_initiatives.json')
        # Visualize the progress of the initiatives
        tracker.visualize_progress()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

Please ensure you have the required `matplotlib` and `pandas` libraries installed in your environment to run this code. You can install them using pip:

```sh
pip install matplotlib pandas
``` 

Make sure to replace `'desertification_initiatives.json'` with the actual path to your JSON file containing the initiatives data, which should include at least the fields 'initiative' and 'progress'.
