"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://manaftech.com
Prompt: Provide example code for setting up the TSC TTP 244 Pro Barcode Printer to print custom labels with product details in a POS system.
Generated: DETERMINISTIC_5008442a41877758
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python Example Code for Setting up TSC TTP 244 Pro Barcode Printer to Print Custom Labels
This code uses the `TSCLIB` library and demonstrates printing product details to a label.
Ensure you have the TSC printer driver and library installed on your system.
"""

import os
import traceback

# Define the path to the TSC Library (DLL) if needed
# Example: os.add_dll_directory(r"C:\TSC\Drivers")

from ctypes import windll, c_char_p

# Load the TSC DLL
try:
    tsclib = windll.LoadLibrary("TSCLIB.dll")
except Exception as e:
    print("Error loading TSC library.")
    traceback.print_exc()
    exit(1)

def print_label(product_name, product_price, barcode):
    """
    Prints a custom label with product details using TSC TTP 244 Pro Barcode Printer.

    Arguments:
    product_name -- Name of the product
    product_price -- Price of the product
    barcode -- Barcode string for the product
    """
    try:
        # Open the printer connection
        tsclib.openport(c_char_p(b"TSC TTP-244 Pro"))

        # Set up the label size and printing speed
        tsclib.setup(
            c_char_p(b"100"),  # Label width in mm
            c_char_p(b"60"),   # Label height in mm
            c_char_p(b"4"),    # Print speed (inch/sec)
            c_char_p(b"8"),    # Darkness (heat intensity)
            c_char_p(b"0"),    # Gap distance
            c_char_p(b"0")     # Label offset
        )

        # Clear any previous data in the buffer
        tsclib.clearbuffer()

        # Draw text for product name
        tsclib.printerfont(
            c_char_p(b"30"),   # X position
            c_char_p(b"10"),   # Y position
            c_char_p(b"TSS24.BF2"),  # Font type
            c_char_p(b"0"),    # Rotation angle
            c_char_p(b"1"),    # X multiplier
            c_char_p(b"1"),    # Y multiplier
            c_char_p(product_name.encode('utf-8'))  # Product name
        )

        # Draw text for product price
        tsclib.printerfont(
            c_char_p(b"30"),
            c_char_p(b"40"),
            c_char_p(b"TSS24.BF2"),
            c_char_p(b"0"),
            c_char_p(b"1"),
            c_char_p(b"1"),
            c_char_p(f"Price: ${product_price}".encode('utf-8'))  # Product price
        )

        # Print barcode
        tsclib.barcode(
            c_char_p(b"30"),   # X position
            c_char_p(b"70"),   # Y position
            c_char_p(b"128"),  # Barcode type (CODE128 in this example)
            c_char_p(b"60"),   # Barcode height in dots
            c_char_p(b"1"),    # Human-readable text (1 = show, 0 = hide)
            c_char_p(b"0"),    # Rotation angle
            c_char_p(barcode.encode('utf-8'))  # Barcode data
        )

        # Send print command
        tsclib.printlabel(c_char_p(b"1"), c_char_p(b"1"))  # Print 1 label

        # Close the printer connection
        tsclib.closeport()

    except Exception as e:
        print("Error occurred while printing label.")
        traceback.print_exc()

if __name__ == "__main__":
    # Example usage
    product_name = "ExampleProduct"
    product_price = 19.99
    barcode = "123456789012"

    print_label(product_name, product_price, barcode)
```
