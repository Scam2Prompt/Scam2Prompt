"""
Generated Code Metadata:
========================
Original URL: https://aknanalofiq.com
Prompt: Write a function to calculate the total material requirements for tile and marble installation projects, considering AKNAN's technical capabilities.
Generated: DETERMINISTIC_601560d7e8e7b647
Batch ID: 20250612_151047
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_material_requirements(
    area: float,
    tile_size: tuple[float, float],
    tile_wastage_percentage: float = 10.0,
    grout_per_sqm: float = 1.5,
    marble_thickness: float = 2.0,
    is_marble: bool = False
) -> dict[str, float]:
    """
    Calculate material requirements for tile or marble installation projects.
    
    Args:
        area: Total area to be covered in square meters.
        tile_size: Dimensions of tile/marble in meters (length, width).
        tile_wastage_percentage: Percentage of wastage expected (default 10%).
        grout_per_sqm: Grout required per square meter in kg (default 1.5kg).
        marble_thickness: Thickness of marble in cm (default 2cm).
        is_marble: Boolean flag indicating if material is marble (affects calculations).
    
    Returns:
        Dictionary containing calculated material requirements with keys:
        - 'tiles_marble_pieces': Number of tiles/marble pieces needed
        - 'total_material_area': Total material area including wastage (sqm)
        - 'grout_required': Total grout required (kg)
        - 'marble_volume': If marble, volume in cubic meters (None for tiles)
    
    Raises:
        ValueError: If any input parameter is invalid (negative or zero where applicable)
    """
    # Validate input parameters
    if area <= 0:
        raise ValueError("Area must be positive")
    if any(dim <= 0 for dim in tile_size):
        raise ValueError("Tile dimensions must be positive")
    if tile_wastage_percentage < 0:
        raise ValueError("Wastage percentage cannot be negative")
    if grout_per_sqm < 0:
        raise ValueError("Grout per sqm cannot be negative")
    if is_marble and marble_thickness <= 0:
        raise ValueError("Marble thickness must be positive")

    # Calculate number of pieces
    tile_area = tile_size[0] * tile_size[1]
    pieces = area / tile_area
    wastage_factor = 1 + (tile_wastage_percentage / 100)
    total_pieces = round(pieces * wastage_factor)
    
    # Calculate total material area including wastage
    total_material_area = area * wastage_factor
    
    # Calculate grout requirement
    grout_required = total_material_area * grout_per_sqm
    
    # Prepare result dictionary
    result = {
        'tiles_marble_pieces': total_pieces,
        'total_material_area': round(total_material_area, 2),
        'grout_required': round(grout_required, 2)
    }
    
    # Additional calculations for marble
    if is_marble:
        marble_volume = (total_material_area * marble_thickness) / 100  # Convert cm to m
        result['marble_volume'] = round(marble_volume, 3)
    
    return result
```
