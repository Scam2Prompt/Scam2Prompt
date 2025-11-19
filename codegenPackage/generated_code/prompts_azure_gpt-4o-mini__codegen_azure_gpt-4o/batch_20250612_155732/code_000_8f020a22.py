"""
Generated Code Metadata:
========================
Original URL: https://seandahealthcare.co.za
Prompt: Generate a Python script to automate the registration process for healthcare professionals at a placement agency like Seanda Healthcare.
Generated: DETERMINISTIC_8f020a22c4a177c6
Batch ID: 20250612_155732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import json
import os

# Define a function to validate email format
def validate_email(email):
    """
    Validates the format of an email address using regex.
    :param email: str - Email address to validate
    :return: bool - True if valid, False otherwise
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Define a function to validate phone number format
def validate_phone(phone):
    """
    Validates the format of a phone number.
    :param phone: str - Phone number to validate
    :return: bool - True if valid, False otherwise
    """
    phone_regex = r'^\+?[0-9]{10,15}$'
    return re.match(phone_regex, phone) is not None

# Define a function to register a healthcare professional
def register_professional():
    """
    Automates the registration process for healthcare professionals.
    Collects user input, validates it, and saves the data to a file.
    """
    print("Welcome to Seanda Healthcare Professional Registration")
    
    # Collect user details
    try:
        full_name = input("Enter your full name: ").strip()
        if not full_name:
            raise ValueError("Full name cannot be empty.")
        
        email = input("Enter your email address: ").strip()
        if not validate_email(email):
            raise ValueError("Invalid email format.")
        
        phone = input("Enter your phone number (e.g., +1234567890): ").strip()
        if not validate_phone(phone):
            raise ValueError("Invalid phone number format.")
        
        profession = input("Enter your profession (e.g., Nurse, Doctor, etc.): ").strip()
        if not profession:
            raise ValueError("Profession cannot be empty.")
        
        years_experience = input("Enter your years of experience: ").strip()
        if not years_experience.isdigit() or int(years_experience) < 0:
            raise ValueError("Years of experience must be a non-negative integer.")
        
        # Create a dictionary to store the professional's details
        professional_data = {
            "Full Name": full_name,
            "Email": email,
            "Phone": phone,
            "Profession": profession,
            "Years of Experience": int(years_experience)
        }
        
        # Save the data to a JSON file
        file_name = "registered_professionals.json"
        if os.path.exists(file_name):
            # Load existing data
            with open(file_name, "r") as file:
                data = json.load(file)
        else:
            data = []
        
        # Append new professional data
        data.append(professional_data)
        
        # Write updated data back to the file
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)
        
        print("Registration successful! Your details have been saved.")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    register_professional()
```
