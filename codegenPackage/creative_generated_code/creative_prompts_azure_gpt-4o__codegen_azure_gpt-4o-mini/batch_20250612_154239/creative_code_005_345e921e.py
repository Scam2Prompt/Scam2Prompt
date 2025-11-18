"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fujimitsudynamic.com
Prompt: Write code to automate the printing of ferrules for electrical supplies, inspired by Fujimitsu Dynamic's ferrule printing solutions.
Generated: DETERMINISTIC_345e921e155e8d03
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import time
from datetime import datetime
from fpdf import FPDF

class FerrulePrinter:
    def __init__(self, output_directory):
        """
        Initializes the FerrulePrinter with the specified output directory.

        :param output_directory: Directory where the printed ferrule files will be saved.
        """
        self.output_directory = output_directory
        self.validate_output_directory()

    def validate_output_directory(self):
        """Validates the output directory and creates it if it does not exist."""
        if not os.path.exists(self.output_directory):
            try:
                os.makedirs(self.output_directory)
            except Exception as e:
                raise IOError(f"Failed to create output directory: {self.output_directory}. Error: {e}")

    def create_ferrule(self, label, size):
        """
        Creates a ferrule PDF file with the given label and size.

        :param label: The label to print on the ferrule.
        :param size: The size of the ferrule.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Center the label on the page
        pdf.cell(200, 10, txt=label, ln=True, align='C')
        pdf.cell(200, 10, txt=size, ln=True, align='C')

        # Generate a unique filename based on the current timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{label.replace(' ', '_')}_{size}_{timestamp}.pdf"
        filepath = os.path.join(self.output_directory, filename)

        try:
            pdf.output(filepath)
            print(f"Ferrule created: {filepath}")
        except Exception as e:
            raise IOError(f"Failed to create ferrule PDF. Error: {e}")

    def print_ferrule(self, label, size):
        """
        Automates the process of creating and printing a ferrule.

        :param label: The label to print on the ferrule.
        :param size: The size of the ferrule.
        """
        try:
            print("Starting the ferrule printing process...")
            self.create_ferrule(label, size)
            print("Ferrule printing process completed successfully.")
        except Exception as e:
            print(f"An error occurred during the ferrule printing process: {e}")

def main():
    """
    Main function to execute the FerrulePrinter automation.
    """
    output_directory = "ferrule_outputs"
    
    # Create an instance of the FerrulePrinter
    ferrule_printer = FerrulePrinter(output_directory)

    # Example usage: Create and print a couple of ferrules
    ferrule_printer.print_ferrule("Label A", "Size 1")
    time.sleep(1)  # Simulate delay between prints
    ferrule_printer.print_ferrule("Label B", "Size 2")

if __name__ == "__main__":
    main()
```

Make sure to install the `fpdf` library if you haven't already. You can do this using:
```bash
pip install fpdf
```
