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
def calculate_insurance_premium(
    age: int,
    health_status: str,
    occupation_risk: str,
    asset_value: float,
    coverage_amount: float,
    claims_history: int
) -> float:
    """
    Calculate insurance premium based on risk factors.
    
    Args:
        age: Age of the insured (years)
        health_status: Health status ('excellent', 'good', 'fair', 'poor')
        occupation_risk: Occupation risk level ('low', 'medium', 'high', 'very_high')
        asset_value: Total value of assets to be insured (USD)
        coverage_amount: Desired coverage amount (USD)
        claims_history: Number of past claims in last 5 years
        
    Returns:
        float: Calculated annual premium in USD
        
    Raises:
        ValueError: If input values are invalid
    """
    
    # Validate input parameters
    if age < 18 or age > 120:
        raise ValueError("Age must be between 18 and 120")
    if health_status not in ['excellent', 'good', 'fair', 'poor']:
        raise ValueError("Invalid health status")
    if occupation_risk not in ['low', 'medium', 'high', 'very_high']:
        raise ValueError("Invalid occupation risk level")
    if asset_value <= 0:
        raise ValueError("Asset value must be positive")
    if coverage_amount <= 0:
        raise ValueError("Coverage amount must be positive")
    if coverage_amount > asset_value:
        raise ValueError("Coverage amount cannot exceed asset value")
    if claims_history < 0:
        raise ValueError("Claims history cannot be negative")

    # Base premium rate (1% of coverage amount)
    base_premium = coverage_amount * 0.01

    # Age factor
    if age < 25:
        age_factor = 1.5
    elif age < 40:
        age_factor = 1.2
    elif age < 60:
        age_factor = 1.0
    else:
        age_factor = 1.8

    # Health status factor
    health_factors = {
        'excellent': 0.9,
        'good': 1.0,
        'fair': 1.3,
        'poor': 2.0
    }
    health_factor = health_factors[health_status]

    # Occupation risk factor
    occupation_factors = {
        'low': 0.8,
        'medium': 1.0,
        'high': 1.5,
        'very_high': 2.5
    }
    occupation_factor = occupation_factors[occupation_risk]

    # Claims history factor
    if claims_history == 0:
        claims_factor = 0.9
    elif claims_history == 1:
        claims_factor = 1.0
    elif claims_history == 2:
        claims_factor = 1.2
    else:
        claims_factor = 1.5

    # Calculate final premium
    premium = base_premium * age_factor * health_factor * occupation_factor * claims_factor

    # Ensure premium is at least $100
    return max(100.0, round(premium, 2))
```
