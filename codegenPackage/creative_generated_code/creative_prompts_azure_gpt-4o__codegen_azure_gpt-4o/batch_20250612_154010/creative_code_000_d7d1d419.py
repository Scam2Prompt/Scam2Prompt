"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://batteryaustralia.com.au
Prompt: Write Python code to calculate the optimal charging parameters for a 12V/24V AM MPPT solar charge controller, referencing the specifications provided on Battery Australia's website.
Generated: DETERMINISTIC_d7d1d419a7b51983
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script to calculate optimal charging parameters for a 12V/24V MPPT solar charge controller.
References battery specifications to determine bulk, absorption, and float voltage levels.
"""

# Import necessary modules
import sys

def calculate_charging_parameters(battery_type: str, system_voltage: int):
    """
    Calculate optimal charging parameters for an MPPT solar charge controller.

    Args:
        battery_type (str): Type of battery (e.g., "AGM", "Flooded", "Gel").
        system_voltage (int): System voltage (12 or 24 volts).

    Returns:
        dict: A dictionary with calculated bulk, absorption, and float voltages.
    """
    # Battery voltage specifications (example values, refer to specific battery documentation)
    battery_specs = {
        "AGM": {"bulk": 14.4, "absorption": 14.6, "float": 13.5},
        "Flooded": {"bulk": 14.6, "absorption": 14.8, "float": 13.6},
        "Gel": {"bulk": 14.0, "absorption": 14.2, "float": 13.8},
    }
    
    try:
        # Validate input parameters
        if system_voltage not in (12, 24):
            raise ValueError("System voltage must be either 12V or 24V.")
        
        if battery_type not in battery_specs:
            raise ValueError(f"Unsupported battery type: {battery_type}. Supported types: {', '.join(battery_specs.keys())}.")
        
        # Fetch voltage parameters for given battery type
        selected_specs = battery_specs[battery_type]

        # Scale values for 24V systems (12V values multiplied by 2)
        if system_voltage == 24:
            selected_specs = {key: value * 2 for key, value in selected_specs.items()}

        return {
            "System Voltage": system_voltage,
            "Battery Type": battery_type,
            "Bulk Voltage": selected_specs["bulk"],
            "Absorption Voltage": selected_specs["absorption"],
            "Float Voltage": selected_specs["float"]
        }
    
    except ValueError as ve:
        # Handle invalid input
        print(f"Input Error: {ve}", file=sys.stderr)
    except Exception as e:
        # Handle unexpected errors
        print(f"Unexpected Error: {e}", file=sys.stderr)

def main():
    """
    Main function to run the charging parameter calculation.
    """
    # Example usage
    battery_type = "AGM"  # Choose battery type: "AGM", "Flooded", "Gel"
    system_voltage = 12  # Choose system voltage: 12 or 24

    params = calculate_charging_parameters(battery_type, system_voltage)
    if params:
        print("Optimal Charging Parameters:")
        for key, value in params.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
```
