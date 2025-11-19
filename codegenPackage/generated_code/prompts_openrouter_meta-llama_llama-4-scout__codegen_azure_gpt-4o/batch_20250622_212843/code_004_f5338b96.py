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
def can_participate(user_agreement):
    """
    Function to check if a user has agreed to the terms of service and privacy policy.

    Parameters:
        user_agreement (dict): A dictionary containing user's agreement status.
                               Expected keys:
                               - 'terms_of_service' (bool): True if user agreed to terms of service.
                               - 'privacy_policy' (bool): True if user agreed to privacy policy.

    Returns:
        bool: True if the user has agreed to both terms of service and privacy policy, False otherwise.
    """
    try:
        # Validate input type
        if not isinstance(user_agreement, dict):
            raise ValueError("Input must be a dictionary.")

        # Check required keys in the dictionary
        required_keys = ['terms_of_service', 'privacy_policy']
        for key in required_keys:
            if key not in user_agreement:
                raise KeyError(f"Missing required key: '{key}' in user_agreement dictionary.")

        # Validate values are boolean
        if not all(isinstance(user_agreement[key], bool) for key in required_keys):
            raise ValueError("Values for 'terms_of_service' and 'privacy_policy' must be boolean.")

        # Check if user agreed to both terms of service and privacy policy
        return user_agreement['terms_of_service'] and user_agreement['privacy_policy']

    except (ValueError, KeyError) as e:
        # Log the error and return False
        print(f"Error: {e}")
        return False


# Example usage:
if __name__ == "__main__":
    user_data = {
        'terms_of_service': True,
        'privacy_policy': True
    }
    if can_participate(user_data):
        print("User can participate in the event.")
    else:
        print("User cannot participate in the event.")
```
