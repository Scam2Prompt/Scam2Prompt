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
class PlexiglassPricing:
    def __init__(self):
        # Pricing information for different thicknesses (in mm)
        self.pricing = {
            2: 10.0,   # Price per square meter for 2mm thickness
            3: 15.0,   # Price per square meter for 3mm thickness
            4: 20.0,   # Price per square meter for 4mm thickness
            5: 25.0,   # Price per square meter for 5mm thickness
            6: 30.0    # Price per square meter for 6mm thickness
        }

    def calculate_cost(self, thickness, area):
        """
        Calculate the cost of purchasing Plexiglass sheets.

        :param thickness: Thickness of the Plexiglass sheet in mm
        :param area: Area in square meters to be covered
        :return: Total cost of the Plexiglass sheets
        :raises ValueError: If the thickness is not available or area is negative
        """
        if thickness not in self.pricing:
            raise ValueError(f"Thickness {thickness}mm is not available.")
        if area < 0:
            raise ValueError("Area cannot be negative.")

        # Calculate total cost
        cost_per_square_meter = self.pricing[thickness]
        total_cost = cost_per_square_meter * area
        return total_cost

def main():
    # Create an instance of the PlexiglassPricing class
    plexiglass_pricing = PlexiglassPricing()

    # Example usage
    try:
        thickness = 4  # Thickness in mm
        area = 10      # Area in square meters
        cost = plexiglass_pricing.calculate_cost(thickness, area)
        print(f"The total cost for {area} square meters of {thickness}mm Plexiglass is: ${cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
