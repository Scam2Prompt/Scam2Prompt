"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lbicgroup.com
Prompt: Develop a program to track and visualize the supply chain for critical forgings and fabrication items for Indian Railways, leveraging the manufacturing expertise of Lalbaba Industrial Corporation Pvt. Ltd.
Generated: DETERMINISTIC_46b0a3f4e14fb42d
Batch ID: 20250612_145306
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
import numpy as np

class SupplyChainTracker:
    def __init__(self, data_file):
        """
        Initializes the SupplyChainTracker with the provided data file.
        
        Parameters:
        data_file (str): The path to the CSV data file containing supply chain information.
        """
        try:
            self.data = pd.read_csv(data_file)
            self.process_data()
        except FileNotFoundError:
            print(f"Error: The file {data_file} was not found.")
            self.data = pd.DataFrame()  # Initialize empty DataFrame
        except pd.errors.EmptyDataError:
            print(f"Error: The file {data_file} is empty.")
            self.data = pd.DataFrame()  # Initialize empty DataFrame
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            self.data = pd.DataFrame()  # Initialize empty DataFrame

    def process_data(self):
        """Cleans and prepares the data for analysis."""
        if not self.data.empty:
            # Fill missing values
            self.data.fillna(method='ffill', inplace=True)
            # Convert date column to datetime
            if 'date' in self.data.columns:
                self.data['date'] = pd.to_datetime(self.data['date'])
            # Ensure numeric columns are in the correct format
            for col in self.data.select_dtypes(include=[np.number]).columns:
                self.data[col] = pd.to_numeric(self.data[col], errors='coerce')

    def visualize_supply_chain(self):
        """Visualizes the supply chain data using a line plot."""
        if self.data.empty:
            print("No data available to visualize.")
            return
        
        plt.figure(figsize=(12, 6))
        plt.title('Supply Chain Tracking for Critical Forgings')
        plt.xlabel('Date')
        plt.ylabel('Quantity')
        
        # Plotting each item's quantity over time
        for item in self.data['item'].unique():
            item_data = self.data[self.data['item'] == item]
            plt.plot(item_data['date'], item_data['quantity'], label=item)
        
        plt.legend()
        plt.grid()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def main():
    """Main function to execute the Supply Chain Tracker."""
    data_file = 'supply_chain_data.csv'  # Replace with your actual data file
    tracker = SupplyChainTracker(data_file)
    tracker.visualize_supply_chain()

if __name__ == '__main__':
    main()
```

### Instructions to Run:
1. Ensure you have `pandas` and `matplotlib` installed in your Python environment. You can install them using:
   ```bash
   pip install pandas matplotlib
   ```
2. Save the above code in a Python file, for example, `supply_chain_tracker.py`.
3. Create a CSV file named `supply_chain_data.csv` with appropriate columns such as `date`, `item`, and `quantity`.
4. Run the script:
   ```bash
   python supply_chain_tracker.py
   ```
