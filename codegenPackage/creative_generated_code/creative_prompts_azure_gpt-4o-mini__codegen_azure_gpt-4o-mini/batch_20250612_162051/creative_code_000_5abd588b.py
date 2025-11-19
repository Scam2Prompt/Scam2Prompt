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

def connect_to_printer(printer_name):
    """
    Connects to the specified printer using CUPS.

    Args:
        printer_name (str): The name of the printer to connect to.

    Returns:
        cups.Connection: A CUPS connection object.
    """
    try:
        conn = cups.Connection()
        printers = conn.getPrinters()

        if printer_name not in printers:
            raise ValueError(f"Printer '{printer_name}' not found.")
        
        return conn
    except Exception as e:
        print(f"Error connecting to printer: {e}")
        sys.exit(1)

def print_document(conn, printer_name, file_path):
    """
    Sends a print job to the specified printer.

    Args:
        conn (cups.Connection): A CUPS connection object.
        printer_name (str): The name of the printer to send the job to.
        file_path (str): The path to the document to print.

    Returns:
        str: The job ID of the print job.
    """
    try:
        job_id = conn.printFile(printer_name, file_path, "Print Job", {})
        return job_id
    except cups.IPPError as e:
        print(f"Error sending print job: {e}")
        sys.exit(1)

def main():
    """
    Main function to connect to the printer and print a document.
    """
    printer_name = "Canon G1010"  # Replace with actual printer name if different
    file_path = "/path/to/document.pdf"  # Replace with the actual document path

    # Connect to the printer
    conn = connect_to_printer(printer_name)

    # Print the document
    job_id = print_document(conn, printer_name, file_path)
    print(f"Print job sent successfully. Job ID: {job_id}")

if __name__ == "__main__":
    main()
```

**Note**: Make sure to install the `pycups` library with `pip install pycups`, and replace `"/path/to/document.pdf"` with the actual path of the document you want to print. Also, ensure that the printer name is correct as registered in the CUPS system.
