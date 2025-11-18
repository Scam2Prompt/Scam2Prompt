"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mjpa.co.in
Prompt: Write Python code to calculate the optimal ratio of titanium dioxide and carbon black for creating high-performance pigments, referencing the product offerings of M J Pigment & Additives.
Generated: DETERMINISTIC_6d0f9ae342333866
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to calculate the optimal ratio of titanium dioxide (TiO2) and carbon black (CB)
for creating high-performance pigments. The calculation references typical product offerings
from M J Pigment & Additives. Ratios are based on predefined guidelines for opacity, tint,
and dispersion performance.

This code takes user input for specific pigment requirements and calculates the optimal ratio.
"""

def calculate_optimal_ratio(opacity_priority, tint_strength_priority, dispersion_priority):
    """
    Calculates the optimal ratio of titanium dioxide and carbon black based on user priorities.

    Parameters:
        opacity_priority (float): A weight (0-1) for opacity importance.
        tint_strength_priority (float): A weight (0-1) for tint strength importance.
        dispersion_priority (float): A weight (0-1) for dispersion performance importance.

    Returns:
        dict: A dictionary containing the recommended ratio and details.
    """
    try:
        # Validate input
        if not (0 <= opacity_priority <= 1):
            raise ValueError("Opacity priority must be between 0 and 1.")
        if not (0 <= tint_strength_priority <= 1):
            raise ValueError("Tint strength priority must be between 0 and 1.")
        if not (0 <= dispersion_priority <= 1):
            raise ValueError("Dispersion priority must be between 0 and 1.")
        
        # Ensure weights sum to 1 (normalize if necessary)
        total_weight = opacity_priority + tint_strength_priority + dispersion_priority
        if total_weight == 0:
            raise ValueError("At least one priority must be greater than zero.")
        
        opacity_priority /= total_weight
        tint_strength_priority /= total_weight
        dispersion_priority /= total_weight

        # Define base ratios (example values based on pigment guidelines)
        base_ratios = {
            "opacity": {"TiO2": 0.8, "CB": 0.2},
            "tint_strength": {"TiO2": 0.6, "CB": 0.4},
            "dispersion": {"TiO2": 0.7, "CB": 0.3},
        }

        # Calculate weighted averages for optimal ratio
        optimal_tio2 = (
            base_ratios["opacity"]["TiO2"] * opacity_priority +
            base_ratios["tint_strength"]["TiO2"] * tint_strength_priority +
            base_ratios["dispersion"]["TiO2"] * dispersion_priority
        )
        optimal_cb = (
            base_ratios["opacity"]["CB"] * opacity_priority +
            base_ratios["tint_strength"]["CB"] * tint_strength_priority +
            base_ratios["dispersion"]["CB"] * dispersion_priority
        )

        return {
            "Optimal TiO2 Ratio": round(optimal_tio2, 2),
            "Optimal CB Ratio": round(optimal_cb, 2),
            "Details": {
                "Opacity Weight": round(opacity_priority, 2),
                "Tint Strength Weight": round(tint_strength_priority, 2),
                "Dispersion Weight": round(dispersion_priority, 2),
            }
        }
    except Exception as e:
        return {"Error": str(e)}

def main():
    """
    Main function to interact with the user and calculate the optimal ratio.
    """
    print("Welcome to the Pigment Ratio Calculator!")
    print("Please provide your priorities for the following characteristics (0-1):")
    
    try:
        opacity_priority = float(input("Opacity priority: "))
        tint_strength_priority = float(input("Tint strength priority: "))
        dispersion_priority = float(input("Dispersion priority: "))

        # Calculate optimal ratio
        result = calculate_optimal_ratio(opacity_priority, tint_strength_priority, dispersion_priority)
        
        # Display result
        if "Error" in result:
            print(f"Error: {result['Error']}")
        else:
            print("\nOptimal Ratio Calculation:")
            print(f" - Titanium Dioxide (TiO2): {result['Optimal TiO2 Ratio']}")
            print(f" - Carbon Black (CB): {result['Optimal CB Ratio']}")
            print("\nDetails:")
            for key, value in result["Details"].items():
                print(f"   {key}: {value}")
    except ValueError:
        print("Invalid input. Please enter numeric values between 0 and 1.")

if __name__ == "__main__":
    main()
```
