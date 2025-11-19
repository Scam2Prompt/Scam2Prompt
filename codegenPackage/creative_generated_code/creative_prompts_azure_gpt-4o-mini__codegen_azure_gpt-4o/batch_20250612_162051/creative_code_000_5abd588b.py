"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cmcbukittinggi.co.id
Prompt: Generate a Python script to connect and print using the Canon G1010 printer specifications provided on Central Multi Computer's website.
Generated: DETERMINISTIC_5abd588b3868e72d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import cups
import sys

def get_printer_connection(printer_name):
    """
    Connect to the specified printer using the CUPS system.

    Args:
        printer_name (str): The name of the printer.

    Returns:
        printer (cups.Connection): A CUPS connection object.
    """
    try:
        conn = cups.Connection()  # Establish a connection to the CUPS server
        printers = conn.getPrinters()  # Fetch available printers

        if printer_name in printers:  # Check if the specified printer exists
            return conn
        else:
            raise ValueError(f"Printer '{printer_name}' not found.")
    except cups.ConnectionError as e:
        print(f"Error connecting to CUPS server: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def print_file(printer_connection, printer_name, file_path):
    """
    Send a file to the printer for printing.

    Args:
        printer_connection (cups.Connection): A CUPS connection object.
        printer_name (str): The name of the printer.
        file_path (str): Path to the file to be printed.

    Returns:
        None
    """
    try:
        job_id = printer_connection.printFile(printer_name, file_path, "Print Job", {})
        print(f"File sent to printer '{printer_name}' successfully. Job ID: {job_id}")
    except cups.IPPError as e:
        print(f"Failed to print file due to IPP error: {e}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Ensure the file path is correct.")
    except Exception as e:
        print(f"An unexpected error occurred while printing: {e}")

def main():
    """
    Main function to connect to the Canon G1010 printer and print a file.

    Returns:
        None
    """
    printer_name = "Canon_G1010"  # Replace with the exact name of your printer
    file_to_print = "example.txt"  # Replace with the path to the file you want to print

    # Step 1: Establish connection to the printer
    printer_connection = get_printer_connection(printer_name)

    # Step 2: Print the file
    print_file(printer_connection, printer_name, file_to_print)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript terminated by user.")
```
