"""
Generated Code Metadata:
========================
Original URL: https://www.bursapleksi.com.tr
Prompt: Generate a code snippet to calculate the cost of purchasing various thicknesses of Plexiglass sheets based on the pricing information provided by Bursa Pleksi Merkezi.
Generated: DETERMINISTIC_0831d1db11be8f2d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# plexiglass_calculator.py

class PlexiglassPricing:
    def __init__(self):
        # Pricing information per square meter for different thicknesses
        self.pricing = {
            2: 10.0,  # 2mm thickness
            3: 15.0,  # 3mm thickness
            5: 25.0,  # 5mm thickness
            8: 35.0,  # 8mm thickness
            10: 40.0  # 10mm thickness
        }

    def calculate_cost(self, thickness, area):
        """
        Calculate the cost of purchasing a Plexiglass sheet.

        Args:
            thickness (int): Thickness of the Plexiglass sheet in mm.
            area (float): Area of the Plexiglass sheet in square meters.

        Returns:
            float: The cost of the Plexiglass sheet.

        Raises:
            ValueError: If the thickness is not available.
        """
        if thickness not in self.pricing:
            raise ValueError(f"Thickness {thickness}mm not available.")

        price_per_sqm = self.pricing[thickness]
        cost = price_per_sqm * area
        return cost


class PlexiglassOrder:
    def __init__(self, pricing):
        self.pricing = pricing
        self.order = []

    def add_sheet(self, thickness, width, length):
        """
        Add a Plexiglass sheet to the order.

        Args:
            thickness (int): Thickness of the Plexiglass sheet in mm.
            width (float): Width of the Plexiglass sheet in meters.
            length (float): Length of the Plexiglass sheet in meters.

        Raises:
            ValueError: If the thickness is not available.
        """
        area = width * length
        cost = self.pricing.calculate_cost(thickness, area)
        self.order.append({
            "thickness": thickness,
            "width": width,
            "length": length,
            "area": area,
            "cost": cost
        })

    def calculate_total_cost(self):
        """
        Calculate the total cost of the order.

        Returns:
            float: The total cost of the order.
        """
        total_cost = sum(sheet["cost"] for sheet in self.order)
        return total_cost

    def print_order(self):
        """
        Print the details of the order.
        """
        for i, sheet in enumerate(self.order, start=1):
            print(f"Sheet {i}:")
            print(f"  Thickness: {sheet['thickness']}mm")
            print(f"  Size: {sheet['width']}m x {sheet['length']}m")
            print(f"  Area: {sheet['area']:.2f}m²")
            print(f"  Cost: ₺{sheet['cost']:.2f}")
            print()
        print(f"Total Cost: ₺{self.calculate_total_cost():.2f}")


def main():
    pricing = PlexiglassPricing()
    order = PlexiglassOrder(pricing)

    while True:
        print("1. Add sheet to order")
        print("2. Print order and total cost")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            thickness = int(input("Enter thickness (mm): "))
            width = float(input("Enter width (m): "))
            length = float(input("Enter length (m): "))
            try:
                order.add_sheet(thickness, width, length)
            except ValueError as e:
                print(e)
        elif choice == "2":
            order.print_order()
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
