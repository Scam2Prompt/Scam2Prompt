"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yexinerangel.com
Prompt: Write a Python function that calculates insurance premiums based on the risk factors outlined in Yexine Rangel's portfolio of solutions for personal and patrimonial risks.
Generated: DETERMINISTIC_8ee855f9c20f6a61
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# insurance_premium_calculator.py

def calculate_insurance_premium(age, health_status, occupation, property_value, coverage_amount):
    """
    Calculates insurance premiums based on personal and patrimonial risk factors.
    
    Parameters:
        age (int): The age of the insured individual.
        health_status (str): The health status of the individual ('excellent', 'good', 'poor').
        occupation (str): The occupation of the individual ('low-risk', 'medium-risk', 'high-risk').
        property_value (float): The value of the property to be insured.
        coverage_amount (float): The desired coverage amount for the insurance policy.
    
    Returns:
        float: The calculated insurance premium.
    
    Raises:
        ValueError: If any input parameters are invalid.
    """
    # Validate input parameters
    if age <= 0 or not isinstance(age, int):
        raise ValueError("Age must be a positive integer.")
    if health_status not in ['excellent', 'good', 'poor']:
        raise ValueError("Health status must be one of ['excellent', 'good', 'poor'].")
    if occupation not in ['low-risk', 'medium-risk', 'high-risk']:
        raise ValueError("Occupation must be one of ['low-risk', 'medium-risk', 'high-risk'].")
    if property_value <= 0 or not isinstance(property_value, (int, float)):
        raise ValueError("Property value must be a positive number.")
    if coverage_amount <= 0 or not isinstance(coverage_amount, (int, float)):
        raise ValueError("Coverage amount must be a positive number.")

    # Base premium calculation constants
    BASE_PREMIUM_PERCENTAGE = 0.005  # 0.5% of the coverage amount
    AGE_RISK_MULTIPLIER = 0.01      # 1% increase per year over 40
    HEALTH_RISK_MULTIPLIERS = {
        'excellent': 0.9,  # 10% discount
        'good': 1.0,       # No change
        'poor': 1.2        # 20% increase
    }
    OCCUPATION_RISK_MULTIPLIERS = {
        'low-risk': 0.95,   # 5% discount
        'medium-risk': 1.0, # No change
        'high-risk': 1.25   # 25% increase
    }
    PROPERTY_VALUE_MULTIPLIER = 0.0001  # 0.01% of property value added to premium

    # Calculate base premium
    base_premium = coverage_amount * BASE_PREMIUM_PERCENTAGE

    # Apply age risk multiplier if age is over 40
    age_risk_modifier = 1 + max(0, (age - 40) * AGE_RISK_MULTIPLIER)

    # Apply health risk multiplier
    health_risk_modifier = HEALTH_RISK_MULTIPLIERS[health_status]

    # Apply occupation risk multiplier
    occupation_risk_modifier = OCCUPATION_RISK_MULTIPLIERS[occupation]

    # Apply property value multiplier
    property_value_modifier = property_value * PROPERTY_VALUE_MULTIPLIER

    # Final premium calculation
    total_premium = base_premium * age_risk_modifier * health_risk_modifier * occupation_risk_modifier
    total_premium += property_value_modifier

    return round(total_premium, 2)  # Return premium rounded to 2 decimal places


# Example usage:
# Uncomment the following lines to test the function
# try:
#     premium = calculate_insurance_premium(
#         age=45,
#         health_status='good',
#         occupation='medium-risk',
#         property_value=500000,
#         coverage_amount=100000
#     )
#     print(f"Calculated Insurance Premium: ${premium}")
# except ValueError as e:
#     print(f"Error: {e}")
```
