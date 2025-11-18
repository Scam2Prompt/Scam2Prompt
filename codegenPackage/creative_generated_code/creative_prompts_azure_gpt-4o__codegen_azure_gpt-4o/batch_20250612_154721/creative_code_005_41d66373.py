"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rayatrecruitment.com
Prompt: Create a Python function to generate and display login credentials (application number and password) after successful registration, mimicking the process on the Rayat Shikshan Sanstha website.
Generated: DETERMINISTIC_41d663730b01b9f5
Batch ID: 20250612_154721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string


def generate_credentials(full_name, date_of_birth):
    """
    Generates and displays login credentials (application number and password) 
    after successful registration.

    Args:
        full_name (str): Full name of the user.
        date_of_birth (str): Date of birth in format 'YYYY-MM-DD'.

    Returns:
        dict: A dictionary containing application number and password.
    """
    try:
        # Validate input arguments
        if not full_name or not isinstance(full_name, str):
            raise ValueError("Full name must be a non-empty string.")
        if not date_of_birth or not isinstance(date_of_birth, str):
            raise ValueError("Date of birth must be a non-empty string in 'YYYY-MM-DD' format.")
        
        # Generate a unique application number
        # Combination of random digits and uppercase letters
        application_number = "RS" + ''.join(
            random.choices(string.ascii_uppercase + string.digits, k=10)
        )
        
        # Generate a random secure password
        # Combination of letters, digits, and special characters
        password = ''.join(
            random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=12)
        )
        
        # Display the credentials
        print(f"Registration Successful!")
        print(f"Your Application Number: {application_number}")
        print(f"Your Password: {password}")
        
        # Return the credentials as a dictionary
        return {"application_number": application_number, "password": password}
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


# Example Usage:
# Replace these values with user input in production
user_full_name = "John Doe"
user_date_of_birth = "2000-01-01"

credentials = generate_credentials(user_full_name, user_date_of_birth)
if credentials:
    print("Credentials generated successfully.")
else:
    print("Failed to generate credentials.")
```
