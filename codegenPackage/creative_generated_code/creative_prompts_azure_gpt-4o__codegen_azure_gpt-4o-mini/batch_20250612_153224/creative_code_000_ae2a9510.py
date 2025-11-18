"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bursapleksi.com.tr
Prompt: Write Python code to calculate the cost of purchasing multiple plexiglass sheets in different sizes and thicknesses, using the pricing structure provided by Bursa Pleksi Merkezi's "Güncel Fiyat Listesi."
Generated: DETERMINISTIC_ae2a9510b8d49be0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PlexiglassSheet:
    """
    A class to represent a plexiglass sheet with its dimensions and thickness.
    
    Attributes:
        length (float): Length of the sheet in meters.
        width (float): Width of the sheet in meters.
        thickness (float): Thickness of the sheet in millimeters.
    """
    
    def __init__(self, length, width, thickness):
        self.length = length
        self.width = width
        self.thickness = thickness

    def area(self):
        """Calculate the area of the sheet in square meters."""
        return self.length * self.width


class Pricing:
    """
    A class to handle pricing for plexiglass sheets based on thickness.
    
    Attributes:
        price_per_sqm (dict): A dictionary mapping thickness to price per square meter.
    """
    
    def __init__(self):
        # Example pricing structure based on thickness in mm
        self.price_per_sqm = {
            2: 100,
            3: 120,
            4: 140,
            5: 160,
            6: 180,
            8: 200,
            10: 250
        }

    def get_price(self, thickness):
        """Get the price per square meter for a given thickness."""
        if thickness not in self.price_per_sqm:
            raise ValueError(f"No price found for thickness: {thickness} mm")
        return self.price_per_sqm[thickness]


class PlexiglassOrder:
    """
    A class to handle the order of multiple plexiglass sheets.

    Attributes:
        sheets (list): A list of PlexiglassSheet objects.
        pricing (Pricing): An instance of the Pricing class.
    """
    
    def __init__(self):
        self.sheets = []
        self.pricing = Pricing()

    def add_sheet(self, length, width, thickness):
        """Add a new plexiglass sheet to the order."""
        try:
            sheet = PlexiglassSheet(length, width, thickness)
            self.sheets.append(sheet)
        except Exception as e:
            print(f"Error adding sheet: {e}")

    def calculate_total_cost(self):
        """Calculate the total cost for all sheets in the order."""
        total_cost = 0.0
        
        for sheet in self.sheets:
            try:
                area = sheet.area()
                price_per_sqm = self.pricing.get_price(sheet.thickness)
                total_cost += area * price_per_sqm
            except ValueError as e:
                print(f"Error calculating cost for sheet {sheet}: {e}")

        return total_cost


if __name__ == "__main__":
    # Example usage
    order = PlexiglassOrder()
    
    # Adding sheets to the order
    order.add_sheet(length=2.0, width=1.5, thickness=3)
    order.add_sheet(length=1.2, width=2.0, thickness=5)
    
    # Calculate and display the total cost of the order
    try:
        total = order.calculate_total_cost()
        print(f"Total cost for plexiglass sheets: {total:.2f} currency units")
    except Exception as e:
        print(f"Error calculating total cost: {e}")
```
