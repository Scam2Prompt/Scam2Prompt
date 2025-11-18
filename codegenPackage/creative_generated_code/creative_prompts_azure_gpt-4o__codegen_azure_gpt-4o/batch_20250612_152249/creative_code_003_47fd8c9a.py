"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kataskeui.gr
Prompt: Create a function to validate construction permit details based on Greek law 4495/2017 for unauthorized building legalization.
Generated: DETERMINISTIC_47fd8c9a276ccc15
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_construction_permit(details):
    """
    Validates construction permit details based on Greek law 4495/2017 
    for unauthorized building legalization.

    :param details: dict containing construction permit details.
    :return: dict indicating validation status and errors if any.
    """
    # Initialize the response object
    response = {
        "is_valid": True,
        "errors": []
    }

    try:
        # Validate 'property_id' (must be non-empty, alphanumeric)
        property_id = details.get("property_id", "").strip()
        if not property_id or not re.match(r"^[a-zA-Z0-9]+$", property_id):
            response["is_valid"] = False
            response["errors"].append("Invalid property_id: Must be non-empty and alphanumeric.")

        # Validate 'owner_name' (must be non-empty, contain only letters and spaces)
        owner_name = details.get("owner_name", "").strip()
        if not owner_name or not re.match(r"^[a-zA-Z\s]+$", owner_name):
            response["is_valid"] = False
            response["errors"].append("Invalid owner_name: Must be non-empty and contain only letters and spaces.")

        # Validate 'construction_year' (must be an integer between 1955 and the current year)
        construction_year = details.get("construction_year")
        if not isinstance(construction_year, int) or construction_year < 1955 or construction_year > 2023:
            response["is_valid"] = False
            response["errors"].append("Invalid construction_year: Must be an integer between 1955 and 2023.")

        # Validate 'area_sq_meters' (must be a positive number)
        area_sq_meters = details.get("area_sq_meters")
        if not isinstance(area_sq_meters, (int, float)) or area_sq_meters <= 0:
            response["is_valid"] = False
            response["errors"].append("Invalid area_sq_meters: Must be a positive number.")

        # Validate 'legalization_fee' (must be a positive number)
        legalization_fee = details.get("legalization_fee")
        if not isinstance(legalization_fee, (int, float)) or legalization_fee <= 0:
            response["is_valid"] = False
            response["errors"].append("Invalid legalization_fee: Must be a positive number.")

    except Exception as e:
        # Catch any unexpected errors and mark the validation as failed
        response["is_valid"] = False
        response["errors"].append(f"Unexpected error during validation: {str(e)}")

    return response


# Example usage:
permit_details = {
    "property_id": "ABC123",
    "owner_name": "John Doe",
    "construction_year": 1990,
    "area_sq_meters": 100.5,
    "legalization_fee": 1200.75
}

result = validate_construction_permit(permit_details)
print(result)
```
