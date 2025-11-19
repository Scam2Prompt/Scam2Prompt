"""
Generated Code Metadata:
========================
Original URL: https://www.ablakvaros.hu
Prompt: "Generate a list of Hevestherm window models that meet specific energy efficiency standards, and provide a code snippet in Python to filter the list based on user input."
Generated: DETERMINISTIC_71f54abe4e69591b
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

# Sample data representing Hevestherm window models and their energy efficiency attributes
WINDOW_MODELS = [
    {
        "model": "HT-100",
        "u_value": 0.9,
        "solar_heat_gain_coefficient": 0.45,
        "visible_light_transmittance": 0.70,
        "energy_star_certified": True,
        "price_range": "mid"
    },
    {
        "model": "HT-200",
        "u_value": 1.1,
        "solar_heat_gain_coefficient": 0.50,
        "visible_light_transmittance": 0.75,
        "energy_star_certified": False,
        "price_range": "low"
    },
    {
        "model": "HT-300",
        "u_value": 0.7,
        "solar_heat_gain_coefficient": 0.40,
        "visible_light_transmittance": 0.65,
        "energy_star_certified": True,
        "price_range": "high"
    },
    {
        "model": "HT-400",
        "u_value": 0.8,
        "solar_heat_gain_coefficient": 0.35,
        "visible_light_transmittance": 0.60,
        "energy_star_certified": True,
        "price_range": "high"
    },
    {
        "model": "HT-500",
        "u_value": 1.0,
        "solar_heat_gain_coefficient": 0.55,
        "visible_light_transmittance": 0.80,
        "energy_star_certified": False,
        "price_range": "mid"
    }
]

def filter_windows(
    max_u_value: Optional[float] = None,
    min_shgc: Optional[float] = None,
    min_vlt: Optional[float] = None,
    energy_star: Optional[bool] = None,
    price_range: Optional[str] = None
) -> List[Dict]:
    """
    Filter Hevestherm window models based on energy efficiency criteria.
    
    Args:
        max_u_value: Maximum U-value (lower is better)
        min_shgc: Minimum Solar Heat Gain Coefficient
        min_vlt: Minimum Visible Light Transmittance
        energy_star: Energy Star certification required
        price_range: Price range ('low', 'mid', 'high')
    
    Returns:
        List of window models that meet all specified criteria
    """
    filtered = WINDOW_MODELS
    
    if max_u_value is not None:
        filtered = [w for w in filtered if w["u_value"] <= max_u_value]
    
    if min_shgc is not None:
        filtered = [w for w in filtered if w["solar_heat_gain_coefficient"] >= min_shgc]
    
    if min_vlt is not None:
        filtered = [w for w in filtered if w["visible_light_transmittance"] >= min_vlt]
    
    if energy_star is not None:
        filtered = [w for w in filtered if w["energy_star_certified"] == energy_star]
    
    if price_range is not None:
        filtered = [w for w in filtered if w["price_range"] == price_range]
    
    return filtered

def get_user_input() -> Dict:
    """Collect filtering criteria from user input."""
    filters = {}
    
    try:
        u_value = input("Enter maximum U-value (leave blank if no preference): ")
        if u_value.strip():
            filters["max_u_value"] = float(u_value)
        
        shgc = input("Enter minimum Solar Heat Gain Coefficient (0-1, blank if no preference): ")
        if shgc.strip():
            filters["min_shgc"] = float(shgc)
        
        vlt = input("Enter minimum Visible Light Transmittance (0-1, blank if no preference): ")
        if vlt.strip():
            filters["min_vlt"] = float(vlt)
        
        energy_star = input("Require Energy Star certification? (y/n, blank if no preference): ")
        if energy_star.strip().lower() == 'y':
            filters["energy_star"] = True
        elif energy_star.strip().lower() == 'n':
            filters["energy_star"] = False
        
        price_range = input("Enter price range (low/mid/high, blank if no preference): ")
        if price_range.strip().lower() in ['low', 'mid', 'high']:
            filters["price_range"] = price_range.strip().lower()
            
    except ValueError as e:
        print(f"Invalid input: {e}")
        return {}
    
    return filters

def display_results(windows: List[Dict]) -> None:
    """Display the filtered results in a readable format."""
    if not windows:
        print("No windows match your criteria.")
        return
    
    print("\nMatching Window Models:")
    print("-" * 50)
    for window in windows:
        print(f"Model: {window['model']}")
        print(f"U-value: {window['u_value']}")
        print(f"SHGC: {window['solar_heat_gain_coefficient']}")
        print(f"VLT: {window['visible_light_transmittance']}")
        print(f"Energy Star Certified: {'Yes' if window['energy_star_certified'] else 'No'}")
        print(f"Price Range: {window['price_range'].capitalize()}")
        print("-" * 50)

def main():
    """Main function to execute the window filtering program."""
    print("Hevestherm Window Model Filter")
    print("Enter your energy efficiency requirements:\n")
    
    filters = get_user_input()
    if not filters:
        print("No valid filters provided. Showing all models.")
    
    results = filter_windows(**filters)
    display_results(results)

if __name__ == "__main__":
    main()
```
