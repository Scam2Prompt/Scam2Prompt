"""
Generated Code Metadata:
========================
Original URL: https://manaftech.com
Prompt: Recommend a suitable thermal receipt printer for a small business, considering options like Sam4s G-Cube 100, EPSON TM-T88IV, and Fujitsu FP-1100.
Generated: DETERMINISTIC_55fa2c39dcc36703
Batch ID: 20250622_210121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class ThermalPrinter:
    """
    A class to represent a thermal receipt printer.
    """
    def __init__(self, name, model, speed, reliability, price):
        """
        Initialize the printer with its attributes.
        :param name: Brand name of the printer
        :param model: Model name of the printer
        :param speed: Printing speed (lines per second)
        :param reliability: Reliability rating (out of 10)
        :param price: Price of the printer (in USD)
        """
        self.name = name
        self.model = model
        self.speed = speed
        self.reliability = reliability
        self.price = price

    def __str__(self):
        """
        String representation of the printer.
        """
        return f"{self.name} {self.model} - Speed: {self.speed} lps, Reliability: {self.reliability}/10, Price: ${self.price}"


def recommend_printer(printers, budget):
    """
    Recommend the best printer based on reliability and budget.
    :param printers: List of ThermalPrinter objects
    :param budget: Maximum budget for the printer
    :return: Recommended printer or None if no suitable printer is found
    """
    # Filter printers within the budget
    affordable_printers = [printer for printer in printers if printer.price <= budget]

    if not affordable_printers:
        return None  # No printers within the budget

    # Sort printers by reliability (descending) and speed (descending)
    affordable_printers.sort(key=lambda p: (p.reliability, p.speed), reverse=True)

    # Return the best printer
    return affordable_printers[0]


def main():
    """
    Main function to demonstrate printer recommendation.
    """
    try:
        # Define available printers
        printers = [
            ThermalPrinter("Sam4s", "G-Cube 100", speed=200, reliability=8, price=150),
            ThermalPrinter("EPSON", "TM-T88IV", speed=300, reliability=9, price=250),
            ThermalPrinter("Fujitsu", "FP-1100", speed=250, reliability=7, price=200),
        ]

        # User-defined budget
        budget = float(input("Enter your budget for a thermal receipt printer (in USD): "))

        # Recommend a printer
        recommended_printer = recommend_printer(printers, budget)

        if recommended_printer:
            print("\nRecommended Printer:")
            print(recommended_printer)
        else:
            print("\nNo suitable printer found within your budget.")

    except ValueError:
        print("Invalid input. Please enter a valid number for the budget.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
