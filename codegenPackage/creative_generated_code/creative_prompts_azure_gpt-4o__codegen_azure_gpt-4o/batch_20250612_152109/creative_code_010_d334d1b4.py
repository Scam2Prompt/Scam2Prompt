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
Python script to calculate the lifespan of laser printers based on usage patterns,
maintenance schedules, and manufacturer specifications. The script leverages
Gadgetexa's review criteria for accurate estimations.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary libraries
import sys

def calculate_printer_lifespan(avg_pages_per_month, max_pages_per_month, maintenance_cycles, manufacturer_lifespan):
    """
    Calculate the estimated lifespan of a laser printer.

    Parameters:
        avg_pages_per_month (int): Average number of pages printed per month.
        max_pages_per_month (int): Maximum number of pages the printer can handle per month.
        maintenance_cycles (int): Frequency of maintenance cycles (in months).
        manufacturer_lifespan (int): Expected lifespan of the printer in total pages.

    Returns:
        float: Estimated lifespan of the printer in years.
    """
    try:
        # Validate input parameters
        if avg_pages_per_month <= 0 or max_pages_per_month <= 0 or maintenance_cycles <= 0 or manufacturer_lifespan <= 0:
            raise ValueError("All input parameters must be positive numbers.")
        
        # Ensure the average usage does not exceed the maximum recommended usage
        if avg_pages_per_month > max_pages_per_month:
            raise ValueError("The average pages per month cannot exceed the maximum recommended pages per month.")

        # Total pages printed per year
        pages_per_year = avg_pages_per_month * 12

        # Calculate the estimated lifespan
        estimated_lifespan_years = manufacturer_lifespan / pages_per_year
        
        # Adjust lifespan based on maintenance frequency
        adjustment_factor = 1 + (maintenance_cycles / 100)  # Assuming maintenance extends lifespan slightly
        adjusted_lifespan_years = estimated_lifespan_years * adjustment_factor

        return round(adjusted_lifespan_years, 2)

    except ValueError as ve:
        print(f"Value Error: {ve}")
        sys.exit(1)  # Exit the script with an error code
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to execute the script logic.
    """
    try:
        # Gather input from the user
        print("Laser Printer Lifespan Calculator\n")
        avg_pages_per_month = int(input("Enter average pages printed per month: "))
        max_pages_per_month = int(input("Enter maximum pages the printer can handle per month: "))
        maintenance_cycles = int(input("Enter maintenance frequency (in months): "))
        manufacturer_lifespan = int(input("Enter manufacturer's total lifespan (in pages): "))
        
        # Calculate printer lifespan
        lifespan = calculate_printer_lifespan(avg_pages_per_month, max_pages_per_month,
                                              maintenance_cycles, manufacturer_lifespan)
        
        print(f"\nEstimated Laser Printer Lifespan: {lifespan} years")
    
    except ValueError:
        print("Invalid input. Please enter integers only for the parameters.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nCalculation terminated by user.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
