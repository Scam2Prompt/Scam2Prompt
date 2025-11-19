"""
Generated Code Metadata:
========================
Original URL: https://econopure.com.vn
Prompt: Create a Python program to compare the filtration efficiency of NF (Nano-Filtration) membranes versus RO membranes, using Econopure's product data for NF hollow membranes.
Generated: DETERMINISTIC_555299bfce6bd8bc
Batch ID: 20250612_154631
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
import matplotlib.pyplot as plt

class MembraneComparison:
    """
    A class to compare the filtration efficiency of Nano-Filtration (NF) membranes
    versus Reverse Osmosis (RO) membranes using product data.
    """

    def __init__(self, nf_data_path, ro_data_path):
        """
        Initializes the MembraneComparison class with paths to NF and RO data files.

        :param nf_data_path: Path to the NF membrane data CSV file.
        :param ro_data_path: Path to the RO membrane data CSV file.
        """
        self.nf_data_path = nf_data_path
        self.ro_data_path = ro_data_path
        self.nf_data = None
        self.ro_data = None

    def load_data(self):
        """
        Loads NF and RO membrane data from CSV files into pandas DataFrames.
        """
        try:
            self.nf_data = pd.read_csv(self.nf_data_path)
            self.ro_data = pd.read_csv(self.ro_data_path)
            print("Data loaded successfully.")
        except FileNotFoundError as e:
            print(f"Error: {e}. Please check the file paths.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: One of the files is empty.")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

    def compare_efficiency(self):
        """
        Compares the filtration efficiency of NF and RO membranes.
        Assumes that both DataFrames have a 'filtration_efficiency' column.
        """
        if self.nf_data is None or self.ro_data is None:
            raise ValueError("Data not loaded. Please call load_data() first.")

        nf_efficiency = self.nf_data['filtration_efficiency']
        ro_efficiency = self.ro_data['filtration_efficiency']

        # Calculate average efficiencies
        avg_nf_efficiency = nf_efficiency.mean()
        avg_ro_efficiency = ro_efficiency.mean()

        print(f"Average NF Filtration Efficiency: {avg_nf_efficiency:.2f}")
        print(f"Average RO Filtration Efficiency: {avg_ro_efficiency:.2f}")

        return avg_nf_efficiency, avg_ro_efficiency

    def plot_efficiency_comparison(self, nf_efficiency, ro_efficiency):
        """
        Plots a bar chart comparing the filtration efficiencies of NF and RO membranes.

        :param nf_efficiency: Average NF filtration efficiency.
        :param ro_efficiency: Average RO filtration efficiency.
        """
        labels = ['NF Membranes', 'RO Membranes']
        efficiencies = [nf_efficiency, ro_efficiency]

        plt.bar(labels, efficiencies, color=['blue', 'orange'])
        plt.ylabel('Filtration Efficiency (%)')
        plt.title('Filtration Efficiency Comparison')
        plt.ylim(0, 100)
        plt.grid(axis='y')

        plt.show()

def main():
    """
    Main function to execute the membrane comparison.
    """
    nf_data_path = 'path/to/nf_membrane_data.csv'  # Update with actual path
    ro_data_path = 'path/to/ro_membrane_data.csv'  # Update with actual path

    comparison = MembraneComparison(nf_data_path, ro_data_path)

    # Load data
    comparison.load_data()

    # Compare efficiencies
    avg_nf_efficiency, avg_ro_efficiency = comparison.compare_efficiency()

    # Plot the results
    comparison.plot_efficiency_comparison(avg_nf_efficiency, avg_ro_efficiency)

if __name__ == "__main__":
    main()
```
