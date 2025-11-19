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
# vehicle_inspection_package.py

class VehicleInspectionPackage:
    """Calculates the cost of a vehicle inspection package."""

    def __init__(self):
        # Define package prices
        self.packages = {
            "KB Paket": 100.0,
            "MM Paket": 200.0,
            "EKS Paket": 300.0
        }

    def calculate_cost(self, package_name, additional_services=None):
        """
        Calculates the total cost of a vehicle inspection package.

        Args:
            package_name (str): Name of the package (e.g., KB Paket, MM Paket, EKS Paket)
            additional_services (dict, optional): Additional services and their prices. Defaults to None.

        Returns:
            float: Total cost of the vehicle inspection package

        Raises:
            ValueError: If the package name is not found
        """
        if package_name not in self.packages:
            raise ValueError(f"Package '{package_name}' not found")

        package_price = self.packages[package_name]
        total_cost = package_price

        if additional_services:
            for service, price in additional_services.items():
                total_cost += price

        return total_cost


def main():
    try:
        inspection_package = VehicleInspectionPackage()

        # Example usage
        package_name = "KB Paket"
        additional_services = {
            "Tire Check": 20.0,
            "Battery Check": 10.0
        }

        total_cost = inspection_package.calculate_cost(package_name, additional_services)
        print(f"Total cost for {package_name} with additional services: ${total_cost:.2f}")

        # Test error handling
        invalid_package_name = "Invalid Paket"
        inspection_package.calculate_cost(invalid_package_name)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
