"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://summar.com
Prompt: Create a script to calculate fuel savings for trucking companies using a fuel card program similar to the one offered by Summar Financial.
Generated: DETERMINISTIC_0979a0c89e7a1120
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class FuelSavingsCalculator:
    """
    A class to calculate fuel savings for trucking companies using a fuel card program.
    """

    def __init__(self, fuel_data_file):
        """
        Initializes the FuelSavingsCalculator with the given fuel data file.

        :param fuel_data_file: str, path to the CSV file containing fuel purchase data.
        """
        self.fuel_data_file = fuel_data_file
        self.fuel_data = None
        self.total_savings = 0.0

    def load_data(self):
        """
        Loads fuel purchase data from the CSV file into a DataFrame.
        
        Raises:
            FileNotFoundError: If the specified CSV file does not exist.
            pd.errors.EmptyDataError: If the file is empty.
            pd.errors.ParserError: If there is an issue parsing the CSV file.
        """
        try:
            self.fuel_data = pd.read_csv(self.fuel_data_file)
            print("Data loaded successfully.")
        except FileNotFoundError as e:
            print(f"Error: The file '{self.fuel_data_file}' was not found.")
            raise e
        except pd.errors.EmptyDataError as e:
            print("Error: The file is empty.")
            raise e
        except pd.errors.ParserError as e:
            print("Error: There was a parsing error with the file.")
            raise e

    def calculate_savings(self):
        """
        Calculates total fuel savings based on fuel purchase data.

        The DataFrame is expected to have columns: 'Fuel_Amount', 'Fuel_Cost', 'Discount_Percentage'.
        The formula for savings is: savings = (Fuel_Amount * Fuel_Cost) * (Discount_Percentage / 100).

        Raises:
            ValueError: If the required columns are missing from the DataFrame.
        """
        if self.fuel_data is None:
            raise ValueError("Data not loaded. Call 'load_data()' before calculating savings.")

        required_columns = ['Fuel_Amount', 'Fuel_Cost', 'Discount_Percentage']
        for column in required_columns:
            if column not in self.fuel_data.columns:
                raise ValueError(f"Missing required column: '{column}' in the data")

        # Calculate savings for each transaction and sum them up
        self.total_savings = (self.fuel_data['Fuel_Amount'] * self.fuel_data['Fuel_Cost'] * 
                              (self.fuel_data['Discount_Percentage'] / 100)).sum()
        print(f"Total savings calculated: ${self.total_savings:.2f}")

    def get_total_savings(self):
        """
        Returns the total calculated savings.

        :return: float, total fuel savings.
        """
        return self.total_savings


if __name__ == "__main__":
    # Example usage of the FuelSavingsCalculator
    fuel_data_file_path = 'fuel_data.csv'  # Replace with actual file path
    calculator = FuelSavingsCalculator(fuel_data_file_path)

    try:
        calculator.load_data()
        calculator.calculate_savings()
        print(f"Total fuel savings: ${calculator.get_total_savings():.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")
```

This script is a complete implementation for calculating fuel savings based on a CSV file containing fuel purchase data. Ensure the CSV file structure matches the expected columns for the calculations to work correctly.
