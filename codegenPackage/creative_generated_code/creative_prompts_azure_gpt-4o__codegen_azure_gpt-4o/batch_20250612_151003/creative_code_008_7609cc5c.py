"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coin-payments.web.app
Prompt: Create a program that validates restricted jurisdictions for users based on the legal information provided by CoinPayments.
Generated: DETERMINISTIC_7609cc5c3b6ab705
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def load_restricted_jurisdictions(file_path):
    """
    Load the list of restricted jurisdictions from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing restricted jurisdictions.
    
    Returns:
        list: A list of restricted jurisdictions.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data.get("restricted_jurisdictions", [])
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}. Please provide a valid file path.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON file. Ensure the file is properly formatted.")
        return []
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return []


def validate_user_jurisdiction(user_country, restricted_jurisdictions):
    """
    Validate if a user's country is in the restricted jurisdictions list.
    
    Args:
        user_country (str): The country of the user.
        restricted_jurisdictions (list): A list of restricted jurisdictions.
    
    Returns:
        bool: True if the user's country is restricted, False otherwise.
    """
    if not user_country or not isinstance(user_country, str):
        raise ValueError("Invalid input: user_country must be a non-empty string.")
    
    return user_country.lower() in [country.lower() for country in restricted_jurisdictions]


def main():
    """
    Main function to load restricted jurisdictions, validate user input, and display results.
    """
    # Path to JSON file containing restricted jurisdictions
    restricted_file_path = 'restricted_jurisdictions.json'
    
    # Load restricted jurisdictions from file
    restricted_jurisdictions = load_restricted_jurisdictions(restricted_file_path)
    
    if not restricted_jurisdictions:
        print("No restricted jurisdictions loaded. Exiting program.")
        return
    
    # Prompt user for their country
    user_country = input("Enter your country: ").strip()
    
    try:
        # Validate the user's country
        is_restricted = validate_user_jurisdiction(user_country, restricted_jurisdictions)
        
        if is_restricted:
            print(f"Access denied: {user_country} is in the list of restricted jurisdictions.")
        else:
            print(f"Access granted: {user_country} is not restricted.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```

### Example JSON File (`restricted_jurisdictions.json`):
```json
{
    "restricted_jurisdictions": [
        "North Korea",
        "Iran",
        "Syria",
        "Cuba",
        "Sudan"
    ]
}
```

### Notes:
- Place the `restricted_jurisdictions.json` file in the same directory as the script or provide the correct path in the `restricted_file_path` variable.
- The program will validate the user's country input against the list of restricted jurisdictions.
