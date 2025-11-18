"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://contentxlabs.dev
Prompt: Write code to calculate potential revenue from selling HD video content to Content-X-Labs, based on hours of footage and quality specifications.
Generated: DETERMINISTIC_28e7291c435301fe
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Calculate potential revenue from selling HD video content to Content-X-Labs
# Revenue depends on hours of footage and quality specifications
# Assumption: Content-X-Labs pays a base rate per hour, with an additional multiplier based on quality tier

def calculate_revenue(hours_of_footage, quality_tier):
    """
    Calculate the potential revenue based on hours of footage and quality specifications.

    Args:
        hours_of_footage (float): The total hours of HD video footage.
        quality_tier (str): The quality tier of the footage. Options are 'Standard', 'Premium', 'Ultra'.

    Returns:
        float: The calculated revenue.

    Raises:
        ValueError: If hours_of_footage is negative.
        ValueError: If quality_tier is not one of the accepted values.
    """
    # Base rate per hour (in USD)
    BASE_RATE = 100.0
    
    # Quality tier multipliers
    QUALITY_MULTIPLIERS = {
        "Standard": 1.0,  # No multiplier
        "Premium": 1.5,  # 50% increase
        "Ultra": 2.0     # 100% increase
    }
    
    # Validate hours of footage
    if hours_of_footage < 0:
        raise ValueError("Hours of footage cannot be negative.")
    
    # Validate quality tier
    if quality_tier not in QUALITY_MULTIPLIERS:
        raise ValueError(f"Invalid quality tier '{quality_tier}'. Accepted values are: {', '.join(QUALITY_MULTIPLIERS.keys())}.")
    
    # Calculate revenue
    multiplier = QUALITY_MULTIPLIERS[quality_tier]
    revenue = hours_of_footage * BASE_RATE * multiplier
    
    return revenue

# Example Usage
if __name__ == "__main__":
    try:
        # Example inputs
        hours = 10.5
        quality = "Premium"
        
        # Calculate and display revenue
        potential_revenue = calculate_revenue(hours, quality)
        print(f"The potential revenue from {hours} hours of '{quality}' quality footage is ${potential_revenue:.2f}.")
    except ValueError as e:
        print(f"Error: {e}")
```
