"""
Generated Code Metadata:
========================
Original URL: https://hyperblox.vercel.app
Prompt: Create a function to validate user eligibility for the HPB Hunt campaign based on the restrictions outlined for USA, UK, and Canada residents.
Generated: DETERMINISTIC_0534575df109cc14
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def validate_hpb_hunt_eligibility(country, age, has_consent):
    """
    Validates user eligibility for the HPB Hunt campaign based on country, age, and consent.
    
    Args:
        country (str): User's country of residence (case-insensitive).
        age (int): User's age in years.
        has_consent (bool): Whether user has given consent to participate.
    
    Returns:
        dict: Dictionary containing:
            - 'is_eligible' (bool): Whether user is eligible
            - 'message' (str): Reason for eligibility status
    
    Raises:
        ValueError: If age is negative or country is empty/None
    """
    
    # Input validation
    if not country:
        raise ValueError("Country cannot be empty")
    if age < 0:
        raise ValueError("Age cannot be negative")
    
    # Normalize country name
    country_lower = country.strip().lower()
    
    # Check eligibility criteria
    eligible_countries = {'usa', 'united states', 'uk', 'united kingdom', 'canada'}
    
    if country_lower not in eligible_countries:
        return {
            'is_eligible': False,
            'message': f"Sorry, the HPB Hunt is not available in {country.title()}"
        }
    
    if age < 18:
        return {
            'is_eligible': False,
            'message': "You must be at least 18 years old to participate"
        }
    
    if not has_consent:
        return {
            'is_eligible': False,
            'message': "You must provide consent to participate"
        }
    
    # All checks passed
    return {
        'is_eligible': True,
        'message': "You are eligible to participate in the HPB Hunt!"
    }
```
