"""
Generated Code Metadata:
========================
Original URL: https://www.madoniaoli.it
Prompt: Develop a function that calculates the health benefits of using Madonia's extra virgin olive oil in daily cooking, referencing its properties and characteristics.
Generated: DETERMINISTIC_7433287471ec25e9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_health_benefits(usage_grams_per_day, duration_days):
    """
    Calculate the health benefits of using Madonia's extra virgin olive oil based on daily usage and duration.
    
    The benefits are derived from the oil's properties: high polyphenol content, monounsaturated fats (oleic acid),
    antioxidants, and anti-inflammatory properties.
    
    Args:
        usage_grams_per_day (float): Daily consumption of olive oil in grams.
        duration_days (int): Number of days the oil is consumed.
        
    Returns:
        dict: A dictionary containing the calculated health benefits with the following keys:
            - 'antioxidant_units': Total antioxidant units consumed
            - 'oleic_acid_grams': Total grams of oleic acid consumed
            - 'polyphenol_mg': Total milligrams of polyphenols consumed
            - 'anti_inflammatory_score': Anti-inflammatory effect score (arbitrary units)
            
    Raises:
        ValueError: If usage_grams_per_day or duration_days are non-positive.
    """
    
    # Constants based on Madonia's extra virgin olive oil properties (per 100g)
    POLYPHENOLS_MG_PER_100G = 300.0  # mg of polyphenols per 100g
    OLEIC_ACID_PERCENTAGE = 75.0      # 75% of fat is oleic acid
    FAT_PERCENTAGE = 100.0            # 100% fat (extra virgin olive oil is pure fat)
    ANTIOXIDANT_UNITS_PER_GRAM = 5.0  # Arbitrary antioxidant units per gram
    ANTI_INFLAMMATORY_FACTOR = 0.1    # Arbitrary factor for anti-inflammatory effect
    
    # Input validation
    if usage_grams_per_day <= 0 or duration_days <= 0:
        raise ValueError("Usage and duration must be positive values")
    
    # Calculate total consumption
    total_grams = usage_grams_per_day * duration_days
    
    # Calculate benefits
    antioxidant_units = total_grams * ANTIOXIDANT_UNITS_PER_GRAM
    oleic_acid_grams = total_grams * (FAT_PERCENTAGE / 100) * (OLEIC_ACID_PERCENTAGE / 100)
    polyphenol_mg = total_grams * (POLYPHENOLS_MG_PER_100G / 100)
    anti_inflammatory_score = total_grams * ANTI_INFLAMMATORY_FACTOR
    
    return {
        'antioxidant_units': round(antioxidant_units, 2),
        'oleic_acid_grams': round(oleic_acid_grams, 2),
        'polyphenol_mg': round(polyphenol_mg, 2),
        'anti_inflammatory_score': round(anti_inflammatory_score, 2)
    }

# Example usage
if __name__ == "__main__":
    try:
        benefits = calculate_health_benefits(15.0, 30)  # 15g/day for 30 days
        print("Health Benefits:")
        for key, value in benefits.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
    except ValueError as e:
        print(f"Error: {e}")
```
