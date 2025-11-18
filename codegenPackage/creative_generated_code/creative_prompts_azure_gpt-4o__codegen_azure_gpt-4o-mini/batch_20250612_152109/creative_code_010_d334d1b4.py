"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gadgetexa.com
Prompt: Provide a Python script to calculate the lifespan of laser printers, incorporating the considerations mentioned in Gadgetexa's review.
Generated: DETERMINISTIC_d334d1b497d80624
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
laser_printer_lifespan.py

This script calculates the lifespan of laser printers based on user-defined parameters.
The parameters include the average monthly page yield, printer model, and expected usage.
It incorporates considerations from Gadgetexa's review.

Usage:
    python laser_printer_lifespan.py
"""

class LaserPrinter:
    def __init__(self, model, average_monthly_page_yield, pages_per_cartridge):
        """
        Initializes the LaserPrinter object with model, monthly page yield, and cartridge details.

        Args:
            model (str): The model name of the laser printer.
            average_monthly_page_yield (int): The average number of pages printed per month.
            pages_per_cartridge (int): The number of pages a toner cartridge can print before needing replacement.
        """
        self.model = model
        self.average_monthly_page_yield = average_monthly_page_yield
        self.pages_per_cartridge = pages_per_cartridge

    def calculate_lifespan_years(self):
        """
        Calculates the estimated lifespan of the printer in years based on the average monthly page yield
        and the page yield per cartridge.

        Returns:
            float: Estimated lifespan of the printer in years.
        """
        if self.average_monthly_page_yield <= 0:
            raise ValueError("Average monthly page yield must be greater than zero.")
        if self.pages_per_cartridge <= 0:
            raise ValueError("Pages per cartridge must be greater than zero.")

        # Calculate the total number of pages printed in a year
        annual_page_yield = self.average_monthly_page_yield * 12
        # Calculate the number of cartridges required per year
        cartridges_per_year = annual_page_yield / self.pages_per_cartridge
        # Calculate the lifespan in years (assuming 5 cartridges for the printer)
        estimated_lifespan = 5 / cartridges_per_year
        return estimated_lifespan

def main():
    """
    Main function to execute the lifespan calculation for laser printers.
    """
    try:
        # User input for printer details
        printer_model = input("Enter the printer model: ").strip()
        average_monthly_page_yield = int(input("Enter the average monthly page yield: "))
        pages_per_cartridge = int(input("Enter the number of pages per cartridge: "))

        # Create a LaserPrinter instance
        printer = LaserPrinter(printer_model, average_monthly_page_yield, pages_per_cartridge)

        # Calculate lifespan
        lifespan = printer.calculate_lifespan_years()
        print(f"The estimated lifespan of the {printer.model} is approximately {lifespan:.2f} years.")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
