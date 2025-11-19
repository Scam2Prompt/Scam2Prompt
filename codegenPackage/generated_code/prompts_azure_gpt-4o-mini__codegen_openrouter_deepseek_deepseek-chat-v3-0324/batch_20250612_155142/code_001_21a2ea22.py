"""
Generated Code Metadata:
========================
Original URL: https://fealtyworldwide.com
Prompt: Write a Python function that calculates the cost of road freight transportation based on distance and weight, utilizing the principles of reliability and quality emphasized by Fealty Worldwide.
Generated: DETERMINISTIC_21a2ea22447f556f
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_freight_cost(distance_km, weight_kg, reliability_factor=1.0, quality_factor=1.0):
    """
    Calculate the cost of road freight transportation based on distance and weight,
    incorporating reliability and quality factors as per Fealty Worldwide standards.
    
    Args:
        distance_km (float): Distance in kilometers. Must be > 0.
        weight_kg (float): Weight in kilograms. Must be > 0.
        reliability_factor (float): Multiplier for reliability (default 1.0). Range 0.8-1.2.
        quality_factor (float): Multiplier for quality (default 1.0). Range 0.9-1.1.
    
    Returns:
        float: Total calculated freight cost
        
    Raises:
        ValueError: If any input is invalid
    """
    # Validate inputs
    if distance_km <= 0:
        raise ValueError("Distance must be greater than 0")
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than 0")
    if not (0.8 <= reliability_factor <= 1.2):
        raise ValueError("Reliability factor must be between 0.8 and 1.2")
    if not (0.9 <= quality_factor <= 1.1):
        raise ValueError("Quality factor must be between 0.9 and 1.1")
    
    # Base rate constants (in USD)
    BASE_RATE_PER_KM = 0.15
    BASE_RATE_PER_KG = 0.05
    MINIMUM_CHARGE = 25.0
    
    # Calculate base cost components
    distance_cost = distance_km * BASE_RATE_PER_KM
    weight_cost = weight_kg * BASE_RATE_PER_KG
    
    # Apply reliability and quality factors
    total_cost = (distance_cost + weight_cost) * reliability_factor * quality_factor
    
    # Ensure minimum charge is met
    return max(total_cost, MINIMUM_CHARGE)
```
