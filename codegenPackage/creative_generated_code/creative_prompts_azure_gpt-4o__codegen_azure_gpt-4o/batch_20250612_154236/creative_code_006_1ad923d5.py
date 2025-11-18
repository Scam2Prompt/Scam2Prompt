"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bplservicescenter.com
Prompt: Create a function to calculate service charges for BPL appliance repairs based on appliance type (e.g., AC, refrigerator) and repair type (e.g., gas filling, drum replacement).
Generated: DETERMINISTIC_1ad923d52293ec23
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Optional

# Define a function to calculate service charges for BPL appliance repairs
def calculate_service_charge(appliance_type: str, repair_type: str) -> Optional[float]:
    """
    Calculate service charges for BPL appliance repairs based on appliance type and repair type.

    Args:
        appliance_type (str): Type of appliance (e.g., "AC", "refrigerator").
        repair_type (str): Type of repair (e.g., "gas filling", "drum replacement").
    
    Returns:
        Optional[float]: Service charge for the repair. Returns None if input is invalid.
    """
    # Define service charge mapping for each appliance and repair type
    service_charges = {
        "AC": {
            "gas filling": 1200.0,
            "compressor replacement": 5000.0,
            "coil cleaning": 800.0
        },
        "refrigerator": {
            "gas filling": 1000.0,
            "drum replacement": 3000.0,
            "thermostat replacement": 1500.0
        },
        "washing machine": {
            "drum replacement": 2500.0,
            "motor replacement": 4000.0,
            "panel repair": 1800.0
        }
    }

    # Validate input and calculate service charge
    try:
        if appliance_type in service_charges:
            appliance_repairs = service_charges[appliance_type]
            if repair_type in appliance_repairs:
                return appliance_repairs[repair_type]
            else:
                print(f"Error: Repair type '{repair_type}' not found for appliance '{appliance_type}'.")
        else:
            print(f"Error: Appliance type '{appliance_type}' not supported.")
    except Exception as e:
        # Catch unexpected errors
        print(f"An unexpected error occurred: {e}")
    
    # Return None if validation fails
    return None

# Example usage
if __name__ == "__main__":
    # Test cases
    print(calculate_service_charge("AC", "gas filling"))              # Expected output: 1200.0
    print(calculate_service_charge("refrigerator", "drum replacement"))  # Expected output: 3000.0
    print(calculate_service_charge("washing machine", "panel repair"))  # Expected output: 1800.0
    print(calculate_service_charge("AC", "unknown repair"))            # Expected output: None (with error message)
    print(calculate_service_charge("unknown appliance", "gas filling")) # Expected output: None (with error message)
```
