"""
Generated Code Metadata:
========================
Original URL: https://tos.hyperliquidfndn.org
Prompt: Write a Python function that checks if a user has agreed to the terms of service and privacy policy before allowing participation in an event, based on the structure seen in the Hyper Foundation's terms.
Generated: DETERMINISTIC_f5338b96d70ae76e
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def check_user_agreement(user_data: dict) -> bool:
    """
    Check if a user has agreed to the terms of service and privacy policy.
    
    Args:
        user_data (dict): Dictionary containing user information including:
            - 'terms_accepted' (bool): Whether terms of service were accepted
            - 'privacy_accepted' (bool): Whether privacy policy was accepted
            - 'acceptance_date' (str, optional): Date when terms were accepted (ISO format)
    
    Returns:
        bool: True if user has accepted both terms and privacy policy, False otherwise
    
    Raises:
        ValueError: If required fields are missing or invalid
    """
    # Check required fields exist
    required_fields = {'terms_accepted', 'privacy_accepted'}
    missing_fields = required_fields - set(user_data.keys())
    if missing_fields:
        raise ValueError(f"Missing required fields: {missing_fields}")
    
    # Validate field types
    if not isinstance(user_data['terms_accepted'], bool):
        raise ValueError("terms_accepted must be boolean")
    if not isinstance(user_data['privacy_accepted'], bool):
        raise ValueError("privacy_accepted must be boolean")
    
    # Optional check for acceptance date if present
    if 'acceptance_date' in user_data:
        try:
            from datetime import datetime
            datetime.fromisoformat(user_data['acceptance_date'])
        except ValueError as e:
            raise ValueError(f"Invalid acceptance_date format: {e}")
    
    # Return True only if both agreements are accepted
    return user_data['terms_accepted'] and user_data['privacy_accepted']
```
