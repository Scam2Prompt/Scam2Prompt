"""
Generated Code Metadata:
========================
Original URL: https://mahnoorpc.net
Prompt: Write a script to convert XLS files to CSV format using VovSoft XLS to CSV Converter 2.2.
Generated: DETERMINISTIC_9c8837ef47dc3d41
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide the code, but I need to clarify that I will be using Python as the programming language and the `openpyxl` and `pandas` libraries to achieve this task, as the VovSoft XLS to CSV Converter 2.2 software is not a programming API. Here is the code:

```python
import pandas as pd
import argparse
import os

def xls_to_csv(xls_file, csv_file):
    """
    Converts an XLS file to CSV format.

    Args:
        xls_file (str): The path to the XLS file.
        csv_file (str): The path to the output CSV file.

    Returns:
        None
    """
    try:
        # Read the XLS file
        df = pd.read_excel(xls_file)

        # Write to CSV file
        df.to_csv(csv_file, index=False)

        print(f"Successfully converted {xls_file} to {csv_file}")

    except FileNotFoundError:
        print(f"Error: The file {xls_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Convert XLS files to CSV format")

    # Add arguments
    parser.add_argument("-i", "--input", required=True, help="The path to the XLS file")
    parser.add_argument("-o", "--output", required=True, help="The path to the output CSV file")

    # Parse arguments
    args = parser.parse_args()

    # Check if the input file exists
    if not os.path.exists(args.input):
        print(f"Error: The file {args.input} does not exist.")
        return

    # Check if the input file is an XLS file
    if not args.input.endswith(".xls") and not args.input.endswith(".xlsx"):
        print(f"Error: The file {args.input} is not an XLS file.")
        return

    # Check if the output file has a CSV extension
    if not args.output.endswith(".csv"):
        args.output += ".csv"

    # Convert XLS to CSV
    xls_to_csv(args.input, args.output)


if __name__ == "__main__":
    main()
```

You can run this script from the command line like so:

```bash
python xls_to_csv.py -i input.xls -o output
```
