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
import os
import subprocess

def convert_xls_to_csv(xls_file_path, output_csv_path, converter_exe_path):
    """
    Converts an XLS file to CSV format using VovSoft XLS to CSV Converter.

    Args:
        xls_file_path (str): Path to the input XLS file.
        output_csv_path (str): Path to save the output CSV file.
        converter_exe_path (str): Path to the VovSoft XLS to CSV Converter executable.

    Returns:
        bool: True if conversion succeeded, False otherwise.
    """
    try:
        # Check if the XLS file exists
        if not os.path.exists(xls_file_path):
            raise FileNotFoundError(f"XLS file not found: {xls_file_path}")
        
        # Check if the converter executable exists
        if not os.path.exists(converter_exe_path):
            raise FileNotFoundError(f"Converter executable not found: {converter_exe_path}")
        
        # Build the command for conversion
        command = [converter_exe_path, xls_file_path, output_csv_path]
        
        # Run the conversion process
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Check for errors during the subprocess call
        if result.returncode != 0:
            raise Exception(f"Conversion failed: {result.stderr.decode().strip()}")
        
        # Verify the output CSV file was created
        if not os.path.exists(output_csv_path):
            raise FileNotFoundError(f"Output CSV file not created: {output_csv_path}")
        
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False


if __name__ == "__main__":
    # Example usage
    xls_file = "example.xls"
    csv_file = "output.csv"
    converter_path = "C:\\Path\\To\\XLS_to_CSV_Converter.exe"
    
    success = convert_xls_to_csv(xls_file, csv_file, converter_path)
    if success:
        print("Conversion completed successfully!")
    else:
        print("Conversion failed.")
```
