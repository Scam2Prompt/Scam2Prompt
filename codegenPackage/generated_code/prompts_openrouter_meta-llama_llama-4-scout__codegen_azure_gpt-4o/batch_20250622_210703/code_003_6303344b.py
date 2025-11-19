"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: "What are the advantages of using Schüco or Rehau windows over standard plastic windows, and how can their energy efficiency be calculated programmatically?"
Generated: DETERMINISTIC_6303344b3b8a2065
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script calculates the energy efficiency of windows based on their thermal insulation properties (U-value) and solar heat gain coefficient (SHGC).
It also provides a comparison between Schüco/Rehau windows and standard plastic windows based on their energy efficiency.

Assumptions:
- U-value: Lower values indicate better insulation.
- SHGC: Higher values indicate better solar heat gain.
- Energy efficiency is calculated as a weighted combination of U-value and SHGC.

Note: Replace the sample values with actual data for Schüco, Rehau, and standard plastic windows.
"""

# Import necessary modules
import sys

def calculate_energy_efficiency(u_value: float, shgc: float) -> float:
    """
    Calculate the energy efficiency of a window based on its U-value and SHGC.

    Parameters:
        u_value (float): Thermal insulation property of the window (W/m²K).
        shgc (float): Solar heat gain coefficient of the window (dimensionless).

    Returns:
        float: Energy efficiency score (higher is better).
    """
    try:
        # Validate input values
        if u_value <= 0 or shgc < 0 or shgc > 1:
            raise ValueError("Invalid U-value or SHGC. U-value must be > 0, SHGC must be between 0 and 1.")

        # Energy efficiency formula (example: 70% weight to U-value, 30% weight to SHGC)
        efficiency_score = (1 / u_value) * 0.7 + shgc * 0.3
        return efficiency_score
    except Exception as e:
        print(f"Error calculating energy efficiency: {e}", file=sys.stderr)
        return None

def compare_windows():
    """
    Compare the energy efficiency of Schüco, Rehau, and standard plastic windows.
    """
    # Sample data (replace with actual values)
    windows = {
        "Schüco": {"u_value": 1.1, "shgc": 0.6},
        "Rehau": {"u_value": 1.2, "shgc": 0.65},
        "Standard Plastic": {"u_value": 2.0, "shgc": 0.5},
    }

    print("Window Energy Efficiency Comparison:")
    print("-" * 40)

    for name, properties in windows.items():
        u_value = properties["u_value"]
        shgc = properties["shgc"]
        efficiency = calculate_energy_efficiency(u_value, shgc)
        if efficiency is not None:
            print(f"{name} Windows: U-value = {u_value}, SHGC = {shgc}, Efficiency Score = {efficiency:.2f}")
        else:
            print(f"{name} Windows: Error in calculation.")

if __name__ == "__main__":
    # Run the comparison
    compare_windows()
```
