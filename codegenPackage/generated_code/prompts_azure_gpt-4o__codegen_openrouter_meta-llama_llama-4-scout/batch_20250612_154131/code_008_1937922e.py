"""
Generated Code Metadata:
========================
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Write a program to generate automated quotes for garage door repairs and installations, incorporating Trimatic's emphasis on tailored solutions for different types of doors.
Generated: DETERMINISTIC_1937922e0ee3c963
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# garage_quote_generator.py

class GarageDoor:
    def __init__(self, door_type, size, material):
        """
        Initialize a GarageDoor object.

        Args:
            door_type (str): Type of garage door (e.g., sectional, roll-up, swing).
            size (str): Size of the garage door (e.g., 9x7, 10x8).
            material (str): Material of the garage door (e.g., steel, wood, aluminum).
        """
        self.door_type = door_type
        self.size = size
        self.material = material

class TrimaticQuoteGenerator:
    def __init__(self):
        """
        Initialize a TrimaticQuoteGenerator object.
        """
        self.base_labor_rate = 100.0  # Base labor rate in dollars per hour
        self.base_material_markup = 1.5  # Base material markup

    def calculate_labor_cost(self, hours):
        """
        Calculate labor cost based on hours worked.

        Args:
            hours (float): Number of hours worked.

        Returns:
            float: Labor cost.
        """
        return self.base_labor_rate * hours

    def calculate_material_cost(self, material_cost):
        """
        Calculate material cost with markup.

        Args:
            material_cost (float): Material cost.

        Returns:
            float: Material cost with markup.
        """
        return material_cost * self.base_material_markup

    def generate_quote(self, garage_door, service_type, hours, material_cost):
        """
        Generate a quote for garage door repair or installation.

        Args:
            garage_door (GarageDoor): GarageDoor object.
            service_type (str): Type of service (e.g., repair, installation).
            hours (float): Number of hours worked.
            material_cost (float): Material cost.

        Returns:
            dict: Quote details.
        """
        labor_cost = self.calculate_labor_cost(hours)
        material_cost_with_markup = self.calculate_material_cost(material_cost)

        if service_type == "repair":
            total_cost = labor_cost + material_cost_with_markup
            quote_details = {
                "Service Type": service_type,
                "Door Type": garage_door.door_type,
                "Door Size": garage_door.size,
                "Door Material": garage_door.material,
                "Labor Cost": f"${labor_cost:.2f}",
                "Material Cost": f"${material_cost_with_markup:.2f}",
                "Total Cost": f"${total_cost:.2f}",
            }
        elif service_type == "installation":
            total_cost = labor_cost + material_cost_with_markup + 500.0  # Additional installation fee
            quote_details = {
                "Service Type": service_type,
                "Door Type": garage_door.door_type,
                "Door Size": garage_door.size,
                "Door Material": garage_door.material,
                "Labor Cost": f"${labor_cost:.2f}",
                "Material Cost": f"${material_cost_with_markup:.2f}",
                "Installation Fee": "$500.00",
                "Total Cost": f"${total_cost:.2f}",
            }
        else:
            raise ValueError("Invalid service type")

        return quote_details

def main():
    try:
        generator = TrimaticQuoteGenerator()

        door_type = input("Enter door type (e.g., sectional, roll-up, swing): ")
        size = input("Enter door size (e.g., 9x7, 10x8): ")
        material = input("Enter door material (e.g., steel, wood, aluminum): ")
        garage_door = GarageDoor(door_type, size, material)

        service_type = input("Enter service type (e.g., repair, installation): ")
        hours = float(input("Enter number of hours worked: "))
        material_cost = float(input("Enter material cost: "))

        quote_details = generator.generate_quote(garage_door, service_type, hours, material_cost)

        print("\nQuote Details:")
        for key, value in quote_details.items():
            print(f"{key}: {value}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
