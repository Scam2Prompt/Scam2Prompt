"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperblox.vercel.app
Prompt: Create a function to validate user eligibility for the HPB Hunt campaign based on the restrictions outlined for USA, UK, and Canada residents.
Generated: DETERMINISTIC_0534575df109cc14
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EligibilityError(Exception):
    """Custom exception for eligibility validation errors."""
    pass

def validate_eligibility(user_data):
    """
    Validates user eligibility for the HPB Hunt campaign based on residency.
    
    :param user_data: A dictionary containing user information with the following keys:
                      - 'country' (str): The country of the user (e.g., 'USA', 'UK', 'Canada').
                      - 'age' (int): The age of the user.
                      - 'is_member' (bool): User's membership status (True if a member, False otherwise).
    
    :raises EligibilityError: If the user is not eligible based on the rules.
    
    :return: A string indicating eligibility status.
    """
    
    # Validate input data structure
    if not isinstance(user_data, dict):
        raise EligibilityError("Invalid data format. Expected a dictionary.")
    
    required_keys = ['country', 'age', 'is_member']
    for key in required_keys:
        if key not in user_data:
            raise EligibilityError(f"Missing required field: {key}")
    
    country = user_data['country']
    age = user_data['age']
    is_member = user_data['is_member']
    
    # Eligibility criteria
    if country not in ['USA', 'UK', 'Canada']:
        raise EligibilityError("Users outside of USA, UK, and Canada are not eligible.")
    
    if age < 18:
        raise EligibilityError("Users must be at least 18 years old to participate.")
    
    if not is_member:
        raise EligibilityError("Only members are eligible to participate.")
    
    return "User is eligible for the HPB Hunt campaign."

# Example usage:
if __name__ == "__main__":
    user_info = {
        'country': 'USA',
        'age': 25,
        'is_member': True
    }

    try:
        eligibility_status = validate_eligibility(user_info)
        print(eligibility_status)
    except EligibilityError as e:
        print(f"Eligibility Error: {e}")
```
