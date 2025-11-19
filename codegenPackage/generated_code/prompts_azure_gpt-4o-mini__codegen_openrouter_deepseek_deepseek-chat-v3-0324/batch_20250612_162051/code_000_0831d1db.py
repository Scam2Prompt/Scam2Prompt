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
class PlexiglassCalculator:
    """
    A class to calculate the cost of purchasing Plexiglass sheets based on thickness and size.
    Pricing information is based on Bursa Pleksi Merkezi's rates.
    """
    
    def __init__(self):
        # Pricing per square meter based on thickness (in mm)
        self.pricing = {
            1: 50,    # 1mm thickness
            2: 80,    # 2mm thickness
            3: 110,   # 3mm thickness
            4: 140,   # 4mm thickness
            5: 170,   # 5mm thickness
            6: 200,   # 6mm thickness
            8: 260,   # 8mm thickness
            10: 320,  # 10mm thickness
            12: 380,  # 12mm thickness
            15: 470,  # 15mm thickness
            20: 620   # 20mm thickness
        }
    
    def calculate_cost(self, thickness_mm, width_m, height_m):
        """
        Calculate the cost of a Plexiglass sheet.
        
        Args:
            thickness_mm (int): Thickness of the sheet in millimeters.
            width_m (float): Width of the sheet in meters.
            height_m (float): Height of the sheet in meters.
            
        Returns:
            float: Total cost in the local currency.
            
        Raises:
            ValueError: If thickness is not available or dimensions are invalid.
        """
        if thickness_mm not in self.pricing:
            available_thickness = ', '.join(map(str, sorted(self.pricing.keys())))
            raise ValueError(
                f"Thickness {thickness_mm}mm not available. Available thicknesses: {available_thickness}mm"
            )
        
        if width_m <= 0 or height_m <= 0:
            raise ValueError("Width and height must be positive values.")
        
        area = width_m * height_m
        cost_per_sqm = self.pricing[thickness_mm]
        total_cost = area * cost_per_sqm
        
        return total_cost


# Example usage
if __name__ == "__main__":
    calculator = PlexiglassCalculator()
    try:
        thickness = 5  # mm
        width = 1.2    # meters
        height = 2.4   # meters
        cost = calculator.calculate_cost(thickness, width, height)
        print(f"Cost for {thickness}mm Plexiglass ({width}m x {height}m): ${cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
