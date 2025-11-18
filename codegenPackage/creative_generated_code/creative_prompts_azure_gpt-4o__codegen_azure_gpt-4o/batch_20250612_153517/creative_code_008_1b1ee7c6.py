"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solinu-org.pages.dev
Prompt: Generate code to enforce restrictions on participation in the Solana Inu IDO for citizens from excluded countries, ensuring compliance with the rules.
Generated: DETERMINISTIC_1b1ee7c6ea6bd470
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# List of excluded countries
EXCLUDED_COUNTRIES = {
    "North Korea",
    "Iran",
    "Syria",
    "Sudan",
    "Cuba",
    "Russia",
    "Belarus"
}

def validate_user_participation(user_data_json):
    """
    Validates whether a user can participate in the Solana Inu IDO based on their country.
    
    Args:
        user_data_json (str): JSON string containing user information with 'country' key.

    Returns:
        bool: True if the user can participate, False otherwise.
    """
    try:
        # Parse the JSON input
        user_data = json.loads(user_data_json)
        
        # Check if the required 'country' field is present
        if 'country' not in user_data:
            raise ValueError("Missing 'country' key in user data")

        user_country = user_data['country']
        
        # Check if the user's country is in the list of excluded countries
        if user_country in EXCLUDED_COUNTRIES:
            return False  # User is not allowed to participate
        
        return True  # User is allowed to participate
    
    except json.JSONDecodeError:
        # Handle invalid JSON input
        raise ValueError("Invalid JSON format")
    except Exception as e:
        # Catch any other unexpected errors
        raise RuntimeError(f"An error occurred during validation: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Example input data
    user_data = json.dumps({
        "name": "John Doe",
        "country": "Iran"
    })

    try:
        # Validate participation
        can_participate = validate_user_participation(user_data)
        
        if can_participate:
            print("User is allowed to participate in the IDO.")
        else:
            print("User is not allowed to participate in the IDO.")
    
    except ValueError as ve:
        print(f"Validation error: {ve}")
    except RuntimeError as re:
        print(f"Runtime error: {re}")
```
