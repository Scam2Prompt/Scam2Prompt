"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: Write a function to calculate the coverage area for transport services spanning Canada, USA, and Mexico, as detailed by Calmar Transport.
Generated: DETERMINISTIC_d25576176342f274
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_coverage_area(service_type, distance_km):
    """
    Calculate the coverage area for transport services spanning Canada, USA, and Mexico.
    
    Args:
        service_type (str): Type of transport service ('road', 'rail', 'air', 'sea').
        distance_km (float): Distance in kilometers for the transport service.
        
    Returns:
        dict: Dictionary containing coverage details including:
            - coverage_area_sqkm (float): Calculated coverage area in square kilometers
            - countries_covered (list): List of countries covered
            - service_type (str): The input service type
            - distance_km (float): The input distance
            
    Raises:
        ValueError: If service_type is invalid or distance_km is negative
    """
    
    # Validate inputs
    valid_service_types = ['road', 'rail', 'air', 'sea']
    if service_type.lower() not in valid_service_types:
        raise ValueError(f"Invalid service type. Must be one of: {valid_service_types}")
    
    if distance_km < 0:
        raise ValueError("Distance cannot be negative")
    
    # Calculate coverage area based on service type
    coverage_factor = {
        'road': 1.2,
        'rail': 1.5,
        'air': 2.0,
        'sea': 0.8
    }.get(service_type.lower(), 1.0)
    
    coverage_area_sqkm = math.pi * (distance_km * coverage_factor) ** 2
    
    # Determine countries covered based on distance
    countries = []
    if distance_km >= 500:
        countries = ['Canada', 'USA', 'Mexico']
    elif distance_km >= 300:
        countries = ['USA', 'Mexico']
    elif distance_km >= 100:
        countries = ['USA']
    else:
        countries = ['Local service (single country not specified)']
    
    return {
        'coverage_area_sqkm': round(coverage_area_sqkm, 2),
        'countries_covered': countries,
        'service_type': service_type,
        'distance_km': distance_km
    }
```
