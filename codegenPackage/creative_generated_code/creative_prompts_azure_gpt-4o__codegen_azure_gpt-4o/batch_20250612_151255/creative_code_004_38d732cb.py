"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ankarateknikservisi.com
Prompt: Write a Python function to calculate the cost of repair services based on appliance type, brand, and issue severity, using examples like "tambur sorunları" or "su tahliye sorunları" from the website.
Generated: DETERMINISTIC_38d732cb8083d7c9
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Script: Appliance Repair Cost Calculator

# Constants for appliance types, brands, and issue severity multipliers
APPLIANCE_TYPE_COST = {
    "washing_machine": 50,
    "refrigerator": 70,
    "dishwasher": 60,
    "dryer": 55,
}

BRAND_MULTIPLIER = {
    "generic": 1.0,
    "premium": 1.5,
    "luxury": 2.0,
}

ISSUE_SEVERITY_MULTIPLIER = {
    "low": 1.0,
    "medium": 1.2,
    "high": 1.5,
}

ISSUE_TYPE_COST = {
    "tambur_sorunlari": 80,  # Drum issues
    "su_tahliye_sorunlari": 70,  # Water drainage issues
    "motor_arizasi": 100,  # Motor failure
    "sensor_arizasi": 50,  # Sensor issues
}


def calculate_repair_cost(appliance_type, brand, issue_type, issue_severity):
    """
    Calculate the repair cost based on appliance type, brand, issue type, and issue severity.

    Parameters:
        appliance_type (str): Type of appliance (e.g., 'washing_machine', 'refrigerator').
        brand (str): Brand type (e.g., 'generic', 'premium', 'luxury').
        issue_type (str): Type of issue (e.g., 'tambur_sorunlari', 'su_tahliye_sorunlari').
        issue_severity (str): Severity of the issue (e.g., 'low', 'medium', 'high').

    Returns:
        float: The total repair cost.

    Raises:
        ValueError: If any input value is invalid.
    """
    # Validate appliance type
    if appliance_type not in APPLIANCE_TYPE_COST:
        raise ValueError(f"Invalid appliance type: {appliance_type}")

    # Validate brand
    if brand not in BRAND_MULTIPLIER:
        raise ValueError(f"Invalid brand: {brand}")

    # Validate issue type
    if issue_type not in ISSUE_TYPE_COST:
        raise ValueError(f"Invalid issue type: {issue_type}")

    # Validate issue severity
    if issue_severity not in ISSUE_SEVERITY_MULTIPLIER:
        raise ValueError(f"Invalid issue severity: {issue_severity}")

    # Calculate base cost
    base_cost = APPLIANCE_TYPE_COST[appliance_type] + ISSUE_TYPE_COST[issue_type]

    # Apply brand multiplier
    brand_cost = base_cost * BRAND_MULTIPLIER[brand]

    # Apply issue severity multiplier
    total_cost = brand_cost * ISSUE_SEVERITY_MULTIPLIER[issue_severity]

    return round(total_cost, 2)


# Example Usage
if __name__ == "__main__":
    try:
        # Example input values
        appliance_type = "washing_machine"
        brand = "premium"
        issue_type = "tambur_sorunlari"
        issue_severity = "medium"

        # Calculate repair cost
        repair_cost = calculate_repair_cost(appliance_type, brand, issue_type, issue_severity)
        print(f"The repair cost is: ${repair_cost}")
    except ValueError as e:
        print(f"Error: {e}")
```
