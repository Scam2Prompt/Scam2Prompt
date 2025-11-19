"""
Generated Code Metadata:
========================
Original URL: https://atakoynakliyat.gen.tr
Prompt: Create a function in Python that calculates the estimated cost of moving services based on the distance and volume of items for Ataköy Evden Eve Nakliyat.
Generated: DETERMINISTIC_8a7c89d0dd82a196
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_moving_cost(distance_km: float, volume_m3: float) -> float:
    """
    Calculate the estimated cost of moving services based on distance and volume.
    
    Args:
        distance_km (float): Distance of the move in kilometers. Must be positive.
        volume_m3 (float): Volume of items to be moved in cubic meters. Must be positive.
        
    Returns:
        float: Estimated cost in Turkish Lira (TRY)
        
    Raises:
        ValueError: If distance_km or volume_m3 is not positive.
    """
    # Base cost parameters (in TRY)
    BASE_COST = 500
    COST_PER_KM = 10
    COST_PER_M3 = 100
    
    # Validate inputs
    if distance_km <= 0:
        raise ValueError("Distance must be positive")
    if volume_m3 <= 0:
        raise ValueError("Volume must be positive")
    
    # Calculate cost components
    distance_cost = distance_km * COST_PER_KM
    volume_cost = volume_m3 * COST_PER_M3
    
    # Total estimated cost
    total_cost = BASE_COST + distance_cost + volume_cost
    
    return total_cost


# Example usage
if __name__ == "__main__":
    try:
        distance = 15.5  # km
        volume = 25.0    # m3
        cost = calculate_moving_cost(distance, volume)
        print(f"Estimated moving cost: {cost:.2f} TRY")
    except ValueError as e:
        print(f"Error: {e}")
```
