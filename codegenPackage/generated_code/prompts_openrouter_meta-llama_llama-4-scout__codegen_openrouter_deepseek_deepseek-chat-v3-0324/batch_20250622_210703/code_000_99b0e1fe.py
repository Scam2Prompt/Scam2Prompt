"""
Generated Code Metadata:
========================
Original URL: https://otoekspertiz.com.tr
Prompt: Write a Python script to calculate the cost of a vehicle inspection package, considering the prices of different packages (e.g., KB Paket, MM Paket, EKS Paket) offered by Computest Oto Ekspertiz.
Generated: DETERMINISTIC_99b0e1fecfc4b0b6
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Vehicle Inspection Package Cost Calculator for Computest Oto Ekspertiz.
Calculates the total cost based on selected package and optional services.
"""

class VehicleInspectionCalculator:
    """
    Calculates the cost of vehicle inspection packages with optional add-ons.
    """
    
    def __init__(self):
        """Initialize package prices and optional services."""
        self.packages = {
            'KB Paket': 1500,
            'MM Paket': 2000,
            'EKS Paket': 2500
        }
        
        self.optional_services = {
            'Detaylı Rapor': 500,
            'Ekspertiz Sonrası Danışmanlık': 300,
            'Acil Durum Paketi': 400
        }
    
    def calculate_cost(self, package_name, optional_services=None):
        """
        Calculate total cost for selected package and optional services.
        
        Args:
            package_name (str): Name of the selected package
            optional_services (list): List of optional service names
            
        Returns:
            float: Total calculated cost
        Raises:
            ValueError: If package name is invalid
        """
        if package_name not in self.packages:
            raise ValueError(f"Invalid package name. Available packages: {list(self.packages.keys())}")
        
        total = self.packages[package_name]
        
        if optional_services:
            for service in optional_services:
                if service not in self.optional_services:
                    raise ValueError(f"Invalid service name: {service}. Available services: {list(self.optional_services.keys())}")
                total += self.optional_services[service]
        
        return total
    
    def display_menu(self):
        """Display available packages and optional services with prices."""
        print("\nAvailable Inspection Packages:")
        for package, price in self.packages.items():
            print(f"- {package}: {price} TL")
        
        print("\nOptional Services:")
        for service, price in self.optional_services.items():
            print(f"- {service}: {price} TL")


def main():
    """Main function to run the calculator interactively."""
    calculator = VehicleInspectionCalculator()
    
    print("Computest Oto Ekspertiz Vehicle Inspection Cost Calculator")
    print("=" * 60)
    
    while True:
        try:
            calculator.display_menu()
            
            # Get package selection
            selected_package = input("\nSelect a package (or 'q' to quit): ").strip()
            if selected_package.lower() == 'q':
                break
                
            if selected_package not in calculator.packages:
                print("Invalid package selection. Please try again.")
                continue
            
            # Get optional services
            selected_services = []
            print("\nSelect optional services (enter one at a time, leave blank when done):")
            while True:
                service = input("Service name (or blank to finish): ").strip()
                if not service:
                    break
                selected_services.append(service)
            
            # Calculate and display total
            total_cost = calculator.calculate_cost(selected_package, selected_services)
            print(f"\nTotal Cost for {selected_package}: {total_cost} TL")
            print("=" * 60)
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
