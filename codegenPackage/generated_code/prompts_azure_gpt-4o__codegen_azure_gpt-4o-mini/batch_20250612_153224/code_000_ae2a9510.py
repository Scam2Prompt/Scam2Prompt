"""
Generated Code Metadata:
========================
Original URL: https://www.bursapleksi.com.tr
Prompt: Write Python code to calculate the cost of purchasing multiple plexiglass sheets in different sizes and thicknesses, using the pricing structure provided by Bursa Pleksi Merkezi's "Güncel Fiyat Listesi."
Generated: DETERMINISTIC_ae2a9510b8d49be0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PlexiglassPricing:
    """
    A class to calculate the cost of purchasing plexiglass sheets based on size and thickness.
    """

    def __init__(self):
        # Pricing structure based on thickness (in mm) and size (in square meters)
        self.pricing_structure = {
            2: 100,  # Price per square meter for 2mm thickness
            3: 120,  # Price per square meter for 3mm thickness
            4: 140,  # Price per square meter for 4mm thickness
            5: 160,  # Price per square meter for 5mm thickness
            6: 180,  # Price per square meter for 6mm thickness
        }

    def calculate_cost(self, width: float, height: float, thickness: int) -> float:
        """
        Calculate the cost of a plexiglass sheet based on its dimensions and thickness.

        :param width: Width of the sheet in meters
        :param height: Height of the sheet in meters
        :param thickness: Thickness of the sheet in mm
        :return: Total cost of the sheet
        :raises ValueError: If the thickness is not supported or dimensions are invalid
        """
        if thickness not in self.pricing_structure:
            raise ValueError(f"Thickness {thickness}mm is not supported. Supported thicknesses: {list(self.pricing_structure.keys())}")

        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive values.")

        # Calculate area in square meters
        area = width * height

        # Calculate cost based on area and pricing structure
        cost_per_square_meter = self.pricing_structure[thickness]
        total_cost = area * cost_per_square_meter

        return total_cost

    def calculate_total_cost(self, orders: list) -> float:
        """
        Calculate the total cost for multiple plexiglass sheets.

        :param orders: A list of tuples containing (width, height, thickness)
        :return: Total cost for all sheets
        :raises ValueError: If any order has invalid dimensions or unsupported thickness
        """
        total_cost = 0.0

        for order in orders:
            if len(order) != 3:
                raise ValueError("Each order must contain exactly three values: (width, height, thickness).")
            width, height, thickness = order
            total_cost += self.calculate_cost(width, height, thickness)

        return total_cost


# Example usage
if __name__ == "__main__":
    pricing = PlexiglassPricing()
    
    # List of orders (width in meters, height in meters, thickness in mm)
    orders = [
        (1.0, 2.0, 3),  # 1m x 2m sheet with 3mm thickness
        (0.5, 1.5, 4),  # 0.5m x 1.5m sheet with 4mm thickness
        (2.0, 1.0, 2),  # 2m x 1m sheet with 2mm thickness
    ]

    try:
        total_cost = pricing.calculate_total_cost(orders)
        print(f"Total cost for the plexiglass sheets: {total_cost:.2f} currency units")
    except ValueError as e:
        print(f"Error: {e}")
```
