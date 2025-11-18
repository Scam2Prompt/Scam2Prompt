"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://manaftech.com
Prompt: Write a script to compare the printing speed and quality of the Sam4s Giant 100 Thermal Receipt Printer and the Fujitsu FP-1100 Thermal Printer in a POS setup.
Generated: DETERMINISTIC_691530f860230011
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class ThermalPrinter:
    """
    Base class for thermal printers.
    """
    def __init__(self, name, speed, quality):
        """
        Initialize the printer with a name, speed (lines per second), and quality (arbitrary score).
        :param name: Name of the printer
        :param speed: Lines per second
        :param quality: Score for print quality (0-100)
        """
        self.name = name
        self.speed = speed
        self.quality = quality

    def print_sample_receipt(self, lines=50):
        """
        Simulates printing a receipt with multiple lines.
        :param lines: Number of lines in the receipt
        :return: Total time taken to print the receipt
        """
        start_time = time.time()
        for line in range(lines):
            time.sleep(1 / self.speed)  # Simulate line printing based on speed
        end_time = time.time()
        return end_time - start_time

    def get_quality_score(self):
        """
        Returns the printer's print quality score.
        :return: Quality score (0-100)
        """
        return self.quality


def compare_printers(printer1, printer2, receipt_lines=50):
    """
    Compare two printers based on speed and quality.
    :param printer1: First printer object
    :param printer2: Second printer object
    :param receipt_lines: Number of lines in the sample receipt
    """
    try:
        print(f"Comparing {printer1.name} and {printer2.name}...\n")

        # Measure printing speed for Printer 1
        print(f"Testing {printer1.name}...")
        time_taken_printer1 = printer1.print_sample_receipt(receipt_lines)
        print(f"{printer1.name} printed {receipt_lines} lines in {time_taken_printer1:.2f} seconds.")
        quality_printer1 = printer1.get_quality_score()
        print(f"{printer1.name} quality score: {quality_printer1}/100\n")

        # Measure printing speed for Printer 2
        print(f"Testing {printer2.name}...")
        time_taken_printer2 = printer2.print_sample_receipt(receipt_lines)
        print(f"{printer2.name} printed {receipt_lines} lines in {time_taken_printer2:.2f} seconds.")
        quality_printer2 = printer2.get_quality_score()
        print(f"{printer2.name} quality score: {quality_printer2}/100\n")

        # Compare results
        print("Comparison Results:")
        if time_taken_printer1 < time_taken_printer2:
            print(f"{printer1.name} is faster than {printer2.name}.")
        elif time_taken_printer1 > time_taken_printer2:
            print(f"{printer2.name} is faster than {printer1.name}.")
        else:
            print("Both printers have the same speed.")

        if quality_printer1 > quality_printer2:
            print(f"{printer1.name} has better print quality than {printer2.name}.")
        elif quality_printer1 < quality_printer2:
            print(f"{printer2.name} has better print quality than {printer1.name}.")
        else:
            print("Both printers have the same print quality.")
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred during the comparison: {str(e)}")


if __name__ == "__main__":
    # Initialize printer objects with name, speed (lines/sec), and quality score (0-100)
    sam4s_giant_100 = ThermalPrinter(name="Sam4s Giant 100", speed=10, quality=85)
    fujitsu_fp_1100 = ThermalPrinter(name="Fujitsu FP-1100", speed=12, quality=80)

    # Compare the printers
    compare_printers(sam4s_giant_100, fujitsu_fp_1100)
```
