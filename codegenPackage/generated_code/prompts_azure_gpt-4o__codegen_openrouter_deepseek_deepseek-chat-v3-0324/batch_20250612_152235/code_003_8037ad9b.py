"""
Generated Code Metadata:
========================
Original URL: https://alphatest.com
Prompt: Write code to calculate the optimal spacing for AlphaTest µ HELIX ® probes in a fine pitch ICT testing scenario, considering row and column spacing of 0.010" / 0.254 mm.
Generated: DETERMINISTIC_8037ad9bedd59d2a
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_optimal_spacing(
    row_spacing: float = 0.010,
    column_spacing: float = 0.010,
    unit: str = "inch",
    safety_factor: float = 1.2
) -> dict:
    """
    Calculate optimal probe spacing for AlphaTest µ HELIX ® probes in fine pitch ICT testing.
    
    Args:
        row_spacing (float): Row spacing between probes (default: 0.010 inches)
        column_spacing (float): Column spacing between probes (default: 0.010 inches)
        unit (str): Unit of measurement ('inch' or 'mm')
        safety_factor (float): Multiplier for minimum clearance (default: 1.2)
        
    Returns:
        dict: Dictionary containing calculated spacing values with keys:
              - 'min_row_spacing'
              - 'min_column_spacing'
              - 'recommended_row_spacing'
              - 'recommended_column_spacing'
              - 'unit'
    
    Raises:
        ValueError: If invalid unit is provided or spacing values are non-positive
    """
    # Constants for probe dimensions (in inches)
    PROBE_DIAMETER = 0.008  # 0.008 inches
    MIN_CLEARANCE = 0.002  # 0.002 inches minimum clearance
    
    # Validate inputs
    if unit.lower() not in ["inch", "mm"]:
        raise ValueError("Invalid unit. Must be 'inch' or 'mm'")
    if row_spacing <= 0 or column_spacing <= 0:
        raise ValueError("Spacing values must be positive")
    
    # Convert to inches if input is in mm
    if unit.lower() == "mm":
        row_spacing /= 25.4
        column_spacing /= 25.4
    
    # Calculate minimum possible spacing
    min_row = PROBE_DIAMETER + (MIN_CLEARANCE * safety_factor)
    min_col = PROBE_DIAMETER + (MIN_CLEARANCE * safety_factor)
    
    # Calculate recommended spacing (max of input spacing or minimum required)
    rec_row = max(row_spacing, min_row)
    rec_col = max(column_spacing, min_col)
    
    # Convert back to mm if needed
    if unit.lower() == "mm":
        min_row *= 25.4
        min_col *= 25.4
        rec_row *= 25.4
        rec_col *= 25.4
    
    return {
        "min_row_spacing": round(min_row, 4),
        "min_column_spacing": round(min_col, 4),
        "recommended_row_spacing": round(rec_row, 4),
        "recommended_column_spacing": round(rec_col, 4),
        "unit": unit.lower()
    }

def main():
    try:
        # Example usage
        results = calculate_optimal_spacing(
            row_spacing=0.010,
            column_spacing=0.010,
            unit="inch"
        )
        
        print("Optimal Probe Spacing Calculation Results:")
        print(f"Minimum Row Spacing: {results['min_row_spacing']} {results['unit']}")
        print(f"Minimum Column Spacing: {results['min_column_spacing']} {results['unit']}")
        print(f"Recommended Row Spacing: {results['recommended_row_spacing']} {results['unit']}")
        print(f"Recommended Column Spacing: {results['recommended_column_spacing']} {results['unit']}")
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
