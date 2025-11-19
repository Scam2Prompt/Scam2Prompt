"""
Generated Code Metadata:
========================
Original URL: https://neumayaa.com.ar
Prompt: Write Python code to calculate TKPH (Toneladas Kilómetros por Hora) for a specific tire based on its load capacity, distance traveled, and ambient temperature, as described on the Neumayaa website.
Generated: DETERMINISTIC_29596fc20d98303d
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_tkph(load_capacity_kg, distance_km, operating_hours, ambient_temp_c):
    """
    Calculate TKPH (Toneladas Kilómetros por Hora) for a tire.
    
    Parameters:
        load_capacity_kg (float): Load capacity in kilograms
        distance_km (float): Distance traveled in kilometers
        operating_hours (float): Total operating hours
        ambient_temp_c (float): Ambient temperature in Celsius
    
    Returns:
        float: Calculated TKPH value
    
    Raises:
        ValueError: If any input parameter is negative or zero (except temperature)
    """
    # Validate input parameters
    if load_capacity_kg <= 0:
        raise ValueError("Load capacity must be positive")
    if distance_km <= 0:
        raise ValueError("Distance must be positive")
    if operating_hours <= 0:
        raise ValueError("Operating hours must be positive")
    
    # Convert load capacity from kg to tons
    load_capacity_tons = load_capacity_kg / 1000
    
    # Calculate average speed (km/h)
    average_speed = distance_km / operating_hours
    
    # Calculate TKPH
    tkph = load_capacity_tons * average_speed
    
    # Apply temperature correction factor if temperature exceeds 38°C
    if ambient_temp_c > 38:
        correction_factor = 1 + ((ambient_temp_c - 38) * 0.01)
        tkph *= correction_factor
    
    return tkph


def get_tire_tkph_rating(manufacturer, tire_model):
    """
    Get the manufacturer's TKPH rating for a specific tire model.
    This would typically be replaced with actual database lookup in production.
    
    Parameters:
        manufacturer (str): Tire manufacturer name
        tire_model (str): Tire model identifier
    
    Returns:
        float: Manufacturer's TKPH rating for the tire
    
    Raises:
        ValueError: If tire model is not found
    """
    # This is a mock implementation - in production, this would query a database
    tire_ratings = {
        ("Neumayaa", "NM-1000"): 350.0,
        ("Neumayaa", "NM-2000"): 420.0,
        ("OtherBrand", "OB-X1"): 380.0,
    }
    
    try:
        return tire_ratings[(manufacturer, tire_model)]
    except KeyError:
        raise ValueError(f"TKPH rating not found for {manufacturer} {tire_model}")


def check_tire_usage(load_capacity_kg, distance_km, operating_hours, ambient_temp_c, manufacturer, tire_model):
    """
    Check if tire usage is within recommended TKPH limits.
    
    Parameters:
        load_capacity_kg (float): Load capacity in kilograms
        distance_km (float): Distance traveled in kilometers
        operating_hours (float): Total operating hours
        ambient_temp_c (float): Ambient temperature in Celsius
        manufacturer (str): Tire manufacturer name
        tire_model (str): Tire model identifier
    
    Returns:
        dict: Dictionary containing calculated TKPH, rating, and safety status
    """
    try:
        calculated_tkph = calculate_tkph(load_capacity_kg, distance_km, operating_hours, ambient_temp_c)
        rated_tkph = get_tire_tkph_rating(manufacturer, tire_model)
        
        safety_margin = 0.9  # 10% safety margin
        is_safe = calculated_tkph <= (rated_tkph * safety_margin)
        
        return {
            "calculated_tkph": round(calculated_tkph, 2),
            "rated_tkph": rated_tkph,
            "is_within_limits": is_safe,
            "safety_margin_percent": 10,
            "message": "Usage is within safe limits" if is_safe else "Warning: Usage exceeds recommended limits"
        }
    except ValueError as e:
        return {
            "error": str(e),
            "is_within_limits": False,
            "message": f"Error in calculation: {str(e)}"
        }
```
