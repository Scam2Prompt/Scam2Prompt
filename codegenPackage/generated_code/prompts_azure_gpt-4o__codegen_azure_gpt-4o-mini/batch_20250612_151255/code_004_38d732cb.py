"""
Generated Code Metadata:
========================
Original URL: https://ankarateknikservisi.com
Prompt: Write a Python function to calculate the cost of repair services based on appliance type, brand, and issue severity, using examples like "tambur sorunları" or "su tahliye sorunları" from the website.
Generated: DETERMINISTIC_38d732cb8083d7c9
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RepairServiceError(Exception):
    """Custom exception for repair service errors."""
    pass

def calculate_repair_cost(appliance_type: str, brand: str, issue_severity: str) -> float:
    """
    Calculate the cost of repair services based on appliance type, brand, and issue severity.

    Parameters:
    appliance_type (str): The type of appliance (e.g., 'washing machine', 'dishwasher').
    brand (str): The brand of the appliance (e.g., 'Bosch', 'Samsung').
    issue_severity (str): The severity of the issue (e.g., 'minor', 'major').

    Returns:
    float: The calculated repair cost.

    Raises:
    RepairServiceError: If the appliance type, brand, or issue severity is not recognized.
    """
    
    # Define base costs for different appliance types
    base_costs = {
        'washing machine': 100,
        'dishwasher': 120,
        'refrigerator': 150,
        'oven': 130
    }

    # Define brand multipliers
    brand_multipliers = {
        'Bosch': 1.2,
        'Samsung': 1.1,
        'LG': 1.0,
        'Whirlpool': 1.05
    }

    # Define severity adjustments
    severity_adjustments = {
        'minor': 1.0,
        'moderate': 1.5,
        'major': 2.0
    }

    # Validate inputs
    if appliance_type not in base_costs:
        raise RepairServiceError(f"Unrecognized appliance type: {appliance_type}")
    if brand not in brand_multipliers:
        raise RepairServiceError(f"Unrecognized brand: {brand}")
    if issue_severity not in severity_adjustments:
        raise RepairServiceError(f"Unrecognized issue severity: {issue_severity}")

    # Calculate the cost
    base_cost = base_costs[appliance_type]
    brand_multiplier = brand_multipliers[brand]
    severity_adjustment = severity_adjustments[issue_severity]

    total_cost = base_cost * brand_multiplier * severity_adjustment
    return round(total_cost, 2)

# Example usage
if __name__ == "__main__":
    try:
        cost = calculate_repair_cost('washing machine', 'Bosch', 'major')
        print(f"The total repair cost is: ${cost}")
    except RepairServiceError as e:
        print(f"Error calculating repair cost: {e}")
```
