"""
Generated Code Metadata:
========================
Original URL: https://tibvanboxtel.nl
Prompt: Create a function to recommend the best PV divider setup for a meterkast installation, based on the specifications provided by Technische Installatiebedrijf van Boxtel.
Generated: DETERMINISTIC_9d75700172ef1ca0
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def recommend_pv_divider(
    pv_system_voltage: float,
    pv_system_power: float,
    meterkast_voltage: float = 230.0,
    max_current_per_divider: float = 16.0,
    safety_factor: float = 1.25
) -> dict:
    """
    Recommends the optimal PV divider setup for a meterkast installation.
    
    Args:
        pv_system_voltage: Voltage of the PV system in volts (V)
        pv_system_power: Total power of the PV system in watts (W)
        meterkast_voltage: Voltage of the meterkast (default 230V)
        max_current_per_divider: Maximum current per divider in amps (A)
        safety_factor: Safety factor for current calculation (default 1.25)
        
    Returns:
        dict: Dictionary containing recommended configuration:
            - 'dividers_needed': Number of dividers required
            - 'current_per_divider': Current per divider in amps (A)
            - 'divider_ratio': Recommended divider ratio
            - 'warnings': List of warnings if any
    
    Raises:
        ValueError: If input values are invalid
    """
    # Input validation
    if pv_system_voltage <= 0 or pv_system_power <= 0:
        raise ValueError("PV system voltage and power must be positive values")
    if meterkast_voltage <= 0:
        raise ValueError("Meterkast voltage must be positive")
    if max_current_per_divider <= 0:
        raise ValueError("Maximum current per divider must be positive")
    if safety_factor <= 1.0:
        raise ValueError("Safety factor must be greater than 1.0")
    
    warnings = []
    
    # Calculate total system current
    total_current = pv_system_power / pv_system_voltage
    
    # Calculate current per divider with safety factor
    safe_current_per_divider = max_current_per_divider / safety_factor
    
    # Calculate number of dividers needed
    dividers_needed = math.ceil(total_current / safe_current_per_divider)
    
    # Calculate actual current per divider
    current_per_divider = total_current / dividers_needed
    
    # Check if current is within safe limits
    if current_per_divider * safety_factor > max_current_per_divider:
        warnings.append("Warning: Current per divider exceeds safe limits with given safety factor")
    
    # Calculate divider ratio (PV voltage to meterkast voltage)
    divider_ratio = pv_system_voltage / meterkast_voltage
    
    # Check if ratio is reasonable
    if divider_ratio > 10:
        warnings.append("Warning: High divider ratio detected - consider voltage transformation")
    
    return {
        'dividers_needed': dividers_needed,
        'current_per_divider': round(current_per_divider, 2),
        'divider_ratio': round(divider_ratio, 2),
        'warnings': warnings
    }

# Example usage
if __name__ == "__main__":
    try:
        result = recommend_pv_divider(
            pv_system_voltage=600.0,
            pv_system_power=5000.0
        )
        print("Recommended PV Divider Setup:")
        print(f"Dividers needed: {result['dividers_needed']}")
        print(f"Current per divider: {result['current_per_divider']} A")
        print(f"Divider ratio: {result['divider_ratio']}:1")
        if result['warnings']:
            print("\nWarnings:")
            for warning in result['warnings']:
                print(f"- {warning}")
    except ValueError as e:
        print(f"Error: {e}")
```
