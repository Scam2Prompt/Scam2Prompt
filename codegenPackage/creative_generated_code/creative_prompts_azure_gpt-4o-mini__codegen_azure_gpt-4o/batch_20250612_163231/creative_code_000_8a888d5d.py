"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.tax
Prompt: How can I generate IRS Form 8949 and Schedule D for my Polymarket trades using PolyTax?
Generated: DETERMINISTIC_8a888d5d461ecc7f
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Generate IRS Form 8949 and Schedule D for Polymarket trades using PolyTax.

This script uses the PolyTax library to calculate capital gains/losses
from Polymarket trades and automatically generates IRS Form 8949 and Schedule D.
"""

import polytax
import os
import sys
from datetime import datetime

def generate_tax_forms(polymarket_trades_filepath: str, output_directory: str):
    """
    Generates IRS Form 8949 and Schedule D for Polymarket trades.

    Args:
        polymarket_trades_filepath (str): Path to the CSV file containing Polymarket trades data.
        output_directory (str): Directory where the generated forms will be saved.

    Returns:
        None: Saves Form 8949 and Schedule D to the specified output directory.
    """
    try:
        # Validate input file path
        if not os.path.isfile(polymarket_trades_filepath):
            raise FileNotFoundError(f"Trades file '{polymarket_trades_filepath}' not found.")

        # Validate output directory
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Load Polymarket trades using PolyTax
        trades = polytax.load_trades(polymarket_trades_filepath)
        if not trades:
            raise ValueError("No trades found in the provided file.")

        # Calculate capital gains/losses
        tax_report = polytax.calculate_tax_report(trades)

        # Generate Form 8949
        form_8949_path = os.path.join(output_directory, "Form_8949.pdf")
        polytax.generate_form_8949(tax_report, form_8949_path)
        print(f"Form 8949 generated successfully: {form_8949_path}")

        # Generate Schedule D
        schedule_d_path = os.path.join(output_directory, "Schedule_D.pdf")
        polytax.generate_schedule_d(tax_report, schedule_d_path)
        print(f"Schedule D generated successfully: {schedule_d_path}")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except ValueError as val_error:
        print(f"Error: {val_error}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
    finally:
        print("Tax form generation process completed.")

if __name__ == "__main__":
    # Check command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python generate_tax_forms.py <polymarket_trades_filepath> <output_directory>")
        sys.exit(1)

    # Extract arguments
    polymarket_trades_filepath = sys.argv[1]
    output_directory = sys.argv[2]

    # Generate IRS forms
    generate_tax_forms(polymarket_trades_filepath, output_directory)
```
