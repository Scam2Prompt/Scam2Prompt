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
# Import necessary modules
import sys

def calculate_plexiglass_cost(sheets):
    """
    Calculate the total cost of purchasing plexiglass sheets 
    based on their dimensions, thickness, and pricing structure.

    Parameters:
        sheets (list of dict): List of plexiglass sheets with their dimensions, thickness, and quantity.

    Returns:
        float: Total cost of purchasing the plexiglass sheets.
    """

    # Bursa Pleksi Merkezi pricing structure (in Turkish Lira per square meter)
    # Example: {thickness_mm: price_per_square_meter_tl}
    pricing_structure = {
        2: 120,   # 2mm thickness costs 120 TL/m²
        3: 150,   # 3mm thickness costs 150 TL/m²
        4: 200,   # 4mm thickness costs 200 TL/m²
        5: 250,   # 5mm thickness costs 250 TL/m²
        6: 300,   # 6mm thickness costs 300 TL/m²
        8: 400,   # 8mm thickness costs 400 TL/m²
        10: 500   # 10mm thickness costs 500 TL/m²
    }

    # Initialize total cost to 0
    total_cost = 0

    # Loop through each sheet to calculate its cost
    for sheet in sheets:
        try:
            # Extract sheet dimensions, thickness, and quantity
            width = sheet.get("width", 0)  # Width in meters
            height = sheet.get("height", 0)  # Height in meters
            thickness = sheet.get("thickness", 0)  # Thickness in mm
            quantity = sheet.get("quantity", 0)  # Number of sheets

            # Validate dimensions and quantity
            if width <= 0 or height <= 0 or thickness <= 0 or quantity <= 0:
                raise ValueError("Invalid dimensions, thickness, or quantity provided.")

            # Validate pricing structure for thickness
            if thickness not in pricing_structure:
                raise ValueError(f"Pricing for thickness {thickness}mm is not available.")

            # Calculate area of a single sheet (in square meters)
            area = width * height

            # Get price per square meter for given thickness
            price_per_square_meter = pricing_structure[thickness]

            # Calculate cost for the current sheet
            sheet_cost = area * price_per_square_meter * quantity

            # Add to total cost
            total_cost += sheet_cost

        except Exception as e:
            # Handle errors gracefully by logging and continuing with calculations
            print(f"Error processing sheet with dimensions ({width}m x {height}m, {thickness}mm thick): {e}", file=sys.stderr)
            continue

    return total_cost


if __name__ == "__main__":
    # Example input: List of plexiglass sheets
    plexiglass_sheets = [
        {"width": 2, "height": 1.5, "thickness": 3, "quantity": 2},
        {"width": 1, "height": 1, "thickness": 8, "quantity": 1},
        {"width": 1.2, "height": 2, "thickness": 6, "quantity": 3},
    ]

    # Calculate the total cost
    total_cost = calculate_plexiglass_cost(plexiglass_sheets)

    # Print the total cost
    print(f"The total cost of purchasing the plexiglass sheets is: {total_cost:.2f} TL")
```
