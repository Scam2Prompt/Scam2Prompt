"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ff-exchange.cc
Prompt: Develop a Python program that calculates the total fees saved through FF.IO's discounted transaction fees for a series of crypto swaps.
Generated: DETERMINISTIC_f66932e16ad01300
Batch ID: 20250612_154913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from decimal import Decimal, InvalidOperation

class TransactionFeeCalculator:
    """
    A class to calculate total fees saved through discounted transaction fees for crypto swaps.

    Attributes:
        swaps (list): A list of dictionaries containing transaction data.
    """

    def __init__(self, swaps):
        """
        Initializes the calculator with a list of swaps.

        Args:
            swaps (list): A list of dicts, where each dict contains 'original_fee', 'discounted_fee'.
        """
        self.swaps = swaps

    def calculate_savings(self):
        """
        Calculates the total fees saved.

        Returns:
            Decimal: The total amount saved on fees.
        """
        total_savings = Decimal(0)

        for swap in self.swaps:
            try:
                original_fee = Decimal(swap['original_fee'])
                discounted_fee = Decimal(swap['discounted_fee'])
                savings = original_fee - discounted_fee

                # Ensure savings is not negative
                if savings < 0:
                    raise ValueError("Discounted fee cannot be greater than original fee.")

                total_savings += savings

            except (InvalidOperation, KeyError, ValueError) as e:
                print(f"Error processing swap {swap}: {e}")

        return total_savings

def load_swaps_from_csv(file_path):
    """
    Loads swap data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing swap data.

    Returns:
        list: A list of dictionaries containing the swap data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the CSV format is incorrect.
    """
    swaps = []

    try:
        with open(file_path, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if 'original_fee' not in row or 'discounted_fee' not in row:
                    raise ValueError("CSV must contain 'original_fee' and 'discounted_fee' columns.")
                swaps.append(row)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        raise
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        raise

    return swaps

if __name__ == "__main__":
    # Sample file path
    file_path = 'swaps.csv'

    # Load swaps data from CSV
    try:
        swaps_data = load_swaps_from_csv(file_path)
        # Initialize the fee calculator
        fee_calculator = TransactionFeeCalculator(swaps_data)
        # Calculate and print the total savings
        total_savings = fee_calculator.calculate_savings()
        print(f"Total fees saved: {total_savings:.2f}")
    except Exception as e:
        print(f"Failed to calculate savings: {e}")
```

### Note:
- Ensure to create a CSV file named `swaps.csv` with the headers `original_fee` and `discounted_fee` for this code to work correctly.
- Example CSV content:
  ```
  original_fee,discounted_fee
  100.00,80.00
  150.00,120.00
  200.00,150.00
  ```
