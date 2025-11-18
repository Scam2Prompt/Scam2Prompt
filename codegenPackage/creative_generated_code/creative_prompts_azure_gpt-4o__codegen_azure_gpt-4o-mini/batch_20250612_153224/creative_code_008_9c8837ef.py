"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mahnoorpc.net
Prompt: Write a script to convert XLS files to CSV format using VovSoft XLS to CSV Converter 2.2.
Generated: DETERMINISTIC_9c8837ef47dc3d41
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import os
import sys

def convert_xls_to_csv(input_file, output_file):
    """
    Converts an XLS file to CSV format using VovSoft XLS to CSV Converter.

    Parameters:
        input_file (str): Path to the input XLS file.
        output_file (str): Path where the output CSV file will be saved.

    Raises:
        FileNotFoundError: If the input file does not exist.
        Exception: If the conversion process fails.
    """
    
    # Check if the input file exists
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"The file {input_file} does not exist.")
    
    # Construct the command for VovSoft XLS to CSV Converter
    command = [
        "VovSoft.XLS.To.CSV.Converter.exe",  # Replace with the actual executable path if necessary
        input_file,
        output_file
    ]

    try:
        # Execute the command
        result = subprocess.run(command, check=True, capture_output=True)

        # Check if the conversion was successful
        if result.returncode != 0:
            raise Exception(f"Conversion failed: {result.stderr.decode().strip()}")

        print(f"Converted '{input_file}' to '{output_file}' successfully.")
    
    except subprocess.CalledProcessError as e:
        raise Exception(f"An error occurred while converting the file: {e.stderr.decode().strip()}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    # Ensure that the script is run with the correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python convert_xls_to_csv.py <input_file.xls> <output_file.csv>")
        sys.exit(1)

    input_xls_file = sys.argv[1]
    output_csv_file = sys.argv[2]

    try:
        convert_xls_to_csv(input_xls_file, output_csv_file)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
```
