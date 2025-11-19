"""
Generated Code Metadata:
========================
Original URL: https://yexinerangel.com
Prompt: Write a Python function that calculates insurance premiums based on the risk factors outlined in Yexine Rangel's portfolio of solutions for personal and patrimonial risks.
Generated: DETERMINISTIC_8ee855f9c20f6a61
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_insurance_premium(age, health_condition, property_value, risk_factor):
    """
    Calculate insurance premiums based on personal and patrimonial risk factors.

    Parameters:
        age (int): The age of the insured person.
        health_condition (str): Health condition of the insured person ('excellent', 'good', 'fair', 'poor').
        property_value (float): Value of the insured property in USD.
        risk_factor (float): Additional risk factor multiplier (e.g., 1.0 for standard risk, >1.0 for higher risk).

    Returns:
        float: Calculated insurance premium in USD.

    Raises:
        ValueError: If any input parameter is invalid.
    """
    try:
        # Validate inputs
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")
        if health_condition not in ['excellent', 'good', 'fair', 'poor']:
            raise ValueError("Health condition must be one of: 'excellent', 'good', 'fair', 'poor'.")
        if not isinstance(property_value, (int, float)) or property_value <= 0:
            raise ValueError("Property value must be a positive number.")
        if not isinstance(risk_factor, (int, float)) or risk_factor <= 0:
            raise ValueError("Risk factor must be a positive number.")

        # Base premium calculation
        base_premium = property_value * 0.01  # 1% of property value

        # Adjust premium based on age
        if age < 25:
            age_multiplier = 1.5  # Higher risk for younger individuals
        elif age <= 60:
            age_multiplier = 1.0  # Standard risk
        else:
            age_multiplier = 1.2  # Higher risk for older individuals

        # Adjust premium based on health condition
        health_multiplier = {
            'excellent': 0.8,  # Lower risk
            'good': 1.0,       # Standard risk
            'fair': 1.2,       # Higher risk
            'poor': 1.5        # Much higher risk
        }[health_condition]

        # Final premium calculation
        premium = base_premium * age_multiplier * health_multiplier * risk_factor

        # Ensure premium is rounded to two decimal places
        return round(premium, 2)

    except ValueError as e:
        logging.error(f"Input validation error: {e}")
        raise

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

# Example usage:
# premium = calculate_insurance_premium(age=30, health_condition='good', property_value=100000, risk_factor=1.2)
# print(f"Calculated Premium: ${premium}")
```
