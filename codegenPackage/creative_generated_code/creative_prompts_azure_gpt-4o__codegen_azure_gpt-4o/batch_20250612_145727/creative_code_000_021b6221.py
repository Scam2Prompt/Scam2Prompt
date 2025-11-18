"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nocreditcheck.online
Prompt: Write code to create a comparison tool for microfinance organizations (MFOs) using data such as loan amounts, interest rates, and repayment terms, similar to the offerings listed on nocreditcheck.online.
Generated: DETERMINISTIC_021b6221ec06f5c2
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from tabulate import tabulate

class MicrofinanceComparisonTool:
    """
    A tool to compare microfinance organizations (MFOs) based on loan amounts, 
    interest rates, and repayment terms.
    """
    
    def __init__(self, data_file):
        """
        Initialize the comparison tool with data from a CSV file.

        :param data_file: Path to the CSV file containing MFO data.
        """
        self.data_file = data_file
        self.mfos = []  # List to store MFO data
        self.load_data()

    def load_data(self):
        """
        Load MFO data from the CSV file into memory.
        """
        try:
            with open(self.data_file, mode='r') as file:
                reader = csv.DictReader(file)
                # Ensure data is read as a list of dictionaries
                self.mfos = [row for row in reader]
        except FileNotFoundError:
            print(f"Error: File {self.data_file} not found.")
        except Exception as e:
            print(f"Error: Could not load data. {e}")

    def display_mfos(self):
        """
        Display the list of MFOs in a tabular format.
        """
        if not self.mfos:
            print("No MFO data available to display.")
            return
        
        print(tabulate(self.mfos, headers="keys", tablefmt="grid"))

    def compare_mfos(self, loan_amount, sort_by='interest_rate'):
        """
        Compare and list MFOs that offer loans greater than or equal to the specified amount.

        :param loan_amount: Minimum loan amount to consider.
        :param sort_by: The field to sort the results by. Default is 'interest_rate'.
        """
        try:
            # Filter MFOs based on loan amount
            filtered_mfos = [
                mfo for mfo in self.mfos if float(mfo['loan_amount']) >= loan_amount
            ]
            
            # Check if any MFOs meet the criteria
            if not filtered_mfos:
                print(f"No MFOs found offering loans greater than or equal to {loan_amount}.")
                return
            
            # Sort the filtered MFOs
            sorted_mfos = sorted(filtered_mfos, key=lambda x: float(x[sort_by]))
            
            # Display the comparison
            print(tabulate(sorted_mfos, headers="keys", tablefmt="grid"))
        except KeyError as e:
            print(f"Error: Invalid sorting field '{e}'. Available fields are: {', '.join(self.mfos[0].keys())}")
        except Exception as e:
            print(f"Error: Could not compare MFOs. {e}")

if __name__ == "__main__":
    # Sample usage
    # Ensure you have a CSV file named 'mfos.csv' with columns: 'name', 'loan_amount', 'interest_rate', 'repayment_term'
    comparison_tool = MicrofinanceComparisonTool(data_file='mfos.csv')

    print("\n--- All Microfinance Organizations ---")
    comparison_tool.display_mfos()

    print("\n--- Filtered and Sorted MFOs ---")
    # Compare MFOs offering a loan amount of at least 500 and sort by interest rate
    comparison_tool.compare_mfos(loan_amount=500, sort_by='interest_rate')
```

This script assumes you have a CSV file (`mfos.csv`) with columns: `name`, `loan_amount`, `interest_rate`, and `repayment_term`. It provides a CLI-based tool for displaying and comparing MFO data.
