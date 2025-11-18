"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cemnazmakine.com
Prompt: Write a script to simulate the operation of a "Patates Paketleme Makinesi," including input parameters like packaging speed and product weight, referencing the technical details from the CEMNAZ Makine website.
Generated: DETERMINISTIC_30d62e2622b76fe5
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to simulate the operation of a "Patates Paketleme Makinesi" (Potato Packaging Machine)

import time
import random

class PotatoPackagingMachine:
    """
    Simulates the operation of a Potato Packaging Machine.
    """

    def __init__(self, packaging_speed, product_weight):
        """
        Initialize the machine with packaging speed and product weight.
        
        :param packaging_speed: (int) Number of packages processed per minute
        :param product_weight: (float) Weight of potatoes per package in kilograms
        """
        if packaging_speed <= 0 or product_weight <= 0:
            raise ValueError("Packaging speed and product weight must be greater than zero.")
        
        self.packaging_speed = packaging_speed
        self.product_weight = product_weight
        self.total_packages = 0
        self.total_weight = 0.0

    def package_potatoes(self, duration_in_minutes):
        """
        Simulates the packaging process for a given duration.

        :param duration_in_minutes: (int) Duration of operation in minutes
        """
        if duration_in_minutes <= 0:
            raise ValueError("Duration must be greater than zero.")

        print(f"Starting the machine for {duration_in_minutes} minutes...")
        for minute in range(1, duration_in_minutes + 1):
            time.sleep(1)  # Simulate real-time operation (1 second per minute for demo purposes)
            packages_this_minute = random.randint(self.packaging_speed - 2, self.packaging_speed + 2)
            self.total_packages += packages_this_minute
            self.total_weight += packages_this_minute * self.product_weight
            print(f"Minute {minute}: Packaged {packages_this_minute} packages "
                  f"({packages_this_minute * self.product_weight:.2f} kg)")

        print("Operation completed.")
        self._print_summary()

    def _print_summary(self):
        """
        Prints a summary of the packaging operation.
        """
        print("\nPackaging Summary:")
        print(f"Total Packages Processed: {self.total_packages}")
        print(f"Total Weight Packaged: {self.total_weight:.2f} kg")

def main():
    """
    Main function to set up and run the Potato Packaging Machine simulation.
    """
    try:
        # Input parameters for the machine; these can be adjusted as needed.
        packaging_speed = int(input("Enter packaging speed (packages per minute): "))
        product_weight = float(input("Enter product weight per package (kg): "))
        duration_in_minutes = int(input("Enter operation duration (minutes): "))

        # Create and start the machine
        machine = PotatoPackagingMachine(packaging_speed, product_weight)
        machine.package_potatoes(duration_in_minutes)
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
