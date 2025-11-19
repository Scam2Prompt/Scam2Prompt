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
"""
Plexiglass Cost Calculator based on Bursa Pleksi Merkezi's pricing structure.
Supports multiple sheets with different sizes and thicknesses.
"""

class PlexiglassCalculator:
    """
    Calculates the cost of plexiglass sheets based on size, thickness, and quantity.
    Pricing data is based on Bursa Pleksi Merkezi's current price list.
    """
    
    def __init__(self):
        # Pricing structure: {thickness (mm): price per m² (TRY)}
        self.price_per_sqm = {
            1: 350,
            2: 450,
            3: 550,
            4: 650,
            5: 750,
            6: 850,
            8: 1050,
            10: 1250,
            12: 1450,
            15: 1750,
            20: 2250,
            25: 2750,
            30: 3250
        }
        
        # Minimum order area in m² (if total area is below this, this value is used)
        self.min_order_area = 0.1
        
        # Cutting and processing fee per sheet (TRY)
        self.processing_fee_per_sheet = 10
        
    def calculate_sheet_cost(self, width_m: float, height_m: float, thickness_mm: int, quantity: int = 1) -> float:
        """
        Calculate the cost for a single plexiglass sheet type.
        
        Args:
            width_m: Width in meters
            height_m: Height in meters
            thickness_mm: Thickness in millimeters (must be a key in price_per_sqm)
            quantity: Number of sheets (default: 1)
            
        Returns:
            Total cost in TRY for these sheets
            
        Raises:
            ValueError: If invalid dimensions or thickness are provided
        """
        if width_m <= 0 or height_m <= 0:
            raise ValueError("Dimensions must be positive numbers")
        if thickness_mm not in self.price_per_sqm:
            raise ValueError(f"Unsupported thickness: {thickness_mm}mm")
        if quantity <= 0:
            raise ValueError("Quantity must be at least 1")
            
        area = width_m * height_m
        effective_area = max(area, self.min_order_area)
        
        price_per_sheet = (effective_area * self.price_per_sqm[thickness_mm]) + self.processing_fee_per_sheet
        total_cost = price_per_sheet * quantity
        
        return total_cost
    
    def calculate_total_cost(self, sheets: list) -> float:
        """
        Calculate the total cost for multiple plexiglass sheets.
        
        Args:
            sheets: List of dictionaries with keys:
                   - 'width_m' (float)
                   - 'height_m' (float)
                   - 'thickness_mm' (int)
                   - 'quantity' (int, optional, default=1)
                   
        Returns:
            Total cost in TRY for all sheets
            
        Raises:
            ValueError: If any sheet data is invalid
        """
        total = 0.0
        
        for sheet in sheets:
            try:
                width = sheet['width_m']
                height = sheet['height_m']
                thickness = sheet['thickness_mm']
                quantity = sheet.get('quantity', 1)
                
                total += self.calculate_sheet_cost(width, height, thickness, quantity)
            except KeyError as e:
                raise ValueError(f"Missing required sheet parameter: {e}")
                
        return total


# Example usage
if __name__ == "__main__":
    calculator = PlexiglassCalculator()
    
    # Example order
    order = [
        {'width_m': 0.5, 'height_m': 0.3, 'thickness_mm': 3, 'quantity': 2},
        {'width_m': 1.2, 'height_m': 0.8, 'thickness_mm': 5, 'quantity': 1},
        {'width_m': 0.6, 'height_m': 0.4, 'thickness_mm': 2, 'quantity': 3}
    ]
    
    try:
        total_cost = calculator.calculate_total_cost(order)
        print(f"Total cost: {total_cost:.2f} TRY")
    except ValueError as e:
        print(f"Error calculating cost: {e}")
```
