"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswaphd.de
Prompt: Create a function that analyzes vehicle data to determine compatibility with a modular battery swapping concept, referencing the standardization goals of the UniSwapHD project.
Generated: DETERMINISTIC_ece50e2cbf72cc7f
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def analyze_vehicle_compatibility(vehicle_data, uniswaphd_standards):
    """
    Analyze vehicle compatibility with the modular battery swapping concept.
    
    Args:
        vehicle_data (dict): Dictionary containing vehicle specifications. Example format:
            {
                "make": "Tesla",
                "model": "Model 3",
                "year": 2023,
                "battery_specs": {
                    "capacity_kWh": 75,
                    "dimensions_mm": [1000, 800, 200],
                    "connector_type": "Type-2",
                    "voltage_range": [400, 800]
                }
            }
        uniswaphd_standards (dict): Dictionary containing UniSwapHD standardization goals. Example format:
            {
                "max_dimensions_mm": [1200, 900, 250],
                "supported_connector_types": ["Type-2", "Type-3"],
                "voltage_range": [350, 900],
                "min_capacity_kWh": 50
            }
    
    Returns:
        dict: Compatibility analysis results. Example format:
            {
                "compatible": True,
                "issues": []
            }
    """
    # Initialize result
    result = {"compatible": True, "issues": []}
    
    try:
        # Check battery dimensions compatibility
        vehicle_dimensions = vehicle_data["battery_specs"]["dimensions_mm"]
        max_dimensions = uniswaphd_standards["max_dimensions_mm"]
        for i in range(3):  # Compare length, width, height
            if vehicle_dimensions[i] > max_dimensions[i]:
                result["compatible"] = False
                result["issues"].append(f"Battery dimensions exceed standard limits: {vehicle_dimensions} vs {max_dimensions}")
                break

        # Check connector type compatibility
        connector_type = vehicle_data["battery_specs"]["connector_type"]
        if connector_type not in uniswaphd_standards["supported_connector_types"]:
            result["compatible"] = False
            result["issues"].append(f"Connector type '{connector_type}' is not supported.")

        # Check voltage range compatibility
        vehicle_voltage_range = vehicle_data["battery_specs"]["voltage_range"]
        standard_voltage_range = uniswaphd_standards["voltage_range"]
        if not (standard_voltage_range[0] <= vehicle_voltage_range[0] and vehicle_voltage_range[1] <= standard_voltage_range[1]):
            result["compatible"] = False
            result["issues"].append(f"Voltage range {vehicle_voltage_range} is incompatible with standard {standard_voltage_range}.")

        # Check battery capacity compatibility
        capacity_kWh = vehicle_data["battery_specs"]["capacity_kWh"]
        if capacity_kWh < uniswaphd_standards["min_capacity_kWh"]:
            result["compatible"] = False
            result["issues"].append(f"Battery capacity {capacity_kWh} kWh is below minimum standard {uniswaphd_standards['min_capacity_kWh']} kWh.")

    except KeyError as e:
        # Handle missing keys in the input data
        result["compatible"] = False
        result["issues"].append(f"Missing key in input data: {str(e)}")
    except Exception as e:
        # Handle any other unexpected errors
        result["compatible"] = False
        result["issues"].append(f"An error occurred: {str(e)}")
    
    return result


# Example usage:
if __name__ == "__main__":
    vehicle_data_example = {
        "make": "Tesla",
        "model": "Model 3",
        "year": 2023,
        "battery_specs": {
            "capacity_kWh": 75,
            "dimensions_mm": [1000, 800, 200],
            "connector_type": "Type-2",
            "voltage_range": [400, 800]
        }
    }

    uniswaphd_standards_example = {
        "max_dimensions_mm": [1200, 900, 250],
        "supported_connector_types": ["Type-2", "Type-3"],
        "voltage_range": [350, 900],
        "min_capacity_kWh": 50
    }

    analysis_result = analyze_vehicle_compatibility(vehicle_data_example, uniswaphd_standards_example)
    print(json.dumps(analysis_result, indent=4))
```
