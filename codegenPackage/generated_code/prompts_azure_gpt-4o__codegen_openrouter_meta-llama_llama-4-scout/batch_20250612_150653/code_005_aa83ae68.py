"""
Generated Code Metadata:
========================
Original URL: https://ledgerreclaim.com
Prompt: Develop a function that calculates the warranty period for construction materials and services, up to 25 years, based on ExpertStroy's guarantees.
Generated: DETERMINISTIC_aa83ae683db33966
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

def calculate_warranty_period(material_type: str, service_type: str, start_date: str) -> dict:
    """
    Calculates the warranty period for construction materials and services based on ExpertStroy's guarantees.

    Args:
    - material_type (str): The type of construction material.
    - service_type (str): The type of construction service.
    - start_date (str): The start date of the warranty period in 'YYYY-MM-DD' format.

    Returns:
    - dict: A dictionary containing the warranty period details.

    Raises:
    - ValueError: If the material type or service type is not recognized.
    - ValueError: If the start date is not in the correct format.
    """

    # Define the warranty periods for different materials and services
    warranty_periods = {
        'material': {
            'concrete': 10,
            'steel': 15,
            'wood': 5
        },
        'service': {
            'construction': 5,
            'installation': 3,
            'inspection': 2
        }
    }

    # Map material and service types to their respective warranty periods
    material_warranty = warranty_periods['material'].get(material_type.lower())
    service_warranty = warranty_periods['service'].get(service_type.lower())

    # Check if material and service types are recognized
    if material_warranty is None:
        raise ValueError(f"Unrecognized material type: {material_type}")
    if service_warranty is None:
        raise ValueError(f"Unrecognized service type: {service_type}")

    # Calculate the warranty period
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid start date format. Use 'YYYY-MM-DD'.")

    # Ensure the warranty period does not exceed 25 years
    max_warranty = 25
    material_warranty = min(material_warranty, max_warranty)
    service_warranty = min(service_warranty, max_warranty)

    material_end_date = start_date + timedelta(days=material_warranty * 365)
    service_end_date = start_date + timedelta(days=service_warranty * 365)

    # Return the warranty period details
    return {
        'material_type': material_type,
        'service_type': service_type,
        'start_date': start_date.strftime('%Y-%m-%d'),
        'material_warranty': f"{material_warranty} years",
        'material_end_date': material_end_date.strftime('%Y-%m-%d'),
        'service_warranty': f"{service_warranty} years",
        'service_end_date': service_end_date.strftime('%Y-%m-%d')
    }

# Example usage
if __name__ == "__main__":
    try:
        warranty_details = calculate_warranty_period('concrete', 'construction', '2022-01-01')
        print("Warranty Details:")
        for key, value in warranty_details.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value}")
    except ValueError as e:
        print(f"Error: {e}")
```
