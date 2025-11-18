"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econopure.com.vn
Prompt: Create a Python program to compare the filtration efficiency of NF (Nano-Filtration) membranes versus RO membranes, using Econopure's product data for NF hollow membranes.
Generated: DETERMINISTIC_555299bfce6bd8bc
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt

class MembraneComparison:
    """
    A class to compare the filtration efficiency of NF (Nano-Filtration) membranes 
    versus RO (Reverse Osmosis) membranes using product data.
    """

    def __init__(self, nf_data_path, ro_data_path):
        """
        Initializes the MembraneComparison with paths to NF and RO data files.

        Args:
            nf_data_path (str): Path to the NF membrane data CSV file.
            ro_data_path (str): Path to the RO membrane data CSV file.
        """
        self.nf_data_path = nf_data_path
        self.ro_data_path = ro_data_path
        self.nf_data = None
        self.ro_data = None

    def load_data(self):
        """Loads data from the provided CSV files into Pandas DataFrames."""
        try:
            self.nf_data = pd.read_csv(self.nf_data_path)
            self.ro_data = pd.read_csv(self.ro_data_path)
            print("Data loaded successfully.")
        except FileNotFoundError as e:
            print(f"Error: {e}")
            raise
        except pd.errors.EmptyDataError:
            print("Error: No data found in the CSV file.")
            raise
        except pd.errors.ParserError:
            print("Error: Could not parse the CSV file.")
            raise

    def compare_filtration_efficiency(self):
        """Compares filtration efficiency between NF and RO membranes and plots the results."""
        if self.nf_data is None or self.ro_data is None:
            print("Error: Data not loaded. Please load data before comparison.")
            return
        
        # Assuming the data contains columns named 'Efficiency' for filtration efficiency
        try:
            nf_efficiency = self.nf_data['Efficiency']
            ro_efficiency = self.ro_data['Efficiency']
            membrane_labels = ['NF Membranes', 'RO Membranes']

            # Create a bar plot to compare the efficiencies
            plt.bar(membrane_labels, [nf_efficiency.mean(), ro_efficiency.mean()], color=['blue', 'green'])
            plt.ylabel('Filtration Efficiency (%)')
            plt.title('Filtration Efficiency Comparison: NF vs RO Membranes')
            plt.ylim(0, 100)
            plt.grid(axis='y')
            plt.show()

        except KeyError as e:
            print(f"Error: Missing expected column in data - {e}")
            raise

if __name__ == "__main__":
    # Paths to the product data CSV files for NF and RO membranes
    nf_data_path = 'econopure_nf_membranes.csv'
    ro_data_path = 'econopure_ro_membranes.csv'

    # Create an instance of MembraneComparison
    comparison = MembraneComparison(nf_data_path, ro_data_path)

    # Load the data
    comparison.load_data()

    # Compare the filtration efficiency
    comparison.compare_filtration_efficiency()
```
