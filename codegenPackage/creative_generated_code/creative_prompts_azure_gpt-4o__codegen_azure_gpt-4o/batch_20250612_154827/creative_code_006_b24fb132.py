"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aibaoinsurance.com
Prompt: Create a script to generate customized insurance plans for high-risk properties, referencing the features of Aibao Insurance's home insurance offerings.
Generated: DETERMINISTIC_b24fb132dbe5ecf8
Batch ID: 20250612_154827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to generate customized insurance plans for high-risk properties.
The script references Aibao Insurance's home insurance offerings.
"""

import json

# Define constants for insurance plan categories and features
INSURANCE_PLAN_TEMPLATES = {
    "Standard": {
        "coverage": {
            "fire_damage": 50000,
            "water_damage": 30000,
            "theft": 20000,
        },
        "premium_rate": 0.02,  # Percentage of property value
        "max_property_value": 500000,  # Maximum property value allowed
    },
    "Enhanced": {
        "coverage": {
            "fire_damage": 100000,
            "water_damage": 60000,
            "theft": 40000,
            "earthquake_damage": 50000,
        },
        "premium_rate": 0.03,  # Percentage of property value
        "max_property_value": 1000000,
    },
    "Premium": {
        "coverage": {
            "fire_damage": 200000,
            "water_damage": 120000,
            "theft": 80000,
            "earthquake_damage": 100000,
            "flood_damage": 75000,
        },
        "premium_rate": 0.05,  # Percentage of property value
        "max_property_value": 2000000,
    },
}

def validate_property_details(property_value, high_risk_features):
    """
    Validates the property details provided by the user.
    
    :param property_value: Value of the property in USD
    :param high_risk_features: List of high-risk features for the property
    :return: Boolean indicating whether the details are valid, and an error message if not
    """
    if property_value <= 0:
        return False, "Property value must be greater than zero."
    if not high_risk_features:
        return False, "High-risk features must be specified."
    return True, None

def suggest_insurance_plan(property_value):
    """
    Suggests an insurance plan based on the property value.
    
    :param property_value: Value of the property in USD
    :return: Suggested insurance plan or a message indicating no suitable plan
    """
    for plan_name, plan_details in INSURANCE_PLAN_TEMPLATES.items():
        if property_value <= plan_details["max_property_value"]:
            return plan_name, plan_details
    return None, "No suitable insurance plan available for the provided property value."

def generate_insurance_plan(property_value, high_risk_features):
    """
    Generates a customized insurance plan for a high-risk property.
    
    :param property_value: Value of the property in USD
    :param high_risk_features: List of high-risk features for the property
    :return: Customized insurance plan details in JSON format
    """
    # Validate property details
    is_valid, error_message = validate_property_details(property_value, high_risk_features)
    if not is_valid:
        return json.dumps({"error": error_message})

    # Suggest an insurance plan
    plan_name, plan_details = suggest_insurance_plan(property_value)
    if not plan_name:
        return json.dumps({"error": plan_details})

    # Calculate premium and include high-risk features
    premium = property_value * plan_details["premium_rate"]
    customized_plan = {
        "plan_name": plan_name,
        "coverage": plan_details["coverage"],
        "premium": premium,
        "property_value": property_value,
        "high_risk_features": high_risk_features,
    }

    return json.dumps(customized_plan, indent=4)

# Main function to accept user input and generate insurance plan
if __name__ == "__main__":
    try:
        # Get user input
        property_value = float(input("Enter the property value (USD): "))
        high_risk_features = input("Enter high-risk features (comma-separated): ").split(",")

        # Generate insurance plan
        insurance_plan = generate_insurance_plan(property_value, [feature.strip() for feature in high_risk_features])

        # Display the result
        print("\nGenerated Insurance Plan:")
        print(insurance_plan)

    except ValueError:
        print("Error: Invalid input. Please provide numeric values where required.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
