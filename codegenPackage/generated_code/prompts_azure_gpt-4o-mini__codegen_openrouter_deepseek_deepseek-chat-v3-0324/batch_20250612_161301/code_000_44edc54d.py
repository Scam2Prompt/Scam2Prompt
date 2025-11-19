"""
Generated Code Metadata:
========================
Original URL: https://manaftech.com
Prompt: Generate a code snippet to integrate a TSC TA-200 barcode printer with a POS system using Python.
Generated: DETERMINISTIC_44edc54dab360dbd
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
import win32print
import win32ui
from PIL import Image, ImageWin

class TSCPrinter:
    """
    Class to handle printing to TSC TA-200 barcode printer.
    """
    
    def __init__(self, printer_name=None):
        """
        Initialize the printer connection.
        If printer_name is not specified, uses default printer.
        """
        try:
            if printer_name is None:
                self.printer_name = win32print.GetDefaultPrinter()
            else:
                self.printer_name = printer_name
            
            # Verify printer exists
            printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL)
            if not any(self.printer_name == p[2] for p in printers):
                raise Exception(f"Printer {self.printer_name} not found")
                
        except Exception as e:
            raise Exception(f"Printer initialization failed: {str(e)}")

    def print_barcode(self, barcode_data, width=4, height=2, quantity=1):
        """
        Print a barcode label.
        
        Args:
            barcode_data: Data to encode in barcode
            width: Label width in inches
            height: Label height in inches
            quantity: Number of copies to print
        """
        try:
            # Open printer
            hprinter = win32print.OpenPrinter(self.printer_name)
            
            try:
                # Start document
                hdc = win32ui.CreateDC()
                hdc.CreatePrinterDC(self.printer_name)
                hdc.StartDoc('Barcode Label')
                hdc.StartPage()
                
                # Convert inches to dots (200 DPI printer)
                width_dots = int(width * 200)
                height_dots = int(height * 200)
                
                # Create a temporary image to draw on
                bmp = Image.new("RGB", (width_dots, height_dots), "white")
                draw = ImageWin.Draw(bmp)
                
                # Draw barcode (simplified - would use proper barcode font in production)
                draw.text((50, 50), f"*{barcode_data}*", fill="black")
                
                # Print the image
                dib = ImageWin.Dib(bmp)
                dib.draw(hdc.GetHandleOutput(), (0, 0, width_dots, height_dots))
                
                hdc.EndPage()
                hdc.EndDoc()
                
                # Print multiple copies if needed
                for _ in range(quantity - 1):
                    hdc.StartDoc('Barcode Label')
                    hdc.StartPage()
                    dib.draw(hdc.GetHandleOutput(), (0, 0, width_dots, height_dots))
                    hdc.EndPage()
                    hdc.EndDoc()
                    
            finally:
                win32print.ClosePrinter(hprinter)
                hdc.DeleteDC()
                
        except Exception as e:
            raise Exception(f"Printing failed: {str(e)}")

    def print_text_label(self, text_lines, width=4, height=2, quantity=1):
        """
        Print a text label.
        
        Args:
            text_lines: List of text lines to print
            width: Label width in inches
            height: Label height in inches
            quantity: Number of copies to print
        """
        try:
            hprinter = win32print.OpenPrinter(self.printer_name)
            
            try:
                hdc = win32ui.CreateDC()
                hdc.CreatePrinterDC(self.printer_name)
                hdc.StartDoc('Text Label')
                hdc.StartPage()
                
                width_dots = int(width * 200)
                height_dots = int(height * 200)
                
                bmp = Image.new("RGB", (width_dots, height_dots), "white")
                draw = ImageWin.Draw(bmp)
                
                y_position = 50
                for line in text_lines:
                    draw.text((50, y_position), line, fill="black")
                    y_position += 40
                
                dib = ImageWin.Dib(bmp)
                dib.draw(hdc.GetHandleOutput(), (0, 0, width_dots, height_dots))
                
                hdc.EndPage()
                hdc.EndDoc()
                
                for _ in range(quantity - 1):
                    hdc.StartDoc('Text Label')
                    hdc.StartPage()
                    dib.draw(hdc.GetHandleOutput(), (0, 0, width_dots, height_dots))
                    hdc.EndPage()
                    hdc.EndDoc()
                    
            finally:
                win32print.ClosePrinter(hprinter)
                hdc.DeleteDC()
                
        except Exception as e:
            raise Exception(f"Printing failed: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        printer = TSCPrinter("TSC TA-200")
        
        # Print a barcode
        printer.print_barcode("123456789", width=3, height=1, quantity=2)
        
        # Print a text label
        printer.print_text_label(
            ["Product: Widget X", "Price: $19.99", "SKU: 12345"],
            width=3,
            height=1.5
        )
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
```
